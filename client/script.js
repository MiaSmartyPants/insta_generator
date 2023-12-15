import { capturePic } from './capturePic.js';
import { displayAd } from './displayAd.js';
console.log("The app has loaded")

// Create a div element
var boxElement = document.createElement("div");

// Set the id attribute for the div element
boxElement.id = "instruction-box";

// Set some styles for the box (you can customize these as needed)
boxElement.style.width = "200px";
boxElement.style.height = "75px";
boxElement.style.padding = "10px";

// Create a paragraph element for the placeholder text
var placeholderElement = document.createElement("p");

// Set the text content for the placeholder
// Set the text content for the placeholder
placeholderElement.innerHTML = "1. Upload PHOTO(S) ONLY to Instagram.<br><br>2. NAVIGATE TO THE LAST PAGE. Right before you click share...<br><br>3. Press Generate and wait!";


// Append the placeholder element to the box element
boxElement.appendChild(placeholderElement);

// Append the box element to the "caption-element" div
var captionElement = document.getElementById("instructions");
captionElement.appendChild(boxElement);






// Create a new button element
const button = document.createElement("button");

// Set button attributes and properties
button.innerHTML = "Generate"; // Set the button's text
button.id = "myButton"; // Set the button's id
button.classList.add("generator_button"); // Add a custom CSS class
button.style.margin = "10px";

// Add a click event listener to the button
button.addEventListener("click", function () {
    displayAd();
    capturePic();
});

document.body.appendChild(button);





