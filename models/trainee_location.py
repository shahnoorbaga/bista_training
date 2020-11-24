from odoo import models, fields, api
class trainee_location(models.Model):
    _name = 'bista_training.trainee_location'
    _description = 'trainee location class'

    location_name = fields.Char("Location Name",required=True)
    street1 = fields.Char('Street 1')
    street2 = fields.Char('Street 2')
    city = fields.Char('City')
    state = fields.Many2one('res.country.state',string='State')
    country = fields.Many2one('res.country',string='Country')