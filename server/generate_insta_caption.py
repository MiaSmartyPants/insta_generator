# Call the OpenAi API, feed in description of picture, recieve caption

import os
import openai
from dotenv import load_dotenv


def generate_instagram_caption(description):
    # Load environment variables from .env file
    load_dotenv()
    # Set the OpenAI API key from the environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"Given these picture descriptions: {description}, create an Instagram caption matching the vibe of the picture the description represents. The caption should always be 5 - 15 words long. Then Add on the most relevant most popular hashtags. Create this caption as if you were the most popular, humble, high-energy vibe person at school. The caption should showcase these qualities and personality."

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200,  # Adjust this based on your desired caption length
            n = 2
        )

        generated_caption1 = response.choices[0].text
        generated_caption2 = response.choices[1].text

        if generated_caption1:
            print("Generated Instagram Caption:")
            print(generated_caption1 + "\n\n\n" + generated_caption2)
        else:
            print("Caption generation failed.")
        generated_caption = generated_caption1 + "\n\n\n" + generated_caption2
        return generated_caption

    except Exception as e:
        print(f"Error: {str(e)}")
        return 'Caption not generated'

