memory를 chain과 연결하는 방법과 두 종류의 chain을 사용해 연결하는 방법

LLM chain을 사용(LLM chain은 off-the-shelf-chain이다- off-the-shelf는 일반적인 목적을 가진 chain을 의미 / 이전에 배운 것은 langchain expression 언어를 활용했다.)

langchain은 verbose라는 아주 좋은 속성을 가지고 있다.
(이 값을 chain에게 전달하면 chain을 실행했을 때 chain의 프롬프트 로그들을 확일할 수 있다.)

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/d78c19a2-b147-4d50-9cf4-6c44ec24cdfd)

이렇게만 하면 대화의 내역이 프롬프트에 계속 추가되지 않았다는 것을 알수 있다.
하지만 memory.load_memory_variables({})를 입력하면 memory에는 요약한 내용(history)과 이전 최근 대화내용이 저장되어있음을 확인할 수 있다.
=> 따라서 우리가 원하는 방식으로 프롬프트에게 대화 기록을 추가할 수 있도록 만들어야한다.


문자열 형태로 된 프롬프트 템플릿에 대화 기록을 추가하고 싶을때 하는 일

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/8bd5a800-dd41-41e1-b2df-8bc391d402cb)
