import { artists_arr, songsArr } from "./connect.js";
var artistsArray = [...artists_arr];
var songsArray = [...songsArr];

function computeLPSArray(pattern) {
  const lps = [0];
  let len = 0;
  let i = 1;

  while (i < pattern.length) {
    if (pattern[i] === pattern[len]) {
      len++;
      lps[i] = len;
      i++;
    } else {
      if (len !== 0) {
        len = lps[len - 1];
      } else {
        lps[i] = 0;
        i++;
      }
    }
  }
  return lps;
}

function KMPSearch(text, pattern) {
  const lps = computeLPSArray(pattern);
  const matches = [];
  let i = 0;
  let j = 0;

  while (i < text.length) {
    if (pattern[j] === text[i]) {
      i++;
      j++;
    }
    if (j === pattern.length) {
      matches.push(i - j);
      j = lps[j - 1];
    } else if (i < text.length && pattern[j] !== text[i]) {
      if (j !== 0) {
        j = lps[j - 1];
      } else {
        i++;
      }
    }
  }
  return matches.length > 0;
}

// // Usage:
// const popularArtists = [
//   "Drake", "Travis Scott", "Michael Jackson", "Taylor Swift",
//   "Lana Del Rey", "Justin Bieber", "The Weeknd", "NBA Youngboy", "Playboi Carti", "Kanye West", "Yeat",
//   // Add more artists here...
// ];

// const songs = [
//   "Hotline Bling","God's Plan","One Dance", "In My Feelings", "Started From the Bottom", 
//   "Passionfruit", "Hold On, We're Going Home", "Too Good", "Nice for What", "Nonstop"
// ];

const popularArtists = [...artistsArray];
const songs = [...songsArray];

function getMatchingArtists(input) {
  const matchingArtists = popularArtists.filter(artist => KMPSearch(artist.toLowerCase(), input.toLowerCase()));
  return matchingArtists.slice(0, 5); // Limit suggestions to 5
}

function getMatchingSongs(input) {
  const matchingSongs = songs.filter(song => KMPSearch(song.toLowerCase(), input.toLowerCase()));
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
    noMatch2.textContent = "No matching songs found";
    suggestions2.appendChild(noMatch2);
  }
});

document.getElementById('finalSong').textContent = chosensong;


export {chosensong, chosenartist};
