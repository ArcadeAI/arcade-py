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

- <code title="post /v1/auth/authorize">client.auth.<a href="./src/arcadepy/resources/auth.py">authorize</a>(\*\*<a href="src/arcadepy/types/auth_authorize_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="post /v1/auth/confirm_user">client.auth.<a href="./src/arcadepy/resources/auth.py">confirm_user</a>(\*\*<a href="src/arcadepy/types/auth_confirm_user_params.py">params</a>) -> <a href="./src/arcadepy/types/confirm_user_response.py">ConfirmUserResponse</a></code>
- <code title="get /v1/auth/status">client.auth.<a href="./src/arcadepy/resources/auth.py">status</a>(\*\*<a href="src/arcadepy/types/auth_status_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/authorization_response.py">AuthorizationResponse</a></code>

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
)
```

Methods:

- <code title="get /v1/tools">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">list</a>(\*\*<a href="src/arcadepy/types/tool_list_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_definition.py">SyncOffsetPage[ToolDefinition]</a></code>
- <code title="post /v1/tools/authorize">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">authorize</a>(\*\*<a href="src/arcadepy/types/tool_authorize_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="post /v1/tools/execute">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">execute</a>(\*\*<a href="src/arcadepy/types/tool_execute_params.py">params</a>) -> <a href="./src/arcadepy/types/execute_tool_response.py">ExecuteToolResponse</a></code>
- <code title="get /v1/tools/{name}">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">get</a>(name, \*\*<a href="src/arcadepy/types/tool_get_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_definition.py">ToolDefinition</a></code>

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
