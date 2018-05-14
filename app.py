from flask import Flask, request, render_template
from flask_pymongo import PyMongo


app=Flask(__name__)

#Using MongoDb Service provider Mlab free sandbox
app.config['MONGO_DBNAME']='Your_DB_NAME'
app.config['MONGO_URI']='Yout_MLAB_URI'


mongo = PyMongo(app)


@app.route('/')
def home_page():
    male_count = mongo.db.census.find({'sex':'Male'}).count()
    female_count=mongo.db.census.find({'sex':'Female'}).count()
    return render_template('index.html',
        male_count=male_count,female_count=female_count)

if __name__ == '__main__':
   app.run()