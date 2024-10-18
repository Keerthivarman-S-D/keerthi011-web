from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_prompt = data.get("prompt", "")

    # Generate a response using the OpenAI API
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_prompt}]
    )
    
    # Extract the output text
    response_text = output['choices'][0]['message']['content']
    
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
