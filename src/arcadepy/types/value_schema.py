# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ValueSchema"]


class ValueSchema(BaseModel):
    val_type: str

    description: Optional[str] = None

    enum: Optional[List[str]] = None

    inner_properties: Optional[object] = None

    inner_required_keys: Optional[List[str]] = None

    inner_val_type: Optional[str] = None

    items: Optional["ValueSchema"] = None

    nullable: Optional[bool] = None

    properties: Optional[object] = None

    required_keys: Optional[List[str]] = None
