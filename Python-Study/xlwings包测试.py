import xlwings as xw

error_code_excel_path = r'C:\Users\18320\Desktop\新建 Microsoft Excel 工作表.xlsx'
app = xw.App()
wb = app.books.open(error_code_excel_path)

error_code_text_path = '03.Python异常代码含义对照表.md'

try:
    ws = wb.sheets[0]
    info = ws.used_range
    sheet0_row = info.last_cell.row
    sheet0_column = info.last_cell.column
    # 把表单中的内容转化为列表(去掉表头)
    Sheet0_List = ws.range((2, 1), (sheet0_row, sheet0_column)).value
    Sheet0_Head = ws.range((1, 1), (1, 2)).value
    with open(error_code_text_path, 'w', encoding='utf-8') as f:
        print('# Python异常代码含义对照表', file=f)
        # 打印表头
        # print(f'x:10s') 格式化输出
        print(f'|序号|{Sheet0_Head[0]}|{Sheet0_Head[1]}|', file=f)
        print('|:----|:----|:----|', file=f)
        # 打印内容
        for i, x in enumerate(Sheet0_List):
            print(f'|{i}|{x[0]}|{x[1]}|', file=f)

    print(f'共{sheet0_row}行,{sheet0_column}列,输入结束')
finally:
    app.quit()


