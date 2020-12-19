# myke pgsql test
# 2020-12-18 2020-12-19 1.2

import psycopg2 as sql
from contextlib import closing
import psycopg2.extras
from psycopg2.extras import DictCursor

print("ok")

# conn = psycopg2.connect(dbname='pgtest', user='postgres', password='postgres', host='localhost')
# cursor = conn.cursor()

with closing(sql.connect(dbname='pgtest', user='postgres', password='postgres', host='localhost')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:

        print("get some data")
        cursor.execute('SELECT * FROM tt')
        for row in cursor:
            print(row, "name=", row['name'])

        print("get tables info")
        cursor.execute("""SELECT t.table_name, pg_catalog.obj_description(pgc.oid, 'pg_class')
            FROM information_schema.tables t
            INNER JOIN pg_catalog.pg_class pgc
            ON t.table_name = pgc.relname 
            WHERE t.table_type='BASE TABLE'
            AND t.table_schema='public'""")
        for row in cursor:
            print(row)

        print("get columns comments")
        cursor.execute("""
            SELECT
            cols.column_name,
            (
                SELECT
                    pg_catalog.col_description(c.oid, cols.ordinal_position::int)
                FROM pg_catalog.pg_class c
                WHERE
                    c.oid     = (SELECT cols.table_name::regclass::oid) AND
                    c.relname = cols.table_name
            ) as column_comment
            FROM information_schema.columns cols
            WHERE
                cols.table_catalog = 'pgtest' AND
                cols.table_schema  = 'public' AND
                cols.table_name    = 'tt';   
            """)
        for row in cursor:
            print(row)

        print("get columns types")
        cursor.execute("""
            select table_name, column_name, data_type, character_maximum_length 
            from information_schema.columns
            where table_name = 'tt' AND table_schema = 'public'
            """)
        for row in cursor:
            print(row)

        print("get columns keys")
        cursor.execute("""
            select kcu.table_schema,
                kcu.table_name,
                tco.constraint_name,
                kcu.ordinal_position as position,
                kcu.column_name as key_column
                from information_schema.table_constraints tco
            join information_schema.key_column_usage kcu 
                on kcu.constraint_name = tco.constraint_name
                and kcu.constraint_schema = tco.constraint_schema
                and kcu.constraint_name = tco.constraint_name
            where 
                tco.constraint_type = 'PRIMARY KEY'
                OR
                tco.constraint_type = 'FOREIGN KEY'
            order by kcu.table_schema,
                kcu.table_name,
                position
            """)
        for row in cursor:
            print(row)

print("Job is done.")

# [Running] python -u "/home/myke/pro/pgtest/py-acc/acc-1.py"
# ok
# get some data
# [1, 'd83d5399-ad78-464f-a227-92648c0ee3f3', 'vasya', 'ok'] name= vasya
# [2, 'b61fe1bc-ed0b-4e41-9889-254387214a81', 'sonya', 'fail'] name= sonya
# get tables info
# ['tt', 'good table tt']
# get columns comments
# ['id', 'primary index']
# ['uuid', 'universal index']
# ['name', 'person name']
# ['bio', 'person biography']
# get columns types
# ['tt', 'id', 'integer', None]
# ['tt', 'uuid', 'uuid', None]
# ['tt', 'name', 'character varying', 255]
# ['tt', 'bio', 'text', None]
# get columns keys
# ['public', 'tt', 'tt_pkey', 1, 'id']
# Job is done.

# [Done] exited with code=0 in 0.086 seconds
