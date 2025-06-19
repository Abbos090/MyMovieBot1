import psycopg2

def write_db(data):
    conn = psycopg2.connect("dbname=postgres user=postgres password=1221")
    cur = conn.cursor()

    query = "INSERT INTO serials (id, name, fasl, year, sec, category, language, video_id, qism) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    values = (data['id'], data['name'], data['fasl'], data['year'], data['sec'], data['category'], data['language'], data['video_id'], data['qism'])

    cur.execute(query, values)

    conn.commit()
    cur.close()
    conn.close()

