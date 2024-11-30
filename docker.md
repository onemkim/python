Reference:

# Docker
- Install Docker: https://app.docker.com/

## PostgreSQL 
Reference:
- https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/

Docker Hub for Postgres
https://hub.docker.com/_/postgres

``` sh
# Pulling image the latest
docker pull postgres

# Executing image
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres


docker run -d \
  --name pgvector \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=example \
  -v psql:/var/lib/postgresql/data \
  -p 5555:5432 \
  postgres:latest
```
