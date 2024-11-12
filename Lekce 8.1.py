
file_path = r"C:\Lukas\Python\Domácí úkoly\HW-8\HW-8-PY-2024\random_nouns.txt"
file_path2 = r"C:\Lukas\Python\Domácí úkoly\HW-8\HW-8-PY-2024\star_nouns.txt"

#Task 1
def task1():
    with open(file_path, "r") as source, open(file_path, "w") as new:
        text = source.read()

        words = []
        seven_words = []

        words = text.split()
        for word in words:
            if len(word) >= 7:
                seven_words.append(word)

        new.writelines(word + "\n" for word in words)

#Task 2
def task2():
    words = []

    with open(file_path, "r") as f:
        words = f.readlines()

    with open(file_path2, "w") as f:
        f.writelines(word for word in words)

#Task 3
def task3():
    words = []

    with open(file_path, "r") as f:
        words = f.readlines()
    
    words.reverse()
    
    with open(file_path2, "w") as f:
       f.writelines(word for word in words)
    print(words)
    print("-" * 50)

#Task 4

def task4():
    words = []
    stars = "*" * 12

    with open(file_path, "r") as source, open(file_path2, "w") as new:
        words = (source.read()).split()
        words.append(stars)
        new.writelines(word + "\n" for word in words)

task4()