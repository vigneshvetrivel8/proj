from pdf2image import convert_from_path
from langchain_community.document_loaders import TextLoader
import pytesseract
import os
from googletrans import Translator
from langchain_google_genai import GoogleGenerativeAI

def pdf_to_text(file_path):
    images = convert_from_path(file_path)
    
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    
    return text

def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

pdf_path = "test data/sample1.pdf"
output_text_file = "output.txt"

pdf_text = pdf_to_text(pdf_path)
save_text_to_file(pdf_text, output_text_file)

print(f"Text extracted from PDF and saved to {output_text_file}")

loader = TextLoader("output.txt")
documents = loader.load()

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

translated_text = translate_text(documents[0].page_content, target_language='en')

print("Contents successfully translated")

# Define the user query
user_query = """extract essential information from documents. This could include:

Identifying and extracting entities like names, dates, locations, and organizations.

Extracting relationships between entities.

Summarizing key information from the document.

Also suggest a category for the documents from the following categories: Utilities, Rent, purchases, subscriptions."""

prompt= (
"""
Use the following pieces of information to answer the user's question.

Context: {context}
Question: {question}

Only return the helpful answer below.
Helpful answer:
""" ).format(context=translated_text, question=user_query)

import os
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"

llm = GoogleGenerativeAI(model="gemini-pro")

response = llm.invoke(prompt)
print("Final response:")
print(response)