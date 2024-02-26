# OutputParser와 LangChain expression language(표현언어)

LangChain expression language는 우리의 코드를 굉장히 줄여주는 역할을 한다.
그리고 다양한 template과 LLM 호출, 서로다른 응답을 함께 사용하게 해준다.


Output Parser가 필요한 이유는 LLM의 응답을 변형해야 할 때가 있기 때문
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/c3097f9a-8b7b-4b78-90a2-f87915513639)

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/d14803ad-69a0-44db-87b0-13639e0d0aca)

## LangChain Expression Language(표준언어)
* chain 이라는 것은 기본적으로 모든 요소를 합쳐주는 역할
* 합쳐진 요소들은 하나의 chain으로 실행 -> 하나하나 순서대로 result를 반환을 할 때까지
* | 주변에 입력한 값들로 chain 형성
* 상위 계층에서의 개발자 경험도 아주 깔끔(복잡한 내부 코드를 안봐도 된다.)
* invoke 메서드의 입력값으로는 dictionary 타입이 들어가야된다.
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/b84ffeb2-1afd-4ef5-b943-40d5b6881825)

