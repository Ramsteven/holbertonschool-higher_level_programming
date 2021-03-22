#!/usr/bin/node
/*
 value_argument
*/
const argument = process.argv[2];
if (argument) {
  console.log(argument);
} else {
  console.log('No argument');
}
