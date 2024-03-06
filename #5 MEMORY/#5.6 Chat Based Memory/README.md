# 대화 기반 메세지의 memory

5.5의 코드에서는 memory.load_memory_variables({})을 하면 대화기반이 아니라 그냥 텍스트가 나오는걸 확인할 수 있다.
(프롬프트에 표시되는 방식은 그냥 텍스트이다.)

ConversationSummaryBufferMemory가 AI, 사람, 시스템 메세지를 줄거고
MessagePlacehoder가 memory class로 대체된다?(메세지가 얼마나 많고 누구에게로부터 왔는지 모르지만)
