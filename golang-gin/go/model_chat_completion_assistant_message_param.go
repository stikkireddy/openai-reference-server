/*
 * OpenAI API Reference Server
 *
 * This is an API reference server that mimics openai server.
 *
 * API version: 0.1.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

type ChatCompletionAssistantMessageParam struct {

	Role string `json:"role"`

	Content *string `json:"content,omitempty"`

	FunctionCall *FunctionCall `json:"function_call,omitempty"`

	Name string `json:"name,omitempty"`

	ToolCalls []ChatCompletionMessageToolCallParam `json:"tool_calls,omitempty"`
}
