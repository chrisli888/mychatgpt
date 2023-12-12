from src.revChatGPT.V3 import Chatbot


# promt="""
# 你是一个小学二年级的班主任，请根据你们班吴静怡女同学在11月1日到12月1日的表现， 写一段日常评语。
# 吴静怡同学在本时段表现最突出的方面是：上课举手回答问题、当小师父、作业完成优秀；需要注意改进提升的是：打架、作业欠交。
# 日常评语需满足以下4个条件：
# 1. 评语要有温度、有文采；
# 2. 只引用1句名人名言或者古诗词；
# 3. 字数不要太长，保持300字以内；
# 4. 合理使用标点符号。
# """

promt="""
在中国使用chatgpt违法么
"""


# chatbot = Chatbot(api_key="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",engine="gpt-3.5-turbo",proxy="http://127.0.0.1:15236")
# for data in chatbot.ask_stream(promt):
#     print(data, end="", flush=True)

chatbot = Chatbot(api_key="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",engine="gpt-3.5-turbo")
for data in chatbot.ask_stream(promt):
    print(data, end="", flush=True)

# chatbot = Chatbot(api_key="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")
# for data in chatbot.ask_stream("Hello world"):
#     print(data, end="", flush=True)