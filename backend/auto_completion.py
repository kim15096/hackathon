from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def get_completion(item, category, keywords):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a university student who is a seller on online marketplace. You will be given keywords to generate a listing based on the keywords in a semi-professional casual tone."},
            {"role": "user", "content": f"You are selling a {item} which is in the category of {category}. Write a very short and very simple description (similar to how its done in facebook marketplace) of the listing using the following keywords: {keywords}. Keep it straightforward and minimal. Do not add quotation marks. Never say fill in the blanks such as [] brackets."}
  ])
        
    return completion.choices[0].message.content


# if __name__ == "__main__":
#     get_completion("mouse", "electronics", "logitech, blue, lightweight")