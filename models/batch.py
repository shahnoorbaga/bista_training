from odoo import models, fields, api
class batch(models.Model):
    _name = 'bista_training.batch'
    _description = 'trainee batch class'

    name = fields.Char("Batch Name")
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    location = fields.Many2one('bista_training.trainee_location',String='Location')
    trainees = fields.One2many('bista_training.trainee','batch')
    trainers = fields.One2many('bista_training.trainer','batch')
    stages = fields.Many2one('bista_training.training_stages','status')
    state = fields.Selection([('draft', 'Draft'), ('progress', 'Progress'), ('done', 'Done')], string="Status",
        default='draft', tracking=True, related="stages.status")
    training_topics = fields.Many2many('bista_training.training_topics','name','subject')

