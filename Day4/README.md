## Python列表小练习 Continued

今天主要练习Python列表在实战中的应用吧。主要学习关于列表增删改查等操作，还有高级一点的sort。此外还要学一点字典的用法。

### 情景描述：

康康想要使用ChatGPT做一个聊天机器人。请你帮助他用Python列表管理对话内容，然后向ChatGPT发送请求。

他目前有一段对话记录，是一个包着字典的列表。每个字典代表一条消息。

消息列表：
```python
messages = [
	{"role": "assistant", "content": "嗯……当然是pigeon啦！毕竟它们不仅可爱，还会咕咕咕，谁能拒绝呢？", "timestamp": 1748795050.4975214},
	{"role": "user", "content": "GPT, GPT, 什么动物是世界上最可爱的动物？", "timestamp": 1748795040.4975214},
	{"role": "system", "content": "与你对话的是世界上最可爱的人，名叫Sarah。请你用温柔可爱的语气和她对话。", "timestamp": 1748795035.4975214}
]
```

但是，目前的对话记录有点乱。康康希望能按照时间戳从新到旧排序。
请你帮他写一个函数`sort_messages(messages)`解决问题。

接下来，康康想要再写一个函数`add_message(role, content, timestamp, messages)`，能够向对话列表中添加新的消息。这个函数接收角色、消息内容和时间戳，并将新的消息添加到列表的末尾。

接下来，请你调用康康已经写好了的函数`send_request_to_chatgpt(messages)`，将处理好的消息列表发送给ChatGPT。

示例：
```
原始消息列表:
{'role': 'assistant', 'content': '嗯……当然是pigeon啦！毕竟它们不仅可爱，还会咕咕咕，谁能拒绝呢？', 'timestamp': 1748795050.4975214}
{'role': 'user', 'content': 'GPT, GPT, 什么动物是世界上最可爱的动物？', 'timestamp': 1748795040.4975214}
{'role': 'system', 'content': '你的名字是ChatGPT。与你对话的是世界上最可爱的人，名叫Sarah。请你用温柔可爱的语气和她对话。', 'timestamp': 1748795035.4975214}
排序后的消息列表:
{'role': 'system', 'content': '你的名字是ChatGPT。与你对话的是世界上最可爱的人，名叫Sarah。请你用温柔可爱的语气和她对话。', 'timestamp': 1748795035.4975214}
{'role': 'user', 'content': 'GPT, GPT, 什么动物是世界上最可爱的动物？', 'timestamp': 1748795040.4975214}
{'role': 'assistant', 'content': '嗯……当然是pigeon啦！毕竟它们不仅可爱，还会咕咕咕，谁能拒绝呢？', 'timestamp': 1748795050.4975214}
添加用户消息后的消息列表:
{'role': 'system', 'content': '你的名字是ChatGPT。与你对话的是世界上最可爱的人，名叫Sarah。请你用温柔可爱的语气和她对话。', 'timestamp': 1748795035.4975214}
{'role': 'user', 'content': 'GPT, GPT, 什么动物是世界上最可爱的动物？', 'timestamp': 1748795040.4975214}
{'role': 'assistant', 'content': '嗯……当然是pigeon啦！毕竟它们不仅可爱，还会咕咕咕，谁能拒绝呢？', 'timestamp': 1748795050.4975214}
{'role': 'user', 'content': 'GPT，GPT，谁是世界上最可爱的人？', 'timestamp': 1748797908.2777233}
ChatGPT:  当然是亲爱的Sarah啦！你的可爱可是无可比拟的哦！✨😊✨
```

希望今天的内容能让你觉得有趣。加油Sarah！