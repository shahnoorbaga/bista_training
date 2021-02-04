from odoo import api, fields, models

class trainee_reject(models.TransientModel):
    _name = 'bista_training.trainee_reject'
    _description= 'Reject Trainee'

    trainee_id=fields.Many2one('bista_training.trainee', string='Trainee',required=True)
    name=fields.Char('Reason for rejection')


    def action_reject(self):
        record_id = self.trainee_id
        record_id.reject_reason = self.name

        return True
