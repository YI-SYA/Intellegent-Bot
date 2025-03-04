# Intelligent Telegram Bot: Integrating Knowledge Base with AI

This project is a Telegram bot powered by AI that integrates a local knowledge base using ChromaDB and the Mistral model via Ollama. The bot can respond to user queries using both pre-trained AI capabilities and custom knowledge stored in `knowledge.txt`.

## Features
- **AI-Powered Responses:** Utilizes the Mistral model via Ollama for natural language processing.
- **Local Knowledge Base:** Retrieves relevant information from `knowledge.txt` stored in ChromaDB.
- **Seamless Telegram Integration:** Built using `python-telegram-bot` to interact with users.

## Installation
### Prerequisites
- Python 3.10+
- Ollama installed ([Install Ollama](https://ollama.ai/))
- Required Python libraries:
  ```sh
  pip install -r requirements.txt
  ```

## Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/YI-SYA/Intellegent-Bot
   cd your-repo
   ```
2. Add your Telegram bot token in `config.py`:
   ```python
   TOKEN = "your-telegram-bot-token"
   ```
3. Train the knowledge base:
   ```sh
   python train_db.py
   ```
4. Run the bot:
   ```sh
   python bot.py
   ```

## Usage
- Start the bot with `/start`
- Ask questions related to the knowledge base or general AI queries

## File Structure
```
📂 your-repo/
 ├── 📂 knowledge/          # Local knowledge base
 │   ├── knowledge.txt      # Custom knowledge source
 ├── bot.py                 # Main bot script
 ├── train_db.py            # Script to train ChromaDB
 ├── config.py              # Configuration file
 ├── requirements.txt       # Dependencies
 ├── README.md              # Project documentation
```

## License
This project is licensed under the MIT License.

## Author
Developed by [Muhyiddin Syarif](https://github.com/YI-SYA)
