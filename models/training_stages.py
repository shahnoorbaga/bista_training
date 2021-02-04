# -*- coding: utf-8 -*-

from odoo import models, fields, api


class training_stages(models.Model):
    _name = 'bista_training.training_stages'
    _description = 'Stages Master'

    #name = fields.Many2one("bista_training.trainee",domain="[('state','=','current')]")
    name = fields.Char('Stage Name')
    batch_available = fields.Boolean('Available on Batch')
    training_available = fields.Boolean('Available on Training Record')
    status = fields.Selection(
        [('draft', 'Draft'), ('progress', 'Progress'), ('done', 'Done')], string="Status",
        default='draft', tracking=True)
