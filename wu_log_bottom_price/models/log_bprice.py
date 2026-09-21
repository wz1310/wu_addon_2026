# -*- coding: utf-8 -*-
from odoo import models, fields, api, SUPERUSER_ID, _
from odoo.exceptions import UserError,ValidationError,RedirectWarning,AccessError
from datetime import timedelta
import re
import datetime,json

import logging,base64
_logger = logging.getLogger(__name__)

class NrsBottomPriceWizard(models.TransientModel):
    _inherit = 'nrs.bottom.price.wizard'

    def confirm(self):
    	# aaaa
        res = super(NrsBottomPriceWizard, self).confirm()
        user = self.env.user.name
        msgs = []
        msgs.append("%s has validated bottom price" %(user,))
        self.so.message_post(body=msgs[0])

        return res