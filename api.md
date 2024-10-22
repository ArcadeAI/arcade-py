# Shared Types

```python
from arcadepy.types import AuthorizationResponse, Error, ToolDefinition
```

# Auth

Types:

```python
from arcadepy.types import AuthRequest
```

Methods:

- <code title="post /v1/auth/authorize">client.auth.<a href="./src/arcadepy/resources/auth.py">authorize</a>(\*\*<a href="src/arcadepy/types/auth_authorize_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/authorization_response.py">AuthorizationResponse</a></code>
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
    Inputs,
    Output,
    Parameter,
    Requirements,
    Response,
    ResponseOutput,
    ToolkitDefinition,
    ValueSchema,
)
```

Methods:

- <code title="get /v1/tools/list">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">list</a>(\*\*<a href="src/arcadepy/types/tool_list_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/tool_definition.py">SyncOffsetPage[ToolDefinition]</a></code>
- <code title="post /v1/tools/authorize">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">authorize</a>(\*\*<a href="src/arcadepy/types/tool_authorize_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="post /v1/tools/execute">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">execute</a>(\*\*<a href="src/arcadepy/types/tool_execute_params.py">params</a>) -> <a href="./src/arcadepy/types/response.py">Response</a></code>
- <code title="get /v1/tools/definition">client.tools.<a href="./src/arcadepy/resources/tools/tools.py">get</a>(\*\*<a href="src/arcadepy/types/tool_get_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/tool_definition.py">ToolDefinition</a></code>

## Formatted

Types:

```python
from arcadepy.types.tools import FormattedListResponse, FormattedGetResponse
```

Methods:

- <code title="get /v1/tools/formatted/list">client.tools.formatted.<a href="./src/arcadepy/resources/tools/formatted.py">list</a>(\*\*<a href="src/arcadepy/types/tools/formatted_list_params.py">params</a>) -> <a href="./src/arcadepy/types/tools/formatted_list_response.py">SyncOffsetPage[object]</a></code>
- <code title="get /v1/tools/formatted/definition">client.tools.formatted.<a href="./src/arcadepy/resources/tools/formatted.py">get</a>(\*\*<a href="src/arcadepy/types/tools/formatted_get_params.py">params</a>) -> <a href="./src/arcadepy/types/tools/formatted_get_response.py">object</a></code>
