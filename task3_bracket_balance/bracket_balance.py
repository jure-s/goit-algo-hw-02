def is_balanced(expression):
    """
    Перевіряє збалансованість дужок у рядку.

    Аргументи:
        expression (str): Рядок з дужками.

    Повертає:
        bool: True, якщо дужки збалансовані, інакше False.
    """
    stack = []
    # Розширений словник пар дужок
    pairs = {')': '(', '}': '{', ']': '[', '>': '<'}

    for char in expression:
        if char in pairs.values():  # Якщо символ - відкриваюча дужка
            stack.append(char)
        elif char in pairs.keys():  # Якщо символ - закриваюча дужка
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack  # Якщо стек порожній, дужки збалансовані
