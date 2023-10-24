# 3.Write a function in Python to read lines from a text file "notes.txt", to find and display the occurrence of the word "the".

def count_word(file,my_word):
    with open(file,"r") as f:
        count=0
        data = f.read().lower()
        words = data.split()
        print(f'The word {my_word} is present {words.count(my_word)} times')

count_word("notes.txt",input("Enter the word you want to search for : ").lower())