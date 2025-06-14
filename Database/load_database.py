import psycopg2

def read_vide_db(id):
    conn = psycopg2.connect("dbname=postgres user=postgres password=1221")
    cur = conn.cursor()

    query = "SELECT video_id FROM admin WHERE id = %s;"
    cur.execute(query, (id,))
    row = cur.fetchone()  # faqat bitta natija kerak bo‘lsa

    cur.close()
    conn.close()

    if row:  # agar topilsa
        return row[0]  # bu yerda row = ('video_id',) => row[0] = 'video_id'
    return None  # agar yo'q bo'lsa

