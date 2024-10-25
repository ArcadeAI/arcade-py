from typing import List, Optional
from unittest.mock import Mock, AsyncMock

import pytest

from arcadepy._client import Arcade, AsyncArcade
from arcadepy.resources.auth import AuthResource, AsyncAuthResource
from arcadepy.types.auth_authorize_params import AuthRequirement, AuthRequirementOauth2
from arcadepy.types.shared.authorization_response import AuthorizationResponse

parametrize_provider_type = pytest.mark.parametrize(
    "provider_type, expected_provider_type",
    [
        (None, "oauth2"),
        ("oauth2", "oauth2"),
        ("custom_type", "custom_type"),
    ],
)

parametrize_scopes = pytest.mark.parametrize(
    "scopes, expected_scopes",
    [
        (["scope1", "scope2"], ["scope1", "scope2"]),
        (None, []),
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


@parametrize_provider_type
@parametrize_scopes
def test_start_calls_authorize_with_correct_params(
    sync_auth_resource: AuthResource,
    provider_type: Optional[str],
    expected_provider_type: str,
    scopes: Optional[List[str]],
    expected_scopes: List[str],
) -> None:
    auth = sync_auth_resource
    auth.authorize = Mock(return_value=AuthorizationResponse(status="pending"))  # type: ignore

    user_id = "user_id"
    provider = "github"

    auth.start(user_id, provider, provider_type=provider_type, scopes=scopes)

    auth.authorize.assert_called_with(
        auth_requirement=AuthRequirement(
            provider_id=provider,
            provider_type=expected_provider_type,
            oauth2=AuthRequirementOauth2(scopes=expected_scopes),
        ),
        user_id=user_id,
    )


@pytest.mark.asyncio
@parametrize_provider_type
@parametrize_scopes
async def test_async_start_calls_authorize_with_correct_params(
    async_auth_resource: AsyncAuthResource,
    provider_type: Optional[str],
    expected_provider_type: str,
    scopes: Optional[List[str]],
    expected_scopes: List[str],
) -> None:
    auth = async_auth_resource
    auth.authorize = AsyncMock(return_value=AuthorizationResponse(status="pending"))  # type: ignore

    user_id = "user_id"
    provider = "github"

    await auth.start(user_id, provider, provider_type=provider_type, scopes=scopes)

    auth.authorize.assert_called_with(
        auth_requirement=AuthRequirement(
            provider_id=provider,
            provider_type=expected_provider_type,
            oauth2=AuthRequirementOauth2(scopes=expected_scopes),
        ),
        user_id=user_id,
    )
