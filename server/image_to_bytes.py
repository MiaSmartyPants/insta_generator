import base64
from io import BytesIO
from PIL import Image

def data_url_to_bytes(data_url):
    # print(data_url)
    try:
        # Split the data URL to get the encoding type and data
        _, encoded_data = data_url.split(',', 1)

        # Decode the base64-encoded data
        image_bytes = base64.b64decode(encoded_data)


        return image_bytes

    except Exception as e:
        print(f"Error converting data URL to bytes: {str(e)}")
        return None

