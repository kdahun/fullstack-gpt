https://python.langchain.com/docs/modules/chains

## 모델 I/O 모듈
입력(input)과 출력(output)이 있다.

입력(input)은 prompt(명령 등을 내리는 곳)이다.
따라서 모델 I/O에서는 prompt templete, Language models, LMS 또는 채팅 모델, output parser등이 있다.

## Retrival
외부 데이터로 접근하여 이를 모델에 어떻게 제공하는 것에 관한 것이다.
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/e4395c18-3681-4c12-8739-66c587aa7476)
* Document loaders
* Text Splitting
* Text embedding models
* Vector stores
* Retrievers
* Indexing
이것들이 전부 우리의 데이터들로 작업하게 하고 모델에게 제공할 수 있는 지에 관한 것이다.

## Chains

## Agents
독립적으로 AI가 작동하도록 만들 수 있게 해주는 agents가 있다.
chains이 필요한 도구들을 선택하여 사용할 수 있도록 해준다.
그냥 일을 chains에게 시키면 그에 맞는 커스텀 도구를 만들어 준다면 chains가 스스로 사용할  tools들을 선택한다.
현재 가장 실험적인 단계

## callbacks
기본적으로 model이 무엇을 하고 있는지 중간에 알 수 있도록 하는 것이다.
(모델이 답변을 제공하기 전에 실제로 모델이 어떤 일을 하고 있는 지 확인할 수 있다.)
