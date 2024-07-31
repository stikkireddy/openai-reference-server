/*
 * OpenAI API Reference Server
 *
 * This is an API reference server that mimics openai server.
 *
 * API version: 0.1.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

// CompletionRequestResponseFormat - Similar to chat completion, this parameter specifies the format of output. Only {'type': 'json_object'} or {'type': 'text' } is supported.
type CompletionRequestResponseFormat struct {

	Type string `json:"type"`
}
