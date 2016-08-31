from openerp import models, fields, api


class nationality(models.Model):

    _name = "book.nationality"
    _description = "Nationality"
    _rec_name = 'country'
    
    country = fields.Char(string='Stato', size=15, required=True)                               #Nome della nazione
    author_ids = fields.One2many('book.author', 'nationality_id', 'Record autori')              #Autori con la relativa nazionalita'
    author_str = fields.Char(string='Autori Relativi', compute='comp_author_str', store=True)   #Campo calcolato per visualizzare nel tree i nomi degli autori in relazione
    
    @api.multi
    @api.depends('author_ids')
    def comp_author_str(self):       #Funzione che mi costruisce una stringa con tutti i nominativi degli autori in relazione
        str = ""
        for author in self.author_ids:
            str = str + author.nominative + ', '
        str = str[0:-2]    
        self.author_str = str
   