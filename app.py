from flask import Flask, request, jsonify, send_file, render_template
import requests
from songs import getSong, getAllSongs
from artists import getAllArtists
from flask_cors import CORS

'''
RVC GUI by Tiger14n at https://github.com/Tiger14n/RVC-GUI
The Weeknd (RVC) 1000 Epochs by clubbedsam#4419 at https://docs.google.com/spreadsheets/d/1leF7_c2Qf5iQRVkmOF51ZSynOvEjz8fHqwriX1wUMPw/edit#gid=1227575351
AudioSet by Google at https://research.google.com/audioset/download.html
'''


app = Flask(__name__)
CORS(app)

# def main():
    # createAIVocals(
    #     'https://www.youtube.com/watch?v=adLGHcj_fmA&pp=ygUTbGVhdmUgdGhlIGRvb3Igb3Blbg%3D%3D', 
    #     'Leave the Door Open', 
    #     'lil_uzi_vert_37K_1000'
    # )
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get_all_artists", methods=['GET'])
def get_all_artists():
    all_artists = getAllArtists()
    print(all_artists)

    all_artists_arr = []
    for artist in all_artists:
        all_artists_arr.append(artist[0].replace('\'', ''))

    return jsonify(all_artists_arr)

@app.route("/get_all_songs", methods=['GET'])
def get_all_songs():
    all_songs = getAllSongs()
    print(all_songs)

    all_songs_arr = []
    for song in all_songs:
        all_songs_arr.append(song[0].replace('\'', ''))

    return jsonify(all_songs_arr)

@app.route("/get_song", methods=['POST'])
def get_song():
    artist_and_song_request = request.data.decode('UTF8').replace("[", "").replace("]", "").replace("\"","")
    print(artist_and_song_request)
    artist_and_song_data = artist_and_song_request.split(',')

    artist_name = artist_and_song_data[0]
    song_name = artist_and_song_data[1]

    if artist_name == None or song_name == None:
        return jsonify("Error: Artist or song not found")

    print("Artist name:", artist_name)
    print("Song name:", song_name)

    song_file = getSong(song_name, artist_name)

    if song_file == None or not song_file.endswith('.wav') and not song_file.endswith('.mp3'):
        return jsonify(f'{song_file}')
    # song_file = 'static/output/lil_uzi_vert_37K_1000_Leave the Door Open_RVC.mp3'
    
    return jsonify(song_file)

if __name__ == '__main__':
    # main()
    app.run(host='127.0.0.1', port=8080)