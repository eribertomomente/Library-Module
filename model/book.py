from openerp import models, fields, api

class book(models.Model):

    _name = "book.book"
    _description = "Simple Book"
    _rec_name = 'title'
    
    title = fields.Char(string='Titolo', size=30, required=True)                                                            #Titolo
    author_id = fields.Many2many('book.author', 'book_author_rel', 'book_id', 'author_id', 'Autori')                        #Autore
    category_id = fields.Many2one('book.category', 'Genere')                                                                           #Descrizione
    pagesnumber = fields.Integer(string='n. pagine')                                                                        #Numero di pagine
    buyer_id = fields.Many2many('book.buyer', 'book_buyer_rel', 'book_id', 'buyer_id', 'Record acquirenti')                 #Acquirente
    number_sales_per_book = fields.Integer(string="Campo d'appoggio", compute='comp_number_sales_per_book', store=True)     #Numero di vendite per libro (campo calcolato)
    
    @api.one
    @api.depends('buyer_id')        
    def comp_number_sales_per_book(self):    #Funzione che conta il numero di vendite per libro 
        count = self.buyer_id.search_count([('book_id.id', '=', self.id)])
        self.number_sales_per_book = count