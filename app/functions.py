import os
import psycopg2
from bottle import request
from beaker.middleware import SessionMiddleware
import urllib, hashlib

def test_connection(sql_query, user, password):
	cur = None
	connstring = 'dbname=db_backup host=172.22.200.110 user=%s password=%s' %(user, password)
	connect = psycopg2.connect(connstring)
	print sql_query
	try:
		cur = connect.cursor()
		cur.execute(sql_query)
		resultado = cur.fetchall()
	except:
		return false
	finally:
		if cur is not None:
			cur.close()
	return resultado

def selectall(sql_query, v_user, v_password):
	cur = None
	connstring = 'dbname=db_backup host=172.22.200.110 user=%s password=%s' %(v_user, v_password)
	connect = psycopg2.connect(connstring)
	print sql_query
	try:
		cur = connect.cursor()
		cur.execute(sql_query)
		resultado = cur.fetchall()
	except:
		return false
	finally:
		if cur is not None:
			cur.close()
	return resultado

def database_select(sql_query, v_user, v_password):
	cur = None
	connstring = 'dbname=db_backup host=172.22.200.110 user=%s password=%s' %(v_user, v_password)
	connect = psycopg2.connect(connstring)
	print sql_query
	try:
		cur = connect.cursor()
		cur.execute(sql_query)
		resultado = cur.fetchone()
	except:
		return false
	finally:
		if cur is not None:
			cur.close()
	return resultado

#def database_insert(sql_query):
#	cur = None
#	print sql_query
#	try:
#		cur = conn.cursor()
#		cur.execute(sql_query)
#		resultado = cur.statusmessage
#		conn.commit()
#	except Exception , e:
#		print 'ERROR:', e[0]
#		if cur is not None:
#			conn.rollback()
#	finally:
#		if cur is not None:
#			cur.close()#
#    return cur.statusmessage
def miniavatar(v_user, v_password):
	sql_query="select user_email from users where user_user = '%s'" %(v_user)
	consulta=database_select(sql_query, v_user, v_password)
	email=consulta[0]
	if email is not None:
		default = "default.jpg"
 		size = 512
 		gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
 		gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
		return gravatar_url
	else:
		return 


def set(key,value):
	s = request.environ.get('beaker.session')

	s[key]=value

def get(key):
	s = request.environ.get('beaker.session')

	if key in s:
		return s[key]
	else:
		return ""
