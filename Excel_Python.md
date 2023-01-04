use the openpyxl library

```python

    import openpyxl

    # open workbook
    work_book = openpyxl.load_workbook("sales.xlsx")
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


