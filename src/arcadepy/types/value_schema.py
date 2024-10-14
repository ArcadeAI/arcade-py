# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ValueSchema"]


class ValueSchema(BaseModel):
    val_type: str

    enum: Optional[List[str]] = None

    inner_val_type: Optional[str] = None
