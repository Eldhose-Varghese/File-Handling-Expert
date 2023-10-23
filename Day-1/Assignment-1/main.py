#1. Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen.

def read_file(file_name):
  with open(file_name,"r") as file:
    for line in file:
      print(line)
read_file("poem.txt")

