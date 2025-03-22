import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:5272/v1/",
    api_key="xyz" # required by API but not used
)

st.title("Chat with Phi-3")
query = st.chat_input("Enter query:")

if query:
    with st.chat_message("user"):
        st.write(query)

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user","content": "You are a university professor."},
            {"role": "user", "content": query}
        ],
        model="mistral-7b-v02-int4-cpu",
    )
    with st.chat_message("assistant"):
        st.write(chat_completion.choices[0].message.content)
