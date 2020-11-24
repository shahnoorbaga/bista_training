from odoo import models, fields, api
class trainer(models.Model):
    _name = 'bista_training.trainer'
    _description = 'trainer class'

    trainer_name = fields.Char(compute='comp_name', store=True)
    trainer_first_name = fields.Char('First Name', required=True)
    trainer_last_name = fields.Char('last Name')

    # api depend for firstname and last name concatination
    @api.depends('trainer_first_name','trainer_last_name')
    def comp_name(self):
        self.trainer_name = (self.trainer_first_name or '') + ' ' + (self.trainer_last_name or '')
