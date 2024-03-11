#!/usr/bin/env node
function print_square(size){
    let square_symbol = "X".repeat(size);
    for (let i = 0; i < size; i++){
	console.log(square_symbol);
    }
}
print_square(process.argv[2]);
