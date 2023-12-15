// displayCaption.js

export function displayCaption(generatedCaption) {

  // Get the caption element
  var captionElement = document.getElementById('caption-element');
  document.getElementById('instructions').textContent ="";

  // Create a container for the caption and copy button
  var container = document.createElement('div');
  container.style.border = '1px solid #ccc';
  container.style.width = '200px';


  // Create a paragraph element for the caption
  var captionText = document.createElement('p');
  captionText.textContent = generatedCaption;

  // Create a button for copying the caption
  var copyButton = document.createElement('button');
  copyButton.textContent = 'Copy Caption';
  copyButton.addEventListener('click', function () {
      // Copy the caption to the clipboard
      copyToClipboard(generatedCaption);
  });

  // Append the caption and copy button to the container
  container.appendChild(captionText);
  container.appendChild(copyButton);

  // Clear any existing content in the caption element
  captionElement.innerHTML = '';

  // Append the container to the caption element
  captionElement.appendChild(container);
}

// Function to copy text to the clipboard
function copyToClipboard(text) {
  var textarea = document.createElement('textarea');
  // Create a textarea for the user to copy the caption
  textarea.style.width = '200px';
  textarea.readOnly = true; 
  textarea.value = text;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand('copy');
  document.body.removeChild(textarea);
}

