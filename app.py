from flask import Flask,render_template,request
import pickle
from sklearn.linear_model import LinearRegression




app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])

def predict():
    if request.method =='POST':
        tv=request.form['TV']
        newspaper=request.form['newspaper']
        radio=request.form['radio'] 

        data=[[float(tv),float(newspaper),float(radio)]]
        lr=pickle.load(open('advertising.pkl','rb'))
        prediction=lr.predict(data)[0]
    return render_template('index.html',prediction=prediction)





if __name__=='__main__':
    app.run()





# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()

#AUTHOR:p.Pavan