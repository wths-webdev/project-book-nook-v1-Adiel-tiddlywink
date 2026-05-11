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
print("Add Book (Add)")
print("Show Books (Show)")
print("Remove Books (Remove)")
print("Count Books (Count)")
print("Quit Nook (Quit)")
#loop
while True:
    user_input = input("What'cha wannna do?")
     # Add
        # ask for book 
    if user_input == "Add":
        book_name = input("Which book would you like to add?")
        # add to list 
        My_Books.append(book_name)
        # success message
        print("Book has been successfully added.")

    # Show 
        # print out list with numbers
    elif user_input == "Show":
        print (My_Books)
    # Remove 
    elif user_input == "Remove":
        # ask for book
        book_name2 = input("Which book would you like to remove?")
        # remove the book
        My_Books.remove(book_name2)
        # success message
        print("Book has been successfully removed.") 
    # Count 
    elif user_input == "Count":
        # print out the message with count number
        print(len(My_Books))
        print("You have books")
    # Quit
    else:
        print("Goodbye, thanks for visiting the Book Nook!")
        break