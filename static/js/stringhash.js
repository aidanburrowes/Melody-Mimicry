import { artists_arr, songsArr } from "./connect.js";
var artistsArray = [...artists_arr];
var songsArray = [...songsArr];


// const popularArtists = [
//   "Drake", "Travis Scott", "Michael Jackson", "Taylor Swift",
//   "Lana Del Rey", "Justin Bieber", "The Weeknd", "NBA Youngboy", "Playboi Carti", "Kanye West", "Yeat",
//   // Add more artists here...
// ];

const popularArtists = [...artistsArray];

// const songs = [
//   "Hotline Bling","God's Plan","One Dance", "In My Feelings", "Started From the Bottom", 
//   "Passionfruit", "Hold On, We're Going Home", "Too Good", "Nice for What", "Nonstop"
// ];
const songs = [...songsArray];

function stringHash(text) {
  let hash = 0;
  if (text.length === 0) return hash;

  for (let i = 0; i < text.length; i++) {
    const char = text.charCodeAt(i);
    hash = (hash << 5) - hash + char;
    hash &= hash; // Convert to 32-bit integer
  }
  return hash;
}

function getMatchingArtists(input) {
  const matchingArtists = popularArtists.filter(artist => {
    return artist.toLowerCase().includes(input.toLowerCase());
  });
  return matchingArtists.slice(0, 5); // Limit suggestions to 5
}

function getMatchingSongs(input) {
  const matchingSongs = songs.filter(song => {
    return song.toLowerCase().includes(input.toLowerCase());
  });
  return matchingSongs.slice(0, 5); // Limit suggestions to 5
}



const searchInput = document.getElementById("artistsearch");
const suggestions = document.getElementById("suggestions1");
let chosenartist = "";
searchInput.addEventListener("input", function() {
  const inputValue = this.value;
  suggestions.innerHTML = ""; // Clear previous suggestions

  if (inputValue.length === 0) {
    return;
  }

  const matchingArtists = getMatchingArtists(inputValue);
  if (matchingArtists.length > 0) {
    for (const artist of matchingArtists) {
      const suggestionItem = document.createElement("div");
      suggestionItem.textContent = artist;
      suggestionItem.classList.add("suggestion");
      suggestionItem.addEventListener("click", function() {
        searchInput.value = artist;
        chosenartist = artist;
        suggestions.innerHTML = ""; // Clear suggestions on click
      });
      suggestions.appendChild(suggestionItem);
    }
  } else {
    const noMatch = document.createElement("div");
    noMatch.textContent = "No matching artists found";
    suggestions.appendChild(noMatch);
  }
});


const searchInput2 = document.getElementById("songsearch");
const suggestions2 = document.getElementById("suggestions2");
let chosensong = "";

searchInput2.addEventListener("input", function() {
  const inputValue = this.value;
  suggestions2.innerHTML = ""; // Clear previous suggestions

  if (inputValue.length === 0) {
    return;
  }

  const matchingSongs = getMatchingSongs(inputValue);
  if (matchingSongs.length > 0) {
    for (const song of matchingSongs) {
      const suggestionItem2 = document.createElement("div");
      suggestionItem2.textContent = song;
      suggestionItem2.classList.add("suggestion");
      suggestionItem2.addEventListener("click", function() {
        searchInput2.value = song;
        chosensong = song;
        suggestions2.innerHTML = ""; // Clear suggestions on click
      });
      suggestions2.appendChild(suggestionItem2);
    }
  } else {
    const noMatch2 = document.createElement("div");
    noMatch2.textContent = "No matching artists found";
    suggestions2.appendChild(noMatch2);
  }
});