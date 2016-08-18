from openerp import models, fields

class book(models.Model):

    _name = "book.book"
    _description = "Simple Book"
    _rec_name = 'title'
    
    title = fields.Char(string='Titolo', size=30, required=True)
    author_id = fields.Many2many('book.author', 'book_author_rel', 'book_id', 'author_id', 'Autori')
    category_id = fields.Many2one('book.category', 'Genere')
    desc = fields.Text(string='Descrizione')
    pagesnumber = fields.Integer(string='n. pagine')
    buyer_id = fields.Many2many('book.buyer', 'book_buyer_rel', 'book_id', 'buyer_id', 'Record acquirenti')
    
