
LCCE를 사용해 MapReduce chain 구현하기

먼저 document list가 필요
list 내부의 모든 document들을 위한 prompt를 만들어줘야한다.
만들어준 prompt는 LLM에 전달
"document를 일고, 사용자의 질문에 답변하기에 적절한 정보가 있는지 확인"를 전달받은 LLM은 응답을 출력
그리고 LLM으로부터 받은 response들을 취합해 하나의 document를 만들어낸다.
그렇게 만들어진 단 하나의 최종 document가 LLM을 위한 prompt로 전달된다.

질문 -> retriever에게 전달(질문과 관련된 document list를 반환) -> list의 모든 document에 대한 prompt를 만들고 -> LLM에 전달
-> LLM 출력들을 하나로 취합해 하나의 document로 만든다 -> prompt -> llm

이 방식과 stuff 중 어떤 상황에서 어느 것을 사용하는 것이 더 효율적일까?
(원하는 prompt의 크기와 검색할 document의 수에 따라 달라진다.)
* 만약  retriever가 검색 결과로 천 개 이상의 document를 반환한다면, stuff는 사용할 수 없다.(stuff의 prompt에 document들을 모두 넣을 수 없기 때문이다.)
* document가 많은 상황에서 이 방법을 사용하는 것이 적절하다.


RunnableLambda는 chain과 그 내부 어디에서든 function을 호출할 수 있도록 해준다.
