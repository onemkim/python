## SaaS
```
Username: neo4j
Password: 2lB8pI5UkNB2Wav9ap460d9mLKgj7dCtrI7qoIBz6Yk
Instance: instance01
```



``` sh
# https://neo4j.com/docs/operations-manual/current/docker/introduction/#docker-simple-volumes
docker run -d \
    --name ai-neo4j \
    --restart always \
    --publish=7474:7474 --publish=7687:7687 \
    --env NEO4J_AUTH=neo4j/password \
    --volume=/Users/minkim/Documents/Working/docker-data-volume:/data \
    neo4j:5.25.1 
    
# Bolt enabled on 0.0.0.0:7687.
# HTTP enabled on 0.0.0.0:7474.



# APOC
# https://neo4j.com/labs/apoc/5/installation/#docker
docker run -d \
    -p 7474:7474 -p 7687:7687 \
    -v /Users/minkim/Documents/Working/neo4j/data:/data -v /Users/minkim/Documents/Working/neo4j/plugins:/plugins \
    --name ai-neo4j \
    --restart always \
    --env NEO4J_AUTH=neo4j/password \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4J_PLUGINS=\[\"apoc-extended\"\] \
    neo4j:5.25.1


# https://anaconda.org/conda-forge/neo4j-python-driver
conda install conda-forge::neo4j-python-driver
```