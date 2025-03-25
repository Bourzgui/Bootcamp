function changeEnough(itemPrice, amountOfChange) {
    const coinValues = [0.25, 0.10, 0.05, 0.01];
    let totalChange = 0;
    
    for (let i = 0; i < amountOfChange.length; i++) {
        totalChange += amountOfChange[i] * coinValues[i]; //add to total
    }
    
    return totalChange >= itemPrice; 
}

// Test cases
console.log(changeEnough(4.25, [25, 20, 5, 0]));  
console.log(changeEnough(14.11, [2, 100, 0, 0])); 
console.log(changeEnough(0.75, [0, 0, 20, 5]));   