def caesar_cipher(text: str, shift: int) -> str:
    """Шифрует текст шифром Цезаря."""
    result = []
    for char in text:
        if char.isalpha():  # буквы сдвигаем, остальные символы не трогаем
            base = ord('A') if char.isupper() else ord('a')  # начало алфавита для регистра
            shifted = (ord(char) - base + shift) % 26 + base  # сдвиг с закольцовыванием
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


# Шифрование
original = "Hello, World!"
encrypted = caesar_cipher(original, 3)
print(f"Оригинал: {original}")
print(f"Зашифровано: {encrypted}")  # Khoor, Zruog!

# Дешифрование (сдвиг в обратную сторону)
decrypted = caesar_cipher(encrypted, -3)
print(f"Расшифровано: {decrypted}") # Hello, World!
