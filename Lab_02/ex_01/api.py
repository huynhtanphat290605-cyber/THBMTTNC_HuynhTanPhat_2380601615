from flask import Flask, request, jsonify

# 1. Khai báo tất cả các module mã hóa ở đầu file
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher 
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

# 2. Khởi tạo các đối tượng mã hóa
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()


# =====================================================================
# 1. CÁC ENDPOINT CHO CAESAR CIPHER
# =====================================================================
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


# =====================================================================
# 2. CÁC ENDPOINT CHO VIGENERE CIPHER
# =====================================================================
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


# =====================================================================
# 3. CÁC ENDPOINT CHO RAILFENCE CIPHER
# =====================================================================
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():  # Đổi tên hàm từ encrypt -> railfence_encrypt để tránh trùng tên ngầm định
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():  # Đổi tên hàm từ decrypt -> railfence_decrypt cho đồng bộ
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})




# Thêm đoạn sau vào trước hàm main

# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayfairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})


@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

# =====================================================================
# HÀM CHẠY ỨNG DỤNG (LUÔN ĐẶT Ở CUỐI FILE)
# =====================================================================
if __name__ == "__main__":
    # Chạy ứng dụng Flask ở local port 5000 và cho phép mạng LAN truy cập
    app.run(host="0.0.0.0", port=5000, debug=True)
    
      # Thêm vào phần đầu của file api.py
