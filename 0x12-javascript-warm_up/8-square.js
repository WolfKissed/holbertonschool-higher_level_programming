#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
}
const a = new Array(Number(size)).fill('X').join('');
for (let i = 0; i < size; i++) {
  console.log(a);
}
