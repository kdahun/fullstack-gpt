FewShotPromptTemplete과 Fewshot Learning

# Fewshot
모델에게 예제들을 준다는 뜻과 같다.(더 나은 대답을 할 수 있도록 하는 예제들을 더 줄 수 있다.)
prompt로 직접 설명해 주기 보다는 내가 원하는 것을 예제로 보여주는 것이 더 성공적이다?

# fewShotPromptTemplate
1. 예제의 형식을 지정(형식화 하려면 형식 지정 도구를 만들어야한다다.)
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/3eff65f1-dd10-4842-a028-93b0f53c1695)



![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/b4c15e80-e9f8-4bed-9835-c3ca50931c44)
이렇게 하면 langchain이 알아서 각각의 예제 리스트들을 이 prompt를 사용하여 형식화 한다.


(예제들을 가져오고 예제들을 prompt를 사용해서 형식화 해주고
그런 다음 이를 fewShotPromptTemplate에 전달하면 끝)
