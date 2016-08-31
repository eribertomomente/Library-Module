from openerp import models, fields, api

class category(models.Model):

    _name = "book.category"
    _description = "Category"
    _rec_name = 'name'

    name = fields.Char(string='Nome', size=15, required=True)                                                           #"Nome" del genere
    number_books = fields.Integer(string='Numero di libri di questo genere', compute='comp_number_books', store=True)   #Numero di libri di quel genere (campo calcolato)
    book_ids = fields.One2many('book.book', 'category_id', 'Record libri')                                              #Libri con il relativo genere
    book_str = fields.Char(string='Libri Relativi', compute='comp_book_str', store=False)                               #Stringa con tutti i titoli dei libri in relazine (campo calcolato)
    number_sales = fields.Integer(string='Numero Vendite', compute='comp_number_sales', store=True)
    
    @api.one
    @api.depends('book_ids')        
    def comp_number_books(self):    #Funzione che conta il numero dei libri in relazione per ogni genere
    
    # verifica se len(self.book_ids) == self.book_ids.search_count([('category_id.id', '=', self.id)]) ____________SI E' LO STESSO
        count = len(self.book_ids)
        self.number_books = count
        
    @api.one
    @api.depends('book_ids')
    def comp_book_str(self):        #Funzione che mi costruisce una stringa con tutti i titoli dei libri in relazione
        str = ""
        for book_title in self.book_ids:
            str = str + book_title.title + ', '
        str = str[0:-2]    
        self.book_str = str
        
    @api.one
    @api.depends('book_ids')        
    def comp_number_sales(self):    #Funzione che conta il numero di vendite per ogni genere
        sales=0
        for count in self.book_ids:
            sales+= count.number_sales_per_book
        self.number_sales = sales
    
        # somma del nuovo campo calcolato su book