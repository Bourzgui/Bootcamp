function hotelCost(nights) {
    return nights * 140; 
}

function planeRideCost(destination) {
    if (destination.toLowerCase() === "london") return 183; 
    if (destination.toLowerCase() === "paris") return 220;
    return 300;
}

function rentalCarCost(days) {
    let cost = days * 40;
    if (days > 10) cost *= 0.95; // 5% discount
    return cost;
}

function totalVacationCost() {
    let nights = NaN;
    let days = NaN;
    let destination = "";
    
    while (isNaN(nights)) {
        nights = Number(prompt("How many nights in the hotel?")); 
    }
    
    while (!destination || typeof destination !== "string") {
        destination = prompt("What's your destination?"); 
    }
    
    while (isNaN(days)) {
        days = Number(prompt("How many days for car rental?")); 
    }
    
    const hotel = hotelCost(nights);
    const plane = planeRideCost(destination);
    const car = rentalCarCost(days);
    
    return `The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}. 
    Total: $${hotel + plane + car}`;
}

console.log(totalVacationCost()); 