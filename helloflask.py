from flask import Flask
from flask import request
from flask import render_template
import logging
from MongoTrack import Track
from mongoengine import connect
from datetime import datetime

connect('SimpleTracking')

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
	text = request.form.get('theurl')
	app.logger.info(text)
	return render_template('home.html')

@app.route('/about',methods=['GET', 'POST'])
def about():
	text = request.form.get('theurl')
	app.logger.info(text)
	return render_template('about.html')

@app.route('/track')
def track():
	theurl= request.args.get('theurl')
	t=Track(URL=theurl,Track_date=datetime.now())
	t.save()
	return t.my_time

@app.route('/Status',methods=['GET', 'POST'])
def status():
	text = request.form.get('theurl')
	app.logger.info(text)
	tracking = Track.objects()
	trackcount = Track.objects.count()
	return render_template('status.html',tracking=tracking,trackcount=trackcount)

if __name__ == '__main__':
    app.run(debug=True)