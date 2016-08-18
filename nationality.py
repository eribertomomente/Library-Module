from openerp import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class nationality(models.Model):

    _name = "book.nationality"
    _description = "Nationality"
    _rec_name = 'country'
    
    country = fields.Char(string='Stato', size=15, required=True)
    author_ids = fields.One2many('book.author', 'nationality_id', 'Record autori')
    author_str = fields.Char(string='xxxxxxxx', compute='comp_author_str', store=True)
    
    @api.depends('author_ids')
    def comp_author_str(self):
        str = ""
        for i in country:
            str = str + i.name + ', '
        _logger.info("____________________SONO_PASSATO_PER_IL_CICLO_______________________")
        self.nominative = str
   