# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class trainee(models.Model):
    _name = 'bista_training.trainee'
    _description = 'Bista Trainee'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(compute='comp_name', store=True)
    id = fields.Integer("ID")
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('last Name')

    employee_id = fields.Many2one('hr.employee', string="Employee Details")

    # unique constraint
    _sql_constraints = [('id', 'unique(trainee_id)', ' Please enter Unique id.')]
    trainee_id = fields.Char(string='Trainee id',
                             default=lambda self: self.env['ir.sequence'].next_by_code('trainee.id'))
    # trainee_id = fields.Char()
    emp_code = fields.Char('Emp code')
    personal_email_id = fields.Char('Personal email id', required=True)
    linkedin = fields.Char('Linkedin Profile Url')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male')
    dob = fields.Date('Date Of Birth')
    doj = fields.Date('Date Of joining')
    location = fields.Many2one('bista_training.trainee_location')
    designation = fields.Many2one('bista_training.designation')
    profile_image = fields.Binary('ProfileImage', attachment=True)
    batch = fields.Many2one('bista_training.batch', string='Select Batch')
    user_id = fields.Many2one("res.user")

    state = fields.Selection(
        [('new', 'New'), ('training', 'Training'), ('rejected', 'Rejected'), ('employed', 'Employed')], string="state",
        default='new', tracking=True)

    # api depend for firstname and last name concatination
    @api.depends('first_name','last_name')
    def comp_name(self):
        self.name = (self.first_name or '') + ' ' + (self.last_name or '')

    def action_reject(self):
        return_val = {
            'name': ('Reject_Trainee'),
            'view_mode': 'form',
            'res_model':'bista_training.trainee_reject',
            'view_id': self.env.ref('bista_training.trainee_reject_view_form').id,
            'type': 'ir.actions.act_window',
            'context': {
                    'default_trainee_id':self.id},
            'target':'new'

        }
        return return_val
        for rec in self:
            rec.state ='rejected'


    def action_employed(self):
        # Actions
        for rec in self:
            rec.state ='employed'
            employee_data = {
                'name': rec.name,
                'work_email': rec.personal_email_id,
                 'image_1920': rec.profile_image,
             }
            employee_record = self.env['hr.employee'].create(employee_data)
            rec.employee_id = employee_record.id
            contact_details = {
            'name': rec.name,
            "email" : rec.personal_email_id,
            }
            contact = self.env['res.partner'].create(contact_details)

            user_details = {
                'name': rec.name,
                'login': rec.personal_email_id,
                'password': rec.personal_email_id,

            }

            user = self.env['res.users'].create(user_details)


        return True


    @api.onchange('name')
    def _onchange_name_update_email(self):
        self.personal_email_id = self.name + '@gmail.com'




    # @api.model(trainee_id)
    # def auto(self):
    # for i in range(count(name)):
    # return i


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
