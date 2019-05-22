#!/usr/bin/env python
#-*- coding:utf-8 -*-
def response()
  with open('sql_solution.txt', 'w') as f:
    f.write('Sql Found!
solution suggest:
1. Do not use dynamic SQL, to avoid the user to put the output into the SQL statement, using prepared statement and parameter query;
2. Do not keep sensitive data in plain text.
3. Limit the database and privileges to avoid the attacker to obtain permissions;
4. Avoid displaying database errors directly to users;
5. Regularly test Web programs that interact with the database, etc')
