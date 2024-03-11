langchain은 Off-the-shelf Chain이 있는데
이건 자동으로 LLM으로부터 응답값을 가져오고 memory를 업데이트 해준다.
(하지만 memory의 기록들을 프롬프트에 넣어줘야한다.)


![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/8671738e-9a3c-4453-8229-674a786d37cb)
* prompt는 MessagesPlaceholder를 가지고 있고, chat_history라는 변수명을 가지고 있는 값에 가지고 있는 메세지 값을 넣어주길 기대한다.(수와 숫자와 상관없이 정말 많은 메세지들을 주기를 기대하고 있다.| 많은 메세지들을 프롬프트에 전달하기 위해)
* 
* 

langchain expression 언어를 활용해서 스스로 하는 법도 있다.
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/07c52b95-aecc-4b94-b25f-425f45b27e43)
load_memory를 chain.invoke를 호출할 때마다 실행한다.
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/37af0492-c678-42f2-804b-3d8f10ae9f0b)

메모리 관리를 수동으로 하고 있기 때문에 사용자와 기계간의 인터렉션을 메모리에 저장해둬야 한다.
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/baa114ae-bd3a-4dc6-ad28-729ae468ded7)
이 함수에서 chain을 호출해서 그 인터렉션을 메모리에 저장한다.
