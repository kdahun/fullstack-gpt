import time
import streamlit as st

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="🍕"
)

st.title("Document GPT")


# session_state가 비어있는지 아닌지 확인
# 만약 비어있다면 초기화 시켜준다.
if "messages" not in st.session_state:
    # 여러번의 재실행에도 data가 보존될 수 있게 해준다.
    st.session_state["messages"] = []

# st.write(st.session_state["messages"])

def send_message(message,role,save=True):
    with st.chat_message(role):
        st.write(message)
    # 만약 save파라미터가 없다면 아래 for문에서 이전 대화내용을 출력해 줄뿐만 아니라 추가도 해줘서
    # for문이 무한 반복 된다. 그래서 save 파라미터를 추가해 만약 읽기만 할때는 세션에 추가해주지 않도록
    # save = false를 넣어준다.
    if save:
        st.session_state["messages"].append({"message":message,"role":role})

for message in st.session_state["messages"]:
    send_message(message["message"],message["role"],save=False)


# 사용자가 보낸 메시지를 message 변수에 넣어준다.
message = st.chat_input("Send a message to the ai")

# 만약 메시지가 있으면
if message:
    # 사용자가 말한 메시지를 위에 보내준다.
    send_message(message,"human")
    time.sleep(2)

    # 미리 입력해 놓은 ai 답변을 사용자가 메시지를 보내고 2초 뒤에 출력해준다.
    send_message(f"You said: {message}","ai")

    # 캐쉬를 확인하고 싶을때
    with st.sidebar:
        st.write(st.session_state)
