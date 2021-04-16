import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

cell_format = workbook.add_format()


cell_format.set_bg_color('ff00ff')

worksheet.write(0, 0, 'Foo', cell_format)
worksheet.write_string(1, 0, 'Bar', cell_format)
worksheet.write_number(2, 0, 3,     cell_format)
worksheet.write_blank (3, 0, '',    cell_format)

for x in range(19):
    cell_format = workbook.add_format()
    cell_format.set_pattern(x)
    worksheet.write(x,1, '', cell_format)
    print(x)





workbook.close()