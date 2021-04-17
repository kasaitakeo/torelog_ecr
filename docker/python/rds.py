import pymysql
import os
Database_endpoint = os.environ['torelog-web.cf88yvjgeanm.ap-northeast-1.rds.amazonaws.com']
Username = os.environ['root']
Password = os.environ['take0928']
try:
    print("Connecting to "+Database_endpoint)
    db = pymysql.connect(Database_endpoint,Username,Password)
    print ("Connection successful to "+Database_endpoint)
except Exception as e:
    print ("Connection unsuccessful due to "+str(e))