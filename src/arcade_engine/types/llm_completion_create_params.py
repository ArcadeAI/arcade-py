# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LlmCompletionCreateParams", "Message", "MessageToolCall", "MessageToolCallFunction", "StreamOptions"]


class LlmCompletionCreateParams(TypedDict, total=False):
    frequency_penalty: int

    logit_bias: Dict[str, int]
    """
    LogitBias is must be a token id string (specified by their token ID in the
    tokenizer), not a word string. incorrect: `"logit_bias":{"You": 6}`, correct:
    `"logit_bias":{"1639": 6}` refs:
    https://platform.openai.com/docs/api-reference/chat/create#chat/create-logit_bias
    """

    logprobs: bool
    """
    LogProbs indicates whether to return log probabilities of the output tokens or
    not. If true, returns the log probabilities of each output token returned in the
    content of message. This option is currently not available on the
    gpt-4-vision-preview model.
    """

    max_tokens: int

    messages: Iterable[Message]

    model: str

    n: int

    parallel_tool_calls: object
    """Disable the default behavior of parallel tool calls by setting it: false."""

    presence_penalty: int

    response_format: Literal["json_object", "text"]

    seed: int

    stop: List[str]

    stream: bool

    stream_options: StreamOptions
    """Options for streaming response. Only set this when you set stream: true."""

    temperature: float

    tool_choice: Literal["", "none", "auto", "required", "execute", "generate"]
    """This can be either a string or an ToolChoice object."""

    tools: object

    top_logprobs: int
    """
    TopLogProbs is an integer between 0 and 5 specifying the number of most likely
    tokens to return at each token position, each with an associated log
    probability. logprobs must be set to true if this parameter is used.
    """

    top_p: float

    user: str


class MessageToolCallFunction(TypedDict, total=False):
    arguments: str

    name: str


class MessageToolCall(TypedDict, total=False):
    id: str

    function: MessageToolCallFunction

    type: Literal["function"]


class Message(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[str]
    """The role of the author of this message.

    One of system, user, tool, or assistant.
    """

    name: str
    """tool Name"""

    tool_call_id: str
    """tool_call_id"""

    tool_calls: Iterable[MessageToolCall]
    """tool calls if any"""


class StreamOptions(TypedDict, total=False):
    include_usage: bool
    """
    If set, an additional chunk will be streamed before the data: [DONE] message.
    The usage field on this chunk shows the token usage statistics for the entire
    request, and the choices field will always be an empty array. All other chunks
    will also include a usage field, but with a null value.
    """