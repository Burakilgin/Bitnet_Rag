from langchain.prompts import PromptTemplate


prompt = """You are an assistant for question-answering tasks.
Use the following documents to answer the question. Your answer should be based solely on the provided documents.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise:
Question: {question}
Documents: {documents}
Answer:"""