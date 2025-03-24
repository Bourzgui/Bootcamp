let pattern = "";
for (let i = 1; i <= 6; i++) {
    pattern = "* ".repeat(i).trim(); 
    console.log(pattern);
}

for (let i = 1; i <= 6; i++) {
    let line = "";
    for (let j = 1; j <= i; j++) {
        line += "* ";
    }
    console.log(line.trim()); 
}