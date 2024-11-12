
file_path = r"C:\Lukas\Python\Domácí úkoly\HW-8\HW-8-PY-2024\random_nouns.txt"
file_path2 = r"C:\Lukas\Python\Domácí úkoly\HW-8\HW-8-PY-2024\seven_nouns.txt"

with open(file_path, "r") as f:
    text = f.read()

words = []
seven_words = []

words = text.split()
for word in words:
    if len(word) >= 7:
        seven_words.append(word)

with open(file_path2, "w") as f:
    f.writelines(word + "\n" for word in seven_words)



print(seven_words)