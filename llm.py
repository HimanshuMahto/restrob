from ai21 import AI21Client

client = AI21Client(
    # This is the default and can be omitted
    api_key="VOlc2aPItH17ktJWw0B1s5nlsYk5P6rC",
)

response=client.completion.create(
  model="j2-ultra",
  prompt="भारत की राजधानी क्या है?",
  temperature=0.8,
  max_tokens=200,
)
generated_text = response.completions[0].data.text
print(generated_text)