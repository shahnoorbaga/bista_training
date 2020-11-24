# -*- coding: utf-8 -*-
from odoo import models, fields, api

class trainee(models.Model):
    _name = 'bista_training.trainee'
    _description = 'trainee class'

    name = fields.Char(compute='comp_name', store=True)
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('last Name')

    # api depend for firstname and last name concatination
    @api.depends('first_name','last_name')
    def comp_name(self):
        self.name = (self.first_name or '') + ' ' + (self.last_name or '')

    # @api.model(trainee_id)
    # def auto(self):
    # for i in range(count(name)):
    # return i

    # unique constraint
    _sql_constraints = [('id', 'unique(trainee_id)', ' Please enter Unique id.')]
    trainee_id = fields.Char(string='Trainee id',default=lambda self:self.env['ir.sequence'].next_by_code('trainee.id'))
    #trainee_id = fields.Char()
    emp_code = fields.Char('Emp code')
    personal_email_id = fields.Char('Personal email id', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male')
    dob = fields.Date('Date Of Birth')
    doj = fields.Date('Date Of joining')
    location = fields.Many2one('bista_training.trainee_location')
    designation = fields.Many2one('bista_training.designation')
    profile_image = fields.Binary('ProfileImage', attachment=True)

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
