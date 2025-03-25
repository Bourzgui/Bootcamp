const nav = document.getElementById("navBar");
nav.setAttribute("id", "socialNetworkNavigation"); 

const newLi = document.createElement("li");
const logoutText = document.createTextNode("Logout");
newLi.appendChild(logoutText);
nav.firstElementChild.appendChild(newLi);

const firstLi = nav.firstElementChild.firstElementChild;
const lastLi = nav.firstElementChild.lastElementChild;
console.log(firstLi.textContent);
console.log(lastLi.textContent);