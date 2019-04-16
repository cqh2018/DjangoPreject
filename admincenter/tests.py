from django.test import TestCase

# Create your tests here.
from sqlalchemy import text, create_engine
import xlsxwriter

import datetime
audit_url = 'postgres://auditor:753f3abce5b2c049@10.175.121.215/auditdb?client_encoding=utf8'
class ExportSenseLog():
    def exportLog(self,sql):
        db = create_engine(audit_url)
        conn = db.connect()
        result = conn.execute(sql)
        record = result.fetchone()
        alist = []
        while record:
            alist.append(record)
            record = result.fetchone()
        result.close()
        conn.close()
        return alist
    #将一个时间段格式化成，数组时间格式
    def getBetweenDay(self,startStr,endStr):
        date_list = []
        begin_date = datetime.datetime.strptime(startStr, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(endStr, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str.replace("-", "_"))
            begin_date += datetime.timedelta(days=1)
        return date_list
    #拼一个时间段的敏感日志sql
    def getSensLogMonthSql(self,startStr,endStr):
        days = self.getBetweenDay(startStr,endStr)
        sql = ""
        i = 0
        for day in days:
            i = i + 1
            sql = sql + "SELECT * from  t_sens_" + day
            if len(days) > 1 and i != len(days):
                sql = sql + " union all "
        return sql
    #给出路径，标题，结果集
    def exportDataToExcel(self,path,title,result):
        workbook = xlsxwriter.Workbook(path)
        format_title = workbook.add_format({
            'font': 'Arial',
            'font_size': 10,  # 字体大小
            'bold': True,  # 是否粗体
            'bg_color': '#ffff66',  # 表格背景颜色
            'font_color': '#000000',  # 字体颜色
            'align': 'center',  # 居中对齐
            'top': 1,  # 上边框
            # 后面参数是线条宽度
            'left': 1,  # 左边框
            'right': 1,  # 右边框
            'bottom': 1  # 底边框
        })
        format = workbook.add_format({
            'font': 'Arial',
            'font_size': 10,  # 字体大小
            'font_color': '#000000',  # 字体颜色
            'align': 'center',  # 居中对齐
            'top': 1,  # 上边框
            'left': 1,  # 左边框
            'right': 1,  # 右边框
            'bottom': 1  # 底边框
        })
        format_content = workbook.add_format({
            'font': 'Arial',
            'font_size': 10,  # 字体大小
            'bg_color': '#FF0000',  # 表格背景颜色
            'font_color': '#000000',  # 字体颜色
            'align': 'center',  # 居中对齐
            'top': 1,  # 上边框
            'left': 1,  # 左边框
            'right': 1,  # 右边框
            'bottom': 1  # 底边框

        })

        worksheet = workbook.add_worksheet()
        #title = ('logid','logname','account','acctype','systemid','accesstype','dip','clientip','url','optypeid','logtime','opcontent','dataname','datarange','datalevel','pingju','pingjutype','hbasession')
        j = 0
        for i in (title):
            worksheet.write(0, j, i, format_title)
            j = j + 1
        for i in range(len(result)):
            # 对result的每个子元素作遍历，
            for j in range(len(result[i])):
                # 将每一行的每个元素按行号i,列号j,写入到excel中。
                if isinstance(result[i][j], datetime.datetime) == True:
                    worksheet.write(i + 1, j, result[i][j].strftime("%Y-%m-%d %H:%M:%S"), format)
                # elif "厂商" in result[i][j]:
                #     worksheet.write(i + 1, j, result[i][j], format_content)
                else:
                    worksheet.write(i + 1, j, result[i][j], format)
                '''
                if result[i][j] == "是":
                    worksheet.write(i + 1, j, result[i][j], format_content)
                else:
                    worksheet.write(i + 1, j, result[i][j], format)
                '''
        workbook.close()
    def exportExcel(self,startStr,endStr,path,title):
        select_sql = self.getSensLogMonthSql(startStr, endStr)
        print(select_sql)
        result = self.exportLog(select_sql)
        self.exportDataToExcel(path, title, result)


if __name__ == "__main__":
    export = ExportSenseLog()
    startStr = "2019-03-01"
    endStr  = "2019-03-01"
    path = "d://敏感日志统计//t_sens_" + endStr + ".xlsx"
    title = (
    'logid', 'logname', 'account', 'acctype', 'systemid', 'accesstype', 'dip', 'clientip', 'url', 'optypeid', 'logtime',
    'opcontent', 'dataname', 'datarange', 'datalevel', 'pingju', 'pingjutype', 'hbasession')
    export.exportExcel(startStr, endStr, path,title)