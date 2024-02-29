# openAI의 모델을 사용할 때 우리가 지출하는 비용을 아는 방법
```
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

chat = ChatOpenAI(
    temperature=0.1
)

with get_openai_callback() as usage:
    a = chat.predict("What is the recipe for soju")
    b= chat.predict("What is the recipe for bread")
    print(a,b,"\n")
    print(usage)
```

![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/8b700f2e-51ae-4031-b3d8-dc1b918794ce)


# 모델을 어떻게 저장하고 불러오는지

모델 변경
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/ea7bde73-9c36-4bd6-a880-87a6040e4b3f)

save("model.json") 결과
![image](https://github.com/kdahun/fullstack-gpt/assets/101082485/eb766fa5-5d42-484f-9e54-0503750d16cb)
