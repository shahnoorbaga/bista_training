from odoo import models, fields, api


class topic_line(models.Model):
    _name = 'bista_training.training_topic_line'
    _description = 'training topic line class'

    topic = fields.Many2one("bista_training.training_topics")
    name = fields.Char('Name')
    remarks_comments = fields.Text('Remarks/Comments')

