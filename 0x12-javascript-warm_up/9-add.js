#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
if (isNaN(a)) {
  console.log('NaN');
} else if (isNaN(b)){
console.log('NaN');
}
console.log(Number(a) + Number(b));
