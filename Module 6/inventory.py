from flask import Flask,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()


###Model for database
class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    #column with datetime
    expire = db.Column(db.DateTime())

    def __str__(self):
        return f"{self.name}"
    
@app.route('/')
def index():
    return "Hello"

@app.route('/inventory')
def inventory():
    items = Item.query.all()
    output = []
    for item in items:
        item_data = {'name':item.name,'expire':f"{item.expire.month} - {item.expire.day} - {item.expire.year}"}
        output.append(item_data)
    return {'items':output}
@app.route('/load',methods=["GET"])
def load_csv():
    df = pd.read_csv('foods.csv')
    for index,row in df.iterrows():
        dateObj = datetime.strptime(row['expiration date'],"%m-%d-%Y")
        item = Item(name=row['name'],expire=dateObj)
        db.session.add(item)
    db.session.commit()
    return "Done"

if __name__ == "__main__":
    app.run(port=9999,debug=True)