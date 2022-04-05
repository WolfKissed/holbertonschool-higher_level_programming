#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
}
const a = new Array(Number(size)).fill('X').join('');
for (let i = 0; i < x; i++) {
  console.log(a);
}
