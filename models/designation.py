from odoo import models, fields, api

class designation(models.Model):
    _name = 'bista_training.designation'
    _description = 'designation class'

    name = fields.Char('Name',required=True)