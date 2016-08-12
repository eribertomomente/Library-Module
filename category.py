from openerp import models, fields

class category(models.Model):

    _name = "book.category"
    _description = "Category"

    name = fields.Char(string='Nome', size=15, required=True)
    number_books = fields.Integer(string='Numero di libri di questo genere')
    book_id = fields.Many2many('book.book', 'book_category_rel', 'category_id', 'book_id', 'Record libri')
