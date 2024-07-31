from fastapi import FastAPI, Request, Depends, HTTPException, APIRouter
from fastapi.security import APIKeyHeader

from protocl import ChatCompletionRequest, ChatCompletionResponse, ChatCompletionResponseChoice, ChatMessage, UsageInfo

app = FastAPI()

api_key_header = APIKeyHeader(name="api-key", auto_error=False)

API_KEY = "foobar"


# Define a dependency that verifies the API key
def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key


router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.post("/{path_name:path}/chat/completions")
async def create_chat_completion(request: ChatCompletionRequest,
                                 raw_request: Request):
    print("Received request", request)
    print("Received headers", raw_request.headers)
    return ChatCompletionResponse(
        model="some-model",
        usage=UsageInfo(
            completion_tokens=100,
            prompt_tokens=200,
            total_tokens=300,
        ),
        choices=[ChatCompletionResponseChoice(
            message=ChatMessage(content="Hello, world!", role="system"),
            index=0,
        )]
    )


app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
