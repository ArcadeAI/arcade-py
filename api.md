# Shared Types

```python
from arcadepy.types import Error
```

# Auth

Types:

```python
from arcadepy.types import AuthorizationResponse
```

Methods:

- <code title="post /v1/auth/authorize">client.auth.<a href="./src/arcadepy/resources/auth.py">authorize</a>(\*\*<a href="src/arcadepy/types/auth_authorize_params.py">params</a>) -> <a href="./src/arcadepy/types/authorization_response.py">AuthorizationResponse</a></code>
- <code title="get /v1/auth/status">client.auth.<a href="./src/arcadepy/resources/auth.py">status</a>(\*\*<a href="src/arcadepy/types/auth_status_params.py">params</a>) -> <a href="./src/arcadepy/types/authorization_response.py">AuthorizationResponse</a></code>

# Chat

Types:

```python
from arcadepy.types import ChatMessage, ChatRequest, ChatResponse
```

Methods:

- <code title="post /v1/chat/completions">client.chat.<a href="./src/arcadepy/resources/chat.py">completions</a>(\*\*<a href="src/arcadepy/types/chat_completions_params.py">params</a>) -> <a href="./src/arcadepy/types/chat_response.py">ChatResponse</a></code>

# Health

Types:

```python
from arcadepy.types import HealthSchema
```

Methods:

- <code title="get /v1/health">client.health.<a href="./src/arcadepy/resources/health.py">check</a>() -> <a href="./src/arcadepy/types/health_schema.py">HealthSchema</a></code>

# Tools

Types:

```python
from arcadepy.types import AuthorizeToolRequest, ExecuteToolRequest, ToolDefinition, ToolResponse
```

Methods:

- <code title="post /v1/tools/authorize">client.tools.<a href="./src/arcadepy/resources/tools.py">authorize</a>(\*\*<a href="src/arcadepy/types/tool_authorize_params.py">params</a>) -> <a href="./src/arcadepy/types/authorization_response.py">AuthorizationResponse</a></code>
- <code title="post /v1/tools/execute">client.tools.<a href="./src/arcadepy/resources/tools.py">execute</a>(\*\*<a href="src/arcadepy/types/tool_execute_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_response.py">ToolResponse</a></code>
- <code title="get /v1/tools/definition">client.tools.<a href="./src/arcadepy/resources/tools.py">retrieve_definition</a>(\*\*<a href="src/arcadepy/types/tool_retrieve_definition_params.py">params</a>) -> <a href="./src/arcadepy/types/tool_definition.py">ToolDefinition</a></code>
