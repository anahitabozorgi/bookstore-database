import mysql.connector
mydb=mysql.connector.connect(host= "localhost",user="Ana",passwd="12345")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE BookStore")

mycursor.execute("USE BookStore")

###Tables ###

mycursor.execute("CREATE TABLE Authors( AuthorID INT AUTO_INCREMENT,Name NVARCHAR(50) NOT NULL,Description nvarchar(300)"
                 " ,PRIMARY KEY (AuthorID)  )");


mycursor.execute("CREATE TABLE Publishers(PublisherID INT AUTO_INCREMENT, Name NVARCHAR(50) NOT NULL, PhoneNumber BIGINT, Address nvarchar(150), PRIMARY KEY(PublisherID))");

mycursor.execute("CREATE TABLE Categories( CatID INT AUTO_INCREMENT, Name NVARCHAR(50) NOT NULL,Description nvarchar(300) ,PRIMARY KEY (CatID))");


mycursor.execute("CREATE TABLE Books (BookID INT NOT NULL  AUTO_INCREMENT,Name NVARCHAR(50) NOT NULL,Year INT NOT NULL,"
                " Price int NOT NULL,AuthorID int, PublisherID int, CategoryID int,"
                " PRIMARY KEY(BookID), FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID),"
                "FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID),"
              "FOREIGN KEY (CategoryID) REFERENCES Categories(CatID))");


mycursor.execute("CREATE TABLE Depository ( BID INT , Supply INT NOT NULL,FOREIGN KEY (BID) REFERENCES Books(BookID), PRIMARY KEY(BID));");


mycursor.execute("CREATE TABLE Customers (CustomerID INT AUTO_INCREMENT,Name NVARCHAR(50) NOT NULL, PhoneNumber BIGINT NOT NULL,"
                "Address nvarchar(150),Interest int,FOREIGN KEY (Interest) REFERENCES Categories(CatID),"
                "PRIMARY KEY (CustomerID) );");
mycursor.execute("CREATE TABLE Factors (FactorID INT AUTO_INCREMENT ,Date_ DATETIME, Cost INT NOT NULL,CustomerID INT,"
                "BOOKID INT, FOREIGN KEY (BOOKID) REFERENCES Books(BookID),"
                " FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),"
               "PRIMARY KEY(FactorID ));");
#
## Inserts ###
## Insert to Authors ###
#
sql = "INSERT INTO Authors (Name, Description) VALUES (%s, %s)"
val =  ('J. R. R. Tolkien', 'John Ronald Reuel Tolkien (Birth: 3 January 1892  and died 2 September 1973) was an English writer, poet, philologist, and academic')
mycursor.execute(sql, val)
sql = "INSERT INTO Authors (Name, Description) VALUES (%s, %s)"
val = (' George R. R. Martin', 'George Raymond Richard Martin (born George Raymond Martin; September 20, 1948), is an American novelist and short story writer');
mycursor.execute(sql, val)
sql = "INSERT INTO Authors (Name, Description) VALUES (%s, %s)"
val = ('Stephen king', 'Stephen Edwin King (born September 21, 1947) is an American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels.');
mycursor.execute(sql, val)
sql = "INSERT INTO Authors (Name, Description) VALUES (%s, %s)"
val = ('Sidney Sheldon', 'Sheldon was prominent in the 1930s, first working on Broadway plays and then in motion pictures, notably writing the successful comedy.');
mycursor.execute(sql, val)
sql = "INSERT INTO Authors (Name, Description) VALUES (%s, %s)"
val = ('Charlotte Brontë', 'Charlotte Brontë  was an English novelist and poet, the eldest of the three Brontë sisters who survived into adulthood and whose novels became classics of English literature.');
mycursor.execute(sql, val)
sql = "INSERT INTO Authors (Name, Description) VALUES (%s, %s)"
val = ('Paulo Coelho', 'Paulo Coelho de Souza Portuguese:  born 24 August 1947) is a Brazilian lyricist and novelist.');
mycursor.execute(sql, val)
sql = "INSERT INTO Authors (Name, Description) VALUES (%s, %s)"
val =  (' Tina Fey', 'Elizabeth Stamatina "Tina" Fey is an American actress, comedian, writer, producer, and playwright. ');
mycursor.execute(sql, val)
sql = "INSERT INTO Authors (Name, Description) VALUES (%s, %s)"
val =  ('Ernest Cline', 'Ernest Christy Cline (born March 29, 1972) is an American science fiction novelist, slam poet, and screenwriter. ');
mycursor.execute(sql, val)
mydb.commit()



