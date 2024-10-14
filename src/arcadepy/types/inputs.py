# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .parameter import Parameter

__all__ = ["Inputs"]


class Inputs(BaseModel):
    parameters: Optional[List[Parameter]] = None
