from vector_store import retriever
from prompt_temp import prompt
from bitnet import BitnetLLM


class RAGApplication:
    def __init__(self, retriever, prompt):
        self.prompt = prompt
        self.retriever = retriever
        self.response_llm = BitnetLLM()

    def run(self, question):
        documents = self.retriever.invoke(question)

        doc_texts = "\n".join([doc.page_content for doc in documents])
        response = self.response_llm.invoke({
            "question": question,
            "documents": doc_texts
        })
        return response


if __name__ == "__main__":
    rag_application = RAGApplication(retriever, prompt)
    question = input("What's your question?\n")
    response = rag_application.run(question)
    print("Question:", question)
    print("Answer:", response)