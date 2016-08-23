from openerp import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class nationality(models.Model):

    _name = "book.nationality"
    _description = "Nationality"
    _rec_name = 'country'
    
    country = fields.Char(string='Stato', size=15, required=True)
    author_ids = fields.One2many('book.author', 'nationality_id', 'Record autori')
    author_str = fields.Char(string='Autori Relativi', compute='comp_author_str', store=True)
    
    @api.multi
    @api.depends('author_ids')
    def comp_author_str(self):
        _logger.info("____________________id istanza = %s_____________________", self.id)
        _logger.info("____________________quanti autori? %s_____________________", len(self.author_ids) )
        str = ""
        for author in self.author_ids:
            str = str + author.nominative + ', '
            _logger.info("____________________SONO_PASSATO_PER_IL_CICLO_DI_%s_____________________", author.nominative)
        str = str[0:-2]    
        self.author_str = str
   