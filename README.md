# azure openai compatible reference server for chat completions

This is a simple reference server for using the OpenAI GPT-3 API to generate chat completions. It is designed to be used with the Azure Bot Service, but can be used with any chatbot platform that supports HTTP POST requests.
This is based on the vllm openai reference server with a few tweaks to be compatible with azure openai.

Change the logic in server.py to handle the request. This makes your "service" openai compatible and can 
integrate easily with available openai integrations.

If you want to quickly test this you can use a service like ngrok and integrate anything that supports chat completions.

Feel free to contribute to embeddings, completions, multi modal, etc.