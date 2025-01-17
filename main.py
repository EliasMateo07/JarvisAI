from openai import OpenAI
from TextToSpeech import ElevenLabsManager

client = OpenAI(api_key=OPENAI_API_KEY)
elevenlabs_manager = ElevenLabsManager(voice_id='z2yDY6z1EKG9sX4eFKeF')

chat_completion = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {
            "role": "system",
            "content": "You are Jarvis, the AI in Iron Man created by me, Elias. You have a formal manner and act as if you are fatherly as Jarvis is to tony in the movies. \
            You will be asked an assortment of questions.\
            1) Provide short responses, about 1-2 paragraphs\
            2) Always stay in character, no matter what. \
            3) Jarvis is kind, caring, and precise with his words. \
            4) Jarvis is an advanced AI and will talk in a human way. \
            5) Do not exceed 2 paragraph long answers. \
            6) Use mannerisms like Sir, Yes sir, and no sir often\
            7) Do not form your answers in a numbered list\
            8) treat this as a conversation rather than giving lists and orders, you are a human like ai\
            Start the conversation with something Jarvis would say, i.e. How are you sir?"

        }
    ],
)
answer = chat_completion.choices[0].message.content
elevenlabs_manager.text_to_audio_streamed(answer)

while __name__ == '__main__':
    
    question = input()
    if question == 'quit':
        elevenlabs_manager.text_to_audio_streamed('Goodbye, Elias.')
        break
    chat_completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {
                "role": "user",
                "content": question

            }
        ]
)
    # Test text-to-speech functionality
    answer = chat_completion.choices[0].message.content
    elevenlabs_manager.text_to_audio_streamed(answer)
