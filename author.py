from openerp import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class authors(models.Model):

    _name = "book.author"
    _description = "Authors"
    _rec_name = 'surname'
    

    name = fields.Char(string='Nome', size=15, required=True)
    surname = fields.Char(string='Cognome', size=15, required=True)
    nominative = fields.Char(string='Nominativo', compute='comp_nominative', store=True)
    book_id = fields.Many2many('book.book', 'book_author_rel', 'author_id', 'book_id','Record libri')
    born_date = fields.Date(string='Data di Nascita')
    number_books = fields.Integer(string='Numero di libri pubblicati', compute='comp_number_books', store=True)
    nationality_id = fields.Many2one('book.nationality', "Nazionalita'")

    @api.depends('name','surname')
    def comp_nominative(self):
        self.nominative = (self.name or '')+' '+(self.surname or '')
        
    @api.depends('book_id')        
    def comp_number_books(self):
        _logger.info("__________________SONO_PASSATO_DI_QUA_" +__name__+ "_____________________")
        #self.number_books  = self.book_id.search_count([])