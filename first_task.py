def count_words(text: str) -> int:
    """Подсчитывает количество слов в тексте."""
    return len(text.split())  # split() делит строку по пробельным символам


# Использование
text = input("Введите текст: ")  # читаем строку целиком
print(f"Количество слов: {count_words(text)}")


# С учётом пунктуации
import re  # модуль для работы с регулярными выражениями


def count_words_clean(text: str) -> int:
    """Подсчитывает слова, игнорируя пунктуацию."""
    words = re.findall(r'\b\w+\b', text)  # находим только слова, без знаков препинания
    return len(words)


text = "Привет, мир! Как дела?"
print(f"Слов (с пунктуацией): {count_words(text)}")        # 4
print(f"Слов (без пунктуации): {count_words_clean(text)}") # 4
