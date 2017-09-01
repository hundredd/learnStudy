#coding:utf-8


from sklearn import linear_model

# 线性回归
clf = linear_model.LinearRegression()
# 训练
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
# 表达式参数
clf.coef_

# 测试
import numpy as np
x = np.array([1, 1])
y = x.dot(clf.coef_)
print 'x:%s,y:%s'%(x,y)

# from  sklearn.linear_model import  LinearRegression
# from  sklearn.datasets import  load_boston
#
# # 加载数据
# boston_data = load_boston()
# print boston_data
# print getattr(boston_data)
# x = boston_data['data']
# y = boston_data['target']
#
# model = LinearRegression()
# model.fit(x,y)
#
# # Make a prediction using the model
# sample_house = [[2.2969000e-01,0.000000e+00,1.069000000e+01,0.000000e+00,4.89000000e-01,
#                  6.32600000e+00,5.2500000e+01,4.3549000e+00,4.000000000e+00,2.7700000e+02,
#                  1.86000000e+01,3.94870000e+02,1.097000000e+01]]
#
# showData = [[10,20,10,20,10,20,10,20]]
#
# # Toto:Predict()
# prediction = model.predict(showData)