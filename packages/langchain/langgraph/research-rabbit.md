Reference:
- https://github.com/langchain-ai/research-rabbit
- https://www.youtube.com/watch?v=XGuTzHoqlj8

Research Rabbit is a web research and summarization assistant that autonomously goes down the rabbit-hole of any user-defined topic. It uses an LLM to generate a search query based on the user's topic, gets web search results, and uses an LLM to summarize the results. It then uses an LLM to reflect on the summary, examines knowledge gaps, and generates a new search query to fill the gaps. This repeats for a user-defined number of cycles, updating the summary with new information from web search and provided the user a final markdown summary with all sources used. It is configured to run with fully local LLMs (via Ollama)!

``` sh
# Pull a local LLM that you want to use from Ollama:
ollama pull llama3.2

# For free web search (up to 1000 requests)
export TAVILY_API_KEY=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

# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
# Use
pip install uv
# Clone GIT
git clone https://github.com/langchain-ai/research-rabbit.git

cd research-rabbit
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev
```