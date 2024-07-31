from fastapi import FastAPI, Request, Depends, HTTPException, APIRouter
from fastapi.security import APIKeyHeader

from protocol import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionResponseChoice,
    ChatMessage,
    UsageInfo,
    EmbeddingRequest,
    EmbeddingResponse,
    EmbeddingResponseData,
    CompletionRequest,
    CompletionResponse,
    CompletionResponseChoice,
)

app = FastAPI()

api_key_header = APIKeyHeader(name="api-key", auto_error=False)

API_KEY = "foobar"


# Define a dependency that verifies the API key
def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key


router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.post("/openai/deployments/{deployment_name:path}/chat/completions")
async def create_chat_completion(request: ChatCompletionRequest, raw_request: Request, deployment_name: str):
    print("Received request", request)
    print("Received headers", raw_request.headers)
    print("Received path_name", deployment_name)
    return ChatCompletionResponse(
        model="some-model",
        usage=UsageInfo(
            completion_tokens=100,
            prompt_tokens=200,
            total_tokens=300,
        ),
        choices=[
            ChatCompletionResponseChoice(
                message=ChatMessage(content="Hello, world!", role="system"),
                index=0,
            )
        ],
    )


@router.post("/openai/deployments/{deployment_name:path}/embeddings")
async def create_embedding(request: EmbeddingRequest, raw_request: Request, deployment_name: str):
    print("Received request", request)
    print("Received headers", raw_request.headers)
    print("Received path_name", deployment_name)
    return EmbeddingResponse(
        model="some-model",
        usage=UsageInfo(
            completion_tokens=100,
            prompt_tokens=200,
            total_tokens=300,
        ),
        data=[EmbeddingResponseData(embedding=[0.1, 0.2, 0.3], index=0)],
    )


@router.post("/openai/deployments/{deployment_name:path}/completions")
async def create_completion(request: CompletionRequest, raw_request: Request, deployment_name: str):
    print("Received request", request)
    print("Received headers", raw_request.headers)
    print("Received path_name", deployment_name)
    return CompletionResponse(
        model="some-model",
        usage=UsageInfo(
            completion_tokens=100,
            prompt_tokens=200,
            total_tokens=300,
        ),
        choices=[
            CompletionResponseChoice(
                text="Hello, world!",
                index=0,
            )
        ],
    )


app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
