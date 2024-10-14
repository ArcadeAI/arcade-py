# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..inputs import Inputs
from ..output import Output
from ..._models import BaseModel
from ..requirements import Requirements
from ..toolkit_definition import ToolkitDefinition

__all__ = ["ToolDefinition"]


class ToolDefinition(BaseModel):
    inputs: Inputs

    name: str

    toolkit: ToolkitDefinition

    description: Optional[str] = None

    output: Optional[Output] = None

    requirements: Optional[Requirements] = None
