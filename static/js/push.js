// import { chosenartist, chosensong } from "./kmp.js";
//import { chosensong, chosenartist } from "./stringhash.js";

const start = performance.now();

let finalTime = 0;
let audioURL = '';

//sending
let get_song = async (apiUrl, request) => await fetch(apiUrl, request)
.then(response => {
  if (response.ok) {
    console.log('POST request successful');
  } else {
    throw new Error('POST request failed');
  }
  return response.json();
})
  .then(response=> {
  const end = performance.now();
  finalTime = end - start;
  audioURL = response;
  console.log(response);
  return [finalTime, audioURL];
})
.catch(error => {
  console.error('Error:', error);
});

export { get_song };

  