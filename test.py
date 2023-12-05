import requests

BASE = "http://128.227.2.46:5000/"

def main():
    response = requests.get(BASE + "get_all_songs")
    print(response.json())

    response = requests.post(BASE + "get_song", '[Lil Uzi, Leave the Door Open]')
    print(response.json())

if __name__ == '__main__':
    main()