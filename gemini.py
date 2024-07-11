import google.generativeai as genai

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

