from groq import Groq
import json
client=Groq(api_key='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')
try:
    with open('messages.json','r') as j:
        messages=json.load(j)
except:
    messages=[]
while True:
    a=input('what can i help you with by to end')
    if a=='by':
        break
    else:
        messages.append({"role": "user", "content": a})

        response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
        )
        ai_reply=(response.choices[0].message.content)
        messages.append({'role':'assistant','content':ai_reply})
        with open('messages.json','w') as j:
            json.dump(messages,j)
       
        print(ai_reply)
        
        
