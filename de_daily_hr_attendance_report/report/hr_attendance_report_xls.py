# -*- coding: utf-8 -*-
import time
from odoo import api, models, _, fields
from datetime import datetime
from datetime import date, datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
import pytz


class HrAttendanceXlsx(models.AbstractModel):
    _name = 'report.de_daily_hr_attendance_report.hr_attendance_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    

    def _get_hr_attendance_data(self, data):
        hr_attendance_list = []
        departments = self.env['hr.department'].search([])
        for department in departments:
            department_list = []
            employees = self.env['hr.employee'].search([('department_id','=', department.id)], order='department_id asc')
            for employee in employees:

                hr_attendance = self.env['hr.attendance'].search([('attendance_date', '=', data['on_date']), ('employee_id','=', employee.id)])

                count = 0
                for count_line in hr_attendance:
                    count += 1
                # shift_schedule = self.env['hr.shift.schedule'].search([('employee_id.name','=', hr_attendance.employee_id.name)])
                count_att = 0
                check_in = False
                check_out = False
                employee_name = ' '
                employee_code = ' '
                emp_identification_no = ' '
                department = ' '
                attendance_date = ' '
                check_in = ' '
                check_out = ' '
                shift_name = ' '
                worked_hours = 0
                for line in hr_attendance:
                    employee_name = line.employee_id.name
                    employee_code = line.employee_id.sequence_no
                    emp_identification_no = line.employee_id.identification_id
                    department = line.departments_id.name
                    attendance_date = str(line.attendance_date)
                    # check_in = (str(line.check_in))
                    # check_out = (str(line.check_out))
    #                 shift_name = line.employee_id.shift_id.name
                    worked_hours += round(line.worked_hours, 2)

                    count_att += 1
                    if count_att == 1:
                        check_in = line.check_in.strftime('%H:%M:%S %p')
    #                     check_in = datetime.datetime.strptime(check_in_time, '%H:%M:%S').strftime('%H:%M:%S')
    #                     datetime.datetime.strptime(", "%b %d %Y %H:%M:%S")
    #                     check_in = (str(line.check_in)).strftime("%H:%M:%S")
                    if count_att == count:
                        if line.check_out:
                            check_out = line.check_out.strftime('%H:%M:%S %p')
                        else:
                            False
    #                     check_out = (str(line.check_out))
    #                     check_out = check_out_time.strftime('%H:%M:%S')
                    # check_in = datetime.datetime.strptime(check_in_time, '%m-%d-%Y %H:%M:%S').strftime('%m-%d-%Y %H:%M:%S')
                    # check_out = (str(line.check_out))
                    # check_out = check_in = datetime.datetime.strptime(check_out_time, '%m-%d-%Y %H:%M:%S').strftime('%m-%d-%Y %H:%M:%S')
                    # if line.employee_id.identification_id:
                    #    emp_identification_no = line.employee_id.identification_id
                    # else:
                    #     emp_identification_no = "-"
                    # if line.employee_id.department_id.name:
                    #    department_name = line.employee_id.department_id.name
                    # else:
                    #     department_name = "-"
        #             stock_cost = line.quantity_done * line.product_id.standard_price
        #             current_date = fields.datetime.now()
        #             delta = fields.datetime.now() - line.date
        #             picking = self.env['stock.picking'].search([('name', '=', line.reference)], limit=1)
                if employee_name != ' ':
