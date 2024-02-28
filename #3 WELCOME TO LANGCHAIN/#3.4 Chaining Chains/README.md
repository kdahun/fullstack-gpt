![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/ce549488-d4fa-4d8e-a12d-6556cfe5e0e0)

OpenAI Api에서 볼수있는 이것이 바로 gpt 3.5 turbo에서 응답 받는 방법(OpenAI Python package만 사용하는 경우)

* Lang Chain은 응답을 파싱하고 AI Message로 변환

# expression language의 구성요소(component)
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/611af37f-20ff-4996-8265-9d3f638c9b9f)

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/10909317-009c-4993-8d62-753040470adf)


ex)
chain = template | chat | CommaOutputParser()
* chain.invoke를 호출하면 template이 가장 먼저 호출 된다.(dictionary는 prompt template으로 보내진다.



streaming은 우리가 model의 응답(response)이 생성되는걸 볼수있게 해준다.(응답이 끝날때까지 기다리기만 하지 않아도 된다.

callbacks => 응답의 진행을 볼수있게된다.
