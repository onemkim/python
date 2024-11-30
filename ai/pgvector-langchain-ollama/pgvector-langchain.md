Reference:
- https://api.python.langchain.com/en/latest/vectorstores/langchain_postgres.vectorstores.PGVector.html
- https://blog.gopenai.com/query-your-postgresql-database-with-langchain-and-llama-3-1-exploring-llms-1-ba3a9560c0d1
- https://python.langchain.com/docs/integrations/text_embedding/ollama/
  
## Steps.
Refer: ai/pgvector

1. In Docker, run pgvector images
``` sh
# Pulling image the latest just postgres. But it doesn't include vector extension which is required for pgVector
docker pull postgres

# pgvector image
docker pull pgvector/pgvector:0.7.4-pg17

# Running DB
docker run -d \
  --name pgvector \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=example \
  -v psql:/var/lib/postgresql/data \
  -p 5555:5432 \
  pgvector/pgvector:0.7.4-pg17
```

2. Run pgAdmin

3. Install

``` sh
pip3 install -qU langchain-postgres
pip3 install -qU langchain_ollama
```
