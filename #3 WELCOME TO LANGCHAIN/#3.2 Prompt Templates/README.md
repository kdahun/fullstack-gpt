prompt는 llm과 의사소통할 수 있는 유일한 방법
prompt 성능이 좋다면 llm의 답변도 좋아진다.

## ChatPromptTemplate은 template을 message로부터 만든다?

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/3681c40b-ef7f-41f6-8a92-7af6a93d2aad)


## PromptTemplate은 그냥 String을 이용해서 template를 만든다.

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/72eb9d53-1556-4f1c-b55d-942a17a00a1a)

먼저 template을 만든다.
template에 넣을 값을 .format에서 넣어 준다.
(이로 인해 검증을 따로 할 필요가 없어진다?.)
.predict에 넣어주면 원하는 답변이 나온다.

