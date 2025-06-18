import psycopg2

def read_vide_db(id):
    conn = psycopg2.connect("dbname=postgres user=postgres password=1221")
    cur = conn.cursor()

    query = "SELECT name, year, sec, category, language, video_id FROM admin WHERE id = %s;"
    cur.execute(query, (id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return {
            'name' : row[0],
            'year' : row[1],
            'sec' : row[2],
            'category' : row[3],
            'language' : row[4],
            'video_id' : row[5],
        }

    return None

