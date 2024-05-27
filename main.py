import language_tool_python
from nltk import sent_tokenize

def grammar_checker(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Initialize language_tool_python for grammar checking
    tool = language_tool_python.LanguageTool('en-UK')

    grammar_errors = 0
    grammar_error_messages = []

    # Check grammar for each sentence
    for sentence in sentences:
        matches = tool.check(sentence)
        grammar_errors += len(matches)

        for match in matches:
            grammar_error_messages.append(f"Grammar error: {match.ruleId} - {match.message}")

    return grammar_errors, grammar_error_messages

if __name__ == "__main__":
    while True:
        # Get user input
        user_input = input("Enter the text you want to check (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        # Run the grammar checker
        grammar_errors, grammar_error_messages = grammar_checker(user_input)

        # Print the errors and counts
        if grammar_error_messages:
            print(f"Grammar errors found: {grammar_errors}")
            if grammar_error_messages:
                print("Grammar Error messages:")
                for error in grammar_error_messages:
                    print(error)
        else:
            print("No grammar errors found.")