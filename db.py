import pymysql

def conexionDB():
	return pymysql.connect(host='localhost',
							user='root',
							password='',
							db='dbflask')
	