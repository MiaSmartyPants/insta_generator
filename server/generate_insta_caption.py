# Call the OpenAi API, feed in description of picture, recieve caption

import os
from openai import OpenAI

from dotenv import load_dotenv

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_instagram_caption(description):
    # Load environment variables from .env file
    load_dotenv()
    # Set the OpenAI API key from the environment variable

    prompt = f"Given these picture descriptions: {description}, create an Instagram caption matching the vibe of the picture the description represents. The caption should always be 5 - 15 words long. Then Add on the most relevant most popular hashtags. Create this caption as if you were the most popular, humble, high-energy vibe person at school. The caption should showcase these qualities and personality."

    try:
        response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
            ],
        max_tokens=200,  # Adjust this based on your desired caption length
        n = 2)

        generated_caption1 = response.choices[0].message.content
        generated_caption2 = response.choices[1].message.content

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

