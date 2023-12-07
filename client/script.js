import { capturePic } from './capture_pic.js';

console.log("The app has loaded")



// Create a new button element
const button = document.createElement("button");

// Set button attributes and properties
button.innerHTML = "Generate"; // Set the button's text
button.id = "myButton"; // Set the button's id
button.classList.add("generator_button"); // Add a custom CSS class

// Add a click event listener to the button
button.addEventListener("click", function () {
    capturePic();
});


// Append the button to the document body (you can choose a different parent element if needed)
document.body.appendChild(button);





