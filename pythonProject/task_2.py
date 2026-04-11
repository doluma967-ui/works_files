word = input("Введите слово: ")

with open('text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

count = 0
found_lines = []

for i, line in enumerate(lines, 1):
    if word in line:
        count += line.count(word)
        found_lines.append(i)

result = f"Найдено: {'Да' if count > 0 else 'Нет'}\nКоличество: {count}\nСтроки: {found_lines}"
print(result)

with open('search_results.txt', 'w', encoding='utf-8') as f:
    f.write(result)