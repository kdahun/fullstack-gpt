
기본적으로 splitter들은 텍스트의 length를 계산해서 한 덩어리의(chunk) 크기를 알아낸다.

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/f92e5428-eaf9-4e49-a39a-4e2ea01f156b)

length_function=len : 텍스트가 얼마나 많은 문자를 갖고 있는지 세준다. 표준 라이브러리의 len 함수를 사용해서

model은 token간의 통계적인 관계를 이해하도록 학습을 한다.
