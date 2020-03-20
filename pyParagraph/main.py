#Brian Parish
#Python Homework
#pyParagraph


import re
import os

wordcount = 0
sentencecount = 0
totalchars = 0

input_files = ["paragraph_1.txt", "paragraph_2.txt"]

for files in input_files:
    with open(files,'r')  as file1:
        print("\nScanning file: " + files)

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
                    chars = chars.replace('"',"")
                    chars = chars.replace(".","")
                    #count all characters in the words and sum them
                    totalchars += len(chars)

        print(f"Paragraph Analysis\n" + \
                "-----------------" + \
                "\nApproximate Word Count: " + str(wordcount) + \
                "\nApproximate Sentence Count: " + str(sentencecount) + \
                "\nCharacters per word: " + str(round(totalchars/wordcount, 1)) + \
                "\nAverage sentence length: " + str(round(wordcount/sentencecount, 1)))
