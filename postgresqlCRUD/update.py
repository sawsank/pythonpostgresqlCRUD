import psycopg2

try:
    con = psycopg2.connect(user="shasank",
                           password = "password",
                           host = "127.0.0.1",
                           port ="5432",
                           database="sampledb")
    cur = con.cursor()

    cur.execute("UPDATE student set AGE = 25")
    con.commit()

    cur.execute("SELECT roll, name, age, address from student")
    records = cur.fetchall()
    print("      STUDENT INFORMATION    ")
    print("--------------------------------")
    for row in records:
        print(" ROLL= ", row[0])

        print(" NAME= ", row[1])

        print(" AGE= ", row[2])

        print(" ADDRESS= ", row[3])
    print(" \n Age is updated \n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if(con):
        cur.close()
        con.close()
        print("\nPostgreSQL connection is closed")