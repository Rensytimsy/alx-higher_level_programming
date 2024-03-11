#!/usr/bin/env node
if (process.argv[3] === " " && process.argv[2] === " "){
    console.log("undefined");
}else{
    console.log(process.argv[2] + " is " + process.argv[3]);
}