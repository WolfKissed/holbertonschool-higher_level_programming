#!/usr/bin/node
const x = 'C is fun';
if (isNaN(process.argv[2])) {
	console.log('Missing number of occurrences');
	process.exit(1);
} else {
for (let i = 0; i < process.argv[2]; i++) {
	console.log(x);
}
}
