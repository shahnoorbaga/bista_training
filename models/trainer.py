from odoo import models, fields, api
class trainer(models.Model):
    _name = 'bista_training.trainer'
    _description = 'trainer class'

    name = fields.Char(compute='comp_name', store=True)
    trainer_first_name = fields.Char('First Name', required=True)
    trainer_last_name = fields.Char('last Name')
    profile_image = fields.Binary('ProfileImage', attachment=True)
    email = fields.Char("Email id")
    id = fields.Integer("ID")
    batch = fields.Many2one('bista_training.batch', string='Select Batch')


    # api depend for firstname and last name concatination
    @api.depends('trainer_first_name','trainer_last_name')
    def comp_name(self):
        self.name = (self.trainer_first_name or '') + ' ' + (self.trainer_last_name or '')