sql = "INSERT INTO Publishers (Name, PhoneNumber,Address) VALUES (%s, %s,%s)"
val = [
  ('Allen & Unwin', '61284250100','83 Alexander St ,Crows Nest, NSW 2065,AUSTRALIA'),
  ('Smith, Elder & Co.', '2222222','Fenchurch Street, London (1824)'),
  ('Doubleday','2129407390', '1745 Broadway New York, NY 10019'),
  ('Penguin Random House', '442085792652',' '),
  ('Bantam Books', '2125726066',' ' ),
  ('Brown and Company', '9901338635',' ' ),
  ('Crown Publishing Group', '8275338758','Ashland, Ohio, United States' )


]
mycursor.executemany(sql, val)
mydb.commit()


sql = "INSERT INTO Categories (Name,Description) VALUES (%s, %s)"
val = [
  ('Horror', 'Horror is a genre of speculative fiction which is intended to frighten, scare, or disgust. Literary historian'),
  ('Fantasy', 'Fantasy is a genre of speculative fiction set in a fictional universe, often inspired by real world myth and folklore. Its roots are in oral traditions, which then became fantasy literature and drama'),
  ('Classic','A classic is a book accepted as being exemplary or noteworthy, for example through an imprimatur such as being listed in a list of great books, or through a readers personal opinion.'),
  ('Comedy','professional entertainment consisting of jokes and sketches, intended to make an audience laugh.'),
  ('Romantic','conducive to or characterized by the expression of love.'),
  ('Science Fiction','fiction based on imagined future scientific or technological advances and major social or environmental changes, frequently portraying space or time travel and life on other planets. '),
]
mycursor.executemany(sql, val)
mydb.commit()


sql = "INSERT INTO Books (Name,Year, Price ,AuthorID , PublisherID , CategoryID) VALUES (%s, %s,%s,%s,%s,%s)"
val = [
('Lord of rings','1954','100','1','1','2'),
('Hobits','1937','100','1','1','2'),
('A Game of Thrones ','1996','140','2','5','2'),
('A Clash of Kings ','1998','140','2','5','2'),
('A Storm of Swords ','2000','110','2','5','2'),
('A Feast for Crows ','2005','80','2','5','2'),
('A Dance with Dragons ','2011','150','2','5','2'),
('The Shining','1977','70','3','3','1'),
('Misery','1987','50','3','3','1'),
('It','1986','50','3','3','1'),
('Shirley‎','1849','100','5','2','3'),
('Veronika Decides to Die‎','1998','100','6','4','3'),
('The winner stands alone‎','2008','100','6','4','3'),
('The Alchemist‎','1988','100','6','4','3'),
('Ready Player‎','2011','120','8','7','6'),
('Bossypants‎','2011','56','7','6','4'),

]
mycursor.executemany(sql, val)
mydb.commit()


sql = "INSERT INTO Customers (Name , PhoneNumber,Interest) VALUES (%s,%s, %s)"
val = [
    ('Ali','015461311','2'),
    ('John', '641344351', '3'),
    ('Aragon', '454534347', '1'),
    ('Arya', '123456781', '1'),
    ('Maila', '4567356781', '2'),

]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Depository (BID,Supply) VALUES (%s,%s)"
val = [
    ('2','20'),
    ('4', '45'),
    ('5', '2'),
    ('11', '6'),
    ('12', '1'),
    ('13', '27'),
    ('7', '13'),
    ('9','71')
]
mycursor.executemany(sql, val)
mydb.commit()


sql = "INSERT INTO Factors (Date_ , Cost ,CustomerID ,BOOKID ) VALUES (%s,%s,%s,%s)"
val = [
('2017-10-07' ,'100' ,'2','2'),
('2019-01-19' ,'150' ,'1','11'),
('2019-05-23' ,'110' ,'5','9'),
('2019-07-07' ,'110' ,'2','9'),
('2019-08-08' ,'120' ,'3','7'),
('2020-02-11' ,'200' ,'1','4'),
('2020-03-20' ,'50' ,'1','13'),
('2018-01-16' ,'50' ,'1','1'),
]
mycursor.executemany(sql, val)
mydb.commit()
