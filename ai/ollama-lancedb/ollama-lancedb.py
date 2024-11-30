import pandas as pd
import lancedb
import time
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import EmbeddingFunctionRegistry
from utils import view

df = pd.read_csv("data/sentences.csv")
df.iloc[0]

registry = EmbeddingFunctionRegistry.get_instance()
embedder = registry.get("ollama").create(name="nomic-embed-text")

class Schema(LanceModel):
  text: str = embedder.SourceField()
  vector: Vector(embedder.ndims()) = embedder.VectorField()
  index: int
  title: str
  url: str

db = lancedb.connect("./lancedb")
table = db.create_table("sentences", schema=Schema)
table.add(df)
table.to_pandas().iloc[0]

rows = (table
  .search(question)
  .limit(3)
  .to_pydantic(Schema)
)

view(rows)

def extract_context(rows):
  return sorted(
    [
      {"title": r.title, "text": r.text, "index": r.index} 
      for r in rows
    ], 
    key=lambda x: x['index']
  )

view(extract_context(rows))

SYSTEM = """
You will receive paragraphs of text from a news article. 
Answer the subsequent question using that context.
"""

question = "What were the iPhone's best new features"
rows = (table.search(question).limit(3).to_pydantic(Schema))
context = extract_context(rows)
stream = ollama.chat(
  model="llama3.1", stream=True,
  messages = [
    { "role": "system", 'content': SYSTEM},
    { "role": "user", 'content': f"Context: {context}"},
    { "role": "user", 'content': f"Question: {question}"}
  ]
)
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)