
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

if __name__ == "__main__":
    print("Top three favorite books: ")
    for book in getFirstThreeBooks():
        print(f"{book['Title']} by {book['Author']}")

    print("Student Database:")
    for student, studentId in studentDatabase.items():
        print(f"{student}: {studentId}")