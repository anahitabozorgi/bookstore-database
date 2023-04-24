import mysql.connector
from datetime import date

mydb = mysql.connector.connect(user='Ana', password='12345', host='localhost')
mycursor = mydb.cursor()

mycursor.execute("USE BookStore")
def function():
    print("لطفا شماره درخواستی را که دارید وارد نمایید(شماره درخواست در کنار هر درخواست امده است)")
    print("1.ثبت نام")
    print("2.خرید کتاب")
    print("3.اسم کتاب ها همراه با نویسنده انها")
    print("4.کتاب ها همراه با موجودی باقی مانده انها")
    print("5.مشاهده نام پرفروش ترین کتاب")
    print("6.لیست کتاب ها به ترتیب فروش")
    print("7.کتاب های ناموجود")
    print("8.مشاهده کتاب های کلاسیک")
    print("9.مشاهده کتاب های فانتزی")
    print("10.لیست کتاب هایی که کاربر خریده است")
    shomare = input("شماره درخواست: ")
    if(shomare == '1'):
        name = input("لطفا نام خود را وارد کنید: ")
        number = input("شماره تلفن خود را وارد کنید: ")
        print("ژانر های کتاب ها همراه با ایدی هر کدام:")
        mycursor.execute("SELECT Categories.Name,Categories.CatID FROM Categories")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        bok=input("لطفا ایدی مربوط به ژانری که علاقه دارید را وارد کنید: ")
        sql = "INSERT INTO Customers (Name , PhoneNumber,Interest) VALUES (%s,%s, %s)"
        val = [
            (name,number,bok)
        ]
        mycursor.executemany(sql, val)
        mydb.commit()
        print("شما با موفقیت ثبت نام شدید")
        sql = "SELECT CustomerID FROM customers WHERE PhoneNumber = %s"
        adr = (number,)
        mycursor.execute(sql, adr)
        myresult = mycursor.fetchall()
        print("به شما یک آیدی داده میشود که برای مشاهده لیست خرید خود لازم است که ایدی خود را حفظ باشید")
        for x in myresult:
            for i in x:
                print("شماره ایدی شما برابر است با:",i)
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()
    elif(shomare == '2'):
        id1 = input("برای خرید کتاب لطفا شماره آیدی که هنگام ثبت نام به شما داده شده بود را وارد کنید: ")
        print("ایدی هر یک از کتاب ها در کنار نام کتاب اورده شده است")

        mycursor.execute("SELECT Books.Name,Books.BookID FROM Books WHERE "
                         "exists (SELECT * FROM Depository where Books.BookID = Depository.BID)")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        bok = input("شماره آیدی کتابی که میخواهید را وارد کنید: ")
        mycursor.execute("SELECT Depository.supply FROM Depository"
                         " WHERE Depository.BID=%s; ", (bok,));
        myresult = mycursor.fetchall()
        for x in myresult:
            a = int(x[0])
            d = a-1
            b = str(d)

        ##des
        sql = "UPDATE Depository SET Supply = %s WHERE BID = %s"
        val = (b, bok)

        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("SELECT  Books.Price FROM Books"
                         " WHERE Books.BookID=%s; ", (bok,));
        myresult = mycursor.fetchall()
        for x in myresult:
            ac = x[0]

        today = date.today()
        ####factors
        sql = "INSERT INTO Factors (Date_ , Cost ,CustomerID ,BOOKID ) VALUES (%s,%s,%s,%s)"
        val = [
        (today ,ac ,id1,bok)
        ]
        mycursor.executemany(sql, val)
        mydb.commit()

        sql = "DELETE FROM Depository WHERE supply = %s"
        val = ("0", )

        mycursor.execute(sql, val)
        mydb.commit()
        print("شما با موفقیت کتاب را خریدید")
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()

    elif (shomare == '3'):
        mycursor.execute("SELECT Authors.Name , Books.Name FROM Authors JOIN Books "
                         " ON Authors.AuthorID=Books.AuthorID ; ");
        myresult = mycursor.fetchall()
        print("1.The authors with their books :")
        for x in myresult:
            print(x)
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()

    elif(shomare == '4'):
        mycursor.execute("SELECT Books.Name , Depository.supply FROM Books JOIN Depository "
                         " ON Depository.BID=Books.BookID ; ");
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()

    elif(shomare == '5'):
        mycursor.execute("SELECT Books.Name FROM Books , Factors WHERE Books.BookID=Factors.BookID "
                         "GROUP BY Factors.BookID "
                         "ORDER BY count(*)  DESC Limit 1 ");
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()

    elif (shomare == '6'):
        mycursor.execute("SELECT Books.Name FROM Books , Factors WHERE Books.BookID=Factors.BookID "
                         "GROUP BY Factors.BookID "
                         "ORDER BY count(*) DESC ");
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()

    elif (shomare == '7'):
        mycursor.execute("SELECT Books.Name FROM Books WHERE "
                         "not exists (SELECT * FROM Depository where Books.BookID = Depository.BID)")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()

    elif (shomare == '8'):
        Name = "Classic"
        mycursor.execute("SELECT Books.Name  FROM Categories JOIN Books   "
                         "ON Categories.catID = Books.categoryID "
                         " WHERE Categories.Name=%s; ", (Name,));
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()

    elif (shomare == '9'):
        Name = "Fantasy"
        mycursor.execute("SELECT Books.Name  FROM Categories JOIN Books   "
                         "ON Categories.catID = Books.categoryID "
                         " WHERE Categories.Name=%s; ", (Name,));
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()

    elif (shomare == '10'):
        id1 = input("برای مشاهده لیست کالا لطفا شماره آیدی که هنگام ثبت نام به شما داده شده بود را وارد کنید: ")

        mycursor.execute("SELECT Customers.Name, Books.Name  FROM Customers JOIN Factors JOIN BOOKS  "
                         "ON Customers.CustomerID=Factors.CustomerID AND "
                         "Books.BookID = Factors.BookID WHERE Customers.CustomerID=%s; ", (id1,));
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        dar = input("ااگر درخواست دیگری دارید عدد 1 و اگر میخواهید خارج شوید عدد 2 را وارد کنید: ")
        if (dar == '2'):
            print("شما خارج شدید")
        elif (dar == '1'):
            function()



function()