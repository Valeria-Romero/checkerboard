from flask import Flask
from flask import render_template

app = Flask( __name__ )

@app.route('/', methods=['GET'])
def loadHome():
    return render_template('index.html', row=8,col=8,color1='black',color2='red')

@app.route('/4', methods=['GET'])
def loadfourbyfour():
    return render_template('index.html', row=4,col=8,color1='black',color2='red')

@app.route('/<row>/<col>', methods=['GET'])
def loadbynumber(row,col):
    row = int(row)
    col = int(row)
    return render_template('index.html', row=row, col=col, color1='black', color2='red')

@app.route('/<row>/<col>/<color1>/<color2>', methods=['GET'])
def loadbycolor(row,col,color1, color2):
    color1 = str(color1)
    color2 = str(color2)
    row = int(row)
    col = int(row)
    return render_template('index.html', row=row, col=col, color1=color1, color2=color2)



if __name__ == "__main__":
    app.run( debug = True )