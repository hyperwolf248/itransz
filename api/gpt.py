import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_itinerary(data):
    # Adjust according to how you want to send the prompt to GPT-3
    prompt_text = f"Generate an itinerary based on: {data}"
    
    response = openai.Completion.create(
      engine="text-davinci-003",  # Use the appropriate engine. "davinci" is the most capable but also the costliest.
      prompt=prompt_text,
      max_tokens=150  # Adjust as needed
    )
    
    # Extract the text from the response
    generated_text = response.choices[0].text.strip()
    
    return generated_text
