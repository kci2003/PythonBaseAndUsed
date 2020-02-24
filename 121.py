import xlrd
nvl = (lambda a,b: a or b)
d = {}

wb = xlrd.open_workbook('E:\\Download\\trekking3.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
sh1 = wb.sheet_by_name(sheet_names[1])
# print(sheet_names[0],sheet_names[1])
for i in range(1,len(sh.col_values(1))):
    # print(sh.col_values(1)[i])
    d[sh.col_values(0)[i]]=(nvl(sh.col_values(1)[i],0),nvl(sh.col_values(2)[i],0),nvl(sh.col_values(3)[i],0),nvl(sh.col_values(4)[i],0))
# d[str(sh.col_values(1)[i]) + str(sh.col_values(0)[i])] = sh.col_values(0)[i]
#     d[(int(sh.col_values(1)[i]),sh.col_values(0)[i])] = sh.col_values(0)[i]
    #print(i,sh.col_values(0)[i])
# print(d)
# print(lt[2])
for k in range(1,10):
    lt = [0, 0, 0, 0]
    for  j in  range(1,len(sh1.col_values(1))):
        if k == int(sh1.col_values(0)[j]):
          # print(sh1.col_values(1)[j])
#   # print(sh1.col_values(1)[j]/100)
#   # print(d[sh1.col_values(0)[j]][0])
          lt[0]  = lt[0] + float((d[sh1.col_values(1)[j]][0])*(sh1.col_values(2)[j]/100))
          lt[1] = lt[1] + float((d[sh1.col_values(1)[j]][1])*(sh1.col_values(2)[j]/100))
          lt[2] = lt[2] + float((d[sh1.col_values(1)[j]][2])*(sh1.col_values(2)[j]/100))
          lt[3] = lt[3] + float((d[sh1.col_values(1)[j]][3])*(sh1.col_values(2)[j]/100))
#   # print(sh1.col_values(0)[j], lt[0],lt[1],lt[2],lt[3] )
    print(int(lt[0]), int(lt[1]), int(lt[2]), int(lt[3]))
#     break