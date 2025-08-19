import os

file_name = "gemini_test.py"

code = """from vertexai.generative_models import GenerativeModel
import vertexai

# Initialize Vertex AI
vertexai.init(project="pranay-469217", location="us-central1")

# Load Gemini model
model = GenerativeModel("gemini-1.5-flash")

# Simple prompt test
prompt = "Give me a one-line motivational quote for students."
response = model.generate_content(prompt)

print("*✨ Gemini Response:")
print(response.text)
"""

with open(file_name, "w") as f:
    f.write(code)

print(f"✅ File created successfully: {file_name}")