# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types import Completion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: OpenAI) -> None:
        completion = client.completions.create(
            model="string",
            prompt="This is a test.",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: OpenAI) -> None:
        completion = client.completions.create(
            model="string",
            prompt="This is a test.",
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=0,
            stop="\n",
            stream=False,
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: OpenAI) -> None:
        response = client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: OpenAI) -> None:
        with client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(Completion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: OpenAI) -> None:
        completion_stream = client.completions.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        )
        completion_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: OpenAI) -> None:
        completion_stream = client.completions.create(
            model="string",
            prompt="This is a test.",
            stream=True,
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=0,
            stop="\n",
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        completion_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: OpenAI) -> None:
        response = client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: OpenAI) -> None:
        with client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        completion = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncOpenAI) -> None:
        completion = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=0,
            stop="\n",
            stream=False,
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(Completion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        completion_stream = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncOpenAI) -> None:
        completion_stream = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
            stream=True,
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=0,
            stop="\n",
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
