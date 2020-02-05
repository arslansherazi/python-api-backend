from app import app


@app.route('/get_response', methods=['GET'])
def get_response():
    return 'Request Authenticated'
