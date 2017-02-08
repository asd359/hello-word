#coding:utf-8
import  os
class socket_info:
	def socket_info(self,df):
		head_data = {}
		head_data["get_file_server"] = "127.1.1.1"
		head_data["get_file_port"] = 8001
		return head_data

	def file_info(self,file="C:\\Users\\rick\\Downloads\\pip-1.0.2.tar.gz"):
		file_path = file
		file_name_list = file_path.rsplit(os.sep,1)
		# print file_name_list
		# print  len(file_name_list)
		if len(file_name_list)>1:
			file_name = file_name_list[-1]
		else:
			file_name = file_path
		# print file_name
		file_size = os.path.getsize(file_path)


		head_data = {}
		# head_data["file_path"] = file
		head_data["file_name"]=file_name
		head_data["file_size"]=file_size
		# head_data["date"]=time.strftime("%b %d %Y %H:%M:%S",time.localtime())
		head_data["charset"]='utf-8'

		return head_data



	def get_info(self,file = "C:\\Users\\rick\\Downloads\\pip-1.0.2.tar.gz" ):
		return self.file_info(file)



# a =socket_info()
# print a.get_info()