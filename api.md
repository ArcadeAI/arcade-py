# Shared Types

```python
from arcadepy.types import AuthorizationResponse
```

# Auth

Methods:

- <code title="post /v1/auth/authorize">client.auth.<a href="./src/arcadepy/resources/auth.py">authorization</a>(\*\*<a href="src/arcadepy/types/auth_authorization_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="get /v1/auth/status">client.auth.<a href="./src/arcadepy/resources/auth.py">status</a>(\*\*<a href="src/arcadepy/types/auth_status_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/authorization_response.py">AuthorizationResponse</a></code>

# Chat

Types:

```python
from arcadepy.types import ChatResponse
```

Methods:

- <code title="post /v1/chat/completions">client.chat.<a href="./src/arcadepy/resources/chat.py">completions</a>(\*\*<a href="src/arcadepy/types/chat_completions_params.py">params</a>) -> <a href="./src/arcadepy/types/chat_response.py">ChatResponse</a></code>

# Health

Types:

```python
from arcadepy.types import HealthSchema
```

Methods:

- <code title="get /v1/health">client.health.<a href="./src/arcadepy/resources/health.py">list</a>() -> <a href="./src/arcadepy/types/health_schema.py">HealthSchema</a></code>

# Tools

Types:

```python
from arcadepy.types import Definition, Response
```

Methods:

- <code title="get /v1/tools/definition">client.tools.<a href="./src/arcadepy/resources/tools.py">retrieve</a>(\*\*<a href="src/arcadepy/types/tool_retrieve_params.py">params</a>) -> <a href="./src/arcadepy/types/definition.py">Definition</a></code>
- <code title="post /v1/tools/authorize">client.tools.<a href="./src/arcadepy/resources/tools.py">authorize</a>(\*\*<a href="src/arcadepy/types/tool_authorize_params.py">params</a>) -> <a href="./src/arcadepy/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="post /v1/tools/execute">client.tools.<a href="./src/arcadepy/resources/tools.py">execute</a>(\*\*<a href="src/arcadepy/types/tool_execute_params.py">params</a>) -> <a href="./src/arcadepy/types/response.py">Response</a></code>
