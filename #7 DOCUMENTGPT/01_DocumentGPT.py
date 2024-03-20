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
from langchain.callbacks.base import BaseCallbackHandler

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="🍕"
)

# callback handler는 event들을 듣는 여러 기능들을 가진다.
class ChatCallbackHandler(BaseCallbackHandler):
    message = ""

    # 이 함수에서는 무수히 많은 argument와 keyword argument를 받고 있다.
    def on_llm_start(self,*args,**kwargs):
        self.message_box = st.empty()

    def on_llm_end(self,*args,**kwargs):
        save_message(self.message,"ai")
    def on_llm_new_token(self,token,*args,**kwargs):
        self.message += token
        self.message_box.markdown(self.message)

llm = ChatOpenAI(
    temperature=0.1,
    streaming=True,
    callbacks=[
        ChatCallbackHandler(),
    ]
)

@st.cache_data(show_spinner="Embedding file...")
def embed_file(file):
    # st.write(file)
    file_content = file.read()
    file_path = f"./.cache/files/{file.name}"

    # 사용자가 올린 파일을 files 폴더에 저장
    with open(file_path,"wb") as f:
        f.write(file_content)
    
    cache_dir = LocalFileStore(f"./.cache/embeddings/{file.name}")

    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
    )
    
    # txt,doc,pdf.html,excel 등등 다양한 file들을 load 할 수 있다.
    loader = UnstructuredFileLoader(file_path)

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

def save_message(message,role):
    st.session_state["messages"].append({"message":message,"role":role})

def send_message(message,role,save=True):
    with st.chat_message(role):
        st.markdown(message)
    if save:
        st.session_state["messages"].append({"message":message,"role":role})

def paint_history():
    for message in st.session_state["messages"]:
        send_message(message["message"],message["role"],save = False)

def format_docs(docs):
    return "\n\n".join(document.page_content for document in docs)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     """
     Answer the question using ONLY the following context. If you don't know the answer
     just say you don't know. DON'T make anything up.

     Context:{context}
     """,),
     ("human","{question}"),
])

st.title("Document GPT")

st.markdown("""
            Welcome

            Use this chatbot to ask questions to an AI about your files!

            Upload your files on the sidebar.
            """)

with st.sidebar:
    file = st.file_uploader("Upload a .txt .pdf .docx file", type=["pdf","txt","docx"])


if file:
    retriever = embed_file(file)
    
    send_message("I'm ready! Ask away!","ai", save=False)

    message = st.chat_input("Ask anything about your file...")
    paint_history()
    if message:
        send_message(message,"human")
        chain = {
            "context":retriever | RunnableLambda(format_docs),
            "question":RunnablePassthrough()
        } | prompt | llm
        with st.chat_message("ai"):
            response = chain.invoke(message)
else:
    st.session_state["messages"] = []
        