gen-go:
	openapi-generator generate -i openapi/openapi.json -g go-gin-server -o golang-gin --additional-properties=isGoSubmodule=true --git-repo-id="example" --git-user-id="stikkireddy"

run-go:
	cd golang-gin && go mod tidy && go run main.go

run-python:
	cd python && make run
