# Request the Watson's TTS to give GPT a voice. This helps create immersion of talking to real human
import os
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

# API keys deleted for obvious reasons
api_key = "MY API KEY"
url = "MY API URL"

authenticator = IAMAuthenticator(api_key)


def text_to_speech(response):
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(url)

    with open('./speech.mp3', 'wb') as audio_file:
        res = tts.synthesize(response, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)

    playsound('speech.mp3')
    os.remove('speech.mp3')