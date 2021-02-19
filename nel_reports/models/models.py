# -*- coding: utf-8 -*-

from odoo import api, models
import logging
import datetime
_logger = logging.getLogger(__name__)

class ParticularReport(models.AbstractModel):
    _name = 'report.studio_customization.studio_report_docume_89133f85-1132-4e8b-af71-de75d2c4c06a'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('studio_customization.studio_report_docume_89133f85-1132-4e8b-af71-de75d2c4c06a')
        user_name = self.env['res.user'].browse(self.env.user).name
        _logger.debug('Work Order Routing Information Report printed at %s by %s', str(datetime.datetime.today()), user_name)

        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self,
        }
        # Run some code
        return docargs