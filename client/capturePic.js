import { displayCaption } from "./displayCaption.js";

export function capturePic() {
  chrome.tabs.query(
    { active: true, windowId: chrome.windows.WINDOW_ID_CURRENT },
    function (tabs) {
      const { id: tabId } = tabs[0];

      const getPicElement = () => {
        // let pictureElement = document.getElementsByClassName("x5yr21d x11njtxf xh8yej3")[24]
        // // let pictureElement = document.querySelector("._aazh");
        // let pictureUrl = pictureElement ? pictureElement.src : null;
        // console.log(pictureUrl, pictureElement)
        let array = document.getElementsByClassName("x5yr21d x11njtxf xh8yej3")
        for (let i = 0; i < array.length; i++) {
            // Check if the current element is an image with the desired class name
            if (array[i].src && array[i].className === 'x5yr21d x11njtxf xh8yej3') {
                // Get the value of the src attribute
                const pictureUrl = array[i].src;
                
                console.log('working',pictureUrl); // Output: URL of the image you want
                // You can break the loop if you only need to select the first matching image
                return pictureUrl;
              }
        }
        
      }

      chrome.scripting.executeScript(
        {
          target: { tabId: tabId },
          function: getPicElement
        },
        async (result) => {
          const pictureUrl = result[0]['result'];
          console.log(result)
          if (pictureUrl) {
            // Convert blob URL to data URL
            const blobData = await fetch(pictureUrl).then(response => response.blob());
            
            const reader = new FileReader();
            reader.onloadend = function() {
              const dataUrl = reader.result;

              // Make an HTTP POST request to your Python server
              fetch('http://localhost:5000/process_image', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({ image_url: dataUrl }),
              })
              .then(response => response.json())
              .then(data => {
                if (data.caption) {
                  // Display the generated caption in your extension popup or content script
                  const generatedCaption = data.caption;
                  displayCaption(generatedCaption)
                  // console.log("Generated Caption:", generatedCaption);
                } else {
                  console.log("Caption not found in the response.");
                }
              })
              .catch(error => {
                console.error("Error while calling the Python server:", error);
              });
            };

            reader.readAsDataURL(blobData);
          } else {
            console.log("Instagram picture element not found.");
          }
        }
      );
    }
  );
}
