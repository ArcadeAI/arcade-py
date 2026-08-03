# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Error", "FieldError"]


class FieldError(BaseModel):
    field: Optional[str] = None
    """
    Field is the json field path of the offending value, rooted at the request body
    with inline-embed levels flattened (e.g. "oauth2.token_request.endpoint").
    """

    message: Optional[str] = None
    """Message is the human-readable, per-field explanation."""

    param: Optional[str] = None
    """Param is the rule's parameter when it has one (e.g.

    "500" for max), omitted otherwise.
    """

    rule: Optional[str] = None
    """Rule is the validation rule that failed (e.g. "required", "max", "url")."""


class Error(BaseModel):
    field_errors: Optional[List[FieldError]] = None
    """
    FieldErrors carries machine-actionable, per-field detail for a request-body
    validation failure so a client can map each failure to a specific input field.
    It is empty (and omitted) for every other error, keeping Message the single
    source of truth for those.
    """

    message: Optional[str] = None

    name: Optional[str] = None
