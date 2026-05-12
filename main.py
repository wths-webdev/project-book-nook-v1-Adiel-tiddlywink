#menu
My_Books = []
#welcome
print("Welcome to my Book Nook!")
#image book
print("\nWelcome to...\n"
    "      ______ ______\n"
    "    _/      Y      \\_\n"
    "   // ~Book | ~~ ~  \\\n"
    "  // ~ ~ ~~ |  Nook~ \\\n"
    " //________.|.________\\\n"
    "`----------`-'----------'\n")
#commands
# Create empty list
My_Books = []

print("Add Book (Add)")
print("Show Books (Show)")
print("Remove Books (Remove)")
print("Count Books (Count)")
print("Quit Nook (Quit)")

# loop
while True:
    user_input = input("What'cha wanna do? ").strip().lower()

    # Add
    if user_input == "add":
        book_name = input("Which book would you like to add? ")
        My_Books.append(book_name)
        print("Book has been successfully added.")

    # Show
    elif user_input == "show":
        print(My_Books)

    # Remove
    elif user_input == "remove":
        book_name2 = input("Which book would you like to remove? ")

        if book_name2 in My_Books:
            My_Books.remove(book_name2)
            print("Book has been successfully removed.")
        else:
            print("Book not found in your collection.")

    # Count
    elif user_input == "count":
        print("You have", len(My_Books), "books.")

    # Quit
    elif user_input == "quit":
        print("Goodbye, thanks for visiting the Book Nook!")
        break

    # Invalid input
    else:
        print("Invalid option. Please try again.")