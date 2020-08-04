from flask import Flask, jsonify, request
from searchSvc import SearchService
from utils import Utils
from werkzeug.exceptions import BadRequestKeyError
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

searchSvc = SearchService()

@app.route('/search/products', methods=['GET'])
def search_products():
    query=None
    try:
        if request.args.get('code', default=None, type=None) is not None:
            query = request.args.get('code', '')
            iCode = int(query)
            row = searchSvc.getProductsByCode(iCode)
            return jsonify(row)
        elif request.args.get('descr', default=None, type=None) is not None:
            query = request.args.get('descr', '')
            rows = searchSvc.getProductsByDescr(query)
            return jsonify(rows)
        else:
            raise BadRequestKeyError("Error getting params")
        
    except Exception as error: 
        if type(error).__name__=="BadRequestKeyError":
            return jsonify(error = "Send code or description") , 400 
        else:
            return jsonify(error = "Error Inesperado, {}".format(error)) , 500 

@app.errorhandler(404)
def not_found(error):
    return jsonify(error = "Not Found"), 404

@app.errorhandler(500)
def not_unexpected(error):
    return jsonify(error = "Unexpected error"), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify(error = "Bad Request"), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')
