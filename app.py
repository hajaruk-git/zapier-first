from flask import Flask, request, jsonify
from responder import my_gpt

app = Flask(__name__)
@app.route("/webhook", methods=["POST"])
def my_function():
    data = request.json
    mail = data.get("user_mail", "")
    answer = my_gpt(mail)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)