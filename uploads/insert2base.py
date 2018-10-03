import dbf

from django.db import connection


def oper(dbf_file):
    rows_list = []
    sql = "INSERT INTO oper VALUES (%s, %s, %s, %s)"
    table = dbf.Table(dbf_file)
    table.open()
    with connection.cursor() as cursor:
        for item in table:
            row_tuple = (item['hkod'], item['name_o'], item['price'], item['notksg'])
            rows_list.append(row_tuple)
        cursor.executemany(sql, tuple(rows_list))
    table.close()