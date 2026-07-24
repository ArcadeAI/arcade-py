# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import value_schema, tool_definition
from .. import _compat
from .usage import Usage as Usage
from .choice import Choice as Choice
from .shared import (
    Error as Error,
    AuthorizationContext as AuthorizationContext,
    AuthorizationResponse as AuthorizationResponse,
)
from .chat_message import ChatMessage as ChatMessage
from .value_schema import ValueSchema as ValueSchema
from .chat_response import ChatResponse as ChatResponse
from .health_schema import HealthSchema as HealthSchema
from .tool_definition import ToolDefinition as ToolDefinition
from .tool_get_params import ToolGetParams as ToolGetParams
from .worker_response import WorkerResponse as WorkerResponse
from .tool_list_params import ToolListParams as ToolListParams
from .auth_status_params import AuthStatusParams as AuthStatusParams
from .chat_message_param import ChatMessageParam as ChatMessageParam
from .worker_list_params import WorkerListParams as WorkerListParams
from .tool_execute_params import ToolExecuteParams as ToolExecuteParams
from .worker_tools_params import WorkerToolsParams as WorkerToolsParams
from .worker_create_params import WorkerCreateParams as WorkerCreateParams
from .worker_update_params import WorkerUpdateParams as WorkerUpdateParams
from .auth_authorize_params import AuthAuthorizeParams as AuthAuthorizeParams
from .confirm_user_response import ConfirmUserResponse as ConfirmUserResponse
from .execute_tool_response import ExecuteToolResponse as ExecuteToolResponse
from .tool_authorize_params import ToolAuthorizeParams as ToolAuthorizeParams
from .worker_health_response import WorkerHealthResponse as WorkerHealthResponse
from .auth_confirm_user_params import AuthConfirmUserParams as AuthConfirmUserParams

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    tool_definition.ToolDefinition.update_forward_refs()  # type: ignore
    value_schema.ValueSchema.update_forward_refs()  # type: ignore
else:
    tool_definition.ToolDefinition.model_rebuild(_parent_namespace_depth=0)
    value_schema.ValueSchema.model_rebuild(_parent_namespace_depth=0)
