from collections import deque

def is_palindrome(string):
    """
    Перевіряє, чи є рядок паліндромом.
    
    Аргументи:
        string (str): Рядок для перевірки.

    Повертає:
        bool: True, якщо рядок є паліндромом, інакше False.
    """
    # Очистимо рядок: видаляємо все, крім букв і цифр, та приводимо до нижнього регістру
    cleaned_string = ''.join(filter(str.isalnum, string)).lower()
    dq = deque(cleaned_string)

    # Порівнюємо символи з обох кінців черги
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
