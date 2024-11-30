from scrapegraphai.graphs import SmartScraperGraph

graph_config = {
    "llm": {
        "model": "ollama/llama3.2:1b",
        "temperature": 0,
        "format": "json", 
        "base_url": "http://localhost:11434", 
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434", 
    },
    "verbose": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the repositories",
    source="https://github.com/onemkim",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)
