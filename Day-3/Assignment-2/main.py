# 5. Evelyn has prepared a file INFO.TXT as part of her project. Soon after saving the file, she realised that she has made a grammatical mistake in a sentence everywhere in the article.

# Write a function definition for Replace_sentence() in Python that would display the corrected version of entire content of the file INFO.TXT with all the sentences corrected.

def list_to_string(lis):
    para =""
    for element in lis:
        if element=="":
            pass
        else:
            para=para+element
            para=para+"."
    print(para)

def Replace_sentence(file,wrong_sentence,right_sentence):
    with open(file,"r") as f:
        paragraph=[]
        data = f.read()
        sentences = data.split(".")
        for sentence in sentences:
            if sentence == wrong_sentence:
                paragraph.append(right_sentence)
            else:
                paragraph.append(sentence)
        print(paragraph)
        list_to_string(paragraph)
                
wrong_sentence="I wants to express my deepest gratitude to my professors and classmates for they're unwavering support throughout this project"
right_sentence="I want to express my deepest gratitude to my professors and classmates for their unwavering support throughout this project"
Replace_sentence("info.txt",wrong_sentence,right_sentence)