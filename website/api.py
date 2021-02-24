from flask_restful import Resource
from flask import session, jsonify



class FinanceAPI(Resource):
    
    def get(self):
        if session["user"]:
            return {"data": session["user"], "api":session['API_KEY']}
        return {"data":"Enter API Key"}
    
    # def post(self):
    #     if session["user"]:
    #         BASE_URL = https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo
    #     return {"data": "Enter API Key"}
    
    
    

