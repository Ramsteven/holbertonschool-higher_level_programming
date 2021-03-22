#!/usr/bin/node
/*
 square
*/

if (process.argv.length >= 3) {
  const square = process.argv[2];
  if (!isNaN(square)) {
    for (let i = 0; i < parseInt(square); i++) {
      console.log('X'.repeat(square));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
