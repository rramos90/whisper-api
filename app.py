from flask import Flask, request, jsonify
from whisper_logic import transcribe_and_summarize

app = Flask(__name__)

# Rota de ping para evitar cold start
@app.route('/', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})

# Rota principal
@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio = request.files['file']
    output = transcribe_and_summarize(audio)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
