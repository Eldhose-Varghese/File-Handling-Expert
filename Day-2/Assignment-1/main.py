def count_word(file,my_word):
    with open(file,"r") as f:
        count=0
        data = f.read().lower()
        words = data.split()
        print(f'The word {my_word} is present {words.count(my_word)} times')
        # for each_word in words:
        #     if each_word == my_word:
        #         count=count+1
    
count_word("notes.txt",input("Enter the word you want to search for : ").lower())