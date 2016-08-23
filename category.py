from openerp import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class category(models.Model):

    _name = "book.category"
    _description = "Category"
    _rec_name = 'name'

    name = fields.Char(string='Nome', size=15, required=True)
    number_books = fields.Integer(string='Numero di libri di questo genere', compute='comp_number_books', store=False)
    book_ids = fields.One2many('book.book', 'category_id', 'Record libri')
    book_str = fields.Char(string='Libri Relativi', compute='comp_book_str', store=False)
    
    @api.one
    @api.depends('book_ids')        
    def comp_number_books(self):
        count = self.book_ids.search_count([('category_id.id', '=', self.id)])
        self.number_books = count
        
    @api.one
    @api.depends('book_ids')
    def comp_book_str(self):
        str = ""
        for book_title in self.book_ids:
            str = str + book_title.title + ', '
        str = str[0:-2]    
        self.book_str = str