# Sarah 的xor加密小程序

import base64

def encrypt(data, key):
    pass

def decrypt(data, key):
    pass

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
