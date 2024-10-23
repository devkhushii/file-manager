from flask import Flask ,request, render_template, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
       
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY']='this-is-api-key'

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
  
    if request.method=='POST':
       
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"})
        
        if file :
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return jsonify({"message": "File uploaded successfully", "file": filename})
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)