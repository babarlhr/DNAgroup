# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta,datetime,date
from odoo.exceptions import Warning, ValidationError


class HrContractExtension(models.Model):
	_inherit = 'hr.contract'

	pitems = fields.One2many('payroll.tree', 'link', string="Salary Structure")
	basic = fields.Float("Basic")
	housing = fields.Float("Housing")
	transporter = fields.Float("Transporter")
	cost_of_living = fields.Float("Cost of Living")
	other_allowance = fields.Float("Other Allowances")
	total = fields.Float("Total")
	gosi = fields.Boolean('GOSI')


	@api.onchange('basic','housing','transporter','cost_of_living','other_allowance')
	def GetTotal(self):
		self.total = self.basic + self.housing + self.transporter + self.cost_of_living + self.other_allowance




class PayrollTree(models.Model):
	_name = 'payroll.tree'

	Type = fields.Many2one('payroll.items')
	desc = fields.Char("Description")
	amnt = fields.Float("Amount")
	link = fields.Many2one("hr.contract")

class PayrollItems(models.Model):
	_name = 'payroll.items'

	name = fields.Char("Name")