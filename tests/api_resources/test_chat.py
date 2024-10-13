# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import ArcadeAI, AsyncArcadeAI
from tests.utils import assert_matches_type
from arcadepy.types import ChatResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_completions(self, client: ArcadeAI) -> None:
        chat = client.chat.completions()
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    def test_method_completions_with_all_params(self, client: ArcadeAI) -> None:
        chat = client.chat.completions(
            frequency_penalty=0,
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            messages=[
                {
                    "content": "content",
                    "role": "role",
                    "name": "name",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "role",
                    "name": "name",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "role",
                    "name": "name",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                    ],
                },
            ],
            model="model",
            n=0,
            parallel_tool_calls={},
            presence_penalty=0,
            response_format="json_object",
            seed=0,
            stop=["string", "string", "string"],
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="",
            tools={},
            top_logprobs=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_completions(self, client: ArcadeAI) -> None:
        response = client.chat.with_raw_response.completions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_completions(self, client: ArcadeAI) -> None:
        with client.chat.with_streaming_response.completions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_completions(self, async_client: AsyncArcadeAI) -> None:
        chat = await async_client.chat.completions()
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    async def test_method_completions_with_all_params(self, async_client: AsyncArcadeAI) -> None:
        chat = await async_client.chat.completions(
            frequency_penalty=0,
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            messages=[
                {
                    "content": "content",
                    "role": "role",
                    "name": "name",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "role",
                    "name": "name",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "role",
                    "name": "name",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        },
                    ],
                },
            ],
            model="model",
            n=0,
            parallel_tool_calls={},
            presence_penalty=0,
            response_format="json_object",
            seed=0,
            stop=["string", "string", "string"],
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="",
            tools={},
            top_logprobs=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_completions(self, async_client: AsyncArcadeAI) -> None:
        response = await async_client.chat.with_raw_response.completions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_completions(self, async_client: AsyncArcadeAI) -> None:
        async with async_client.chat.with_streaming_response.completions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
