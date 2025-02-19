
# This function will make a list of my favorite books and it will get the first three books in the list including title and author.
def getFirstThreeBooks():

    # List of my favorite books with titles and authors
    bookList = [
        {"Title": "Diary of a Wimpy Kid", "Author": "Jeff Kinney"},
        {"Title": "Big Nate and Friends", "Author": "Lincoln Peirce"},
        {"Title": "Harry Potter and the Goblet of Fire", "Author": "J.K. Rowling"},
        {"Title": "Hatchet", "Author": "Gary Paulsen"},
        {"Title": "Hunger Games", "Author": "Suzanne Collins"}
    ]

    # Returns the first three books in the list.
    return bookList[:3]

# The student database with names and student ID numbers.
studentDatabase = {
    "Ale": "71020",
    "Michael": "60921",
    "Josh": "14221",
    "Pablo": "35037"
}

# This function will test the getFirstThreeBooks function to ensure that it does printout the correct first three books in the list.
def testGetFirstThreeBooks():
    expectedBooks = [
        {"Title": "Diary of a Wimpy Kid", "Author": "Jeff Kinney"},
        {"Title": "Big Nate and Friends", "Author": "Lincoln Peirce"},
        {"Title": "Harry Potter and the Goblet of Fire", "Author": "J.K. Rowling"},
    ]

    assert getFirstThreeBooks() == expectedBooks

# This will check the student database and make sure it has a name and a student ID number.
def testStudentDatabase():

    correctDatabase = {
        "Ale": "71020",
        "Michael": "60921",
        "Josh": "14221",
        "Pablo": "35037"
    }

    assert studentDatabase == correctDatabase