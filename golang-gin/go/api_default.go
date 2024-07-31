/*
 * OpenAI API Reference Server
 *
 * This is an API reference server that mimics openai server.
 *
 * API version: 0.1.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

import (
	"github.com/gin-gonic/gin"
)

type DefaultAPI struct {
}

// Post /openai/deployments/:deployment_name/chat/completions
// Create Chat Completion 
func (api *DefaultAPI) CreateChatCompletionOpenaiDeploymentsDeploymentNameChatCompletionsPost(c *gin.Context) {
	// Your handler implementation
	c.JSON(200, gin.H{"status": "OK"})
}

// Post /openai/deployments/:deployment_name/completions
// Create Completion 
func (api *DefaultAPI) CreateCompletionOpenaiDeploymentsDeploymentNameCompletionsPost(c *gin.Context) {
	// Your handler implementation
	c.JSON(200, gin.H{"status": "OK"})
}

// Post /openai/deployments/:deployment_name/embeddings
// Create Embedding 
func (api *DefaultAPI) CreateEmbeddingOpenaiDeploymentsDeploymentNameEmbeddingsPost(c *gin.Context) {
	// Your handler implementation
	c.JSON(200, gin.H{"status": "OK"})
}

