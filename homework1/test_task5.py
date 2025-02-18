import task5

# This function will test the getFirstThreeBooks function to ensure that it does printout the correct first three books in the list.
def testGetFirstThreeBooks():
    expectedBooks = [
        {"Title": "Diary of a Wimpy Kid", "Author": "Jeff Kinney"},
        {"Title": "Big Nate and Friends", "Author": "Lincoln Peirce"},
        {"Title": "Harry Potter and the Goblet of Fire", "Author": "J.K. Rowling"},
    ]

    assert task5.getFirstThreeBooks() == expectedBooks

# This will check the student database and make sure it has a name and a student ID number.
def testStudentDatabase():

    correctDatabase = {
        "Ale": "S1020",
        "Michael": "S0921",
        "Josh": "S4221",
        "Pablo": "S5037"
    }

    assert task5.studentDatabase == correctDatabase