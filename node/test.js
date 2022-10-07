const path = require("path");
console.log("Hello, world")
const hello = "Hello from Node JS Variable!"
console.log('Printing variable hello: ${hello}');
console.log(hello)

console.log("directory name: " +_dirname);
console.log("directory and file name: " +_filename);

console.log("Using PATH module:");
console.log('Hello from file ${path.basename(_filename)}');
console.log('Process args: ${process.argv}');