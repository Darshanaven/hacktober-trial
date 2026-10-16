from google import genai

# Automatically picks up GEMINI_API_KEY from environment variables
client = genai.Client()

response = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    contents="Give me a 1-sentence idea for an open-source hackathon project.",
)

print("\n--- AI Response ---")
print(response.text)