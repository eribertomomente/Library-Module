from openerp import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class category(models.Model):

    _name = "book.category"
    _description = "Category"
    _rec_name = 'name'

    name = fields.Char(string='Nome', size=15, required=True)
    number_books = fields.Integer(string='Numero di libri di questo genere', compute='comp_number_books', store=True)
    book_ids = fields.One2many('book.book', 'category_id', 'Record libri')
    
    @api.depends('book_ids')        
    def comp_number_books(self):
        
        _logger.info("__________________SONO_PASSATO_DI_QUA_" +__name__+ "_____________________")
        
        #count = self.book_id.search_count([])
        #_logger.info("__________%s__________", type(count).__name__)
        
        #self.number_books = count
        
