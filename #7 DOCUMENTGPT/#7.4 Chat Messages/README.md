
# Streamlit이 가진 Chat element를 사용하는 방법

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/170369a0-726c-4bb9-878a-1572726ba429)

```
with st.chat_message("human"):
  st.write("Hellooo")

with st.chat_message("ai"):
  st.write("how are you")

st.chat_input("Send a message to the ai")
  
```
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/f3f679bf-a066-4f06-8552-75db3119902f)

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/7c1d96f2-b97d-4776-96cf-87707b0d2c88)

하지만 이 코드에는 중요한 문제가 있는 데,
바로 message 들에 대한 기록이 없다.
(streamlit에서 입력?이 있으면 DocumentGPT.py 파이썬 코드를 처음부터 다시 읽는다.)

## Session state
: 여러번의 재실행에도 data가 보존 될 수 있게 해준다.

### initialize values in session state
```
if "messages" not in st.session_state:
  st.session_state["messages"] = []
```
현재 세션의 상태에서 "messages"라는 키가 있는지를 확인을 하고, 만약 "messages" 키가 세션 상태에 없다면 새로운 빈 리스트가 messages라는 키로 세션 상태에 추가된다. 이를 통해 나중에 이 세션에서 "messages"를 사용할 때, 초기화되지 않고 이전에 저장된 데이터를 보존할 수 있다.
