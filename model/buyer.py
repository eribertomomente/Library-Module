from openerp import models, fields

class buyer(models.Model):

    _name = "book.buyer"
    _description = "Buyer"
    _rec_name = 'name'
    
    name = fields.Char(string='Nome', size=15, required=True)                                           #Nome dell'acquirente
    surname = fields.Char(string='Cognome', size=15, required=True)                                     #Cognome dell'acquirente
    book_id = fields.Many2many('book.book', 'book_buyer_rel', 'buyer_id', 'book_id', 'Record libri')    #Libri acquistati dall'acquirente
    born_date = fields.Date(string='Data di Nascita')                                                   #Data di nascita dell'acquirente
    
    
    

