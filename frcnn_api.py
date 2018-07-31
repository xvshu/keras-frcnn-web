from flask import Flask, jsonify, abort, make_response, request, url_for,render_template
from flask_httpauth import HTTPBasicAuth
import test_frcnn
import os
from werkzeug.utils import secure_filename
import cv2
from scipy import misc

app = Flask(__name__)
# 图片最大为16M
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
auth = HTTPBasicAuth()

#设置post请求中获取的图片保存的路径
UPLOAD_FOLDER = 'pic_tmp/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
else:
    pass
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template("img_fit.html")

@app.route('/img/fit', methods=['POST'])
def face_insert():
    #分别获取post请求中的图片信息
    upload_files = request.files['imagefile']
    #从post请求图片保存到本地路径中
    file = upload_files
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print(image_path)
    img = cv2.imread(os.path.expanduser(image_path))
    # img = misc.imread(os.path.expanduser(image_path), mode='RGB')

    return test_frcnn.tf_fit_img(img)


@auth.get_password
def get_password(username):
    if username == 'root':
        return 'root'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Invalid data!'}), 400)

if __name__ == '__main__':
    app.run(host='172.30.53.250', port=8099)

