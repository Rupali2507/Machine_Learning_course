
'''
in jinja2 template engine
{{ }} expressions to print output in html

{%...%} conditions, for loops
{#...#} this is for comments

'''


from flask import Flask,render_template,request,url_for, redirect
### WSGI application
app=Flask(__name__) 


@app.route("/")
def welcome():
  return "<html><H1>welcome to the this  course.This is an amazing course</H1></html>"


@app.route("/index",methods=['GET'])
def index():
  return render_template('index.html')

@app.route("/about")
def about():
  return render_template('about.html')



@app.route("/submitt",methods=['GET','POST'])
def submitt():
  if request.method=='POST':
    name=request.form['name']
    return f'Hello {name}'
  return render_template('form.html')

# variable rule
@app.route("/success/<int:score>")
def success(score):
  res=''
  if score>=50:
    res="PASSED"
  else:
    res="FAILED"
  return render_template('result.html',results=res)    


@app.route("/success_res/<int:score>")
def success_res(score):
  res=''
  if score>=50:
    res="PASSED"
  else:
    res="FAILED"

  exp={'score':score, "res":res}  
  return render_template('res_1.html',results=exp) 

@app.route("/successif/<int:score>")
def successif(score):
  
 
  return render_template('result.html',results=score) 

# variable rule
@app.route("/fail/<int:score>")
def fail(score):
 
  return render_template('result.html',results=score)  

@app.route('/submit', methods=['POST','GET'])
def submit():
  total_score =0
  if request.method=='POST':
    science = float(request.form['science'])
    maths = float(request.form['maths'])
    c=float(request.form['c'])
    data_science=float(request.form['datascience'])

    total_score=(science + maths + c+ data_science)/4
  return redirect(url_for('success_res',score=total_score))  
 



if __name__ == "__main__":
  app.run(debug=True)