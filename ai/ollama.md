## Ollama
1. Download llama: https://ollama.com/download
2. Install ollama: run install file
3. Install model : https://github.com/ollama/ollama/blob/main/docs/faq.md
- For Windows:  
  - C:\users\[user]\AppData\Local\Programs\Ollama
  - C:\users\[user]\.ollama
- For MAC: Min's Personal MacBook Pro 
  - /Users/minkim/.ollama/models

``` sh
# Install and run model: https://github.com/ollama/ollama
ollama run mistral
# llama3.2:1b 1.3 GM
ollama pull llama3.2:1b

# Pull embedding model. It doesn't need to be running - 274 MB
ollama pull ollama/nomic-embed-text 
# or 
ollama pull nomic-embed-text 


#Show model info: 
ollama show llama3.2:1b

# List models on your computer: 
ollama list

# List which models are currently loaded: 
ollama ps

# Stop ollama: 
ollama stop llama3.2:1b

# stop model
/bye
```
4. Python programming with ollama
``` sh
pip3 install ollama

```


## ollama API
API documentation: https://github.com/ollama/ollama/blob/main/docs/api.md

- Generate :
``` sh
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "Why is the sky blue?",
  "format": "json",
  "stream": false
}'
```

- Chat:
``` sh
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2:1b",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}'
```
- chat with function - need to confirm it..
``` sh
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2:1b",
  "messages": [
    {
      "role": "user",
      "content": "What is the weather today in Paris?"
    }
  ],
  "stream": false,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather for a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The location to get the weather for, e.g. San Francisco, CA"
            },
            "format": {
              "type": "string",
              "description": "The format to return the weather in, e.g. 'celsius' or 'fahrenheit'",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location", "format"]
        }
      }
    }
  ]
}'
``` 
