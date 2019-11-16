from flask import Flask, render_template, request
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  passwd="root",
  auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()
mycursor.execute("use mydocuments;")
app = Flask(__name__)

@app.route("/")
def webapp():
    return render_template('webpage.html')

@app.route("/", methods=['POST'])
def formInput():
	student=request.form['students']
	options=[]
	keys=request.form.keys()
	keys=list(keys)
	if 'option1' in keys:
		option1=request.form['option1']
		options.append(option1)
	if 'option2' in keys:
		option2=request.form['option2']
		options.append(option2)
	if 'option3' in keys:
		option3=request.form['option3']
		options.append(option3)
	if 'option4' in keys:
		option4=request.form['option4']
		options.append(option4)
	print(options)
	# import pdb; pdb.set_trace()
	# return render_template('result.html')
	dataFetch(student, options)
def dataFetch(student, options):
	import pdb; pdb.set_trace()
	str=""
	for i in options:
		str=str+i+" "
	print(str)
	temp="SELECT"+" "+str+"FROM"+" "+"student_details"+" "+"where"+" "+"SName="+"\""+student+"\""
	mycursor.execute(temp)
	myresult= mycursor.fetchall()
	for x in myresult:
		print(x)
	# return render_template('result.html')

if __name__ == "__main__":
	app.run(debug=True,host="127.0.0.1", port=9999)


