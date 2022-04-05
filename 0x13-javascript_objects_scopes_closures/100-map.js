#!/usr/bin/node
const a = require('./100-data.js').list;
console.log(a);
const b = a.map((x, index) => x * index);
console.log(b);
