#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2

DBNAME = 'news'

db = psycopg2.connect(database=DBNAME)
c = db.cursor()

c.execute('''   SELECT *
                FROM topArticles
                LIMIT 3;
                ''')
popularArticles = c.fetchall()

for (articleTitle, totalViews) in popularArticles:
    print r'"{}" - {} views'.format(articleTitle, totalViews)

c.execute('''   SELECT name, total
                FROM topAuthors, authors
                WHERE topAuthors.author = authors.id;
                ''')
popularAuthors = c.fetchall()

print '\n'
for (authorName, totalViews) in popularAuthors:
    print r'{} - {} views'.format(authorName, totalViews)

c.execute('''   SELECT to_char(time, 'Mon DD, YYYY'), percentError
                FROM percentError
                WHERE percentError > 1;
                ''')
percentErrors = c.fetchall()

print '\n'
for (date, error) in percentErrors:
    print r'{} - {} % errors'.format(date, error)

db.close()
