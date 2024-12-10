import PyPDF2
import requests
from io import BytesIO

def download_pdf(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        print("Failed to download PDF")
        return None

def get_pdf_pages(pdf_file):
    pages = []
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text = page.extract_text()
        pages.append(text)
        # Testing for text
        print(text)
    return pages

pdf_file = download_pdf("https://arxiv.org/pdf/2103.15348.pdf")

if pdf_file:
    pages = get_pdf_pages(pdf_file)
