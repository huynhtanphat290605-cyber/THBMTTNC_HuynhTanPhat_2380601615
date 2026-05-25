class VigenereCipher:
    def __init__(self):
        pass
    
    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        
        for char in plain_text:
            if char.isalpha():
                # Lấy ký tự khóa hiện tại, chuyển thành chữ hoa và tính khoảng cách shift
                current_key_char = key[key_index % len(key)].upper()
                key_shift = ord(current_key_char) - ord('A')
                
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                
                key_index += 1
            else:
                encrypted_text += char
                
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        disabled_text = ""  # decrypted_text
        key_index = 0
        
        for char in encrypted_text:
            if char.isalpha():
                current_key_char = key[key_index % len(key)].upper()
                key_shift = ord(current_key_char) - ord('A')
                
                if char.isupper():
                    # Thêm + 26 để đảm bảo giá trị luôn dương trước khi chia lấy dư
                    disabled_text += chr((ord(char) - ord('A') - key_shift + 26) % 26 + ord('A'))
                else:
                    # Thêm + 26 để sửa lỗi lệch ký tự viết thường
                    disabled_text += chr((ord(char) - ord('a') - key_shift + 26) % 26 + ord('a'))
                
                key_index += 1
            else:
                disabled_text += char
                
        return disabled_text

# --- VÍ DỤ CÁCH SỬ DỤNG ---
if __name__ == "__main__":
    cipher = VigenereCipher()
    
    van_ban_goc = "Hello, World!"
    khoa = "KEY"
    
    # 1. Mã hóa
    van_ban_ma_hoa = cipher.vigenere_encrypt(van_ban_goc, khoa)
    print(f"Văn bản gốc:   {van_ban_goc}")
    print(f"Văn bản mã hóa: {van_ban_ma_hoa}")  # Kết quả chuẩn: Riijz, Thvng!
    
    # 2. Giải mã
    van_ban_giai_ma = cipher.vigenere_decrypt(van_ban_ma_hoa, khoa)
    print(f"Văn bản giải mã: {van_ban_giai_ma}") # Kết quả chuẩn: Hello, World!