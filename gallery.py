html = """
<html>
    <head>
        <title>FCSG</title>
    </head>
    <body>
        <h1>FCSG</h1>
        Kämpfen und Siegen
    </body>
</html>
"""
print(html)

with open("index.html", "w") as file:
    file.write(html)