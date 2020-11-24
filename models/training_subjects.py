from odoo import models, fields, api

class training_subjects(models.Model):
    _name = 'bista_training.training_subjects'
    _description = 'training subjects class'

    name = fields.Char('Name',required=True)
    description = fields.Html("Description")
    topics = fields.One2many('bista_training.training_topics','name',String="Topic Name")
    trainer = fields.Many2many('bista_training.trainer','trainer_name')

