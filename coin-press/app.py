from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from flask_cors import CORS
import lin_reg_interactive

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)
CORS(app, origins="http://localhost:8080", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True, intercept_exceptions=False)

parser = reqparse.RequestParser()
parser.add_argument('n_values', type=list, location='json')
parser.add_argument('d', type=int, location='json')
parser.add_argument('iters', type=int, location='json')
parser.add_argument('total_privacy_budget', type=float, location='json')


@app.before_request
def authorize_token():
    if request.endpoint == 'losses':
        try:
            if request.method != 'OPTIONS':  # <-- required
                auth_header = request.headers.get("Authorization")
                if "Bearer" in auth_header:
                    token = auth_header.split(' ')[1]
                    if token != '12345678':
                        raise ValueError('Authorization failed.')
        except Exception as e:
            return "401 Unauthorized\n{}\n\n".format(e), 401


class CoinpressExperiment(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        n_values = args['n_values']
        d = int(args['d'])
        iters = int(args['iters'])
        total_privacy_budget = float(args['total_privacy_budget'])
        excess_private_loss, excess_nonprivate_loss = \
            lin_reg_interactive.losses(n_values, d, iters, total_privacy_budget)
        return {"excess_private_loss": excess_private_loss, "excess_nonprivate_loss": excess_nonprivate_loss}


@app.after_request
def add_cors_headers(response):
    r = request.referrer[:-1]
    response.headers.add('Access-Control-Allow-Origin', r)
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
    response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response

api.add_resource(CoinpressExperiment, '/losses')

if __name__ == '__main__':
    app.run(debug=True)
