## 🗣️ Yunus Voicebot

A friendly, interview-style voicebot powered by a local LLM (Mistral via Ollama) and built with Streamlit. Designed to showcase strategic thinking, product polish, and real-world resilience—just like Yunus himself.

---

### 🚀 Features

- 🎙️ **Voicebot UI** built with Streamlit  
- 🧠 **Local LLM backend** using Mistral via Ollama (no API key or billing required)  
- 💬 **Preloaded answers** for key interview questions  
- 🔊 **Text-to-speech playback** using gTTS  
- 🖼️ **Custom avatar branding** via `yunus_avatar.png`  
- 🛡️ **Offline-capable** with fallback responses  
- ⚡ **Fast and quota-free**—no external API dependencies

---

### 💡 Sample Questions

Try asking:
- What should we know about your life story in a few sentences  
- What’s your #1 superpower  
- What are the top 3 areas you’d like to grow in  
- What misconception do your coworkers have about you  
- How do you push your boundaries and limits  

---

### 🛠️ Setup Instructions

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   pip install Pillow (To load and display your avatar image)
   ```
2. **Ollama should be downloaded in the sytem through Google Chrome**
   ```bash
   https://ollama.com/download
   ```
   
3. **Start Ollama with Mistral**  
   ```bash
   ollama run mistral
   ```

4. **Run the app**  
   ```bash
   streamlit run app.py
   ```

---

### 📁 Folder Structure

```
├── app.py                 # Main Streamlit app
├── utils.py               # gTTS voice playback
├── responses.py           # Cached answers for key questions
├── assets/
│   └── yunus_avatar.png   # Custom avatar image
├── requirements.txt       # Python dependencies
```

---

### ✅ Requirements Met

- Uses ChatGPT API or free alternative ✅  
- Dynamic responses via local LLM ✅  
- Interview-style interaction ✅  
- Voice playback ✅  
- Reviewer polish and branding ✅

---

### 🧠 Built By

Yunus from Chittoor — a full-stack dev who builds like a founder. Strategic, resilient, and product-minded.

---


