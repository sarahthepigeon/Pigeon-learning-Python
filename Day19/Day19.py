import os
import time
from openai import OpenAI  # 如果这行报错，你需要在终端里输入 pip install openai

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
	raise ValueError("请设置环境变量 OPENAI_API_KEY 或在代码中手动填充 API 密钥。但是如果手动填充 API 密钥，不要将其上传到GitHub上。")
client = OpenAI(api_key=api_key)

def addMessage(role, content, messages):
    """
    添加一条消息到对话中。
    :param role: 消息的角色（如"user"或"assistant"）。
    :param content: 消息的内容。
    :param messages: 当前对话的消息列表。
    """
    messages.append({"role": role, "content":content})
    return messages

def sendMessagetoGPT(model, messages):
    """
    送请求到ChatGPT并返回响应。
    :param model: 选用的模型
    :param messages: 包含对话内容的列表，每个元素是一个字典，包含角色和内容。
    :return: ChatGPT的响应内容。
    """
    if model == "o3":
        Model = "gpt-4o"
    elif model == "GPT4.1":
        Model = "gpt-4-0613"
    else:
        ValueError("Unknown Model type")

    response = client.chat.completions.create( model= Model, messages=messages)
    responseContent = response.choices[0].message.content
    return responseContent

def main():
    model = "o3"
    messages = []
    while True:
        newMessageContent = input("User: ")
        addMessage("user", newMessageContent, messages);     
        reply = sendMessagetoGPT(model, messages)
        addMessage("assistant", reply, messages)
        print("ChatGPT: " + reply)

main()

