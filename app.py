from flask import Flask, request, jsonify
from whisper_logic import transcribe_and_summarize

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio = request.files['file']
    output = transcribe_and_summarize(audio)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
