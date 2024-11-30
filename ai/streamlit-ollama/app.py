import streamlit as st
import json
import requests

st.set_page_config(page_title="Chatbot - Powered by Open Source LLM")

## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    #message_placeholder = st.empty()
#    full_response = ""
#    #messages.append({"role": "user", "content": message.content})
#    output =  litellm.completion(
#            model="ollama/llama3.2:1b",
#            messages=prompt,
#            api_base="http://localhost:11434/",
#            stream=True
#    )
#    #
#    for chunk in output:
#        if chunk:
#            content = chunk.choices[0].delta.content
#            if content:
#                full_response += content
#         #
#    return full_response
    
    model = "llama3.2:1b" 
    r = requests.post(
        "http://localhost:11434/api/chat",
        json={"model": model, "messages": prompt, "stream": True},
	    stream=True
    )

    #r.raise_for_status()
    
    output = ""

    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
        if body.get("done") is False:
            message = body.get("message", "")
            content = message.get("content", "")
            output += content
            # the response streams one token at a time, print that as we receive it
            print(content, end="", flush=True)

        if body.get("done", False):
            message["content"] = output
            return message


st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Ollama & Lllama3.2:1b LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = generate_response(st.session_state.messages)
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)