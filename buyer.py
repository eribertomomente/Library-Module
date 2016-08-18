from openerp import models, fields

class buyer(models.Model):

    _name = "book.buyer"
    _description = "Buyer"
    
    name = fields.Char(string='Nome', size=15, required=True)
    surname = fields.Char(string='Cognome', size=15, required=True)
    book_id = fields.Many2many('book.book', 'book_buyer_rel', 'buyer_id', 'book_id', 'Record libri')
    #booktitle = fields.Char(string='Libro acquistato', related='book_id.title')
    born_date = fields.Date(string='Data di Nascita')
