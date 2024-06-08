## Requirements:
#### Before running the Python module, run the following commands:
    pip install -r Requirements.txt
    sudo apt-get update
    sudo apt-get install poppler-utils
    sudo apt-get install tesseract-ocr


## Conversion, OCR, and Preprocessing:
We create a pipeline to convert PDF files to text, perform OCR on the text, save the extracted content to a .txt file, and translate the contents into English using Google Translate.

#### Features
PDF to Image Conversion: Uses pdf2image to convert PDF files into images.  
Optical Character Recognition (OCR): Utilizes pytesseract to extract text from images.  
Text Translation: Leverages googletrans to translate the extracted text into English.  
Integration with LangChain: Uses langchain for loading and processing text documents


## LLM-Powered Understanding and Actions:
We've chosen Google Gemini, a Large Language Model (LLM), for this task. It boasts an impressive context length, allowing it to consider a significant amount of information when processing invoices. Additionally, Gemini offers a generous free tier of 1500 responses per day, making it a cost-effective solution.  

The prompt we use for Gemini helps generate quick summaries of invoices, including their key details and categorizing them based on predefined categories (Utilities, Rent, purchases, subscriptions). We can fine-tune the prompt as needed to better suit the specific requirements of our invoice processing tasks.  

For very large or complex invoices, we might explore incorporating additional techniques like Response Augmentation Generation (RAG), embeddings, and vector databases to enhance processing efficiency.
