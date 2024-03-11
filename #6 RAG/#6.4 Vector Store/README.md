
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/b8b8ddf3-e85e-4758-980a-59f4e759dfb3)

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/f614fbe0-fcc3-4e20-96b1-71d80216cfc6)

문서들을 벡터로 바꾸고
그 벡터들을 넣은 vector store를 활용해서 검색을 함


![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/b725dd2a-2ab3-47e3-a17f-2b1ed9dcc370)

cache directory 만들기


cached embeddings를 생성하는 법
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/93d2bc16-48cc-46ab-850f-44bc5e527179)

CacheBackedEmbeddings.from_bytes_store(embedder, embeddings를 저장할 장소)
이렇게 하면 다음에 Chroma.from_documents를 호출할 때에는 OpenAIEmbeddings 대신 미리 cache되어 있는 embeddings를 전달한다.

1. 캐시에 embeddings가 이미 존재하는지 확인 만약 없다면 vector store(Chroma.from_documents)를 호출할 때, 문서들과 함께 OpenAIEmbeddings를 사용한다. 그다음에 캐싱된다.
2. 
