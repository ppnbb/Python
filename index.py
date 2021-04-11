#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/' +pageId, 'r').read()

else:
    pageId = 'Welcome'
    description = 'Hello web'
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Web1 - Welcome</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1><a href="index_no_id.py">Web</a></h1>
    <ol>
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=CSS">CSS</a></li>
        <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    </ol>
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description))