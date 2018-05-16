from flask import Flask, request, render_template,jsonify
from flask_pymongo import PyMongo
import os,json
from flask_caching import Cache


app=Flask(__name__)

#Using MongoDb Service provider Mlab free sandbox
app.config['MONGO_DBNAME']='dbname'
app.config['MONGO_URI']='mongodb://username:password@ds139262.mlab.com:39262/database'

#Initialize cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

mongo = PyMongo(app)


@app.route('/')
def home_page():
    data= list(mongo.db.census.find().limit(100))
    return render_template('index.html',data=data)

@app.route('/gender')
def getMaleFemaleCount():
    result= list(mongo.db.census.aggregate([{"$group":{"_id":"$sex","count":{"$sum":1}}}]))
    countResult= {}
    for res in result:
        countResult[res.get('_id')] = res.get('count')
    return jsonify(json.dumps(countResult))

@app.route('/relationship')
def getRelationshipCount():
    result= list(mongo.db.census.aggregate([{"$group":{"_id":"$relationship","count":{"$sum":1}}}]))
    countResult= {}
    for res in result:
        countResult[res.get('_id')] = res.get('count')
    return jsonify(json.dumps(countResult))

    
    
    
    
#This fucntion get all data from data base and save it
#In a cache 
# @cache.cached(timeout=50, key_prefix='censusData')
# def getFullData():
#     data= list(mongo.db.census.find().limit(5))
#     return data
    
# app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

port = int(os.environ.get('PORT', 5000))
app.run(host="0.0.0.0", port=port, debug=True)