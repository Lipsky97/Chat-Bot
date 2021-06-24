# The real main module of the program, here the GPT's DaVinci engine is queried with the conversation
import openai
import transcribe
from grammar_check import grammar_check
from tts import text_to_speech

# API key removed for privacy reasons
openai.api_key = "MY API KEY"


def chat_bot():
    # Start sequences, the chat bot is programmed with the "prompt", that is extended with each sentence, this is
    # specific to the transformer architecture, instead of sending queries one by one each human/AI response is
    # appended to give the AI context for the next answer
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "
    text_to_speech("I am an AI created by OpenAI. How can I help you today?")
    prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\n\n"

    # To create a sense of having a continuous conversation new parts of the prompt are appened in a loop
    while True:
        input("Press Enter to say something...")
        transcript = transcribe.main()
        if transcript != "":
            transcript = grammar_check(transcript)
        else:
            print("Transcript value is: " + transcript)
            quit()


        prompt += "Human: " + transcript + start_sequence

        print(restart_sequence + transcript)

        response = openai.Completion.create(
          engine="davinci",
          prompt=prompt,
          temperature=0.9,
          max_tokens=150,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0.7,
          stop=["\n", " Human:", " AI:"]
        )
        choices = response["choices"]
        choices = choices[0]
        text = choices["text"]

        prompt += text + "\n"


        if text != "":
            text_to_speech(text[1:])
        else:
            text_to_speech("I have no answer for that")

        print(start_sequence + text)
