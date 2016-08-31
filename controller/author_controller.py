import openerp.http as http
from openerp.http import controllers_per_module
from openerp import models, fields, api

class AuthorController(http.Controller):

    
    @api.depends('number_books') 
    @http.route('/cogito/library/authors_list', type='http')
    def authors_list(self):
        auth = http.request.env['book.author']
        author_list = auth.search([('number_books', '>', '1')])
        return http.request.render('library_module.index_of_authors', { 
            'authors' : author_list
        })
