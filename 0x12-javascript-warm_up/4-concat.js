#!/usr/bin/node

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('Error: Two arguments are required.');
} else {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
}
