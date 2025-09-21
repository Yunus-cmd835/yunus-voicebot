import streamlit as st
import requests
from utils import speak_text
from responses import cached_answers
from PIL import Image
import os

# Page setup
st.set_page_config(page_title="Yunus Voicebot", layout="centered")

# Load avatar image
avatar = Image.open("assets/yunus_avatar.png")
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(avatar, caption=None, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Title and instructions
st.markdown("<h1 style='text-align: center;'>🎙️ Yunus Voicebot</h1>", unsafe_allow_html=True)
st.markdown("Ask me anything you'd ask Yunus in an interview!")

# Sample questions for reviewers
st.markdown("💡 Sample questions:")
st.markdown("- What should we know about your life story in a few sentences? ")
st.markdown("- What’s your #1 superpower?")
st.markdown("- What are the top 3 areas you’d like to grow in?")
st.markdown("- What misconception do your coworkers have about you?")
st.markdown("- How do you push your boundaries and limits?")

# AI response function
def get_ai_response(prompt):
    for key in cached_answers:
        if key in prompt.lower():
            return cached_answers[key]
    # Fallback to Ollama if no match
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": f"You are Yunus, a strategic, resilient, product-minded developer. Answer this interview question: {prompt}",
                "stream": False
            },
            timeout=30
        )
        result = response.json()
        return result.get("response", "❌ No response received.")
    except Exception as e:
        return f"❌ Error: {e}"

# Input field
question = st.text_input("Type your question here 👇")

# Response logic
if question:
    with st.spinner("Thinking like Yunus..."):
        response = get_ai_response(question)
        st.success(response)

        try:
            audio_file = speak_text(response)
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3")
            os.remove(audio_file)
        except Exception as e:
            st.error(f"❌ Voice playback failed: {e}")