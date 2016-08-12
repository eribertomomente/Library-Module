from openerp import models, fields, api

class authors(models.Model):

    _name = "book.author"
    _description = "Authors"
    _rec_name = 'nominative'

    name = fields.Char(string='Nome', size=15, required=True)
    surname = fields.Char(string='Cognome', size=15, required=True)
    nominative = fields.Char(string='Nominativo', compute='comp_nominative', store=True)
    book_id = fields.Many2many('book.book', 'book_author_rel', 'author_id', 'book_id','Record libri')
    born_date = fields.Char(string='Data di Nascita', size=10)
    number_books = fields.Integer(string='Numero di libri pubblicati')
#'number_books' : fields.integer(string='Numero di libri pubblicati', compute='comp_number_books', store=False)

    @api.depends('name','surname')
    def comp_nominative(self):
        self.nominative = (self.name or '')+' '+(self.surname or '')
        
    #def comp_number_books(self)
    #    self.number_books = 
