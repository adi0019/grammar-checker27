from flask import Flask, request, jsonify
import language_tool_python
from nltk import sent_tokenize

app = Flask(__name__)

def grammar_checker(text):
    sentences = sent_tokenize(text)
    tool = language_tool_python.LanguageTool('en-UK')

    grammar_error_messages = []

    for sentence in sentences:
        matches = tool.check(sentence)

        for match in matches:
            error_message = f"{match.ruleId} - {match.message}, Suggestions: {', '.join(match.replacements)}"
            grammar_error_messages.append(error_message)

    return grammar_error_messages

@app.route('/grammarcheck', methods=['POST'])
def grammarcheck():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    grammar_error_messages = grammar_checker(text)

    response = {
        "grammar_error_messages": grammar_error_messages
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)