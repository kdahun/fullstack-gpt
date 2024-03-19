import time
import streamlit as st

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, CacheBackedEmbeddings
from langchain.vectorstores import FAISS
from langchain.storage import LocalFileStore
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="🍕"
)

def embed_file(file):
    st.write(file)
    file_content = file.read()
    file_path = f"./.cache/files/{file.name}"


    with open(file_path,"wb") as f:
        f.write(file_content)
    
    cache_dir = LocalFileStore(f"./.cache/embeddings/{file.name}")

    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
    )
    
    # txt,doc,pdf.html,excel 등등 다양한 file들을 load 할 수 있다.
    loader = UnstructuredFileLoader("./.cache/files/KAIA-JKIICE.pdf")

    docs = loader.load_and_split(text_splitter=splitter)

    # Embedding은 text에 의미별로 적절한 점수를 부여해서 vector 형식으로 표현한것,

    embeddings = OpenAIEmbeddings()

    # ChacheBackedEmbedding을 사용하여 만들어진 Embedding을 cache(저장) 한다.

    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings,cache_dir)

    # Vector store를 호출 해주고 FAISS사용
    # from_documents 메서드는 document 별로 embedding 작업 후 결과를 저장한 vector store를 반환
    # 이를 이용해 document 검색도 하고, 연관성이 높은 document들을 찾는다.
    vectorstore = FAISS.from_documents(docs,cached_embeddings)

    # retriver는 document들의 list를 반환
    retriever = vectorstore.as_retriever()
    
    return retriever



st.title("Document GPT")

st.markdown("""
            Welcome

            Use this chatbot to ask questions to an AI about your files!

            """)

file = st.file_uploader("Upload a .txt .pdf .docx file", type=["pdf","txt","docx"])

if file:
    retriever = embed_file(file)
    s = retriever.invoke("winston")
    s

        