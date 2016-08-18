from openerp import models, fields

class nationality(models.Model):

    _name = "book.nationality"
    _description = "Nationality"
    _rec_name = 'country'
    
    country = fields.Char(string='Stato', size=15, required=True)
    author_ids = fields.One2many('book.author', 'nationality_id', 'Record autore')
   