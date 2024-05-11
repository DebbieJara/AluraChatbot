#Personal info chat.py
import google.generativeai as genai

GOOGLE_API_KEY="Insert:_API_Key"
genai.configure(api_key=GOOGLE_API_KEY)
generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}
safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
    }
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)
chat = model.start_chat(history=[])

prompt = input('Esperando prompt: ')

while prompt != "fim":
  response = chat.send_message(prompt)
  print("Resposta:", response.text, '\n\n')
  prompt = input('Esperando prompt: ')
