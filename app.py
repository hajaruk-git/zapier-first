from flask import Flask, request, jsonify
from responder import my_gpt
import os

app = Flask(__name__)
@app.route("/webhook", methods=["POST"])
def my_function():
    data = request.json
    print("📩 Requête reçue:", data)
    mail = data.get("user_mail", "")
    answer = my_gpt(mail)
    print("Réponse GPT:", answer)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)