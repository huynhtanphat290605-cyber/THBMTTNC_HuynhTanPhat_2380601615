class PlayfairCipher:
    def __init__(self) -> None:
        pass
        
    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        
        matrix = []
        for letter in key:
            if letter in alphabet and letter not in matrix:
                matrix.append(letter)
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break
        return [matrix[i:i+5] for i in range(0, len(matrix), 5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return 0, 0

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper().replace(" ", "")
        encrypted_text = ""
        
        prepared_text = ""
        i = 0
        while i < len(plain_text):
            prepared_text += plain_text[i]
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i+1]:
                    prepared_text += "X"
                    i += 1
                else:
                    prepared_text += plain_text[i+1]
                    i += 2
            else:
                i += 1
        if len(prepared_text) % 2 != 0:
            prepared_text += "X"
            
        for i in range(0, len(prepared_text), 2):
            pair = prepared_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper().replace(" ", "")
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        banro = ""
        for i in range(0, len(decrypted_text) - 2, 2):
            if decrypted_text[i] == decrypted_text[i+2] and decrypted_text[i+1] == "X":
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + decrypted_text[i+1]
        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2:]
        return banro