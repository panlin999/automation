# coding="utf-8"
# import pymysql
import xlrd


class method:
    #  #excel版数据
    tr = xlrd.open_workbook(filename="建筑材料管理系统.xls")
    ts = tr.sheet_by_index(0)
    SuccessData = []
    for i in range(1, ts.nrows):
        da = ts.row_values(i)[0:12]
        SuccessData.append(da)
    print(SuccessData)
###实现运行第2 4 6 8条用例
# for a in range(1,ts.nrows):
#   if ts.row_values(a)[:1][0] % 2 == 0:
#
#       SuccessData.append(ts.row_values(a))
# print(SuccessData)

# t1=xlrd.open_workbook(filename="建筑材料管理系统.xls")
# t2=t1.sheet_by_index(0)
# ErrorData=[]
# for j in range(1,t2.nrows):
#     t3=t2.row_values(j)[3:10]
#     ErrorData.append(t3)
# print(ErrorData)


# # 两个列表变成字典
# l1 = ["A", "B", "C", "D"]
# l2 = [1, 2, 3, 4]
# d = dict(zip(l1, l2))
# print(d)

# 数据库版数据
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     passwd="root",
#     db="bank"
# )
#
# cursor=mydb.cursor()
# sql="select ID,账号,密码,expect,bug标题,指派给,严重级别,优先级别,备注,复现步骤,预期结果,实际结果 from c0"
# cursor.execute(sql)
# c=cursor.fetchall()
# SuccessData=c
# print(SuccessData)
