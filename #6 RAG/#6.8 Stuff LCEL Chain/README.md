
LangChain Expression Language를 사용해서 stuff chain을 구현하기

- chain의 구성요소
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/593cc3d2-754a-4c4f-9af0-1417f9310229)

Retriever은 한개의 string을 입력받는다.
질문이나 그와 관련성이 있는 document를 얻기위한 query를 입력받는다.

Retriever의 출력값은 document들은 List이다.


chain의 구성요소들의 순서
1. 모든 document를 가져오기(query와 관련있는건 전부 가져와야한다.) => Retriever을 첫번째로 넣어주면된다.
2. document들은 template에 입력되어야 한다.
3. LLM은 prompt와 그 내부에 입력될 데이터를 전달한다.
4. chain.invoke("")를 실행하면 string이 retriever에게 전달

* chain.invoke("") 안의 값을 retriever에 전달
* 그 결과로 출력된 document를 prompt의 context에 입력 또한 이 chain.invoke("")의 질문을 prompt의 question property로 전달
