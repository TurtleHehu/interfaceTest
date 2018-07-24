import pymysql
import readConfig as readConfig
from common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()


class MyDB():
	global host, username, password, port, database, config
	host = localReadConfig.get_db("host")
	username = localReadConfig.get_db("username")
	password = localReadConfig.get_db("password")
	port = localReadConfig.get_db("port")
	database = localReadConfig("database")
	config = {
		'host': str(host),
		'user': str(username),
		'passwd': str(password),
		'port': int(port),
		'db': database
	}
	
	
	def __init__(self):
		self.log = Log.get_log()
		self.logger = self.log.get_logger()
		self.db = None
		self.cursor = None
	
	def connectDB(self):
		try:
			self.db = pymysql.connect(**config)
			self.cursor = self.db.cursor()
			print("Connect DB successfully!")
		except Exception as ex:
			self.logger.error(str(ex))
	
	def executeSQL(self,sql,params):
		self.connectDB()
		self.cursor.execute(sql,params)
		self.db.commit()
		return self.cursor
		
	def get_all(self,cursor):
		value = cursor.fetchall()
		return value
		
	def get_one(self,cursor):
		value = cursor.fetchone()
		return value