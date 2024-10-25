from typing import List, Union, Optional
from unittest.mock import Mock, AsyncMock

import pytest

from arcadepy._types import NOT_GIVEN, NotGiven
from arcadepy._client import Arcade, AsyncArcade
from arcadepy.resources.auth import AuthResource, AsyncAuthResource
from arcadepy.types.shared.authorization_response import AuthorizationResponse

parametrize_scopes = pytest.mark.parametrize(
    "scopes, expected_scopes",
    [
        (["scope1"], "scope1"),
        (["scope1", "scope2"], "scope1 scope2"),
        (None, NOT_GIVEN),
    ],
)


@pytest.fixture
def sync_auth_resource() -> AuthResource:
    client = Arcade(api_key="test")
    auth = AuthResource(client)
    return auth


@pytest.fixture
def async_auth_resource() -> AsyncAuthResource:
    client = AsyncArcade(api_key="test")
    auth = AsyncAuthResource(client)
    return auth


@parametrize_scopes
def test_wait_for_completion_calls_status_from_auth_response(
    sync_auth_resource: AuthResource, scopes: Optional[List[str]], expected_scopes: Union[str, NotGiven]
) -> None:
    auth = sync_auth_resource
    auth.status = Mock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth_response = AuthorizationResponse(status="pending", authorization_id="auth_id123", scopes=scopes)

    auth.wait_for_completion(auth_response)

    auth.status.assert_called_with(
        authorization_id="auth_id123",
        scopes=expected_scopes,
        wait=45,
    )


def test_wait_for_completion_raises_value_error_for_empty_authorization_id(sync_auth_resource: AuthResource) -> None:
    auth = sync_auth_resource
    auth_response = AuthorizationResponse(status="pending", authorization_id="", scopes=["scope1"])

    with pytest.raises(ValueError, match="Authorization ID is required"):
        auth.wait_for_completion(auth_response)


@parametrize_scopes
def test_wait_for_completion_calls_status_with_auth_id(
    sync_auth_resource: AuthResource, scopes: Optional[List[str]], expected_scopes: Union[str, NotGiven]
) -> None:
    auth = sync_auth_resource
    auth.status = Mock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth.wait_for_completion("auth_id456", scopes)

    auth.status.assert_called_with(
        authorization_id="auth_id456",
        scopes=expected_scopes,
        wait=45,
    )


@pytest.mark.asyncio
@parametrize_scopes
async def test_async_wait_for_completion_calls_status_from_auth_response(
    async_auth_resource: AsyncAuthResource, scopes: Optional[List[str]], expected_scopes: Union[str, NotGiven]
) -> None:
    auth = async_auth_resource
    auth.status = AsyncMock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth_response = AuthorizationResponse(status="pending", authorization_id="auth_id789", scopes=scopes)

    await auth.wait_for_completion(auth_response)

    auth.status.assert_called_with(
        authorization_id="auth_id789",
        scopes=expected_scopes,
        wait=45,
    )


@pytest.mark.asyncio
async def test_async_wait_for_completion_raises_value_error_for_empty_authorization_id(
    async_auth_resource: AsyncAuthResource,
) -> None:
    auth = async_auth_resource
    auth_response = AuthorizationResponse(status="pending", authorization_id="", scopes=["scope1"])

    with pytest.raises(ValueError, match="Authorization ID is required"):
        await auth.wait_for_completion(auth_response)


@pytest.mark.asyncio
@parametrize_scopes
async def test_async_wait_for_completion_calls_status_with_auth_id(
    async_auth_resource: AsyncAuthResource, scopes: Optional[List[str]], expected_scopes: Union[str, NotGiven]
) -> None:
    auth = async_auth_resource
    auth.status = AsyncMock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    await auth.wait_for_completion("auth_id321", scopes)

    auth.status.assert_called_with(
        authorization_id="auth_id321",
        scopes=expected_scopes,
        wait=45,
    )
