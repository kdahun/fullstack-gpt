# fullstack-gpt

# LangChain이란?
: 대규모 언어 모델을 활용한 혁신적인 프레임 워크
(팻봇, 질의응답 시스템, 자동 요약 등 다양한 LLM 애플리케이션을 쉽게 개발할 수 있도록 지원하는 프레임워크)

랭체인은 안정 버전을 출시하면서, 두 가지 주요 아키텍처를 변경했는 데,
1. langchain-core를 별도로 분리 : langchain-core에는 주요 추상화, 인터페이스, 그리고 핵심 기능이 포함되어 있다.
2. langchain에서 파트너 패키지를 분리 : langchain-communiy와 독립적인 파트너 패키지를 구분하여 제공

***
## LangChain 프레임워크의 구성
: 랭체인 프레임워크는 LLM 애플리케이션 개발에 도움이 되는 여러 구성요소로 이루어져 있다. 특히 개발자들이 다양한 LLM 작업을 신속하게 구축하고 배포할 수 있도록 설계되었다.

1. 랭체인 라이브러리(LangChain Libraries) : 파이썬과 자바스크립트 라이브러리를 포함하여, 다양한 컴포넌트의 인터페이스와 통합, 이 컴포넌트들을 체인과 에이전트로 결합할 수 있는 기본 런타임, 그리고 체인과 에이전트의 사용 가능한 구현이 가능하다.

2. 랭체인 탬플릿(LainChain Templates) : 다양한 작업을 위한 쉽게 배포할 수 있는 참조 아키텍처 모음이다. 이 템플릿은 개발자들이 특정 작업에 맞춰 빠르게 애플리케이션을 구축할 수 있도록 돕는다.

3. 랭서브(LangServe) : 랭체인 체인을 REST API로 배포할 수 있게 하는 라이브러리이다. 이를 통해 개발자들은 자신의 애플리케이션을 외부 시스템과 쉽게 통합할 수 있다.

4. 랭스미스(LangSmith) : 개발자 플랫폼으로, LLM 프레임워크에서 구축된 체인을 디버깅, 테스트, 평가, 모니터링할 수 있으며, 랭체인과의 원할한 통합을 지원한다.

***
## 기본 LLM 체인의 구성 요소

1. 프롬트프(Prompt) : 사용자 또는 시스템에서 제공하는 입력으로, LLM에게 특정 작업을 수행하도록 요청하는 지시문이다. 프롬프트는 질문, 명령, 문장 시작 부분 등 다양한 형태를 취할 수 있으며, LLM의 응답을 유도하는 데 중요한 역할을 한다.

2. LLM(Large Language Model) : GPT, Gemini 등 대규모 언어 모델로, 대량의 텍스트 데이터에서 학습하여 언어를 이해하고 생성할 수 있는 인공지능 시스템이다. LLM은 프롬프트를 바탕으로 적절한 응답을 생성하거나, 주어진 작업을 수행하는 데 사용.

***
## 일반적인 작동 방식

1. 프롬프트 생성 : 사용자의 요구 사항이나 특정 작업을 정의하는 프롬프트를 생성한다. 이 프롬프틎는 LLM에게 전달되기 전에, 작업의 목적과 맥락을 정확히 전달하기 위해 최적화될 수 있다.

2. LLM 처리 : LLM은 제공된 프롬프트를 분석하고, 학습된 지식을 바탕으로 적절한 응답을 생성한다. 이 과정에서 LLM은 내부적으로 다양한 언어 패턴과 내외부 지식을 활용하여, 요청된 작업을 수행하거나 정보를 제공한다.

3. 응답 반환 : LLM에 의해 생성된 응답은 최종 사용자에게 필요한 형태로 변환되어 제공된다. 이 응답은 직접적인 답변, 생성된 텍스트, 요약된 정보 등 다양한 형태를 취할 수 있다.

***

## 실습 예제
```
from langchain_openai import ChatOpenAI

# model
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

# chain 실행
llm.invoke("지구의 자전 주기는?")
```

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# prompt + model + output parser
prompt = ChatPromptTemplate.from_template("You are an expert in astronomy. Answer the question. <Question>: {input}")
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
output_parser = StrOutputParser()

# LCEL chaining
chain = prompt | llm | output_parser

# chain 호출
chain.invoke({"input": "지구의 자전 주기는?"})
```
