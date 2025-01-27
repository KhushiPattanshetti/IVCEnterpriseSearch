from flask import Flask, request
from controllers.document_controller import upload_document
from controllers.query_controller import query_document

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    return upload_document(file)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get('query')
    return query_document(user_query)

if __name__ == '__main__':
    app.run(debug=True)
