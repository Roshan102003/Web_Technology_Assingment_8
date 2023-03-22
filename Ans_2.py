import os
headers=["Content-type:text/html"]

qs=os.environ['QUERY_STRING']

def sendHeaders():
    for h in headers:
        print(h)
        print("\n")


def sendForm():
    print('''
   <html>
    <body>
        <form action="ssp2.py" method="get">
            <label for="myname">enter your name</label>
            <input id="myname" type="text" name="firstname" value="Abhi">
            <input type="submit">
        </form>
    </body>
   </html>
    ''')


def sendPage(name):
    print(
        '''
        <html>
        <body>
        <h1>hello{0}</h1>
        </body>
        </html>'''.format(name)
    )
if 'firstname' in qs:
    name=qs.split('=')[1]
else:
    name='No Name Provided'
sendHeaders()

sendForm()
sendPage(name)

print("<html>")
print("<body>")
print("<h1>Hello %s</h1>" % name)
print("</pre>")
print("</body>")
print("</html>")