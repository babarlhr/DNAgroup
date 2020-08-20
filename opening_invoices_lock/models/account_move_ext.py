# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import Warning, ValidationError


class AccMoveExt(models.Model):
	_inherit='account.move'


	lock_opening_invoice = fields.Boolean(string = "Lock" , copy=False)


	def unlink(self):
		for inv in self:
			if inv.lock_opening_invoice == True:
				raise ValidationError('This opening record is locked, You cannot perform this action.')
			return super(AccMoveExt, self).unlink()