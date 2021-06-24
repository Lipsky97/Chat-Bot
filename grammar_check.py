# As GPT-3 is very sensitive to incorrect grammar this module will check Watson's STT output to make sure GPT's output is
# sensible enough
import openai

openai.api_key = "MY API KEY"

# API request to curie engine to correct flawed Watson's output
def grammar_check(transcript):
    response = openai.Completion.create(
      engine="curie",
      prompt="Original: she didnt go to the market\n"
             "Corrected: She didn't go to the market.\n\n"
             "Original: force restart iphone x iphone xs iphone xr iphone eleven or iphone 12\n"
             "Corrected: Force restart iPhone X, iPhone XS, iPhone XR, iPhone 11, or iPhone 12\n\n"
             "Original: thanks again you made it look so fantastically simple\n"
             "Corrected: Thanks again, you made it look so fantastically simple\n\n"
             "Original: to get started with gcp download and install the google cloud sdk for your operating system for "
             "additional guidance beyond what you’ll find in this tutorial you can consult google app engine’s "
             "documentation\n"
             "Corrected: To get started with GCP, download and install the Google Cloud SDK for your operating system for "
             "additional guidance beyond what you’ll find in this tutorial, you can consult Google App Engine’s"
             " documentation.\n\n"
             "Original: "+transcript+"\nCorrected:",
      temperature=0,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
    )

    choices = response["choices"]
    cho = choices[0]
    text = cho["text"]
    print(text[1:])

    return text[1:]
