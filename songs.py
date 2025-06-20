import psycopg2
from ai_vocals import createAIVocals
import os

cockroach_username = os.environ["COCKROACH_USERNAME"]
cockroach_password = os.environ["COCKROACH_PASSWORD"]


def getAllSongs():
    # Connect to database
    conn = psycopg2.connect(
        host="hoarse-ray-6455.g8z.cockroachlabs.cloud", 
        port=26257,
        database="defaultdb", 
        user=f"{cockroach_username}",
        password=f"{cockroach_password}",
        sslmode="require" 
    )
    cur = conn.cursor()

    cur.execute("SELECT song_name FROM songs")
    all_songs = cur.fetchall()

    cur.close()
    conn.close()

    return all_songs

def getSong(song_name, artist_name):
    # Connect to database
    conn = psycopg2.connect(
        host="hoarse-ray-6455.g8z.cockroachlabs.cloud", 
        port=26257,
        database="defaultdb", 
        user=f"{cockroach_username}",
        password=f"{cockroach_password}",
        sslmode="require" 
    )
    cur = conn.cursor()

    print(song_name)
    cur.execute(
        f"SELECT link FROM songs WHERE song_name = '{song_name}'"
    )
    link = cur.fetchone()

    if link == None:
        return "Error: Song not found"
    
    link = link[0]

    cur.execute(
        f"SELECT path FROM artists WHERE artist_name = '{artist_name}'"
    )
    artist_path = cur.fetchone()

    if artist_path == None:
        return "Error: Artist not found"
    
    artist_path = artist_path[0]

    cur.close()
    conn.close()

    return createAIVocals(link, song_name, artist_path)


