# Shared Types

```python
from arcade_engine.types import AuthorizationResponse
```

# Auth

Methods:

- <code title="post /v1/auth/authorize">client.auth.<a href="./src/arcade_engine/resources/auth.py">authorization</a>(\*\*<a href="src/arcade_engine/types/auth_authorization_params.py">params</a>) -> <a href="./src/arcade_engine/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="get /v1/auth/status">client.auth.<a href="./src/arcade_engine/resources/auth.py">status</a>(\*\*<a href="src/arcade_engine/types/auth_status_params.py">params</a>) -> <a href="./src/arcade_engine/types/shared/authorization_response.py">AuthorizationResponse</a></code>

# Chat

Types:

```python
from arcade_engine.types import ChatResponse
```

Methods:

- <code title="post /v1/chat/completions">client.chat.<a href="./src/arcade_engine/resources/chat.py">completions</a>(\*\*<a href="src/arcade_engine/types/chat_completions_params.py">params</a>) -> <a href="./src/arcade_engine/types/chat_response.py">ChatResponse</a></code>

# Health

Types:

```python
from arcade_engine.types import HealthSchema
```

Methods:

- <code title="get /v1/health">client.health.<a href="./src/arcade_engine/resources/health.py">list</a>() -> <a href="./src/arcade_engine/types/health_schema.py">HealthSchema</a></code>

# Tools

Types:

```python
from arcade_engine.types import Definition, Response
```

Methods:

- <code title="get /v1/tools/definition">client.tools.<a href="./src/arcade_engine/resources/tools.py">retrieve</a>(\*\*<a href="src/arcade_engine/types/tool_retrieve_params.py">params</a>) -> <a href="./src/arcade_engine/types/definition.py">Definition</a></code>
- <code title="post /v1/tools/authorize">client.tools.<a href="./src/arcade_engine/resources/tools.py">authorize</a>(\*\*<a href="src/arcade_engine/types/tool_authorize_params.py">params</a>) -> <a href="./src/arcade_engine/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="post /v1/tools/execute">client.tools.<a href="./src/arcade_engine/resources/tools.py">execute</a>(\*\*<a href="src/arcade_engine/types/tool_execute_params.py">params</a>) -> <a href="./src/arcade_engine/types/response.py">Response</a></code>
