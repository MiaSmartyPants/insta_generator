export function displayCaption(generatedCaption){
    // Display the generated caption in your extension popup or content script
    console.log("Generated Caption:", generatedCaption);

    document.getElementById('caption-element').textContent = generatedCaption;
  } 
