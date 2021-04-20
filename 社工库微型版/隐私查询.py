from flask import Flask ,render_template,request
import os,sqlite3
app = Flask(__name__)
@app.route('/i', methods=['GET', 'POST'])
def insertuser():
    if request.method == 'POST':
        conn=sqlite3.connect('user.db')
        cursor=conn.cursor()
        cursor.execute('select  *  from  user')
        a=cursor.fetchall()
        id1=len(a)+1
        name=request.form['name']
        age=request.form['age']
        sex=request.form['sex']
        homeaddress=request.form['homeaddress']
        QQ=request.form['QQ']
        IDcard=request.form['IDcard']
        school=request.form['school']
        xueli=request.form['xueli']
        wechat=request.form['wechat']
        telegram=request.form['telegram']
        work=request.form['work']
        fanzui=request.form['fanzui']
        relatives=request.form['relatives']
        phonenumber=request.form['phonenumber']
        #xueli=request.form['xueli']
        conn=sqlite3.connect('user.db')
        cursor=conn.cursor()
        data=(str(id1),name,age,sex,homeaddress,QQ,wechat,telegram,work,fanzui,relatives,phonenumber,xueli,school,IDcard)
        isql='insert  into  user(id,name,age,sex,homeaddress,QQ,wechat,telegram,work,fanzui,relatives,phonenumber,xueli,school,IDcard)values'
        isql=isql+str(data)
        try:
            cursor.execute(isql)
        except:
            return "字段不合法"
        
        cursor.close()
        conn.commit()
        conn.close()
        return render_template("insert.html")
    else:
        return render_template("insert.html")
@app.errorhandler(404)
def page_not_found(e):
    return  render_template('404.html'),404
@app.errorhandler(500)
def page_wrong(e):
    return  render_template('500.html'),500
@app.route('/s', methods=['GET', 'POST'])
def selectuser():
    if request.method == 'POST':
        conn=sqlite3.connect('user.db')
        cursor=conn.cursor()
        s=request.form['s']
        text=request.form['text']
        sql="select  *  from  user  where  "+s+'="'+text+'"'
        print(sql)
        cursor.execute(sql)
        result=cursor.fetchall()
        if len(result)!=0:
            return render_template("select.html",rec=result)
        else:
            return "没有相关数据"
        cursor.close()
        conn.close()
    else:
        return render_template("select.html")
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=443,ssl_context=('server.crt','server.key'))
