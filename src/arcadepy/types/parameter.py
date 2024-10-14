# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .value_schema import ValueSchema

__all__ = ["Parameter"]


class Parameter(BaseModel):
    name: str

    value_schema: ValueSchema

    description: Optional[str] = None

    inferrable: Optional[bool] = None

    required: Optional[bool] = None
