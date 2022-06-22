# coding="utf-8"
import xlrd


class login:
    tr = xlrd.open_workbook(filename="bugfree_login.xls")
    ts = tr.sheet_by_index(0)
    SuccessData1 = []
    #
    # for i in range(1, ts.nrows):
    #     da = ts.row_values(i)[0:4]
    #     SuccessData1.append(da)
    # print(SuccessData1)
    for a in range(1, ts.nrows):
        if ts.row_values(a)[:1][0] % 2 == 0:
            c = ts.row_values(a)[0:4]
            SuccessData1.append(c)
    print(SuccessData1)

    # print(t)
    #
    # # a0=xlrd.open_workbook(filename="bugfree_login.xls")
    # # a1=a0.sheet_by_index(0测试)
    # # SuccessData2=[]
    # # for k in range(1,a1.nrows,2):
    # #     a2=a1.row_values(k)[1:3]
    # #     SuccessData2.append(a2)
    # # print(SuccessData2)
    #
    t1 = xlrd.open_workbook(filename="bugfree_login.xls")
    t2 = t1.sheet_by_index(1)
    ErrorData1 = []
    for j in range(1, t2.nrows):
        t3 = t2.row_values(j)[0:4]
        ErrorData1.append(t3)
    print(ErrorData1)
