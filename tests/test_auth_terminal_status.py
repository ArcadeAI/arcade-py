from __future__ import annotations

from typing import List, Union

import httpx
import pytest

from arcadepy import Arcade, AsyncArcade
from arcadepy.types.shared import AuthorizationResponse


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    "initial,statuses,expected",
    [
        (AuthorizationResponse(id="auth_123", status="pending"), ["failed"], "failed"),
        (AuthorizationResponse(id="auth_123", status="failed"), [], "failed"),
        (AuthorizationResponse(id="auth_123", status="completed"), [], "completed"),
        ("auth_123", ["failed"], "failed"),
        ("auth_123", ["pending", "failed"], "failed"),
        ("auth_123", ["completed"], "completed"),
        ("auth_123", ["pending", "completed"], "completed"),
    ],
)
async def test_wait_stops_at_terminal_status(
    asynchronous: bool, initial: Union[AuthorizationResponse, str], statuses: List[str], expected: str
) -> None:
    requests: List[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        assert len(requests) < len(statuses), "polled after terminal authorization status"
        status = statuses[len(requests)]
        requests.append(request)
        return httpx.Response(200, json={"id": "auth_123", "status": status})

    if asynchronous:
        async with AsyncArcade(
            api_key="test", max_retries=0, http_client=httpx.AsyncClient(transport=httpx.MockTransport(respond))
        ) as client:
            result = await client.auth.wait_for_completion(initial)
    else:
        with Arcade(
            api_key="test", max_retries=0, http_client=httpx.Client(transport=httpx.MockTransport(respond))
        ) as sync_client:
            result = sync_client.auth.wait_for_completion(initial)
    assert result.status == expected
    assert result.id == "auth_123"
    assert len(requests) == len(statuses)
    for request in requests:
        assert request.url.params["id"] == "auth_123"
        assert request.url.params["wait"] == "45"
