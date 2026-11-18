# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolRequirementsResponse", "AuthorizationItemsValue", "Authorization", "SecretsItemsValue", "Secrets"]


class AuthorizationItemsValue(BaseModel):
    authorization_id: Optional[str] = None

    met: Optional[bool] = None

    provider_id: Optional[str] = None

    provider_type: Optional[str] = None

    scopes: Optional[List[str]] = None

    status: Optional[Literal["active", "inactive"]] = None

    token_status: Optional[Literal["not_started", "pending", "completed", "failed"]] = None

    tool_names: Optional[List[str]] = None

    url: Optional[str] = None


class Authorization(BaseModel):
    items: Optional[Dict[str, AuthorizationItemsValue]] = None

    met: Optional[bool] = None


class SecretsItemsValue(BaseModel):
    met: Optional[bool] = None

    status_reason: Optional[str] = None

    tool_names: Optional[List[str]] = None


class Secrets(BaseModel):
    items: Optional[Dict[str, SecretsItemsValue]] = None

    met: Optional[bool] = None


class ToolRequirementsResponse(BaseModel):
    authorization: Optional[Authorization] = None

    met: Optional[bool] = None

    secrets: Optional[Secrets] = None
