import psycopg2

def read_vide_db(id):
    conn = psycopg2.connect("dbname=postgres user=postgres password=1221")
    cur = conn.cursor()

    query = "SELECT name, category, video_id FROM admin WHERE id = %s;"
    cur.execute(query, (id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return {
            'name' : row[0],
            'category' : row[1],
            'video_id' : row[2]
        }

    return None

