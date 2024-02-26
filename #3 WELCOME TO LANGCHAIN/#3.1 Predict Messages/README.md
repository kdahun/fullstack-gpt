Chat model은 대화에 최적화 되어 있다. 
(단지 질문을 받을 수  있을 뿐만 아니라, 대화를 할 수 있다.)

만약 model의 설정을 바꾸고 싶으면 model의 constructure(생성자)에서 할 수 있다.
* max_tokens : 반환하는 결과의 최대 token을 정함.
* temperature : model 얼마나 창의적인지를 결정한다.(낮은 값일수록 창의적이지 않고, 높은 값일수록 창의성과 무작위성을 갖게 된다.)


SystemMessage : AI에 일종의 기본 설정, 기본 값, 기본 context 설정(시스템이 생성한 메시지를 나타낸다.)
AIMessage : string을 미리 만들어두고 일종의 가상 대화를 만들기(인공지능 모델이 생성한 메시지를 나타낸다.)
HumanMessage : 사용자로서 질문(사용자가 보낸 메시지를 나타낸다.)
