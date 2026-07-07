from app.services.translator import TranslatorService


translator = TranslatorService()

text = "FastAPI क्या है?"

print("=" * 50)
print("Original")
print("=" * 50)
print(text)

print()

language = translator.detect_language(text)

print("=" * 50)
print("Detected Language")
print("=" * 50)
print(language)

print()

english = translator.translate_to_english(text)

print("=" * 50)
print("English Translation")
print("=" * 50)
print(english)

print()

hindi = translator.translate_from_english(
    english,
    "Hindi",
)

print("=" * 50)
print("Back to Hindi")
print("=" * 50)
print(hindi)