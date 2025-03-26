document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("libform");
    const storySpan = document.getElementById("story");

    const stories = [
        "{person} walked into {place} with a {adjective} {noun} and decided to {verb} in front of everyone!",
        "In {place}, {person} found a {adjective} {noun} and tried to {verb} with it!",
        "{person} was so {adjective} that they took their {noun} to {place} just to {verb} all day long!",
        "Yesterday, {person} discovered a {adjective} {noun} at {place} and couldn't stop {verb}!"
    ];

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        const noun = document.getElementById("noun").value.trim();
        const adjective = document.getElementById("adjective").value.trim();
        const person = document.getElementById("person").value.trim();
        const verb = document.getElementById("verb").value.trim();
        const place = document.getElementById("place").value.trim();

        if (!noun || !adjective || !person || !verb || !place) {
            alert("Please fill in all the fields!");
            return;
        }

        generateStory(noun, adjective, person, verb, place);
    });

    function generateStory(noun, adjective, person, verb, place) {
        const randomStory = stories[Math.floor(Math.random() * stories.length)];
        storySpan.textContent = randomStory
            .replace("{noun}", noun)
            .replace("{adjective}", adjective)
            .replace("{person}", person)
            .replace("{verb}", verb)
            .replace("{place}", place);
    }

    // Add a shuffle button
    const shuffleButton = document.createElement("button");
    shuffleButton.textContent = "Shuffle Story";
    document.body.appendChild(shuffleButton);

    shuffleButton.addEventListener("click", () => {
        const noun = document.getElementById("noun").value.trim();
        const adjective = document.getElementById("adjective").value.trim();
        const person = document.getElementById("person").value.trim();
        const verb = document.getElementById("verb").value.trim();
        const place = document.getElementById("place").value.trim();

        if (!noun || !adjective || !person || !verb || !place) {
            alert("Please fill in all the fields before shuffling!");
            return;
        }

        generateStory(noun, adjective, person, verb, place);
    });
});
