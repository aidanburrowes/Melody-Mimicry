import { chosenartist, chosensong } from "./kmp.js";
//import { chosensong, chosenartist } from "./stringhash.js";
import { get_song } from "./push.js";

const audio = document.getElementById('audioPlayer');
const playBtn = document.getElementById('playBtn');
const pauseBtn = document.getElementById('pauseBtn');
const skipBtn = document.getElementById('skipBtn');

let finalTime = 0
let audioURL = ""

document.getElementById('finalizeButton').onclick = async () => {
  console.log(chosenartist);
  console.log(chosensong);

  const apiUrl = '/get_song';
  const finalPost = [
    chosenartist,
    chosensong
  ];

  //setting up post
  const request = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json' 
    },
    body: JSON.stringify(finalPost)
  };

  var spinner = document.querySelector('.spinner');
  spinner.classList.remove('hidden');
  const res = await get_song(apiUrl, request);
  finalTime = res[0];
  audioURL = res[1];
  spinner.classList.add('hidden');
  revealHiddenSection();
};

function revealHiddenSection() {

   var spinner = document.querySelector('.spinner');
  spinner.classList.add('hidden');
  
  var hiddenSection = document.querySelector('.hiddenSection');
  hiddenSection.style.display = 'block';

 

  hiddenSection.scrollIntoView({ behavior: 'smooth' });
  var audio = document.getElementById('audioPlayer');
  audio.src = audioURL;
  audio.play();
}

playBtn.addEventListener('click', function() {
  audio.play();
});

pauseBtn.addEventListener('click', function() {
  audio.pause();
});

skipBtn.addEventListener('click', function() {
  
  audio.currentTime += 10;
});

