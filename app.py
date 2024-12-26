from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined chatbot responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm here to help!",
    "bye": "Goodbye! Have a great day!",
    "what is your name": "I'm your friendly chatbot created using Flask.",
    "default": "I'm sorry, I didn't understand that. Can you rephrase?"
}

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

# Home route to display chat interface
@app.route("/")
def home():
    return render_template("chat.html")

# Chat route to handle user input
@app.route("/get", methods=["GET"])
def chatbot_response():
    user_input = request.args.get("msg")
    bot_response = get_response(user_input)
    return jsonify(response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)







