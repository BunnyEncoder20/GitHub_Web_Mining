import os 
import string 
from collections import defaultdict

# fucntion to extarct the text from the file 
def extract_text_from_file(file_path) : 
    # try :
        # determine theh file extension 
        _, file_extension = os.path.splitext(file_path)

        # read the text from the file 
        if file_extension == ".txt"  :
            with open(file_path, "r") as file :
                text = file.read().lower()

        elif file_extension in [".docx",".pdf"] : 
            if file_extension == ".docx" :
                import docx
                doc = docx.Document(file_path) 
                text = " ".join([paragraph.text.lower() for paragraph in doc.paragraphs])

            else :
                import PyPDF2
                pdf = PyPDF2.PdfReader(file_path)
                text = " ".join([pdf.reader.pages[page_num].extractText().lowe() for page_num in range(len(pdf.pages))])

        # remove any punctuation from the text 
        text = text.translate(str.maketrans("","", string.punctuation))
        return text 
    # except  :
    #     # print("is this running ?")
    #     return ""



# Function to create the Inverted Index 
def create_inverted_index(file_paths) :
    inverted_index = defaultdict(set) 
    for file_path in file_paths :   
        text = extract_text_from_file(file_path)
        words = text.split()
        for word in words :
            inverted_index[word].add(file_path)
    return inverted_index


# defining the paths to read 
file_paths = [
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text1.docx",
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text2.txt",
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text3.docx",
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text4.txt",
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text5.docx",
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text6.pdf",
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text7.pdf",
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text8.pdf",
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text9.pdf",
    "C:/Users/gener/Coding/GitHub_Web_Mining/Lab 4/documents/text10.pdf"
]

# Create the inverted index 
inverted_index = create_inverted_index(file_paths)

# print the inverted index
for word, file_paths in inverted_index.items() : 
    print(f"{word} : {len(file_paths)}")
