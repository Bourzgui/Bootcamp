//Afficher une alerte après 2 secondes
setTimeout(() => alert("Hello World"), 2000);

// Ajouter un paragraphe après 2 secondes
setTimeout(() => {
    const container = document.getElementById("container");
    const p = document.createElement("p");
    p.textContent = "Hello World";
    container.appendChild(p);
}, 2000);

//Ajouter un paragraphe toutes les 2 secondes et arrêter après 5
let counter = 0;
const interval = setInterval(() => {
    const container = document.getElementById("container");
    if (counter >= 5) {
        clearInterval(interval);
        return;
    }
    const p = document.createElement("p");
    p.textContent = "Hello World";
    container.appendChild(p);
    counter++;
}, 2000);

// Arrêter l'intervalle lorsqu'on clique sur le bouton
document.getElementById("clear").addEventListener("click", () => {
    clearInterval(interval);
});
