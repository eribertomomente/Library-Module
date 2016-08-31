from openerp import models, fields, api


class authors(models.Model):

    _name = "book.author"
    _description = "Authors"
    _rec_name = 'surname'
    

    name = fields.Char(string='Nome', size=15, required=True)                                                       #Nome
    surname = fields.Char(string='Cognome', size=15, required=True)                                                 #Cognome
    nominative = fields.Char(string='Nominativo', compute='comp_nominative', store=True)                            #Nome e Cognome dell'autore
    book_id = fields.Many2many('book.book', 'book_author_rel', 'author_id', 'book_id','Record libri')               #Libri scritti dal relativo autore
    born_date = fields.Date(string='Data di Nascita')                                                               #Data di Nascita
    number_books = fields.Integer(string='Numero di libri pubblicati', compute='comp_number_books', store=True)     #Numero di libri scritto da ogni autore (campo calcolato)
    nationality_id = fields.Many2one('book.nationality', "Nazionalita'")                                            #Nazionalita' dell'autore

    @api.one
    @api.depends('name','surname')          #Restituisce una stringa concatenando il nome e il cognome di ogni autore
    def comp_nominative(self):
        self.nominative = (self.name or '')+' '+(self.surname or '')
    
    @api.one    
    @api.depends('book_id')        
    def comp_number_books(self):            #Calcola il numero di libri scritti da ogni autore
        count = self.book_id.search_count([('author_id.id', '=', self.id)])
        self.number_books = count