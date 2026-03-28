from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

result = splitter.split_documents(docs)

print(result[0].page_content)

