import psycopg2 #import psycopg module


try:
    con = psycopg2.connect(user ="shasank",
                           password = "",
                           host="127.0.0.1",
                           port="5432",
                           database = "sampledb")
    cur = con.cursor()

    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("\n you  are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to Postgresql",error)

finally:
            # closing database connection.
            if (con):
                cur.close()
                con.close()
            print("PostgreSQL connection is closed")