let artist_results = async() => await fetch('/get_all_artists')
.then(response => response.json())
.catch(error => {
  console.error('Error fetching artists:', error);
});

let song_results = async () => await fetch('/get_all_songs')
.then(response => response.json())
.catch(error => {
  console.error('Error fetching songs:', error);
});

let songsArr = await song_results();
console.log(songsArr);

let artists_arr = await artist_results();
console.log(artists_arr);

export { artists_arr, songsArr };