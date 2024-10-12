# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from ..types import llm_completion_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.chat_response import ChatResponse

__all__ = ["LlmCompletionsResource", "AsyncLlmCompletionsResource"]


class LlmCompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LlmCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arcade-engine-python#accessing-raw-response-data-eg-headers
        """
        return LlmCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arcade-engine-python#with_streaming_response
        """
        return LlmCompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        frequency_penalty: int | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, int] | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[llm_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        parallel_tool_calls: object | NotGiven = NOT_GIVEN,
        presence_penalty: int | NotGiven = NOT_GIVEN,
        response_format: Literal["json_object", "text"] | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        stop: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        stream_options: llm_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["", "none", "auto", "required", "execute", "generate"] | NotGiven = NOT_GIVEN,
        tools: object | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatResponse:
        """
        Talk to different LLM Chat APIs via OpenAI's API

        Args:
          logit_bias: LogitBias is must be a token id string (specified by their token ID in the
              tokenizer), not a word string. incorrect: `"logit_bias":{"You": 6}`, correct:
              `"logit_bias":{"1639": 6}` refs:
              https://platform.openai.com/docs/api-reference/chat/create#chat/create-logit_bias

          logprobs: LogProbs indicates whether to return log probabilities of the output tokens or
              not. If true, returns the log probabilities of each output token returned in the
              content of message. This option is currently not available on the
              gpt-4-vision-preview model.

          parallel_tool_calls: Disable the default behavior of parallel tool calls by setting it: false.

          stream_options: Options for streaming response. Only set this when you set stream: true.

          tool_choice: This can be either a string or an ToolChoice object.

          top_logprobs: TopLogProbs is an integer between 0 and 5 specifying the number of most likely
              tokens to return at each token position, each with an associated log
              probability. logprobs must be set to true if this parameter is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chat/completions",
            body=maybe_transform(
                {
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                },
                llm_completion_create_params.LlmCompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )


class AsyncLlmCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLlmCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arcade-engine-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLlmCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arcade-engine-python#with_streaming_response
        """
        return AsyncLlmCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        frequency_penalty: int | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, int] | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[llm_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        parallel_tool_calls: object | NotGiven = NOT_GIVEN,
        presence_penalty: int | NotGiven = NOT_GIVEN,
        response_format: Literal["json_object", "text"] | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        stop: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        stream_options: llm_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["", "none", "auto", "required", "execute", "generate"] | NotGiven = NOT_GIVEN,
        tools: object | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatResponse:
        """
        Talk to different LLM Chat APIs via OpenAI's API

        Args:
          logit_bias: LogitBias is must be a token id string (specified by their token ID in the
              tokenizer), not a word string. incorrect: `"logit_bias":{"You": 6}`, correct:
              `"logit_bias":{"1639": 6}` refs:
              https://platform.openai.com/docs/api-reference/chat/create#chat/create-logit_bias

          logprobs: LogProbs indicates whether to return log probabilities of the output tokens or
              not. If true, returns the log probabilities of each output token returned in the
              content of message. This option is currently not available on the
              gpt-4-vision-preview model.

          parallel_tool_calls: Disable the default behavior of parallel tool calls by setting it: false.

          stream_options: Options for streaming response. Only set this when you set stream: true.

          tool_choice: This can be either a string or an ToolChoice object.

          top_logprobs: TopLogProbs is an integer between 0 and 5 specifying the number of most likely
              tokens to return at each token position, each with an associated log
              probability. logprobs must be set to true if this parameter is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                },
                llm_completion_create_params.LlmCompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )


class LlmCompletionsResourceWithRawResponse:
    def __init__(self, llm_completions: LlmCompletionsResource) -> None:
        self._llm_completions = llm_completions

        self.create = to_raw_response_wrapper(
            llm_completions.create,
        )


class AsyncLlmCompletionsResourceWithRawResponse:
    def __init__(self, llm_completions: AsyncLlmCompletionsResource) -> None:
        self._llm_completions = llm_completions

        self.create = async_to_raw_response_wrapper(
            llm_completions.create,
        )


class LlmCompletionsResourceWithStreamingResponse:
    def __init__(self, llm_completions: LlmCompletionsResource) -> None:
        self._llm_completions = llm_completions

        self.create = to_streamed_response_wrapper(
            llm_completions.create,
        )


class AsyncLlmCompletionsResourceWithStreamingResponse:
    def __init__(self, llm_completions: AsyncLlmCompletionsResource) -> None:
        self._llm_completions = llm_completions

        self.create = async_to_streamed_response_wrapper(
            llm_completions.create,
        )
