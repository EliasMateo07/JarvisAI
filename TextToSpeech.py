from elevenlabs import stream
from elevenlabs.client import ElevenLabs
import os

class ElevenLabsManager:
    def __init__(self, voice_id):
        try:
            try:
              self.client = ElevenLabs(
                api_key = os.getenv("ELEVENLABS_API_KEY") 
              )
            except:
                raise ValueError("API key not set in environment variables.")
            print("ElevenLabs API key set successfully!")

            # Fetch all voices
            self.all_voices = self.client.voices.get_all()
            self.voice_id = voice_id
        except Exception as e:
            print(f"Error initializing ElevenLabs: {e}")
            exit(1)
        
    def text_to_audio_streamed(self, input_text):
        try:
            # Generate audio stream
            audio_stream = self.client.generate(
                text=input_text,
                voice=self.voice_id,
                model="eleven_multilingual_v2",
                stream=True
            )
            print("Audio stream generated. Playing audio...")
            stream(audio_stream)
        except Exception as e:
            print(f"Error generating or streaming audio: {e}")


if __name__ == '__main__':
    elevenlabs_manager = ElevenLabsManager(voice_id='z2yDY6z1EKG9sX4eFKeF')

    # Test text-to-speech functionality
    test_text = "This is my streamed test audio, I'm so much cooler than played."
    elevenlabs_manager.text_to_audio_streamed(test_text)
