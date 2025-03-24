const family = {
    father: "John",
    mother: "Jane",
    son: "Mike"
};

// Keys
for (let key in family) {
    console.log(key);
}

// Values
for (let key in family) {
    console.log(family[key]);
}