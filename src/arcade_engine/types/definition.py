# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "Definition",
    "Inputs",
    "InputsParameter",
    "InputsParameterValueSchema",
    "Output",
    "OutputValueSchema",
    "Requirements",
    "RequirementsAuthorization",
    "RequirementsAuthorizationOauth2",
]


class InputsParameterValueSchema(BaseModel):
    val_type: str

    enum: Optional[List[str]] = None

    inner_val_type: Optional[str] = None


class InputsParameter(BaseModel):
    name: str

    value_schema: InputsParameterValueSchema

    description: Optional[str] = None

    inferrable: Optional[bool] = None

    required: Optional[bool] = None


class Inputs(BaseModel):
    parameters: Optional[List[InputsParameter]] = None


class OutputValueSchema(BaseModel):
    val_type: str

    enum: Optional[List[str]] = None

    inner_val_type: Optional[str] = None


class Output(BaseModel):
    available_modes: Optional[List[str]] = None

    description: Optional[str] = None

    value_schema: Optional[OutputValueSchema] = None


class RequirementsAuthorizationOauth2(BaseModel):
    authority: Optional[str] = None

    scopes: Optional[List[str]] = None


class RequirementsAuthorization(BaseModel):
    provider: str

    oauth2: Optional[RequirementsAuthorizationOauth2] = None


class Requirements(BaseModel):
    authorization: Optional[RequirementsAuthorization] = None


class Definition(BaseModel):
    inputs: Inputs

    name: str

    version: str

    description: Optional[str] = None

    output: Optional[Output] = None

    requirements: Optional[Requirements] = None
