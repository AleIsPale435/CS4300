import pytest
# This function will take a text file, read it, and calculate the amount of words in that file.
def fileWordCount(fileName):

    # Opens the file, reads the file, then splits each word, and finally stores the amount of words in a variable to return.
    with open(fileName, 'r', encoding='UTF-8') as file:
        content = file.read()
    words = content.split()
    return len(words)

# This dictionary maps text filenames to their expected word counts.
expectedFileCount = {
    "task6_read_me.txt": 127
}

"""
The following code I got help from ChatGPT.
"""

# This for loop will generate pytest test functions based on the filenames.
for filename, expected in expectedFileCount.items():

    # This creates a valid function name with the filename, replacing any periods that cause errors with underscores.
    testName = f"testWordCount{filename.replace('.', '_')}"

    # This function will test the function with the current file and its word count.
    def testFunction(filename=filename, expected=expected):
        count = fileWordCount(filename)
        assert count == expected

    # This will inject the test function into the modules global namespace.
    globals()[testName] = testFunction

"""
OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. https://chat.openai.com/
"""