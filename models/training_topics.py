from odoo import models, fields, api

class training_topics(models.Model):
    _name = 'bista_training.training_topics'
    _description = 'training topics class'

    name = fields.Char("Name", required=True)
    subject = fields.Many2one('bista_training.training_subjects',string="Subject")
