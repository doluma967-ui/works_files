with open('words.txt', 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f if line.strip()]

alphabetical = sorted(words)                   
by_length = sorted(words, key=len)            
reverse_alpha = sorted(words, reverse=True)    

with open('sorted_alphabetically.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(alphabetical))

with open('sorted_by_length.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(by_length))

with open('sorted_reverse.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(reverse_alpha))

print("Готово!")
print(f"Всего слов: {len(words)}")
print(f"По алфавиту: {alphabetical[:3]}...")
print(f"По длине: {by_length[:3]}...")
print(f"Обратный алфавит: {reverse_alpha[:3]}...")
