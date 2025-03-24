const people = ["Greg", "Mary", "Devon", "James"];
people.shift();  // removes first element

// Replace James 
people[people.indexOf("James")] = "Jason";

// Add your name
people.push("fatima zahra");

console.log(people.indexOf("Mary"));  

const copy = people.slice(1, -1);  // starts at index 1, ends before last element
console.log(copy);  // ["Devon", "Jason"]

console.log(people.indexOf("Foo"));  // not exist in array

const last = people[people.length - 1];

for (let person of people) {
    console.log(person);
}

for (let person of people) {
    console.log(person);
    if (person === "Devon") break;
}