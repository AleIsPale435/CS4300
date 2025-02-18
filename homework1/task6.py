
# This function will take a text file, read it, and calculate the amount of words in that file.
def fileWordCount(fileName):

    # Opens the file, reads the file, then splits each word, and finally stores the amount of words in a variable to return.
    with open(fileName, 'r', encoding='utf-8') as file:
        content = file.read()
    words = content.split()
    return len(words)

if __name__ == "__main__":

    file = "task6_readme.txt"
    wordCount = fileWordCount(fileName)
    print("Word count in " + file + ": " + wordCount)
