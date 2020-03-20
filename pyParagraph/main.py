#Brian Parish
#Python Homework
#pyParagraph


import re
import os

wordcount = 0
sentencecount = 0
totalchars = 0

files = os.listdir("./")
i=1
for file in files:
    if file.__contains__(".txt"):
        print(f"({i})" + file)
        i += 1
user_input = input("Type the number for the file to read: ")

if(int(user_input) < i):
    text_file = files[int(user_input)-1]
    print("You selected: " + text_file)
    file1 = open(text_file,'r')
    
    for paragraph in file1:
        sentences = re.split("(?<=[.!?]) +", paragraph)
        if(sentences[0] != "\n"):
            sentencecount += len(sentences)
        for sentence in sentences:
        #split sentence by spaces to count words
            words = sentence.split(" ")
            wordcount += len(words)
            for chars in words:
                #Don't count non-letter characters
                chars = chars.replace(",","")
                chars = chars.replace("'","")
                chars = chars.replace('"',"")
                chars = chars.replace(".","")
                chars = chars.replace("\n","")
                #count all characters in the words and sum them
                totalchars += len(chars)

    print(f"\nParagraph Analysis\n" + \
            "-----------------" + \
            "\nApproximate Word Count: " + str(wordcount) + \
            "\nApproximate Sentence Count: " + str(sentencecount) + \
            "\nCharacters per word: " + str(round(totalchars/wordcount, 1)) + \
            "\nAverage sentence length: " + str(round(wordcount/sentencecount, 1)))
else:
    print("Invalid input, enter a value between 1 and " + str(i-1))
