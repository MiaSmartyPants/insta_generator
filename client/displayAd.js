export function displayAd() {
    // Get the caption element
    var captionElement = document.getElementById('caption-element');

    // Create a div element for the dotted box
    var adBox = document.createElement('div');

    // Set styles for the dotted box
    adBox.style.border = '1px dashed #000'; 
    adBox.style.height = '100px'
    adBox.style.margin = '10px'; 

    // Create a paragraph element for the text
    var adText = document.createElement('p');

    // Set the text content for the paragraph
    adText.textContent = 'Promote your business here';

    // Append the paragraph element to the dotted box
    adBox.appendChild(adText);

    // Append the dotted box to the caption element
    captionElement.appendChild(adBox);
}


