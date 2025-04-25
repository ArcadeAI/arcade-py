# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .value_schema import ValueSchema

__all__ = [
    "ToolDefinition",
    "Input",
    "InputParameter",
    "Toolkit",
    "Output",
    "Requirements",
    "RequirementsAuthorization",
    "RequirementsAuthorizationOauth2",
    "RequirementsSecret",
]


class InputParameter(BaseModel):
    name: str

    value_schema: ValueSchema

    description: Optional[str] = None

    inferrable: Optional[bool] = None

    required: Optional[bool] = None


class Input(BaseModel):
    parameters: Optional[List[InputParameter]] = None


class Toolkit(BaseModel):
    name: str

    description: Optional[str] = None

    version: Optional[str] = None


class Output(BaseModel):
    available_modes: Optional[List[str]] = None

    description: Optional[str] = None

    value_schema: Optional[ValueSchema] = None


class RequirementsAuthorizationOauth2(BaseModel):
    scopes: Optional[List[str]] = None


class RequirementsAuthorization(BaseModel):
    id: Optional[str] = None

    oauth2: Optional[RequirementsAuthorizationOauth2] = None

    provider_id: Optional[str] = None

    provider_type: Optional[str] = None


class RequirementsSecret(BaseModel):
    key: str


class Requirements(BaseModel):
    authorization: Optional[RequirementsAuthorization] = None

    secrets: Optional[List[RequirementsSecret]] = None


class ToolDefinition(BaseModel):
    fully_qualified_name: str

    input: Input

    name: str

    qualified_name: str

    toolkit: Toolkit

    description: Optional[str] = None

    formatted_schema: Optional[Dict[str, object]] = None

    output: Optional[Output] = None

    requirements: Optional[Requirements] = None
