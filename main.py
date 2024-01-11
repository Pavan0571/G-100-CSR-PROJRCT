import datetime
import os
import smtplib
from email.mime.text import MIMEText
from flask import render_template, session, redirect, url_for
import firebase_admin
import random
from flask import Flask, request
from firebase_admin import credentials, firestore
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
app=Flask(__name__)
app.secret_key="CSR_Portal@1234"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = '/static/upload'
sender = "pavan.7031@gmail.com"
password = ""

events=['Environmental Responsibility','Ethical Responsibility',
'Philonthropic Responsibility','Economic Responsibility','Others']
locations=['Bangalore','Mangalore','Mysore','Mumbai', 'Raichur','Davangere', 'Gulbarga' ]

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

@app.route('/')
def homepage():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/adminadddetails')
def adminadddetails():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newcorporate')
        staffdata = newstaff_ref.get()
        data=[]
        for doc in staffdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data " , data)
        return render_template("adminadddetails.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminadddetails1', methods=['POST','GET'])
def adminadddetails1():
    try:
        #userid=session['staffid']
        corporateid = request.args['id']
        db = firestore.client()
        newdb_ref = db.collection('newcorporate')
        data = newdb_ref.document(corporateid).get().to_dict()
        print("Data : ", data)
        return render_template("adminadddetails1.html", data=data)
    except Exception as e:
        return str(e)
        return render_template("adminadddetails1.html", msg=e)


@app.route('/adminadddetails2',methods=["POST","GET"])
def adminadddetails2():
    try:
        msg=""
        if request.method == 'POST':
            print("Add New User page")
            cname = request.form['cname']
            cid = request.form['cid']
            actualprescribed = request.form['actualprescribed']
            prescribedcsr= request.form['prescribedcsr']
            email = request.form['email']
            phnum = request.form['phnum']
            actualcsr = request.form['actualcsr']
            id = str(random.randint(1000, 9999))
            json = {'id': id, 'CorporateId':cid,
                    'CorporateName': cname,
                    'ActualPrescribed': actualprescribed,'PrescribedCsr':prescribedcsr,
                    'EmailId': email,'PhoneNumber':phnum,
                    'ActualCsr': actualcsr}
            db = firestore.client()
            newuser_ref = db.collection('newdetails')
            id = json['id']
            newuser_ref.document(id).set(json)
            msg="New Details Added Success"
            return redirect(url_for("adminadddetails"))
        else:
            return redirect(url_for("adminadddetails"))
    except Exception as e:
        return str(e)

@app.route('/usermainpage')
def usermainpage():
    try:
        return render_template("usermainpage.html")
    except Exception as e:
        return str(e)

@app.route('/index')
def indexpage():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/logout')
def logoutpage():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/about')
def aboutpage():
    try:
        return render_template("about.html")
    except Exception as e:
        return str(e)

@app.route('/logout')
def logout():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/adminmainpage')
def adminmainpage():
    try:
        return render_template("adminmainpage.html")
    except Exception as e:
        return str(e)

@app.route('/services')
def servicespage():
    try:
        return render_template("services.html")
    except Exception as e:
        return str(e)

@app.route('/types')
def typespage():
    try:
        return render_template("types.html")
    except Exception as e:
        return str(e)

@app.route('/environmentpage')
def environmentpage():
    try:
        return render_template("environmentpage.html")
    except Exception as e:
        return str(e)

@app.route('/ethicalpage')
def ethicalpage():
    try:
        return render_template("ethicalpage.html")
    except Exception as e:
        return str(e)

@app.route('/philanthropicpage')
def philanthropicpage():
    try:
        return render_template("philanthropicpage.html")
    except Exception as e:
        return str(e)

@app.route('/economicpage')
def economicpage():
    try:
        return render_template("economicpage.html")
    except Exception as e:
        return str(e)

@app.route('/gallery')
def gallerypage():
    try:
        return render_template("gallery.html")
    except Exception as e:
        return str(e)

@app.route('/adminviewstaffs')
def adminviewstaffspage():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newngo')
        staffdata = newstaff_ref.get()
        data=[]
        for doc in staffdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data " , data)
        return render_template("adminviewstaffs.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewdetails')
def adminviewdetails():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newdetails')
        staffdata = newstaff_ref.get()
        data=[]
        for doc in staffdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data " , data)
        return render_template("adminviewdetails.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewusers')
def adminviewuserspage():
    try:
        db = firestore.client()
        dbref = db.collection('newcorporate')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data ", data)
        return render_template("adminviewusers.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffviewusers')
def staffviewusers():
    try:
        db = firestore.client()
        dbref = db.collection('newcorporate')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data ", data)
        return render_template("staffviewusers.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffaccept_reject')
def staffaccept_reject():
    try:
        db = firestore.client()
        dbref = db.collection('newproject')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data ", data)
        return render_template("staffaccept_reject.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffaccept_reject1', methods=['POST','GET'])
def staffaccept_reject1():
    try:
        id = request.args['id']
        status = request.args['status']
        if(status=='Accept'):
            status='NGO Accepted'
        else:
            status = 'NGO Rejected'
        db = firestore.client()

        data_ref = db.collection(u'newproject').document(id)
        data_ref.update({u'Status': status})

        dbref = db.collection('newproject')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print("Staff Data ", data)
        return render_template("staffaccept_reject.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewcontacts')
def adminviewcontacts():
    try:
        db = firestore.client()
        dbref = db.collection('newcontact')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            print(doc.to_dict())
            print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        print(data)
        return render_template("adminviewcontacts.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/userviewownevents')
def userviewownevents():
    try:
        userid= session['userid']
        db = firestore.client()
        dbref = db.collection('newproject')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if(temp['UserId']==userid):
                data.append(doc.to_dict())
        print(data)
        return render_template("userviewownevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/userviewallevents')
def userviewallevents():
    try:
        userid = session['userid']
        db = firestore.client()
        dbref = db.collection('newevent')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if (temp['UserId'] != userid):
                data.append(doc.to_dict())
        return render_template("userviewallevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewevents')
def adminviewevents():
    try:
        db = firestore.client()
        dbref = db.collection('newevent')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            data.append(doc.to_dict())
        return render_template("adminviewevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffviewevents')
def staffviewevents():
    try:
        db = firestore.client()
        dbref = db.collection('newevent')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            data.append(doc.to_dict())
        return render_template("staffviewevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewreports')
def adminviewreports():
    try:
        #userid = session['userid']
        db = firestore.client()
        dbref = db.collection('newproject')
        dbdata = dbref.get()
        data = []
        for doc in dbdata:
            data.append(doc.to_dict())
        """
        pie_data = []
        for x in events:
            cnt=0
            for doc in dbdata:
                temp = doc.to_dict()
                if(temp['EventType']==x):
                    cnt+=1
            if(cnt>0):
                tempdata = {"label": x, "y": cnt}
                pie_data.append(tempdata)
        """
        #return render_template("adminviewreports.html", data=data, pie_data=pie_data)
        return render_template("adminviewreports.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/userviewreports')
def userviewreports():
    try:
        userid = session['userid']
        db = firestore.client()
        dbref = db.collection('newproject')
        dbdata = dbref.get()
        data = []
        for doc in dbdata:
            if(userid==doc.to_dict()['UserId']):
                data.append(doc.to_dict())
        """
        pie_data = []
        for x in events:
            cnt=0
            for doc in dbdata:
                temp = doc.to_dict()
                if(temp['EventType']==x):
                    cnt+=1
            if(cnt>0):
                tempdata = {"label": x, "y": cnt}
                pie_data.append(tempdata)
        """
        #return render_template("adminviewreports.html", data=data, pie_data=pie_data)
        return render_template("userviewreports.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffviewreports')
def staffviewreports():
    try:
        #userid = session['userid']
        db = firestore.client()
        dbref = db.collection('newresponse')
        dbdata = dbref.get()
        data = []
        for doc in dbdata:
            data.append(doc.to_dict())
        data_points = []
        for x in events:
            cnt=0
            for doc in dbdata:
                temp = doc.to_dict()
                if(temp['EventType']==x):
                    cnt+=1
            if(cnt>0):
                tempdata = {"label": x, "y": cnt}
                data_points.append(tempdata)
        return render_template("staffviewreports.html", data=data, data_points=data_points)
    except Exception as e:
        return str(e)

@app.route('/userviewresponses')
def userviewresponses():
    try:
        #userid = session['userid']
        id=request.args['id']
        db = firestore.client()
        dbref = db.collection('newresponse')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if (temp['EventId'] == id):
                data.append(doc.to_dict())
        return render_template("userviewresponses.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewresponses')
def adminviewresponses():
    try:
        #userid = session['userid']
        id=request.args['id']
        db = firestore.client()
        dbref = db.collection('newresponse')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if (temp['EventId'] == id):
                data.append(doc.to_dict())
        return render_template("adminviewresponses.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffviewresponses')
def staffviewresponses():
    try:
        #userid = session['userid']
        id=request.args['id']
        db = firestore.client()
        dbref = db.collection('newresponse')
        userdata = dbref.get()
        data = []
        for doc in userdata:
            temp = doc.to_dict()
            if (temp['EventId'] == id):
                data.append(doc.to_dict())
        return render_template("staffviewresponses.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminlogin',methods=["POST","GET"])
def adminloginpage():
    try:
        print('hi')
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            if uname == "govt" and pwd == "govt":
                return render_template("adminmainpage.html")
            else:
                return render_template("adminlogin.html", msg="UserName/Password is Invalid")
        return render_template("adminlogin.html",msg="")
    except Exception as e:
        return str(e)

@app.route('/userlogincheck', methods=['POST'])
def userlogincheck():
    try:
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            db = firestore.client()
            print("Uname : ", uname, " Pwd : ", pwd);
            newdb_ref = db.collection('newuser')
            dbdata = newdb_ref.get()
            data = []
            flag = False
            for doc in dbdata:
                #print(doc.to_dict())
                #print(f'{doc.id} => {doc.to_dict()}')
                #data.append(doc.to_dict())
                data = doc.to_dict()
                if(data['UserName']==uname and data['Password']==pwd):
                    flag=True
                    session['userid']=data['id']
                    break
            if(flag):
                print("Login Success")
                return render_template("usermainpage.html")
            else:
                return render_template("userlogin.html", msg="UserName/Password is Invalid")
    except Exception as e:
        return render_template("userlogin.html", msg=e)

@app.route('/stafflogincheck', methods=['POST'])
def stafflogincheck():
    try:
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            db = firestore.client()
            print("Uname : ", uname, " Pwd : ", pwd);
            newdb_ref = db.collection('newngo')
            dbdata = newdb_ref.get()
            data = []
            flag = False
            for doc in dbdata:
                data = doc.to_dict()
                if(data['UserName']==uname and data['Password']==pwd):
                    flag=True
                    session['userid']=data['id']
                    break
            if(flag):
                print("Login Success")
                return render_template("staffmainpage.html")
            else:
                return render_template("stafflogin.html", msg="UserName/Password is Invalid")
    except Exception as e:
        return render_template("stafflogin.html", msg=e)

@app.route('/userlogin',methods=["POST","GET"])
def userloginpage():
    try:
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            db = firestore.client()
            newdb_ref = db.collection('newcorporate')
            dbdata = newdb_ref.get()
            flag = False
            for doc in dbdata:
                data = doc.to_dict()
                if (data['UserName'] == uname and data['Password'] == pwd):
                    flag = True
                    session['userid'] = data['id']
                    break
            if (flag):
                print("Login Success")
                return render_template("usermainpage.html")
            else:
                return render_template("userlogin.html", msg="UserName/Password is Invalid")
        return render_template("userlogin.html")
    except Exception as e:
        return str(e)

@app.route('/stafflogin',methods=["POST","GET"])
def staffloginpage():
    try:
        return render_template("stafflogin.html")
    except Exception as e:
        return str(e)

@app.route('/newuser',methods=["POST","GET"])
def newuser():
    try:
        msg=""
        if request.method == 'POST':
            print("Add New User page")
            cname = request.form['cname']
            #lname = request.form['lname']
            uname = request.form['uname']
            pwd = request.form['pwd']
            email = request.form['email']
            phnum = request.form['phnum']
            address = request.form['address']
            id = str(random.randint(1000, 9999))
            json = {'id': id,
                    'CorporateName': cname,
                    'UserName': uname,'Password':pwd,
                    'EmailId': email,'PhoneNumber':phnum,
                    'Address': address}
            db = firestore.client()
            newuser_ref = db.collection('newcorporate')
            id = json['id']
            newuser_ref.document(id).set(json)
            msg="New Corporate Added Success"
            return render_template("newuser.html", msg=msg)
        else:
            return render_template("newuser.html", msg=msg)
    except Exception as e:
        return str(e)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/newstaff', methods=['POST',"GET"])
def newstaff():
    try:
        msg=""
        return render_template("adminaddstaff.html", msg=msg)
    except Exception as e:
        return str(e)

@app.route('/adminaddstaff', methods=['POST',"GET"])
def adminaddstaff():
    try:
        msg=""
        if request.method == 'POST':
            print("Add New Staff page")
            nname = request.form['nname']
            #lname = request.form['lname']
            uname = request.form['uname']
            pwd = request.form['pwd']
            email = request.form['email']
            phnum = request.form['phnum']
            address = request.form['address']
            id = str(random.randint(1000, 9999))
            json = {'id': id,
                    'NGOName': nname,
                    'UserName': uname,'Password':pwd,
                    'EmailId': email,'PhoneNumber':phnum,
                    'Address': address}
            db = firestore.client()
            newuser_ref = db.collection('newngo')
            id = json['id']
            newuser_ref.document(id).set(json)
            msg="New NGO Added Success"
            return render_template("adminaddstaff.html", msg=msg)
        else:
            return render_template("adminaddstaff.html", msg=msg)
    except Exception as e:
        return str(e)

@app.route('/userapplyresponse', methods=['POST',"GET"])
def userapplyresponse():
    try:
        id=request.args['id']
        print("Id",id)
        db = firestore.client()
        newdb_ref = db.collection('newevent')
        data = newdb_ref.document(id).get().to_dict()
        return render_template("userapplyresponse.html", data=data)
    except Exception as e:
        return str(e)
        return render_template("userapplyresponse.html", msg=e)

@app.route('/userapplyresponse1', methods=['POST',"GET"])
def userapplyresponse1():
    try:
        msg=""
        if request.method == 'POST':
            print("Add Response to a Event page")
            eid = request.form['eid']
            ename = request.form['ename']
            etype = request.form['etype']
            location = request.form['location']
            description = request.form['description']
            email = request.form['email']
            phnum = request.form['phnum']
            edate = request.form['edate']
            userid = session['userid']
            comments = request.form['comments']

            id = str(random.randint(1000, 9999))
            json = {'id': id, 'EventId':eid,
                    'EventName': ename,'EventType':etype,
                    'Description': description,'Location':location,
                    'ContactEmailId': email,'ContactPhoneNumber':phnum,
                    'UserId': userid,'EventDate':edate, 'Comments':comments}
            db = firestore.client()
            newdb_ref = db.collection('newresponse')
            id = json['id']
            newdb_ref.document(id).set(json)
            print("Add New Response Added")
            userid = session['userid']
            newdb_ref = db.collection('newcorporate')
            data = newdb_ref.document(userid).get().to_dict()
            subject="Event Notification"
            fname = data['FirstName']
            lname = data['LastName']
            body = "A User "+fname + " " + lname + " sent a response please login & check"
            recipients = []
            recipients.append(email)
            print(recipients)
            send_email(subject, body, sender, recipients, password)
            msg="New Response to a Event Added Success"
            db = firestore.client()
            newdb_ref = db.collection('newevent')
            data = newdb_ref.document(eid).get().to_dict()
            return render_template("userapplyresponse.html", data=data, msg=msg)
        else:
            return render_template("userapplyresponse.html", msg=msg)
    except Exception as e:
        return str(e)

@app.route('/useraddevents', methods=['POST',"GET"])
def useraddevents():
    try:
        msg=""
        current_date = datetime.date.today()
        if request.method == 'POST':
            print("Add New Project page")
            pname = request.form['pname']
            numofprojects = request.form['numofprojects']
            numofcompanies = request.form['numofcompanies']
            amountspent = request.form['amountspent']
            percentage = request.form['percentage']
            userid = session['userid']
            print("Add New Event page")
            id = str(random.randint(1000, 9999))
            json = {'id': id, 'UserId':userid,
                    'ProjectName': pname,'NumOfProjects':numofprojects,
                    'NumOfCompanies': numofcompanies,'AmountSpent':amountspent, 'Percentage':percentage,
                    'UserId': userid,'Status':'Created'}
            db = firestore.client()
            newdb_ref = db.collection('newproject')
            id = json['id']
            newdb_ref.document(id).set(json)
            msg="New CSR Added Success"
            return render_template("useraddevents.html", msg=msg)
        else:
            return render_template("useraddevents.html", msg=msg)
    except Exception as e:
        return str(e)

@app.route('/contact',methods=['POST','GET'])
def contactpage():
    try:
        msg=""
        if request.method == 'POST':
            cname = request.form['cname']
            email = request.form['emailid']
            subject = request.form['subject']
            message = request.form['message']
            phone = request.form['phnum']
            id = str(random.randint(1000, 9999))
            json = {'id': id,
                    'ContactName': cname,
                    'Message': message, 'Subject': subject,
                    'EmailId': email, 'PhoneNumber':phone}
            db = firestore.client()
            db_ref = db.collection('newcontact')
            id = json['id']
            db_ref.document(id).set(json)
            msg="Contact Added Success"
        return render_template("contact.html",msg=msg)
    except Exception as e:
        return str(e)

@app.route('/userviewprofile')
def userviewprofile():
    try:
        id=session['userid']
        print("Id",id)
        db = firestore.client()
        newdb_ref = db.collection('newcorporate')
        data = newdb_ref.document(id).get().to_dict()
        return render_template("userviewprofile.html", data=data)
    except Exception as e:
        return str(e)
        return render_template("userviewprofile.html", msg=e)

@app.route('/staffviewprofile')
def staffviewprofile():
    try:
        id=session['userid']
        print("Id",id)
        db = firestore.client()
        newdb_ref = db.collection('newngo')
        data = newdb_ref.document(id).get().to_dict()
        print(data)
        return render_template("staffviewprofile.html", data=data)
    except Exception as e:
        return str(e)
        return render_template("stafflogin.html", msg=e)

if __name__ == '__main__':
    app.run(debug=True)