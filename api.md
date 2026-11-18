# Shared Types

```python
from arcadepy.types import AuthorizationContext, AuthorizationResponse, Error
```

# Admin

## UserConnections

Types:

```python
from arcadepy.types.admin import UserConnectionResponse
```

Methods:

- <code title="get /v1/admin/user_connections">client.admin.user_connections.<a href="./src/arcadepy/resources/admin/user_connections.py">list</a>(\*\*<a href="src/arcadepy/types/admin/user_connection_list_params.py">params</a>) -> <a href="./src/arcadepy/types/admin/user_connection_response.py">SyncOffsetPage[UserConnectionResponse]</a></code>
- <code title="delete /v1/admin/user_connections/{id}">client.admin.user_connections.<a href="./src/arcadepy/resources/admin/user_connections.py">delete</a>(id) -> None</code>

## AuthProviders

Types:

```python
from arcadepy.types.admin import (
    AuthProviderCreateRequest,
    AuthProviderResponse,
    AuthProviderUpdateRequest,
    AuthProviderListResponse,
)
```

Methods:

- <code title="post /v1/admin/auth_providers">client.admin.auth_providers.<a href="./src/arcadepy/resources/admin/auth_providers.py">create</a>(\*\*<a href="src/arcadepy/types/admin/auth_provider_create_params.py">params</a>) -> <a href="./src/arcadepy/types/admin/auth_provider_response.py">AuthProviderResponse</a></code>
- <code title="get /v1/admin/auth_providers">client.admin.auth_providers.<a href="./src/arcadepy/resources/admin/auth_providers.py">list</a>() -> <a href="./src/arcadepy/types/admin/auth_provider_list_response.py">AuthProviderListResponse</a></code>
- <code title="delete /v1/admin/auth_providers/{id}">client.admin.auth_providers.<a href="./src/arcadepy/resources/admin/auth_providers.py">delete</a>(id) -> <a href="./src/arcadepy/types/admin/auth_provider_response.py">AuthProviderResponse</a></code>
- <code title="get /v1/admin/auth_providers/{id}">client.admin.auth_providers.<a href="./src/arcadepy/resources/admin/auth_providers.py">get</a>(id) -> <a href="./src/arcadepy/types/admin/auth_provider_response.py">AuthProviderResponse</a></code>
- <code title="patch /v1/admin/auth_providers/{id}">client.admin.auth_providers.<a href="./src/arcadepy/resources/admin/auth_providers.py">patch</a>(path_id, \*\*<a href="src/arcadepy/types/admin/auth_provider_patch_params.py">params</a>) -> <a href="./src/arcadepy/types/admin/auth_provider_response.py">AuthProviderResponse</a></code>

## Secrets

Types:

```python
from arcadepy.types.admin import SecretResponse, SecretListResponse
```

Methods:

- <code title="get /v1/admin/secrets">client.admin.secrets.<a href="./src/arcadepy/resources/admin/secrets.py">list</a>() -> <a href="./src/arcadepy/types/admin/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /v1/admin/secrets/{secret_id}">client.admin.secrets.<a href="./src/arcadepy/resources/admin/secrets.py">delete</a>(secret_id) -> None</code>

# Auth

Types:

```python
from arcadepy.types import AuthRequest, ConfirmUserRequest, ConfirmUserResponse
```

Methods:

