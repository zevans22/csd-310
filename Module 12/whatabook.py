import mysql.connector
from mysql.connector import errorcode
import sys

#Establishing a connection to the mysql database.
db = mysql.connector.connect(
    host ="localhost",
    user = "whatabook_user",
    password = "MySQL8IsGreat!",
    database = "whatabook"
)


#Constructing the function for the menu.
def show_menu():
    print("\n MAIN MENU ")
    print("1 View Books ")
    print("2 View Where The Store Is Located ")
    print("3 User's Account ")
    print("4 Exit Program ")

    try: 
        user_choice = int(input("\n Enter the number associated with the desired option: "))
        return user_choice

    except ValueError:
        print("The inputted number is invalid, please try again")

        sys.exit()

#Constructing the function for the application to show all books in Whatabook.
def show_books(_cursor):

    _cursor.execute("SELECT book_id, book_name, author, details_V FROM book")
    
    books = _cursor.fetchall()

    print(" Available Books ")
    for book in books:
        print("Book ID: {}".format(book[0]))
        print("Book Name: {}".format(book[1]))
        print("Author: {}".format(book[2]))
        print("Book Details: {}".format(book[3]))
        

#Constructing the function for the store's location details
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    location = _cursor.fetchall()

    print(" Whatabook Location ")
    for store in location:
        print("Store ID: {}".format(store[0]))
        print("Whatabook Location: {}".format(store[1]))
        print()


#Constructing the function for the method that will validate if the user has the correct ID.
def validate_user():
    print ("Please Validate your user ID")
    try:
        user_id = int(input("\n Enter your user ID"))
        if user_id < 1011 or user_id > 1013:
            print("No User ID was found. Please try again.")

            validate_user()
        return user_id
    except ValueError:
        sys.exit ("An invalid ID was Entered, pleaase try again.")

#Constructing the function for the user account menu
def show_account_menu():
    print("Account Menu ")
    print ("1. Wishlist ")
    print ("2. Add Books to Wishlist")
    print ("3. Main Menu ")
    account_choice = int(input("Enter the number associated with the desired option."))

    return account_choice 

#Constructing the function for the user's wishlist.
def show_wishlist(_cursor,_user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author\
        FROM wishlist\
        INNER JOIN user ON wishlist.user_id = user.user_id\
        INNER JOIN book ON wishlist.book_id = book.book_id\
        WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()
    
    print(" Books in Wishlist ")
    
    for book in wishlist:
        print("Book Name: {}".format(book[4]))
        print("Author: {}".format(book[5]))

#Constructing the function to allow the user to view the available books to be inserted into their wishlist. 
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author\
        FROM book\
        WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add_to_wishlist = _cursor.fetchall()

    print(" Books that can be added to the wishlist ")

    for book in books_to_add_to_wishlist:
        print(" Book ID: {}".format(book[0]))
        print(" Book Name: {}".format(book[1]))
        print(" Auther: {}".format(book[2]))

#Constructing the function that will allow the user to insert their disried book into their wishlist.
def add_book_to_whishlist(_cursor,_user_id,_book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


cursor = db.cursor()

print("WhataBook Application")

selection_choice = show_menu()

#Below code is focused on establishing the correct pathway in response to the user's inputted choice.
while selection_choice != 4:

    #The 'break' located on lines '134' and '138' is to avoid the ouput from infinitely repeating the output. 
    if selection_choice == 1:
        show_books(cursor)
        break

    if selection_choice == 2:
        show_locations(cursor)
        break

    if selection_choice == 3:
        verify_user = validate_user()
        user_account_choice = show_account_menu()

        if user_account_choice == 1:
            show_wishlist(cursor, verify_user)

        if user_account_choice == 2:
            show_books_to_add(cursor, verify_user)

            book_id = int(input(" Please enter the ID of the book you would like to add to your wishlist."))

            add_book_to_whishlist(cursor,verify_user,book_id)

            db.commit()

            print("The book ID {} was added to your wishlist.".format(book_id))

        if user_account_choice == 3:
            show_menu()

        #This code is to allow the user to know that the inputted response was wrong.
        if user_account_choice < 0 or user_account_choice > 3:
            print("The option chosen does not exist, please try again.")
            user_account_choice = show_account_menu()

    if selection_choice == 4:
        print("Whatabook Application is now close.")
        db.close()

    if selection_choice < 0 or selection_choice > 4:
        print("The option chosen does not exist, please try again.")
        selection_choice = show_menu()


