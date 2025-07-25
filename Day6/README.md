## Day 6 加密/解密小游戏

好久不见！今天我们探索一下xor加密解密小游戏。通过今天的练习，你可以学到：
1. python表示二进制的方法
2. 二进制数据和字符串的转换
3. xor的加密解密原理

来，让Claude老师讲一下xor的加密解密原理：

```Markdown
XOR加密是一种非常简单的加密方法，让我用通俗的话来解释：

## 什么是XOR？
XOR是"异或"运算，规则很简单：
- 相同为0，不同为1
- 1 XOR 1 = 0
- 0 XOR 0 = 0  
- 1 XOR 0 = 1
- 0 XOR 1 = 1

## XOR加密原理
把明文和密钥进行XOR运算就得到密文。神奇的是，如果用同样的密钥再次XOR密文，就能还原出原始明文。

**公式：**
- 加密：明文 XOR 密钥 = 密文
- 解密：密文 XOR 密钥 = 明文

## 简单例子
假设要加密字母"A"：
1. "A"的二进制是：01000001
2. 密钥选择：11110000
3. 加密：01000001 XOR 11110000 = 10110001（密文）
4. 解密：10110001 XOR 11110000 = 01000001（还原成"A"）

## 特点
**优点：**
- 算法简单，运算速度快
- 加密和解密使用相同操作

**缺点：**
- 安全性不高，容易被破解
- 密钥不能重复使用
- 主要用于简单的数据混淆，不适合重要信息加密

XOR加密更多是作为其他复杂加密算法的基础组件，或者用于简单的数据保护场景。
```
顺带一提我的日记就是用xor加密的。
那么，让我们来写两个小函数来玩一玩这个吧。

请你写：
1. 一个加密函数`encrypt(data, key)`，输入数据和密钥，返回加密后的数据。
2. 一个解密函数`decrypt(data, key)`，输入加密数据和密钥，返回解密后的原始数据。

注意，这些函数都要使用字符串类型的输入和输出。如何做到？我听说可以使用base64编码。

哦对了，一般我们python程序的入口要写成 `if __name__ == "__main__":` 。
现阶段你可以就这样写，但是这么写是有它的道理的，可以保证这个程序在作为包被导入的时候不被运行。

今天有点晚了，我明天再写参考答案哈哈哈。加油Sarah！