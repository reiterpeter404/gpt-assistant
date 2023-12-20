from gpt.connection import OopAssistent

# using an empty conversation file name, will create a new conversation
# by loading a conversation file, you can continue a conversation in the next session
# conversation_file_name = ""
conversation_file_name = "conversation.yaml"


if __name__ == '__main__':

    # to use the GPT API, you need to create a file 'api.key' and paste your API key into it
    # the file will not be uploaded to the Git repository!!!
    with open('api.key', 'r') as api_key:
        API_KEY = api_key.read()

    chat_gpt = OopAssistent(API_KEY, conversation_file_name)

    # let the student ask questions until he/she inserts "X"
    print("Enter your question or 'X' to exit.")
    while (question := input('\n> ')) != 'X':
        answer = chat_gpt.ask(question)
        print(answer)