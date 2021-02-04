from odoo import models, fields, api


class training_record_line(models.Model):
    _name = 'bista_training.training_record_line'
    _description = 'training record line class'

    trainee = fields.Many2one('bista_training.trainee')
    name = fields.Char('Name')
    remarks_comments = fields.Text('Remarks/Comments')
    attendence_status = fields.Selection([("present","Present"),("absent","Absent")])
    training_record = fields.Many2one('bista_training.training_record',ondelete="cascade")



