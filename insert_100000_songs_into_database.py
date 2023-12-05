import psycopg2
import creds
import os
import csv

def main():
    conn = psycopg2.connect(
        host="hoarse-ray-6455.g8z.cockroachlabs.cloud", 
        port=26257,
        database="defaultdb", 
        user=f"{creds.cockroach_username}",
        password=f"{creds.cockroach_password}",
        sslmode="require" 
    )
    cur = conn.cursor()

    youtube_url = 'https://www.youtube.com/watch?v='
    urls = []

    file = open('data/unbalanced_train_segments.csv')
    reader = csv.reader(file, delimiter=',')

    count = 0
    offset = 3
    for row in reader:
        if count < offset:
            count += 1
            continue
        for i, column in enumerate(row):
            if i != 0 or count > 100000 + offset:
                break
            urls.append(column)
            count += 1

    for url in urls:
        cur.execute(f"INSERT INTO songs2 (song_name, artist_name, link) VALUES ('{url}', '{url}', '{youtube_url}{url}');")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()