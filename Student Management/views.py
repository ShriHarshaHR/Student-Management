from flask import Flask,render_template,redirect,request
import pymysql as py
app=Flask(__name__)
@app.route('/')
def display():
    try:
        db=py.Connect(host='localhost',user='root',password='',database='shriharsha')
        cur=db.cursor()
        sqq='select * from login'
        cur.execute(sqq)
        data=cur.fetchall()
    except Exception as e:
        print('Error:',e)    
    return render_template('dashboard.html',data=data)

@app.route('/create')
def create():
    return render_template('form.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')


@app.route('/edit/<rid>')
def edit(rid):
    try:
        db=py.Connect(host='localhost',user='root',password='',database='shriharsha')
        cur=db.cursor()
        sq3="select * from login where id='{}'".format(rid)
        cur.execute(sq3)
        data=cur.fetchall()
        return render_template('editform.html',data=data)
    except Exception as e:
        print('Error',e)
    
        
@app.route('/store',methods=['POST'])
def store():
    N=request.form['Name']
    Cou=request.form['Course']
    Ag=request.form['Age']
    date=request.form['date']
    Phno=request.form['Phno']

    try:
        db=py.Connect(host='localhost',user='root',password='',database='shriharsha')
        cur=db.cursor()
        qu='insert into login(Name,Course,Age,date,Phno) values("{}","{}","{}","{}","{}")'.format(N,Cou,Ag,date,Phno)
        cur.execute(qu)
        db.commit()
    except Exception as e:
        print('FAILED to INSERT',e)
    return redirect('/')

@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    N=request.form['Name']
    Cou=request.form['Course']
    Ag=request.form['Age']
    date=request.form['date']
    Phno=request.form['Phno']
    try:
        db=py.Connect(host='localhost',user='root',password='',database='shriharsha')
        cur=db.cursor()
        sq2="update login set Name='{}',Course='{}',Age='{}',date='{}',Phno='{}' WHERE id='{}'".format(N,Cou,Ag,date,Phno,rid)
        cur.execute(sq2)
        db.commit()
    except Exception as e:
        print('Failed to update',e)
    return redirect('/')

    
@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=py.Connect(host='localhost',user='root',password='',database='shriharsha')
        cur=db.cursor()
        sq1="delete from login where id='{}'".format(rid)
        cur.execute(sq1)
        data=cur.fetchall()
        db.commit()
        return redirect('/')
    except Exception as e:
        print('Error',e)
    
app.run(debug=True)
 
