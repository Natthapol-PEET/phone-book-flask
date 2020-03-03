from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'project'
    }
mydb = mysql.connector.connect(**config)

@app.route('/')
def hello_world():

    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    sql = 'SQL'
    name = 'name'
    phone = 'phone'
    search_name = 'search_name'

    block = 0
    try:
        block = 1
        search_name = request.form['search_name']
        sql = "SELECT id_phone, phone, name FROM phone WHERE name like '%" + str(search_name) + "%'"
    except:
        try:
            block = 2
            name = request.form['name']
            phone = request.form['phone']
        except:
            pass

    if block == 1:  # Search 
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            name, phone, index = [], [], []
            i = 0
            for x in myresult:
                i += 1
                index.append(i)
                name.append(x[1])
                phone.append(x[2])

            index.reverse()
            name.reverse()
            phone.reverse()

            data = []
            s = []
            count = len(index)

            for i in range(count):
                s = []
                s.append( index.pop() )
                s.append( name.pop() )
                s.append( phone.pop() )
                data.append( s )

    if block == 2:  # insert
        sum = []
        sum.append(phone)
        sum.append(name)
        val = tuple(sum)
        mycursor = mydb.cursor()
        sql = "INSERT INTO phone (phone, name) VALUES (%s, %s)"
        mycursor.execute(sql, val)

        # show all
        sql = "SELECT id_phone, phone, name FROM phone"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        name, phone, index = [], [], []
        i = 0
        for x in myresult:
            i += 1
            index.append(i)
            name.append(x[1])
            phone.append(x[2])

        index.reverse()
        name.reverse()
        phone.reverse()

        data = []
        s = []
        count = len(index)

        for i in range(count):
            s = []
            s.append( index.pop() )
            s.append( name.pop() )
            s.append( phone.pop() )
            data.append( s )

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
