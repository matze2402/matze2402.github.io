from docx import Document
from markdownify import markdownify

def convert_docx_to_markdown(docx_path, markdown_path):
    # Read DOCX file
    doc = Document(docx_path)

    # Extract text from paragraphs
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]

    # Combine paragraphs into a single string
    doc_text = '\n'.join(paragraphs)

    # Convert to Markdown using markdownify
    markdown_text = markdownify(doc_text)

    # Write Markdown to a file
    with open(markdown_path, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_text)

if __name__ == "__main__":
    # Replace 'input.docx' with your DOCX file path
    input_docx_path = 'C:/Users/smmagack/Desktop/word/test.docx'
    
    # Replace 'output.md' with the desired Markdown file path
    output_markdown_path = 'C:/Users/smmagack/Desktop/word/testnew.md'

    convert_docx_to_markdown(input_docx_path, output_markdown_path)