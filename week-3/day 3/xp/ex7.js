const allBooks = [
    {
        title: "Harry Potter",
        author: "JK Rowling",
        image: "harrypotter.jpg",
        alreadyRead: true
    },
    {
        title: "Lord of the Rings",
        author: "JRR Tolkien",
        image: "lotr.jpg",
        alreadyRead: false
    }
];

const section = document.querySelector(".listBooks"); //select the section with class 

allBooks.forEach(book => {
    const div = document.createElement("div");//create div 
    const text = document.createTextNode(`${book.title} written by ${book.author}`); //text node
    const img = document.createElement("img"); //create img
    
    img.src = book.image; 
    img.style.width = "100px";
    
    if (book.alreadyRead) {
        div.style.color = "red";
    }
    
    div.appendChild(text);
    div.appendChild(img);
    section.appendChild(div);
});