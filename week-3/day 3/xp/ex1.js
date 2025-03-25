function displayNumbersDivisible(divisor = 23) {
    let sum = 0;
    let divisibleNumbers = [];
    
    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            divisibleNumbers.push(i); //add to table 
            sum += i;
        }
    }
    
    console.log(divisibleNumbers.join(' ')); 
    console.log(`Sum: ${sum}`);
}

// Test cases
displayNumbersDivisible();    
displayNumbersDivisible(3);   
displayNumbersDivisible(45);  