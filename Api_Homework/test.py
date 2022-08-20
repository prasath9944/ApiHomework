from flask import Flask,request,jsonify
import pymysql


app=Flask(__name__)

@app.route('/retreiveall',methods=['GET'])
def retriveAll():
    if request.method=='GET':
        connection, cursor = sql_connection()
        cursor.execute('select * from login')
        data=cursor.fetchall()
        return jsonify(str(data))


@app.route('/insert',methods=['GET','POST'])
def insert_data():
    if (request.method=='POST'):
        id=request.json['id']
        name=request.json['name']
        emailid=request.json['emailid']
        passwd=request.json['passwd']
        gender=request.json['gender']
        coursename=request.json['coursename']
        row="insert into login(id,name,emailid,passwd,gender,coursename) values(%s,%s,%s,%s,%s,%s)"
        connection,cursor=sql_connection()
        cursor.execute(row,(id,name,emailid,passwd,gender,coursename))
        connection.commit()
        return jsonify(str(cursor))



@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        connection, cursor = sql_connection()
        id=request.json['id']
        row="delete from login where id="+str(id)
        cursor.execute(row)
        connection.commit()
        return jsonify(str(cursor))


@app.route('/update',methods=['POST'])
def update():
    if request.method == 'POST':
        connection, cursor = sql_connection()
        id=request.json['id']
        name = request.json['name']
        emailid = request.json['emailid']
        passwd = request.json['passwd']
        gender = request.json['gender']
        coursename = request.json['coursename']
        row="update login set name=%s ,emailid=%s ,passwd=%s ,gender=%s ,coursename=%s where id=%s"
        cursor.execute(row,(name,emailid,passwd,gender,coursename,id))
        connection.commit()
        return jsonify(str(cursor))


def sql_connection():
    connection = pymysql.connect(host='localhost', user='root', passwd='Luci1108$', db='logindetails')
    cursor = connection.cursor()
    return (connection,cursor)

if __name__=='__main__':
    app.run(debug=True)