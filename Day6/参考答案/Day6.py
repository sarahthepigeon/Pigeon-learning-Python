# Ken 的xor加密小程序

import base64

def encrypt(data, key):
    # 逻辑：首先将data和key转成字节串，然后对每个字节进行异或操作，最后将结果编码为base64，然后再解码为字符串
    data_bytes = data.encode('utf-8')
    key_bytes = key.encode('utf-8')
    encrypted_bytes = bytearray()
    key_len = len(key_bytes)
    for i in range(len(data_bytes)):
        encrypted_bytes.append(data_bytes[i] ^ key_bytes[i % key_len])
    encrypted_bytes_base64 = base64.b64encode(encrypted_bytes)
    return encrypted_bytes_base64.decode('utf-8')

def decrypt(encrypted_str, key):
    # 逻辑：首先将data从base64编码成字节串，然后对每个字节进行异或操作，最后将结果解码为字符串
    encrypted_bytes_base64 = encrypted_str.encode('utf-8')
    encrypted_bytes = base64.b64decode(encrypted_bytes_base64)
    key_bytes = key.encode('utf-8')
    data_bytes = bytearray()
    key_len = len(key_bytes)
    for i in range(len(encrypted_bytes)):
        data_bytes.append(encrypted_bytes[i] ^ key_bytes[i % key_len])
    return data_bytes.decode('utf-8')


if __name__ == '__main__':
    choice = input("请选择操作：1.加密 2.解密\n")
    if choice == '1':
        data = input("请输入要加密的数据：")
        key = input("请输入加密密钥：")
        encrypted_data = encrypt(data, key)
        print(f"加密后的数据：{encrypted_data}")
    elif choice == '2':
        data = input("请输入要解密的数据：")
        key = input("请输入解密密钥：")
        decrypted_data = decrypt(data, key)
        print(f"解密后的数据：{decrypted_data}")
    else:
        print("无效的选择，请重新运行程序。")
