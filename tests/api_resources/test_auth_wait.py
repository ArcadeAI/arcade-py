from unittest.mock import Mock, AsyncMock

import pytest

from arcadepy._client import Arcade, AsyncArcade
from arcadepy.types.shared import AuthorizationResponse
from arcadepy.resources.auth import AuthResource, AsyncAuthResource


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


def test_wait_for_completion_calls_status_from_auth_response(sync_auth_resource: AuthResource) -> None:
    auth = sync_auth_resource
    auth.status = Mock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth_response = AuthorizationResponse(status="pending", id="auth_id123")

    auth.wait_for_completion(auth_response)

    auth.status.assert_called_with(id="auth_id123", wait=45)


def test_wait_for_completion_raises_value_error_for_empty_authorization_id(sync_auth_resource: AuthResource) -> None:
    auth = sync_auth_resource
    auth_response = AuthorizationResponse(status="pending", id="", scopes=["scope1"])

    with pytest.raises(ValueError, match="Authorization ID is required"):
        auth.wait_for_completion(auth_response)


def test_wait_for_completion_calls_status_with_auth_id(sync_auth_resource: AuthResource) -> None:
    auth = sync_auth_resource
    auth.status = Mock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth.wait_for_completion("auth_id456")

    auth.status.assert_called_with(id="auth_id456", wait=45)


@pytest.mark.asyncio
async def test_async_wait_for_completion_calls_status_from_auth_response(
    async_auth_resource: AsyncAuthResource,
) -> None:
    auth = async_auth_resource
    auth.status = AsyncMock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth_response = AuthorizationResponse(status="pending", id="auth_id789")

    await auth.wait_for_completion(auth_response)

    auth.status.assert_called_with(id="auth_id789", wait=45)


@pytest.mark.asyncio
async def test_async_wait_for_completion_raises_value_error_for_empty_authorization_id(
    async_auth_resource: AsyncAuthResource,
) -> None:
    auth = async_auth_resource
    auth_response = AuthorizationResponse(status="pending", id="", scopes=["scope1"])

    with pytest.raises(ValueError, match="Authorization ID is required"):
        await auth.wait_for_completion(auth_response)


@pytest.mark.asyncio
async def test_async_wait_for_completion_calls_status_with_auth_id(async_auth_resource: AsyncAuthResource) -> None:
    auth = async_auth_resource
    auth.status = AsyncMock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    await auth.wait_for_completion("auth_id321")

    auth.status.assert_called_with(id="auth_id321", wait=45)
