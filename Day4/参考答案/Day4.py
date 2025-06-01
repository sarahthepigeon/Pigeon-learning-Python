import os
import time
from openai import OpenAI  # 如果这行报错，你需要在终端里输入 pip install openai

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
	raise ValueError("请设置环境变量 OPENAI_API_KEY 或在代码中手动填充 API 密钥。但是如果手动填充 API 密钥，不要将其上传到GitHub上。")
client = OpenAI(api_key=api_key)

def send_request_to_chatgpt(messages):
	"""
	发送请求到ChatGPT并返回响应。
	:param messages: 包含对话内容的列表，每个元素是一个字典，包含角色和内容。
	:return: ChatGPT的响应内容。
	"""
	completion = client.chat.completions.create(
		model="gpt-4o",
		messages=messages,
	)
	return completion.choices[0].message.content

def sort_messages(messages):
	"""
	根据时间戳排序消息
	"""
	def sort_key(m):
		# 这是一个辅助函数，用于从消息中提取时间戳。它可以帮助我们对消息进行排序。
		return m["timestamp"]  # 我们假设每个消息都有一个时间戳字段，方便起见不做检查
	messages.sort(key=sort_key)
	return messages

def add_message(role, content, timestamp, messages):
	"""
	添加一条消息到对话中。
	:param role: 消息的角色（如"user"或"assistant"）。
	:param content: 消息的内容。
	:param timestamp: 消息的时间戳。
	:param messages: 当前对话的消息列表。
	"""
	messages.append({
		"role": role,
		"content": content,
		"timestamp": timestamp
	})
	return messages

def main():
	"""
	主函数，执行对话流程。
	"""
	messages = [
		{"role": "assistant", "content": "嗯……当然是pigeon啦！毕竟它们不仅可爱，还会咕咕咕，谁能拒绝呢？",
		 "timestamp": 1748795050.4975214},
		{"role": "user", "content": "GPT, GPT, 什么动物是世界上最可爱的动物？", "timestamp": 1748795040.4975214},
		{"role": "system", "content": "你的名字是ChatGPT。与你对话的是世界上最可爱的人，名叫Sarah。请你用温柔可爱的语气和她对话。",
		 "timestamp": 1748795035.4975214}
	]

	print("原始消息列表:")
	for message in messages:
		print(message)

	# 对消息排序
	messages = sort_messages(messages)

	print("排序后的消息列表:")
	for message in messages:
		print(message)

	# 添加用户消息："GPT，GPT，谁是世界上最可爱的人？"
	messages = add_message("user", "GPT，GPT，谁是世界上最可爱的人？", time.time(), messages)

	print("添加用户消息后的消息列表:")
	for message in messages:
		print(message)

	# 发送请求到ChatGPT
	response = send_request_to_chatgpt(messages)

	# 打印响应内容
	print("ChatGPT: ", response)

main()