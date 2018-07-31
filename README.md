# keras-frcnn-web
利用keras建立 faster rcnn网络，训练完成后，将检测api释放为rest接口，方便后端调用

# 数据集格式
数据集为VOC2007，数据格式如下：
顶层目录
Annotations —目标真值区域
ImageSets —-类别标签
JPEGImages —–图像

生成数据集，可参考博客
https://blog.csdn.net/xvshu/article/details/81298625

# 训练命令
python train_frcnn.py -p $your_train_voc2007_path

# 测试命令
python test_frcnn.py -p $your_test_img_path

测试结果：


# 发布api命令
python frcnn_api.py

# 测试页面
## 传入图片
## 检测结果

