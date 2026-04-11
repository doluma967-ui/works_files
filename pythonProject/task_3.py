files = ['file1.txt', 'file2.txt', 'file3.txt']

with open('combined.txt', 'w', encoding='utf-8') as out_file:
    for file_name in files:
        try:
            with open(file_name, 'r', encoding='utf-8') as in_file:
                out_file.write(f"=== Содержимое {file_name} ===\n")
                out_file.write(in_file.read())
                out_file.write("\n\n")
        except FileNotFoundError:
            out_file.write(f"=== Содержимое {file_name} ===\n")
            out_file.write("[Файл не найден]\n\n")

print("Файлы объединены в combined.txt")



