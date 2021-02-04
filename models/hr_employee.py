

from odoo import api, fields, models


class HrEmployeePrivate(models.Model):
    _name = "hr.employee"
    _inherit = ['hr.employee']

    is_trained = fields.Boolean('is trained')