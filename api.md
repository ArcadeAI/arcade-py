# Shared Types

```python
from arcade_engine.types import AuthorizationResponse
```

# Authorization

Methods:

- <code title="post /v1/auth/authorize">client.authorization.<a href="./src/arcade_engine/resources/authorization.py">authorize</a>(\*\*<a href="src/arcade_engine/types/authorization_authorize_params.py">params</a>) -> <a href="./src/arcade_engine/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="get /v1/auth/status">client.authorization.<a href="./src/arcade_engine/resources/authorization.py">status</a>(\*\*<a href="src/arcade_engine/types/authorization_status_params.py">params</a>) -> <a href="./src/arcade_engine/types/shared/authorization_response.py">AuthorizationResponse</a></code>

# LlmCompletions

Types:

```python
from arcade_engine.types import ChatResponse
```

Methods:

- <code title="post /v1/chat/completions">client.llm_completions.<a href="./src/arcade_engine/resources/llm_completions.py">create</a>(\*\*<a href="src/arcade_engine/types/llm_completion_create_params.py">params</a>) -> <a href="./src/arcade_engine/types/chat_response.py">ChatResponse</a></code>

# Operations

Types:

```python
from arcade_engine.types import HealthSchema
```

Methods:

- <code title="get /v1/health">client.operations.<a href="./src/arcade_engine/resources/operations.py">health</a>() -> <a href="./src/arcade_engine/types/health_schema.py">HealthSchema</a></code>

# Tools

Types:

```python
from arcade_engine.types import Definition, ToolResponse
```

Methods:

- <code title="post /v1/tools/authorize">client.tools.<a href="./src/arcade_engine/resources/tools.py">authorize</a>(\*\*<a href="src/arcade_engine/types/tool_authorize_params.py">params</a>) -> <a href="./src/arcade_engine/types/shared/authorization_response.py">AuthorizationResponse</a></code>
- <code title="get /v1/tools/definition">client.tools.<a href="./src/arcade_engine/resources/tools.py">definition</a>(\*\*<a href="src/arcade_engine/types/tool_definition_params.py">params</a>) -> <a href="./src/arcade_engine/types/definition.py">Definition</a></code>
- <code title="post /v1/tools/execute">client.tools.<a href="./src/arcade_engine/resources/tools.py">execute</a>(\*\*<a href="src/arcade_engine/types/tool_execute_params.py">params</a>) -> <a href="./src/arcade_engine/types/tool_response.py">ToolResponse</a></code>
