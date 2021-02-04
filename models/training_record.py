from odoo import models, fields, api
from datetime import datetime
class training_record(models.Model):
    _name = 'bista_training.training_record'
    _description = 'training record class'
    _inherit = ['bista_training.trainee_attendence']

    name = fields.Char(compute='comp_name', store=True)
    date = fields.Date('Date')
    batch = fields.Many2one('bista_training.batch')
    training_lines = fields.One2many('bista_training.training_record_line','training_record')
    topics_covered = fields.One2many('bista_training.training_topic_line','id')
    attendence = fields.One2many('bista_training.trainee_attendence', 'id')
    stages = fields.Many2one('bista_training.training_stages','status')

    @api.depends('date')
    def comp_name(self):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        self.name = 'Training record for:' + ' ' + (date_time or '')

    @api.onchange('batch')
    def comp_name1(self):
        # loop to avoid singelton error
        for rec in self:
            dict1 = [(5,0,0)]
            # dict1 = []
            # loop in batch model with trainee id
            for dict2 in self.batch.trainees:
                var1 = {
                    'id': dict2.id,
                    'name': dict2.name,
                }
                dict1.append((0,0, var1))
            rec.training_lines = dict1

            # for data2 in self.batch.trainees:
            #     var={
            #     trainee_id:data2.id,
            #     name:data2.name,
            #     }
            #     data1.append(var)
            # rec.training_lines=data1
