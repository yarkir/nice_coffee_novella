from pathlib import Path

import streamlit as st


st.set_page_config(page_title="Вышел за кофе", page_icon="☕", layout="wide")

game_file = Path(__file__).with_name("novella.html")
game_html = game_file.read_text(encoding="utf-8")
# Keep the game's fragment links inside the embedded document.
game_html = game_html.replace("<head>", '<head><base href="about:srcdoc">', 1)
st.iframe(game_html, height="content")
