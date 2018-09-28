import os
import pandas as pd
import json
from aws_requests_auth.aws_auth import AWSRequestsAuth
from elasticsearch import Elasticsearch, RequestsHttpConnection
import sys

class AWSes:
	def __init__(self,access_key,secret_access_key,host,region,current_index = 1):
		self.host = host
		self.secret_access_key = secret_access_key
		self.access_key = access_key
		self.region = region
		self.user = None
		self.current_index = 0

	def login(self):
		'''
		aws_access_key = 你的AWS IAM Access Key ID
		aws_secret_access_key = 你的AWS IAM Secret Access Key
		host = 你的AWS Elasticsearch domain
		aws_region = 你於AWS所設置的地區
		aws_service = es  ==> 使用AWS Elasticsearch
		'''

		auth = AWSRequestsAuth(aws_access_key = self.access_key,
							   aws_secret_access_key = self.secret_access_key,
							   aws_host = self.host,
							   aws_region = self.region,
							   aws_service = 'es')
		self.user = Elasticsearch(host = self.host,port = 80,connection_class=RequestsHttpConnection,http_auth=auth)
		print("Login Success")

	def create_bulk(self,read_file,write_file):
		'''
		來源為xls格式，產生符合格式之資料檔
		'''

		#讀取原始檔
		df = pd.read_excel(read_file)
		
		#創建寫入暫存檔
		write_to_file = open(write_file,'w')

		#取得欄名
		column_mapping = list(df.columns.values)

		
		for i in range(self.current_index,len(df)):		
			try:

				#以行為單位進行處理
				each_row = df[i:i+1]

				#生成標題格式，分別有_index,_type,_id
				#_index相較於RDBMS的Database，_type等同於RDMBS的Table，current_index則為當前應寫入的id號
				title = {str(col):str(each_row[col].values[0]) for col in column_mapping[:3]}

				#將id換為歷史寫入id，若在原始檔已處理此事項則可略過此行
				title['_id'] = self.current_index

				write_to_file.write(json.dumps({"index":title}))
				#上傳格式要求
				write_to_file.write('\n')

				#產生寫入data格式
				data = {str(col):str(each_row[col].values[0]) for col in column_mapping[3:]}
				write_to_file.write(json.dumps(data))

				#上傳格式要求
				write_to_file.write('\n')

				#寫入一筆，類別變數current_index加1
				self.current_index+=1

			
			except:
				err_type,err_message,err_traceback_object = sys.exc_info()
				print('error類型:{0},\nerror訊息:{1},\n目前寫入到{2}號'.format(err_type,err_message,self.current_index))

		else:
			#原始檔皆以寫入完畢，關閉寫入檔。
			write_to_file.close()	

			#檢查寫入檔是否有成功被寫入，若是則開始上傳
			if(os.stat(write_file).st_size != 0):
				self.bulk_upload(write_file_name)

	def bulk_upload(self,file):
		#批次上傳資料
		with open(file) as f:
			self.user.bulk(body = f.read())

if __name__ == "__main__":
	awses = AWSes(access_key = 'IAM user的 access key id',
				  secret_access_key = 'IAM user的secrect access key',
				  host = 'AWS Elasticsearch domain',
				  region = 'AWS設置地區')

	awses.login()
	awses.create_bulk('欲上傳原始檔目錄位置(須為xlsx檔格式)','暫存檔目錄位置(須為json檔格式)','(欲寫入id之起始位置)')
