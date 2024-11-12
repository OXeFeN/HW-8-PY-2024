
file_path = r"C:\Lukas\Python\Domácí úkoly\HW-8\HW-8-PY-2024\random_nouns.txt"
file_path2 = r"C:\Lukas\Python\Domácí úkoly\HW-8\HW-8-PY-2024\replace_nouns.txt"

def task0():
    with open(file_path, "r") as source:
        words = list((source.read().split()))

    with open(file_path, "w") as source:
        source.writelines(word + "\n" for word in words)
    
#Task 1
def task1():
    with open(file_path, "r") as source, open(file_path2, "w") as new:
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

#Task 4
def task4():
    with open(file_path, "r") as source, open(file_path2, "w") as new:
        words = (source.read()).split()
        words.append("*" * 12)
        new.writelines(word + "\n" for word in words)

#Task 5
def task5():
    with open(file_path, "r") as source, open(file_path2, "w") as new:
        words = (source.read()).split()
        user = str(input("Set a character for the filter: ").strip().lower())
        for word in words:
            if word.startswith(user[0]):
                new.writelines(word + "\n")

#Task 6
def task6():
    user = str(input("Set a character for replace: ").strip().lower())
    with open(file_path, "r") as source, open(file_path2, "w") as new:
        words = (source.read()).replace((user[0]), "*")
        words.split()
        new.writelines(words + "\n")