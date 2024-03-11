#!/usr/bin/env node
if (isNaN(process.argv[2])){
    console.log("Missing Number");
}
let i = 0;
while(i < process.argv[2]){
    console.log("X".repeat(process.argv[2]));
    i++;
}