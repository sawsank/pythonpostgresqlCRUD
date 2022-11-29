import psycopg2

try:
    con = psycopg2.connect(user="shasank",
                           password = "",
                           port="5432",
                           database = "sampledb")
    cur = con.cursor()

    cur.execute("SELECT roll, name, age,  address from Student")
    records = cur.fetchall()
    print("      student information      ")
    print("---------------------------------")
    for row in records:
        print("     ROLL = ", row[0])

        print("     NAME = ", row[1])

        print("     AGE = ", row[2])

        print("     ADDRESS = ", row[3])
        "\n"

    con.commit()
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection
        if(con):
            cur.close()
            con.close()
            print("\nPostgreSQL connection is closed")