- <code title="post /v1/auth/authorize">client.auth.<a href="./src/arcadepy/resources/auth.py">authorize</a>(\*\*<a href="src/arcadepy/types/auth_authorize_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/auth_authorization_response.py">AuthorizationResponse</a></code>
- <code title="post /v1/auth/confirm_user">client.auth.<a href="./src/arcadepy/resources/auth.py">confirm_user</a>(\*\*<a href="src/arcadepy/types/auth_confirm_user_params.py">params</a>) -> <a href="./src/arcadepy/types/confirm_user_response.py">ConfirmUserResponse</a></code>
- <code title="get /v1/auth/status">client.auth.<a href="./src/arcadepy/resources/auth.py">status</a>(\*\*<a href="src/arcadepy/types/auth_status_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/auth_authorization_response.py">AuthorizationResponse</a></code>

# Health

Types:

```python
from arcadepy.types import HealthSchema
```

Methods:

- <code title="get /v1/health">client.health.<a href="./src/arcadepy/resources/health.py">check</a>() -> <a href="./src/arcadepy/types/health_schema.py">HealthSchema</a></code>

# Chat

Types:

```python
from arcadepy.types import ChatMessage, ChatRequest, ChatResponse, Choice, Usage
```

## Completions

Methods:

- <code title="post /v1/chat/completions">client.chat.completions.<a href="./src/arcadepy/resources/chat/completions.py">create</a>(\*\*<a href="src/arcadepy/types/chat/completion_create_params.py">params</a>) -> <a href="./src/arcadepy/types/chat_response.py">ChatResponse</a></code>

# Tools

Types:

```python
from arcadepy.types import (
    AuthorizeToolRequest,
    ExecuteToolRequest,
    ExecuteToolResponse,
    ToolDefinition,
    ToolExecution,
    ToolExecutionAttempt,
    ValueSchema,
    ToolRequirementsResponse,
    ToolListExecutionsResponse,
    ToolCountExecutionsResponse,
    ToolRetrieveExecutionResponse,
    ToolListScheduledInProjectResponse,
    ToolRetrieveScheduledInProjectResponse,
)
```

Methods:

- <code title="get /v1/tools">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">list</a>(\*\*<a href="src/arcadepy/types/tool_list_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_definition.py">SyncOffsetPage[ToolDefinition]</a></code>
- <code title="post /v1/tools/authorize">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">authorize</a>(\*\*<a href="src/arcadepy/types/tool_authorize_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="post /v1/tools/execute">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">execute</a>(\*\*<a href="src/arcadepy/types/tool_execute_params.py">params</a>) -> <a href="./src/arcadepy/types/execute_tool_response.py">ExecuteToolResponse</a></code>
- <code title="get /v1/tools/{name}">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">get</a>(name, \*\*<a href="src/arcadepy/types/tool_get_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_definition.py">ToolDefinition</a></code>
- <code title="post /v1/tools/requirements">client.tools.<a href="./src/arcadepy/resources/tools.py">requirements</a>(\*\*<a href="src/arcadepy/types/tool_requirements_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_requirements_response.py">ToolRequirementsResponse</a></code>
- <code title="get /v1/orgs/{org_id}/projects/{project_id}/tool_executions">client.tools.<a href="./src/arcadepy/resources/tools.py">list_executions</a>(org_id, project_id, \*\*<a href="src/arcadepy/types/tool_list_executions_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_list_executions_response.py">ToolListExecutionsResponse</a></code>
- <code title="get /v1/orgs/{org_id}/projects/{project_id}/tool_executions/count">client.tools.<a href="./src/arcadepy/resources/tools.py">count_executions</a>(org_id, project_id, \*\*<a href="src/arcadepy/types/tool_count_executions_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_count_executions_response.py">ToolCountExecutionsResponse</a></code>
- <code title="get /v1/orgs/{org_id}/projects/{project_id}/tool_executions/{id}">client.tools.<a href="./src/arcadepy/resources/tools.py">retrieve_execution</a>(org_id, project_id, id, \*\*<a href="src/arcadepy/types/tool_retrieve_execution_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_retrieve_execution_response.py">ToolRetrieveExecutionResponse</a></code>
- <code title="get /v1/orgs/{org_id}/projects/{project_id}/scheduled_tools">client.tools.<a href="./src/arcadepy/resources/tools.py">list_scheduled_in_project</a>(org_id, project_id, \*\*<a href="src/arcadepy/types/tool_list_scheduled_in_project_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_list_scheduled_in_project_response.py">ToolListScheduledInProjectResponse</a></code>
- <code title="get /v1/orgs/{org_id}/projects/{project_id}/scheduled_tools/{id}">client.tools.<a href="./src/arcadepy/resources/tools.py">retrieve_scheduled_in_project</a>(org_id, project_id, id) -> <a href="./src/arcadepy/types/tool_retrieve_scheduled_in_project_response.py">ToolRetrieveScheduledInProjectResponse</a></code>

## Scheduled

Types:

```python
from arcadepy.types.tools import ScheduledGetResponse
```

Methods:

- <code title="get /v1/scheduled_tools">client.tools.scheduled.<a href="./src/arcadepy/resources/tools/scheduled.py">list</a>(\*\*<a href="src/arcadepy/types/tools/scheduled_list_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_execution.py">SyncOffsetPage[ToolExecution]</a></code>
- <code title="get /v1/scheduled_tools/{id}">client.tools.scheduled.<a href="./src/arcadepy/resources/tools/scheduled.py">get</a>(id) -> <a href="./src/arcadepy/types/tools/scheduled_get_response.py">ScheduledGetResponse</a></code>

## Formatted

Methods:

- <code title="get /v1/formatted_tools">client.tools.formatted.<a href="./src/arcadepy/resources/tools/formatted.py">list</a>(\*\*<a href="src/arcadepy/types/tools/formatted_list_params.py">params</a>) -> SyncOffsetPage[object]</code>
- <code title="get /v1/formatted_tools/{name}">client.tools.formatted.<a href="./src/arcadepy/resources/tools/formatted.py">get</a>(name, \*\*<a href="src/arcadepy/types/tools/formatted_get_params.py">params</a>) -> object</code>

# Workers

Types:

```python
from arcadepy.types import (
    CreateWorkerRequest,
    UpdateWorkerRequest,
    WorkerHealthResponse,
    WorkerResponse,
    WorkerAuthorizeResponse,
)
```

Methods:

- <code title="post /v1/workers">client.workers.<a href="./src/arcadepy/resources/workers.py">create</a>(\*\*<a href="src/arcadepy/types/worker_create_params.py">params</a>) -> <a href="./src/arcadepy/types/worker_response.py">WorkerResponse</a></code>
- <code title="patch /v1/workers/{id}">client.workers.<a href="./src/arcadepy/resources/workers.py">update</a>(id, \*\*<a href="src/arcadepy/types/worker_update_params.py">params</a>) -> <a href="./src/arcadepy/types/worker_response.py">WorkerResponse</a></code>
- <code title="get /v1/workers">client.workers.<a href="./src/arcadepy/resources/workers.py">list</a>(\*\*<a href="src/arcadepy/types/worker_list_params.py">params</a>) -> <a href="./src/arcadepy/types/worker_response.py">SyncOffsetPage[WorkerResponse]</a></code>
- <code title="delete /v1/workers/{id}">client.workers.<a href="./src/arcadepy/resources/workers.py">delete</a>(id) -> None</code>
- <code title="get /v1/workers/{id}">client.workers.<a href="./src/arcadepy/resources/workers.py">get</a>(id) -> <a href="./src/arcadepy/types/worker_response.py">WorkerResponse</a></code>
- <code title="get /v1/workers/{id}/health">client.workers.<a href="./src/arcadepy/resources/workers.py">health</a>(id) -> <a href="./src/arcadepy/types/worker_health_response.py">WorkerHealthResponse</a></code>
- <code title="get /v1/workers/{id}/tools">client.workers.<a href="./src/arcadepy/resources/workers.py">tools</a>(id, \*\*<a href="src/arcadepy/types/worker_tools_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_definition.py">SyncOffsetPage[ToolDefinition]</a></code>
- <code title="get /v1/workers/{id}/authorize">client.workers.<a href="./src/arcadepy/resources/workers.py">authorize</a>(id) -> <a href="./src/arcadepy/types/worker_authorize_response.py">WorkerAuthorizeResponse</a></code>

# Hooks

Types:

```python
from arcadepy.types import HookListResponse, HookCreateResponse, HookBulkUpsertResponse, HookRetrieveResponse, HookUpdateResponse
```

Methods:

- <code title="get /v1/hooks">client.hooks.<a href="./src/arcadepy/resources/hooks.py">list</a>(\*\*<a href="src/arcadepy/types/hook_list_params.py">params</a>) -> <a href="./src/arcadepy/types/hook_list_response.py">HookListResponse</a></code>
- <code title="post /v1/hooks">client.hooks.<a href="./src/arcadepy/resources/hooks.py">create</a>(\*\*<a href="src/arcadepy/types/hook_create_params.py">params</a>) -> <a href="./src/arcadepy/types/hook_create_response.py">HookCreateResponse</a></code>
- <code title="patch /v1/hooks/bulk">client.hooks.<a href="./src/arcadepy/resources/hooks.py">bulk_upsert</a>(\*\*<a href="src/arcadepy/types/hook_bulk_upsert_params.py">params</a>) -> <a href="./src/arcadepy/types/hook_bulk_upsert_response.py">HookBulkUpsertResponse</a></code>
- <code title="get /v1/hooks/{hook_id}">client.hooks.<a href="./src/arcadepy/resources/hooks.py">retrieve</a>(hook_id, \*\*<a href="src/arcadepy/types/hook_retrieve_params.py">params</a>) -> <a href="./src/arcadepy/types/hook_retrieve_response.py">HookRetrieveResponse</a></code>
- <code title="patch /v1/hooks/{hook_id}">client.hooks.<a href="./src/arcadepy/resources/hooks.py">update</a>(hook_id, \*\*<a href="src/arcadepy/types/hook_update_params.py">params</a>) -> <a href="./src/arcadepy/types/hook_update_response.py">HookUpdateResponse</a></code>
- <code title="delete /v1/hooks/{hook_id}">client.hooks.<a href="./src/arcadepy/resources/hooks.py">delete</a>(hook_id) -> None</code>

# Plugins

Types:

```python
from arcadepy.types import PluginListResponse, PluginCreateResponse, PluginRetrieveResponse, PluginUpdateResponse
```

Methods:

- <code title="get /v1/plugins">client.plugins.<a href="./src/arcadepy/resources/plugins.py">list</a>(\*\*<a href="src/arcadepy/types/plugin_list_params.py">params</a>) -> <a href="./src/arcadepy/types/plugin_list_response.py">PluginListResponse</a></code>
- <code title="post /v1/plugins">client.plugins.<a href="./src/arcadepy/resources/plugins.py">create</a>(\*\*<a href="src/arcadepy/types/plugin_create_params.py">params</a>) -> <a href="./src/arcadepy/types/plugin_create_response.py">PluginCreateResponse</a></code>
- <code title="get /v1/plugins/{plugin_id}">client.plugins.<a href="./src/arcadepy/resources/plugins.py">retrieve</a>(plugin_id) -> <a href="./src/arcadepy/types/plugin_retrieve_response.py">PluginRetrieveResponse</a></code>
- <code title="patch /v1/plugins/{plugin_id}">client.plugins.<a href="./src/arcadepy/resources/plugins.py">update</a>(plugin_id, \*\*<a href="src/arcadepy/types/plugin_update_params.py">params</a>) -> <a href="./src/arcadepy/types/plugin_update_response.py">PluginUpdateResponse</a></code>
- <code title="delete /v1/plugins/{plugin_id}">client.plugins.<a href="./src/arcadepy/resources/plugins.py">delete</a>(plugin_id) -> None</code>

# Gateways

Types:

```python
from arcadepy.types import GatewayListResponse, GatewayCreateResponse, GatewaySlugInfoResponse, GatewayRetrieveResponse, GatewayReplaceResponse, GatewayUpdateResponse
```

Methods:

- <code title="get /v1/orgs/{org_id}/projects/{project_id}/gateways">client.gateways.<a href="./src/arcadepy/resources/gateways.py">list</a>(org_id, project_id, \*\*<a href="src/arcadepy/types/gateway_list_params.py">params</a>) -> <a href="./src/arcadepy/types/gateway_list_response.py">GatewayListResponse</a></code>
- <code title="post /v1/orgs/{org_id}/projects/{project_id}/gateways">client.gateways.<a href="./src/arcadepy/resources/gateways.py">create</a>(org_id, project_id, \*\*<a href="src/arcadepy/types/gateway_create_params.py">params</a>) -> <a href="./src/arcadepy/types/gateway_create_response.py">GatewayCreateResponse</a></code>
- <code title="post /v1/orgs/{org_id}/projects/{project_id}/gateways/slug">client.gateways.<a href="./src/arcadepy/resources/gateways.py">slug_info</a>(org_id, project_id, \*\*<a href="src/arcadepy/types/gateway_slug_info_params.py">params</a>) -> <a href="./src/arcadepy/types/gateway_slug_info_response.py">GatewaySlugInfoResponse</a></code>
- <code title="get /v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}">client.gateways.<a href="./src/arcadepy/resources/gateways.py">retrieve</a>(org_id, project_id, gateway_id) -> <a href="./src/arcadepy/types/gateway_retrieve_response.py">GatewayRetrieveResponse</a></code>
- <code title="put /v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}">client.gateways.<a href="./src/arcadepy/resources/gateways.py">replace</a>(org_id, project_id, gateway_id, \*\*<a href="src/arcadepy/types/gateway_replace_params.py">params</a>) -> <a href="./src/arcadepy/types/gateway_replace_response.py">GatewayReplaceResponse</a></code>
- <code title="patch /v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}">client.gateways.<a href="./src/arcadepy/resources/gateways.py">update</a>(org_id, project_id, gateway_id, \*\*<a href="src/arcadepy/types/gateway_update_params.py">params</a>) -> <a href="./src/arcadepy/types/gateway_update_response.py">GatewayUpdateResponse</a></code>
- <code title="delete /v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}">client.gateways.<a href="./src/arcadepy/resources/gateways.py">delete</a>(org_id, project_id, gateway_id) -> None</code>
