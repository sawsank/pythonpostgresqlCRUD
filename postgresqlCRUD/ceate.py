import psycopg2

try:
    con=psycopg2.connect(user = "shasank",
                         password = "",
                         host="127.0.0.1",
                         port = "5432",
                         database="sampledb")
    cur = con.cursor()

    cur.execute('''CREATE TABLE Student
          (ROll INT PRIMARY KEY     NOT NULL,
          NAME           TEXT    NOT NULL,
          AGE            INT     NOT NULL,
          ADDRESS        CHAR(50)
                   );''')
    con.commit()

    print("Table created successfully")

except (Exception, psycopg2.Error) as error :
    print("Error while connection to PostgreSQL", error)

finally:
        # closing database connection.
        if (con):
            cur.close()
            con.close()
            print("PostgreSQL connection is closed")