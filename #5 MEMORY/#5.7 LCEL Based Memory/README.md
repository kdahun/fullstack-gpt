
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/729584ce-ca0f-4ae2-8203-a9029c7f3abd)

langchain은 load_memory 함수를 먼저 호출(기본적으로 프롬프트가 필요로 하는 chat_history key 내부에 넣어준다.)

그후 프롬프트로 chat_history를 넘겨준다.(RunnablePassthrough가 하는 일, 프롬프트가 format되기 전에 우리가 함수를 실행시키는 걸 허락해준다. 그리고 이 함수에서 우리가 원하는 어떤 값이든 변수에 할당할 수 있다.)

근데 이렇게만 하면 오류가 발생한다.

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/21ecad6c-59b2-4256-8a19-dc5ae2660b20)

load_memory 함수는 argument를 하나 받아야 하는데 그런 공간을 안만들어서이다.
보다시피 argument는 0개인데, 실행을 시작하면 하나의 argument가 제공된다.
왜냐하면 runnablePassthrough.assign()을 할 때 사용자의 input을 받기 때문이다.

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/3b899f4d-2f88-4495-9ab6-7c9ba0a06bc5)

이렇게 
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/fb9dabd9-e813-4eef-90b8-25f9a26b7fb5)
input인 My name is Nico를 넣어주게 만들어주면 된다.

메모리에 question들이 저장되도록 해야된다. => 제일 좋은 방법은 체인을 호출하는 함수를 만드는 것이다?

기본적으로 메모리 키가 history이기 때문에 모든 hat_history를 이걸로 대체할 수 잇다.
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/499deb14-a62d-4a16-a1f4-a23135da2e5e)

memory_key="chat_history" 생략 가능

복습
load_memory_variables는 메모리를 로드시키는 것
save_context는 사람과 AI의 메시지인 input과 output을 메모리에 저장
