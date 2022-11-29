import psycopg2

try:
    con = psycopg2.connect(user = "shasank",
                           password="",
                           host ="127.0.0.1",
                           port = "5432",
                           database = "sampledb")
    cur = con.cursor()

    cur.execute('''INSERT INTO Student (ROLL,NAME,AGE,ADDRESS) \
          VALUES (1, 'DAINA', 20, 'Mumbai')''');

    con.commit()
    print("Record inserted successfully")

except (Exception, psycopg2.Error) as error :
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing database connection.
    if (con):
            cur.close()
            con.close()
            print("PostgreSQL connection is closed")