#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let s = '';
    for (let j = 0; j < size; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
