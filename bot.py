import logging
import ollama
import chromadb
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from sentence_transformers import SentenceTransformer
from config import TOKEN

# Setup logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Load ChromaDB
chroma_client = chromadb.PersistentClient(path="./knowledge_db")
collection = chroma_client.get_collection(name="knowledge")

# Load model embedding
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def search_knowledge(query):
    """Mencari knowledge terkait dalam database vektor"""
    query_embedding = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=1)

    if results["documents"]:
        return results["documents"][0][0]  # Mengembalikan dokumen terdekat
    return None

def chat_with_ollama(prompt):
    """Gabungkan knowledge lokal dari ChromaDB dan Ollama untuk menjawab"""
    knowledge_answer = search_knowledge(prompt)

    if knowledge_answer:
        final_prompt = f"Informasi dari knowledge lokal:\n{knowledge_answer}\n\n"
        final_prompt += f"Jika informasi di atas tidak cukup, berikan jawaban tambahan:\nUser: {prompt}\nBot:"
    else:
        final_prompt = f"User: {prompt}\nBot:"

    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": final_prompt}])
    return response["message"]["content"]

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Halo! Saya adalah bot KINO. Silakan bertanya!")

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    response = chat_with_ollama(user_text)
    await update.message.reply_text(response)

def main():
    """Main function untuk menjalankan bot Telegram"""
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot sedang berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
