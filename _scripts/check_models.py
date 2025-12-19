import os
import google.generativeai as genai

# Get the key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ Error: API Key not found!")
    exit(1)

# Configure
genai.configure(api_key=api_key)

print("🔍 Checking available models for your API Key...")
try:
    for m in genai.list_models():
        # Only show models that can write text (generateContent)
        if 'generateContent' in m.supported_generation_methods:
            print(f" - {m.name}")
except Exception as e:
    print(f"❌ Error listing models: {e}")
