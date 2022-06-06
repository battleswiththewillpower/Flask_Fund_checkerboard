from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')
def level_one():

    return render_template("index.html", num = 3,color1 = "purple", color2 = "aquamarine")

@app.route('/x/<int:num>/<color1>/<color2>')          
def board_two(num, color1, color2):
    return render_template("index.html",num=num,color1=color1,color2=color2)

@app.route('/x/<int:num>')
def add_row(num):
    return render_template("index.html", num = num, color1 = "purple", color2 = "aquamarine")









if __name__=="__main__":      
    app.run(debug=True)    

