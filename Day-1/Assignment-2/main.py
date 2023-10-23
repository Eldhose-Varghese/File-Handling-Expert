# 2. Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T". 

def get_count_no_T(file_name):
  with open(file_name,"r") as file:
    count=0
    lines=0
    for line in file:
      lines=lines+1
      if line[0]=="T":
        count=count+1
    print(lines-count)
get_count_no_T("story.txt")
        

