from website import create_app
from website.api import FinanceAPI
from flask_restful import Api
app = create_app()

api = Api(app)
api.add_resource(FinanceAPI, "/data")

if __name__ == '__main__':
    app.run(debug=True)