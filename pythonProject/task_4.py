SHIFT = 3

def caesar(text, shift):
    """Шифрует или расшифровывает текст сдвигом shift"""
    result = ""
    for char in text:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Читаем secret.txt
with open('secret.txt', 'r', encoding='utf-8') as f:
    original = f.read()

# Шифруем
encrypted = caesar(original, SHIFT)

# Записываем encrypted.txt
with open('encrypted.txt', 'w', encoding='utf-8') as f:
    f.write(encrypted)

# Расшифровываем (сдвиг -3)
decrypted = caesar(encrypted, -SHIFT)

# Записываем decrypted.txt
with open('decrypted.txt', 'w', encoding='utf-8') as f:
    f.write(decrypted)

print("Готово!")
print(f"Оригинал: {original[:50]}...")
print(f"Зашифровано: {encrypted[:50]}...")
print(f"Расшифровано: {decrypted[:50]}...")







