# Copyright 2016 Antonio Espinosa <antonio.espinosa@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MembershipLine(models.Model):
    _inherit = "membership.membership_line"

    date_withdrawal = fields.Date(
        string="Withdrawal date",
        help="Date when member requested membership withdrawal")
    withdrawal_reason_id = fields.Many2one(
        string="Withdrawal reason",
        comodel_name='membership.withdrawal_reason')
