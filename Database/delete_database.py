import psycopg2

def delete_db(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1221")
    cur = conn.cursor()

    query = "delete from admin where id=%s;"

    cur.execute(query, (id,))

    conn.commit()

    cur.close()
    conn.close()
