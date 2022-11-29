import psycopg2

try:
    con = psycopg2.connect(user="shasank",
                           password="",
                           host = "127.0.0.1",
                           database = "sampledb")

    cur = con.cursor()

    cur.execute("DELETE from Student where roll= 1;")
    con.commit()
    print("Total number of rows deleted: ", cur.rowcount)

    cur.execute("SELECT roll, name, age,  address from Student")
    records = cur.fetchall()
    print("     STUDENT INFORMATION       ")
    print("---------------------------------")
    for row in records:
        print("     ROLL =", row[0])

        print("     ROLL =", row[1])

        print("     ROLL =", row[2])

        print("     ROLL =", row[3])
        "\n"

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL",error)

finally:

    if(con):
        cur.close()
        con.close()
        print("\nPostgreSQL connection is closed")