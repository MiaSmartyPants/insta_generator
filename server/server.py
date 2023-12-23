from flask import Flask, request, jsonify
from flask_cors import CORS  
from image_to_bytes import data_url_to_bytes
from image_parsing import image_to_text
from generate_insta_caption import generate_instagram_caption 

app = Flask(__name__)
CORS(app)  

@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the image URL from the POST request
    image_url = request.json.get('image_url') #[5:]
    # print(image_url[:50])

    #convert image to bytes
    source_image_bytes = data_url_to_bytes(image_url)
    # print(source_image_bytes[:50])

    # Call your image processing function here
    result = image_to_text(source_image_bytes)
    # print(result[:50])
    
    if result:
        # Generate Instagram caption based on the image description
        generated_caption = generate_instagram_caption(result)
        
        # Return the result and the generated caption as JSON
        response = {"result": result, "caption": generated_caption}
        return jsonify(response)
    else:
        return jsonify({"error": "caption generation failed"})


if __name__ == '__main__':
    app.run()