#                     department_list.append({
#                         'department': department,
#                     })
                    department_list.append({
                        #                 'ref':   line.reference,
                        'employee_name': employee_name,
                        'employee_code': employee_code,
                        'emp_identification_no': emp_identification_no,
                        'department': department,
                        'attendance_date': attendance_date,
                        'check_in': check_in,
                        'check_out': check_out,
    #                     'shift_name': shift_name,
                        'worked_hours': worked_hours,
            #                 'stock_value': stock_cost,
            #                 'no_of_days': delta.days,
                    })
            hr_attendance_list.append(department_list)            
        return hr_attendance_list

    # #         data = []
    # #         domain = [
    # #             ('create_date', '<=', on_date + ' 00:00:00'),
    # # #             ('create_date', '<=', stop_at + ' 23:59:59'),
    # # #             ('order_id.shop_id', 'in', shop_ids.ids)
    # #         ]
    #         order_line_ids = self.env['stock.move'].sudo()
    # #         discunt_data = self._get_pos_sale(order_line_ids)
    #         product_ids = order_line_ids.mapped('product_id')
    #         lines_by_product = {}
    #         for line in order_line_ids:
    #             if line.product_id.id in lines_by_product:
    #                 lines_by_product[line.product_id.id] |= line
    #             else:
    #                 lines_by_product[line.product_id.id] = line

    #             data.append({
    #                  'product_name':product.name,
    #             })
    #         return data
    def generate_xlsx_report(self, workbook, data, products):
        on_date = data.get('on_date')
        
        data_list = self._get_hr_attendance_data(data)

        #         for rec in move_list:
        #             stock_move.append({
        #                 'product_name': rec.product_id.name,
        #             })
        sheet = workbook.add_worksheet("Daily Attendance Report")
        format1 = workbook.add_format({'font_size': 15})
        format2 = workbook.add_format(
            {'font_size': 10, 'bold': True, 'bg_color': '#D3D3D3', 'border': 1, 'valign': 'vcenter'})
        format3 = workbook.add_format({'font_size': 10})
        format6 = workbook.add_format({'font_size': 10})
        format5 = workbook.add_format({'font_size': 10, 'bold': True})
        num_format = workbook.add_format({'font_size': 10, 'num_format': '0.00'})
        format4 = workbook.add_format({'font_size': 10, 'top': 1, 'bottom': 6, 'num_format': '#,##0.00'})
        format7 = workbook.add_format({'font_size': 10, 'top': 1, 'bottom': 6})
        format1.set_align('center')
        format2.set_align('center')
        format5.set_align('center')
        format6.set_align('center')
        format7.set_align('center')

        headers = ['Department', 'Date' 'Check In', 'Check Out', 'Work Hours']

        row = 4
        col = 3
        sheet.set_column(row, 0, 20)
        sheet.set_column(row, 1, 25)
        sheet.set_column(row, 2, 20)
        sheet.set_column(row, 3, 20)
        sheet.set_column(row, 4, 20)
        sheet.set_column(row, 5, 20)
        sheet.set_column(row, 6, 20)
        sheet.set_column(row, 7, 20)
        for header in headers:
            sheet.set_column(col, 1, 8)
            sheet.write(row, col, header, format2)
            col += 1
        
        emp_department = []
        
        row = 6
        col = 0
        sheet.merge_range('A1:G2', 'Daily Attendance Report', format1)
        sheet.merge_range('A3:G3', 'Date: ' + on_date, format5)
        #         sheet.merge_range('A3:G3',  'As on:', format5)
        #         sheet.merge_range('A4:A6', 'S.No.', format2)
        #         sheet.merge_range('B4:B6', 'POS Shop', format2)
        sheet.merge_range('A4:A6', 'Employee', format2)
        sheet.merge_range('B4:B6', 'Employee Code', format2)
        sheet.merge_range('C4:C6', 'Identification No', format2)
#         sheet.merge_range('D4:D6', 'Department', format2)
        sheet.merge_range('D4:D6', 'Date', format2)
        sheet.merge_range('E4:E6', 'Check In', format2)
        sheet.merge_range('F4:F6', 'Check Out', format2)
#         sheet.merge_range('G4:G6', 'Shift', format2)
        sheet.merge_range('G4:G6', 'Work Hours', format2)

#         final_data = []
#         pd = []
#         item_data = []
#         for product in data_list:
#             pd.append(product['internal_ref'])
#         unique_pd = set(pd)
#         for item in unique_pd:
#             product_name = ' '
#             internal_ref = ' '
#             partner_id = ' '
#             purchase_date = ' '
#             tot_quantity_done = 0.00
#             tot_stock_value = 0.00
#             tot_no_of_days = 0
#             for item_data in data_list:
#                 if item_data['internal_ref'] == item:
#                     product_name = item_data['product_name']
#                     internal_ref = item_data['internal_ref']
#                     partner_id = item_data['partner_id']
#                     purchase_date = item_data['purchase_date']
#                     tot_quantity_done = tot_quantity_done + item_data['quantity_done']
#                     tot_stock_value = tot_stock_value + item_data['stock_value']
#                     tot_no_of_days = item_data['no_of_days']
#             final_data.append({
#                 'product_name': product_name,
#                 'internal_ref': internal_ref,
#                 'partner_id': partner_id,
#                 'purchase_date': purchase_date,
#                 'quantity_done': tot_quantity_done,
#                 'stock_value': tot_stock_value,
#                 'no_of_days': tot_no_of_days,
#             })
        for val in data_list:
            sheet.write(row, col + 0, val['employee_name'], format3)
            sheet.write(row, col + 1, val['employee_code'], format6)
            sheet.write(row, col + 2, val['emp_identification_no'], format6)
            sheet.write(row, col + 3, val['department'], format6)
            sheet.write(row, col + 4, val['attendance_date'], format6)
            # #             sheet.write(row, col + 4, val['ref'], format6)
            sheet.write(row, col + 5, val['check_in'], format6)
            sheet.write(row, col + 6, val['check_out'], format6)
#             sheet.write(row, col + 6, val['shift_name'], format6)
            sheet.write(row, col + 7, val['worked_hours'], format6)
            row += 1