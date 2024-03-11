RAG(Retrieval Augmented Generation, 검색 증강 생성)
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/606d1907-9fdf-4ee9-a760-3278d510064d)

1. foo가 뭐지? 라는 질문을 하면 우리는 그 질문을 prompt에 전달한다. 또한, 동시에 우리의 질문과 관련이 있는 문서들도 준비하게 된다.
2. 그 문서들을 context로써 우리의 질문과 함께 묶어서 큰 Language Model에 보낸다.
   이제 Model은 기존에 학습된 수 많은 data와 함께 우리가 Model이 더 나은 답변을 하도록 도와주기 위해 추가로 전송한 data까지 갖는다.
   -> 이게 바로 Retriecal Augmented Generation(RAG)이다.(개인으로부터 제공된 data를 사용하거나 탐색함으로써 우리가 Language Model의 능력을 확장시킨다.)
   
이렇게 하면  Model은 우리의 질문, 이미 학습된 data, 그리고 우리가 추가로 보낸 data까지 갖고 있다.
그리고 prompt를 사용해 model에게 우리가 보낸 문서만을 가지고 답변 하게 할 수 있다.
(기존의 학습한 데이터를 아예 참고하지 않고) -> 기존의 예날에 학습한 data는 참조하지 않게 하기 위해서 사용해 볼수 있다.
