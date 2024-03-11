https://python.langchain.com/docs/modules/data_connection/

# Retrieval

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/77fe850c-bdc5-49f1-ad6f-6ed434b75549)

전체 문서를 로드하고, 분할한다.
(나중에 데이터를 임베드하기 위해 데이터를 분할한다)

Loader는 소스에서 데이터를 추출하고 랭체인에 가져다 주는 코드이다.

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/122efe91-cf42-4b59-8895-0b409d68935e)


만약 문서를 임베드, 저장하거나 언어모델에 주고 싶다면 질문에 답해야할 때 필요한 파일의 부분들만을 전달할 수 있다?

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/ae8beaf5-9cd9-4ba6-a8fb-b12fc7044698)

문장과 문단 구조를 유지하고 문서를 나눈다
하지만 chunk_size를 200으로 줘서 문장이 이어지지 않는다

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/3457668b-3106-4691-89cb-99ee252b3394)


이 속성은 문장이나 문단을 분할할 때 앞 조각 일부분을 가져오게 만든다.(중복되는 부분이 생길수도)

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/25cc3ac3-ddf8-452b-8d49-83c5e38b7682)

이건 한줄 단위로 문서를 분할
