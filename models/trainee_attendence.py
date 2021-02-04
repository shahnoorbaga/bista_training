from odoo import models, fields, api
from datetime import datetime
class trainee_attendence(models.Model):
    _name = 'bista_training.trainee_attendence'
    _description = 'trainee attendence class'

    name = fields.Char(compute='comp_name', store=True)
    #name = fields.Char(compute='comp_name')
    date = fields.Date(String="Date", default=datetime.today())
    trainee = fields.Many2one('bista_training.trainee',String='Trainee')
    log_in_time = fields.Datetime('Log in Time')
    log_out_time = fields.Datetime('Log out time')
    hours = fields.Float('Hours')
    training_record = fields.Char('Training Record')


    @api.depends('name','date')
    def comp_name(self):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        self.name = ('Training record for:') + ' ' + (date_time or '')
    #@api.depends('name','date')
  #  def comp_name(self):
       # self.name = 'Training Attendence Record Of' + self.date
