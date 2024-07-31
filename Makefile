gen-go:
	openapi-generator generate -i openapi/openapi.json -g go-gin-server -o golang --additional-properties=isGoSubmodule=true --git-repo-id="reference-openai-server" --git-user-id="stikkireddy"

run-go:
	cd golang && go mod tidy && go run main.go

run-python:
	cd python && make run
