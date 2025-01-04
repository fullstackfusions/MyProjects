from flask import Flask, request, jsonify
from your_model import generate_text  # Assuming you have a custom function for text generation

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data['prompt']
        length = data.get('length', 50)  # Default length
        generated_text = generate_text(prompt, length)
        return jsonify({'generated_text': generated_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
