

// function myFunction() {
//     document.getElementById("ratingForm").reset();
//     console.log('done')
//   }

// const date = new Date();
const d = new Date();

 

const date = d.getDate();

const month = d.getMonth() + 1; // Since getMonth() returns month from 0-11 not 1-12

const year = d.getFullYear();

const dateStr = date + "/" + month + "/" + year;

document.querySelector('.day').innerHTML = dateStr;




