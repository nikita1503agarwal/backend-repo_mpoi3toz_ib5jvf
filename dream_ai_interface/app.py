"""Flask web interface for Dream.AI

Provides a minimal HTML page with buttons to trigger the same actions as the
CLI. When a button is clicked, the corresponding function from main.py is
invoked and its printed output is captured and displayed in the page.

Run:
    python dream_ai_interface/app.py
"""
from __future__ import annotations

from flask import Flask, request, redirect, url_for, render_template_string
from io import StringIO
import contextlib

# Import the CLI functions to reuse logic
from dream_ai_interface.main import (
    menu_image,
    menu_video,
    menu_transcription,
    menu_question,
    TITLE,
)

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dream.AI</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; }
    .container { max-width: 760px; margin: 40px auto; padding: 24px; background: #111827; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.4); }
    h1 { text-align: center; font-size: 28px; margin-top: 0; }
    .grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
    form { margin: 0; }
    button { width: 100%; padding: 14px 16px; border: 0; border-radius: 10px; background: #334155; color: #e2e8f0; cursor: pointer; font-weight: 600; }
    button:hover { background: #475569; }
    .quit { background: #7f1d1d; }
    .quit:hover { background: #991b1b; }
    pre { background: #0b1020; padding: 16px; border-radius: 12px; white-space: pre-wrap; word-break: break-word; }
  </style>
</head>
<body>
  <div class="container">
    <h1>🎨 DREAM.AI MENU 🎨</h1>
    <div class="grid">
      <form method="post"><input type="hidden" name="action" value="image"><button>Image</button></form>
      <form method="post"><input type="hidden" name="action" value="video"><button>Vidéo</button></form>
      <form method="post"><input type="hidden" name="action" value="transcription"><button>Transcription</button></form>
      <form method="post"><input type="hidden" name="action" value="question"><button>Question</button></form>
    </div>
    <form method="post" style="margin-top: 12px;"><input type="hidden" name="action" value="quit"><button class="quit">Quitter</button></form>
    {% if output %}
    <h3>Résultat</h3>
    <pre>{{ output }}</pre>
    {% endif %}
  </div>
</body>
</html>
"""


def _capture_output(func):
    buf = StringIO()
    with contextlib.redirect_stdout(buf):
        result = func()
    text = buf.getvalue().strip()
    # Prefer printed output; if none, show returned message
    return text or (result if isinstance(result, str) else str(result))


@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        action = request.form.get("action", "")
        if action == "image":
            output = _capture_output(menu_image)
        elif action == "video":
            output = _capture_output(menu_video)
        elif action == "transcription":
            output = _capture_output(menu_transcription)
        elif action == "question":
            output = _capture_output(menu_question)
        elif action == "quit":
            output = "Au revoir ! (Cette action ne ferme pas le serveur en mode démo)"
        else:
            output = "Action inconnue"

    return render_template_string(TEMPLATE, output=output)


if __name__ == "__main__":
    # Debug mode enabled for development
    app.run(host="0.0.0.0", port=5000, debug=True)
