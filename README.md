# keras-frcnn-web

利用keras建立 faster rcnn网络，训练完成后，将检测api释放为rest接口，方便后端调用

# linux 环境搭建
(''')
  1. wget  https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz
  2. tar Jxvf  Python-3.5.2.tar.xz
  3. cd Python-3.5.2
  4. ./configure --prefix=/usr/local/python3
  5. make && make install  # 成功提示：Ignoring ensurepip failure: pip 7.1.2 requires SSL/TLS
  6. ln -s /usr/local/python3/bin/pip3.5 /usr/local/bin/pip3.5
  7. ln -s /usr/local/python3/bin/python3.5 /usr/local/bin/python3
  8. pip3.5 install --upgrade pip
  9. pip3.5 install keras
  10. pip3.5 install  tensorflow
  11. pip3.5 install flask
  12. pip3.5 install  flask_httpauth
  13. pip3.5 install  werkzeug
  14.pip install opencv-python
(''')

# 数据集格式

数据集为VOC2007，数据格式如下：

顶层目录

Annotations —目标真值区域

ImageSets —-类别标签

JPEGImages —–图像


生成数据集，可参考博客

https://blog.csdn.net/xvshu/article/details/81298625

# 训练命令

  >python train_frcnn.py -p $your_train_voc2007_path


# 测试命令

  >python test_frcnn.py -p $your_test_img_path


测试结果：
<img src="https://github.com/xvshu/keras-frcnn-web/blob/master/doc/img-fit.jpg" >


# 发布api命令

  >python frcnn_api.py


# 测试页面
## 传入图片
<img src="https://github.com/xvshu/keras-frcnn-web/blob/master/doc/mian_web.jpg" >


## 检测结果
<img src="https://github.com/xvshu/keras-frcnn-web/blob/master/doc/fit_web.jpg" >



