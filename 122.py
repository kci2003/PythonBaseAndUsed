import io
import zipfile
import requests  # $ pip install requests
from xlrd import open_workbook
a = {}
r = requests.get("https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip")
with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
    for member in archive.infolist():
        wb = open_workbook('E:\Sergey\Python\\stepic\\course1\\temp\\'+ member.filename)
        sheet_names = wb.sheet_names()
        sh = wb.sheet_by_name(sheet_names[0])
        a[sh.col_values(1)[1]]=sh.col_values(3)[1]
for i in sorted(a.items()):
    print(i[0],int(i[1]))