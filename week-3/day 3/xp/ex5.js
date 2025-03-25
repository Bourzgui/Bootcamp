const container = document.getElementById("container");
console.log(container);

const lists = document.getElementsByClassName("list");

lists[0].children[1].textContent = "Richard";

lists[1].children[1].remove();
for (let list of lists) {
    list.firstElementChild.textContent = "fatima zahra";
}

for (let list of lists) {
    list.classList.add("student_list");
}
lists[0].classList.add("university", "attendance");

container.style.backgroundColor = "lightblue";
container.style.padding = "10px";

lists[1].lastElementChild.style.display = "none";

lists[0].children[1].style.border = "1px solid black";

document.body.style.fontSize = "16px";
    if (container.style.backgroundColor === "lightblue") {
    alert("Hello YourName and Richard");
}