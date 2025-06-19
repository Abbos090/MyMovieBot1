import psycopg2

def read_vide_db(id):
    conn = psycopg2.connect("dbname=postgres user=postgres password=1221")
    cur = conn.cursor()

    query = "SELECT name, qism, year, sec, category, language, video_id FROM serials WHERE id = %s;"
    cur.execute(query, (id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return {
            'name' : row[0],
            'qism' : row[1],
            'year' : row[2],
            'sec' : row[3],
            'category' : row[4],
            'language' : row[5],
            'video_id' : row[6],
        }

    return None

def read_qism_db(id):
    conn = psycopg2.connect("dbname=postgres user=postgres password=1221")
    cur = conn.cursor()

    query = "SELECT name, qism, year, sec, category, language, video_id FROM serials WHERE id = %s;"
    cur.execute(query, (id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return