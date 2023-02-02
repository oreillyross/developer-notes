use the openpyxl library

```python

    import openpyxl

    # open workbook
    work_book = openpyxl.load_workbook("sales.xlsx")
    # alternatively open a new workbook in-memory
    work_book = openpyxl.Workbook()
    # get a handle to the active sheet
    sheet = work_book.active
    # or call it by name
    sheet_obj = work_book['100 Sales Records']

    max_col = sheet_obj.max_column
    max_rows = sheet_obj.max_row

    for row in sheet_obj.iter_rows(min_row=1, max_row=2, min_col=1, max_col=3, values_only=True):
    print(row)

    for col in sheet_obj.iter_cols(min_row=1, max_row=2, min_col=1, max_col=3, values_only=True):
    print(col)


```
iter_cols and iter_rows will get you access to most of the cells, returned as tuples of data.

One can access the cells by following 

```
    sheet['A1'] = 'Helllo'
    sheet['A1'].value # Hello

    sheet.calculate_dimension() # A1:C1
    sheet.append('One', 'Two')

    # insert rows and cols

    sheet.insert_rows(idsx = 2, amount = 3)
    sheet.insert_cols(idx = 3) # in excel it is one based indexing
```

This is an in-memory representation, you need to workbook.save(""file.xlsx)

#### Freezing panes

```
    sheet.freeze_panes = 'A2'
```

#### Filtering and Sorting Data

```
    sheet.calculate_dimension() # A1:B22
    sheet.auto_filter.ref = sheet.calculate_dimension()
    sheet.auto_filter.add_filter_column(0, ['Brazil', 'Argentina'])
    # there is a glitch, you need to go to Data in excel and click reapply

    # for sorting you need a range string representing all of the data in the range
    range_str = sheet['B'][1].coordinate + ':' + sheet['B'][-1].coordinate #     'B2:B22'


    sheet.auto_filter.add_sort_condition(range_str, descending=True)
    # there is a glitch, you need to go to Data in excel and click reapply

```

#### Resizing Rows and Columns

```
    sheet_obj # <Worksheet "Sheet">

    sheet_obj['C1'] = 'A high row'

    sheet_obj.row_dimensions[1].height = 70
    sheet_obj.column_dimensions['D'].width = 100


```

```
    from openpyxl.styles import Alignment
    sheet['A1'].alignment = Alignment(horizontal='right', vertical='center')

    sheet.merge_cells('B5:G5')
    
```

### Styling Excel sheets using openpyxl

```
    from openpyxl.styles import Font, Color, Alignment, Border, Side, colors
    bold = Font(bold=True)
    double_border = ...
    square = Border(top=double_border)
    sheet["D7"].font = bold
    workbook.save(file location) # important to apply changes
```

Excel has indexes starting at 1

```
    sheet[1]
```

#### Other formatting objects
- PatternFill
- NamedStyle

#### Applying formatting numbers 


eforxcel.com is handy to get dummy data

```
for row in sheet["K2:M101"]:
    for cell in row:
        cell.number_format = "#,##0"
```

ColorScaleRule

IconSetRule

DataBarRule

dat_bar_rule = DataBarRule(start_type="num", start_value=1, end_type="num", end_num=4, color=colors.RED)

sheet.conditional_formatting.add("G2:G9234", dat_bar_rule)