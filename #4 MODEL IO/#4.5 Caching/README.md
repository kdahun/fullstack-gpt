# set_llm_cache
캐싱을 사용하면 LM(언어 모델)의 응답을 저장할 수 있다.
(이미 답변한 답을 캐싱을 이용해 저장한 후에 다시 재사용 할 수 있다.)
-> 똑같은 질문을 하면 똑같은 대답이 나온다.

### set_llm_cache(InMemoryCache())
: 모든 response가 메모리에 저장된다.

### set_llm_cache(SQLiteCache("cache.db"))
cache.db라는 sqlite 데이터베이스가 생기고 response가 db에 저장된다.
