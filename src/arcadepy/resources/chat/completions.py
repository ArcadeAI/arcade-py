# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chat import completion_create_params
from ..._base_client import make_request_options
from ...types.chat_response import ChatResponse
from ...types.chat_message_param import ChatMessageParam

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, int] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        messages: Iterable[ChatMessageParam] | Omit = omit,
        model: str | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: SequenceNotStr[str] | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: completion_create_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: object | Omit = omit,
        tools: object | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatResponse:
        """
        Interact with language models via OpenAI's chat completions API

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
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        frequency_penalty: float | Omit = omit,
        logit_bias: Dict[str, int] | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        messages: Iterable[ChatMessageParam] | Omit = omit,
        model: str | Omit = omit,
        n: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        seed: int | Omit = omit,
        stop: SequenceNotStr[str] | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: completion_create_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: object | Omit = omit,
        tools: object | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatResponse:
        """
        Interact with language models via OpenAI's chat completions API

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
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
