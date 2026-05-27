from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    translated_text = ""
    audio_file = ""

    if request.method == "POST":

        text = request.form["text"]

        source_language = request.form["source_language"]

        target_language = request.form["target_language"]

        translated_text = GoogleTranslator(
            source=source_language,
            target=target_language
        ).translate(text)

        tts = gTTS(
            text=translated_text,
            lang=target_language
        )

        if not os.path.exists("static"):
            os.makedirs("static")

        audio_file = "static/output.mp3"

        tts.save(audio_file)

    return render_template(
        "index.html",
        translated_text=translated_text,
        audio_file=audio_file
    )

if __name__ == "__main__":
    app.run(debug=True)