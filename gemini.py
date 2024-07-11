import google.generativeai as genai
#GOOGLE_API_KEY='AIzaSyDK3DT3MtOaGvkaahpgQ7i8WReQJ-UgCn0'
#genai.configure(api_key=GOOGLE_API_KEY)

def get_response_from_model(code, API_KEY):
    generation_config = {
    "temperature": 0.1,
    "max_output_tokens": 5000
    }
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config)


    prompt_parts = [f'''Provide a concise summary of the key points in the following text, focusing on the main arguments: 
                    # write in a paragraph
                    # in 100 words or less
                    # Don't give points ''']
    response = model.generate_content(prompt_parts)
    output=response.text
    return output
#code='''The aroma of freshly baked bread hung heavy in the air, a warm invitation wafting from the little bakery tucked away on the corner. Inside, sunlight streamed through the window, casting a golden glow on flour-dusted shelves overflowing with crusty baguettes and flaky croissants. A gentle symphony of sounds filled the space - the rhythmic thump of dough being kneaded, the satisfying sizzle of pastries meeting the hot oven, and the cheerful chatter of customers exchanging greetings. It was a haven for bread enthusiasts, a place where simple ingredients were transformed into edible works of art, promising a delightful sensory experience with every bite.'''
#print(get_response_from_model(code,GOOGLE_API_KEY))
