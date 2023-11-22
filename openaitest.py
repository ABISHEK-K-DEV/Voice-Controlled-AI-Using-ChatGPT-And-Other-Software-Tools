import openai
apikey = "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"
openai.api_key = apikey

response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt="Write an mail for leave for college?",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)
