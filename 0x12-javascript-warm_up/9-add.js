#!/usr/bin/node
/*
  js
*/
const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  if (isNaN(parseInt(a)) || isNaN(parseInt(b))) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}

add(a, b);
