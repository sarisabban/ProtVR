# Author: Sari Sabban
# Email:  sari.sabban@gmail.com
# URL:    https://github.com/sarisabban
#
# Created By:   	Sari Sabban
# Created Date: 	20 March 2017

from ProtVR import ProtVR
from flask import *
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST':
		global protein
		protein=request.form.get('something')
		return redirect(url_for('result'))
	return(render_template('index.html'))

@app.route('/result')
def result():
	return(ProtVR(protein))

@app.route('/sitemap.xml')
def static_from_root():
    return(send_from_directory(app.static_folder, request.path[1:]))

if __name__ == '__main__':
	app.run(debug=True)
