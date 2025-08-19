from vertexai.generative_models import GenerativeModel
import vertexai

# Init Vertex AI
vertexai.init(project="pranay-469217", location="us-central1")

# Correct model (Gemini 2.5 flash-lite)
model = GenerativeModel("gemini-2.5-flash-lite")

# Test prompt
response = model.generate_content("Hello Gemini! Ek chhoti si kahani sunao.")
print("Gemini Output:")
print(response.text)
