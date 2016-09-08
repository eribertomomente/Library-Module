import openerp.http as http
from openerp.http import request
from openerp import models, fields, api

class MyController(http.Controller):

    @http.route('/my_url/some_html', type="http")
    def some_html(self):
        return "<h1>This is a test</h1>"
        
    @api.depends('number_books') 
    @http.route('/my_url/some_json', type="json", auth="public")
    def some_json(self):
    
        ## qui faccio la logica di chiamata etc...
        
        
        # qui conto il numeri dei libri
        auth = http.request.env['book.author']
        authors_number = auth.search_count([('number_books', '>', '1')])
        
        
        # qui chiamo la procedura
        
        # valorizzo il risultato
        result = True;
        message = "tutto ok";
    
        return {"result": result, "message":  message, "number": authors_number}