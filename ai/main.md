Reference:
- https://github.com/hnawaz007/pythondataanalysis/blob/main/RAG%20App/RAG%20with%20PDF%20Document.ipynb
- Overall: https://www.youtube.com/watch?v=Ii4ouKEUgz4
- ollama quick tutorial: https://www.youtube.com/watch?v=CE9umy2NlhE

## Prerequisites:
1. Setup Huggingface

## Huggingface 
1. Create huggingface account: https://huggingface.co/ 
2. Create Access Tokens: https://huggingface.co/settings/tokens  
   1. token1 and “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”


## Packages

``` sh
# conda

# langchain: https://python.langchain.com/v0.1/docs/get_started/installation/
conda install langchain -c conda-forge

# openai: https://anaconda.org/conda-forge/openai
conda install conda-forge::openai

# chromadb: https://anaconda.org/conda-forge/chromadb
conda install conda-forge::chromadb

# pip3
# https://python.langchain.com/v0.1/docs/get_started/installation/
pip3 install langchain-core
pip3 install langchain-community
pip3 install pypdf
pip3 install fastembed
# https://pypi.org/project/scrapegraphai/
pip3 install scrapegraphai  
pip3 install chromadb
pip3 install huggingface-hub
```


## Local LLM 
- Ollama: https://ollama.com/
- LM Studio: https://lmstudio.ai/
- AutoGen Studio: https://autogen-studio.com/autogen-studio-ui


## Streamlit
1. Run streamlit
``` sh
streamlit run app.py
```

## ollama with conda 

``` sh
conda env list
conda activate env312
ollama run llama3.2:1b // pull model if it is not downloaded before and run
```
