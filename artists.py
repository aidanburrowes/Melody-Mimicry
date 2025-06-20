import psycopg2
import os

cockroach_username = os.environ["COCKROACH_USERNAME"]
cockroach_password = os.environ["COCKROACH_PASSWORD"]

def getAllArtists():
    conn = psycopg2.connect(
        host="hoarse-ray-6455.g8z.cockroachlabs.cloud", 
        port=26257,
        database="defaultdb", 
        user=f"{cockroach_username}",
        password=f"{cockroach_password}",
        sslmode="require" 
    )
    cur = conn.cursor()

    cur.execute(
        f"SELECT artist_name FROM artists"
    )
    all_artists = cur.fetchall()

    cur.close()
    conn.close()

    return all_artists