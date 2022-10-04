#MySQL code for creating the tables named 'user', 'wishlist', 'book', and 'store'.
CREATE TABLE user(
    user_id INT NULL AUTO_INCREMENT,
    first_name VARCHAR (75) NOT NULL,
    last_name VARCHAR (75) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE wishlist(
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book (book_id)
);

CREATE TABLE book(
    book_id INT NULL AUTO_INCREMENT,
    book_name VARCHAR (200) NOT NULL,
    details_V VARCHAR (500),
    author VARCHAR (200) NOT NULL
    PRIMARY KEY (book_id)
);

CREATE TABLE store(
    store_id INT NOT NULL,
    locale VARCHAR (500) NOT NULL,
    PRIMARY KEY (store_id)
);

#Below are the MySQL insert statements for the required records for each table.

#Insert statements for table named store.
INSERT INTO store(store_id, locale)
    VALUES (1001, "1008 Almond RD, Knoxville, TN 36540"
);

#Insert statements for table named book.
INSERT into book(book_id, book_name, details_V, author)
    VALUES (01, "Ocean", "Information about the Pacific Ocean.", "James King");

INSERT into book(book_id, book_name, details_V, author)
    VALUES(02, "Ground", "Information About the History of the North American ground.", "Carl Sue");

INSERT into book(book_id, book_name, details_V, author)
    VALUES(03, "Taste of Gum", "An overview about the history of Gum in hte United States.", "David Martinez");

INSERT into book(book_id, book_name, details_V, author)
    VALUES(04, "Smelling Markers", " An investigation into the effects of long term permanent marker sniffing.", "Mark Sharp");

INSERT into book(book_id, book_name, details_V, author)
    VALUES(05, "VsCode and MySQL", "Informational help pertaining to the use of VsCode and MySQL.", "Marvin Brown");

INSERT into book(book_id, book_name, details_V, author)
    VALUES(06, "Apple vs Samsung", "Compairing the Pros and Cons between Apple and Samsung.", "Blake Smart");

INSERT into book(book_id, book_name, details_V, author)
    VALUES(07, "Whales", "An overview of how whales live in the ocean.", "Sung Yun");

INSERT into book(book_id, book_name, details_V, author)
    VALUES(08, "YouTube", "How YouTube can both help and hinder a child's development in school.", "Henry Armstrong");

INSERT into book(book_id, book_name, details_V, author)
    VALUES(09, "Bubbles", "How to build a bubble machine.", "Fred Evans");

#Insert statements for table named user.
INSERT INTO user(user_id, first_name, last_name)
    VALUES 
    (1011, "Jim", "Barry"),
    (1012, "Kevin", "Sanders"),
    (1013, "Jane", "Doe");

#Insert statements for table named wishlist.
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = "Jim"),
        (SELECT book_id FROM book WHERE book_name = "Ocean")
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = "Kevin"),
        (SELECT book_id FROM book WHERE book_name = "Ground")
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = "Jane"),
        (SELECT book_id FROM book WHERE book_name = "Bubbles")
    );
