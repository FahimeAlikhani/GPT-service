import openai

def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",  #The model you want to use for your request of https://platform.openai.com/docs/models/gpt-3-5         
        prompt = text,                #Prompt is the set of words you ask as a question to generate a response from the API
        temperature = 0.6,            #Set how professional or creative your text should sound
        max_tokens = 2048,            #The maximum number of words in the generated response
    )
    return print(response.choices[0].text)

def main():

    while True:
        print('GPT: Ask me a question\n')
        myQuestion = input()
        askGPT(myQuestion)
main()