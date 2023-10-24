# 4. Write a function in Python to count uppercase character in a text file.
def count_upper(file):
    with open(file,"r") as f:
        count=0
        for letter in f.readline():
            if letter.isupper():
                count=count+1
    print(f'The file {file} has {count} uppercase characters.')
count_upper("text_file.txt")                
