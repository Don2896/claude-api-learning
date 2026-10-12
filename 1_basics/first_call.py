import anthropic

# SDK auto-reads ANTHROPIC_API_KEY from your environment
client = anthropic.Anthropic()

chat_history = []

chat_history.append({"role": "user", "content": "My name is Donald"})
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=chat_history
)
reply = response.content[0].text
chat_history.append ({"role": "assistant", "content": reply})
print(reply)


chat_history.append({"role": "user", "content": "What's my name?"})
response = client.messages.create(
    model="claude-sonnet-4-6", 
    max_tokens=512, 
    messages=chat_history)
print(response.content[0].text)

print("\n--- Full response ---")
print(f"Model: {response.model}")
print(f"Stop reason: {response.stop_reason}")
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")