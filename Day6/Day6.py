# Sarah 的xor加密小程序

import base64

def encrypt(data, key):
    # data(string) -> data(bytes)
    data_bytes = data.encode("utf-8")
    # key(string) -> key(byte)
    key_bytes = key.encode("utf-8")
    # xor
    data_encrypted_list = []
    for i in range(len(data_bytes)):
        data_encrypted_list.append(data_bytes[i] ^ key_bytes[i % len(key_bytes)])

    data_encrypted_bytes = bytes(data_encrypted_list)
    #print(data_encrypted_bytes)
    data_encrypted_base64 = base64.b64encode(data_encrypted_bytes)
    data_encrypted = data_encrypted_base64.decode("utf-8")
    return data_encrypted


def decrypt(data, key):
    # data(string)（是一个base64翻译成的string） -> data(bytes)
    data_bytes = base64.b64decode(data)
    # key(string) -> key(byte)
    key_bytes = key.encode("utf-8")
    # xor
    data_decrypted_list = []
    for i in range(len(data_bytes)):
        data_decrypted_list.append(data_bytes[i] ^ key_bytes[i % len(key_bytes)])

    data_decrypted_bytes = bytes(data_decrypted_list)
    # print(data_decrypted_bytes)
    data_decrypted = data_decrypted_bytes.decode("utf-8")
    return data_decrypted

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
