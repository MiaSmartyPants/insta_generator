# Call the OpenAi API, feed in description of picture, recieve caption

import os
import openai
from dotenv import load_dotenv


def generate_instagram_caption(description):
    # Load environment variables from .env file
    load_dotenv()
    # Set the OpenAI API key from the environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"Given this picture description: {description}, create an Instagram caption with relevant popular hashtags."

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,  # Adjust this based on your desired caption length
            n = 1
        )

        generated_caption = response.choices[0].text.strip()
        if generated_caption:
            print("Generated Instagram Caption:")
            print(generated_caption)
            # print("this is the generated Caption - generateInst.py")
        else:
            print("Caption generation failed.")
        return generated_caption

    except Exception as e:
        print(f"Error: {str(e)}")
        return 'Caption not generated'

