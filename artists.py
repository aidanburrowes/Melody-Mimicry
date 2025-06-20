import psycopg2
import creds

def getAllArtists():
    conn = psycopg2.connect(
        host="hoarse-ray-6455.g8z.cockroachlabs.cloud", 
        port=26257,
        database="defaultdb", 
        user=f"{creds.cockroach_username}",
        password=f"{creds.cockroach_password}",
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