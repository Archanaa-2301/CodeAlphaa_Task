from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    translated_text = GoogleTranslator(source='auto', target='fr').translate(data['text'])
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
