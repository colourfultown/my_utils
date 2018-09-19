#coding:utf-8
'''
 author:dabo
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def the_current_time():
	"""
	调用函数，打印当前时间
	:return:
	"""
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
