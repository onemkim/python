Reference:
- https://medium.com/kinomoto-mag/local-ai-powered-web-and-local-docs-scraping-at-no-cost-ba027e98380a
- https://ollama.com/library/nomic-embed-text
- https://scrapegraph-ai.readthedocs.io/en/latest/scrapers/llm.html#azure
- https://www.datacamp.com/tutorial/scrapegraphai-web-scraping
- https://scrapegraph-doc.onrender.com/docs/intro  

``` sh
ollama pull nomic-embed-text
pip3 install scrapegraphai
playwright install
```

``` sh
curl http://localhost:11434/api/embeddings -d '{
  "model": "nomic-embed-text",
  "prompt": "The sky is blue because of Rayleigh scattering"
}'
```