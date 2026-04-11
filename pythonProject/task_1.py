import os

if not os.path.exists("input.txt"):
    f = open("input.txt", "w", encoding="utf-8")
    f.write("Разработка кода инфоримационных систем\n")
    f.write("Компьютер, мышка и кнопка\n")
    f.write("Программисты\n")
    f.close()

f = open("input.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

line_count = len(lines)

word_count = 0
for line in lines:
    words = line.split()
    word_count = word_count + len(words)

f = open("statistics.txt", "w", encoding="utf-8")
f.write("Статистика файла input.txt\n")
f.write("-" * 30 + "\n")
f.write("Количество строк: " + str(line_count) + "\n")
f.write("Количество слов: " + str(word_count) + "\n")
f.close()

print("Готово! Результат в файле statistics.txt")
print("Строк:", line_count)
print("Слов:", word_count)