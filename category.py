from openerp import models, fields, api

class category(models.Model):

    _name = "book.category"
    _description = "Category"

    name = fields.Char(string='Nome', size=15, required=True)
    number_books = fields.Integer(string='Numero di libri di questo genere', compute='comp_number_books', store=False)
    book_id = fields.Many2many('book.book', 'book_category_rel', 'category_id', 'book_id', 'Record libri')
    
    @api.depends()        
    def comp_number_books(self):        
        count = self.book_id.search_count([])
        self.number_books = count
