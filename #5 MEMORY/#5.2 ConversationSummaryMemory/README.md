# ConversationSummaryMemory

llm을 사용한다.
메시지를 그대로 저장하는 것이 아니라 conversation의 요약을 자체적으로 해준다.

초반에는 ConversationSummaryMemory는 이전보다 더 많은 토큰과 저장공간을 차지하게 된다.
그러나 conversation 버퍼 메모리를 사용하고 있어서 대화가 진행될수록 저장된 모든 메시지가 매우 많아지면서 연결된다.
conversation의 메시지가 많아질수록 ConversationSummaryMessage의 도움을 받아 요약하는 것이 토큰의 양도 줄어들면서 훨씬 더 나은 방법이 된다.
(저장하는것보다 Conversation를 사용하여 요약하는 것이 훨씬 더 낫다?)

대화가 길어질수록 surmmary가 각각 메시지보다 더 효율적일것이다.
