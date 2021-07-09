import requests
import json
import time



def loadData():

	print("Load Json save file")

	# 읽기
	with open('./save.json', 'r') as f:

		json_data = json.load(f)


	return json_data


def saveData(arg_json_data):

	# 쓰기
	with open('./save.json', 'w', encoding='utf-8') as f:

		arg_json_data = json.dump(arg_json_data, f, indent=2)

	f.close()


def loggingURL(URL):


	with open('./ApacheServerURL.txt', 'a', encoding='utf-8') as f:

		f.write(URL+'\n')

	f.close()


def scanServer(arg_ip):

	URL = 'http://'+arg_ip

	print('scanning Apache server at ', URL)

	try:

		response = requests.get(url = URL, timeout = 1.2)

		if ( "Apache" in response.headers['Server'] ):

			print("\n**** FOUND Apache Server! ****")
			print("URL : "+ URL)
			print("******************************\n")
		
			loggingURL(URL)

	except:

		a=1






if __name__ == '__main__':

	json_data = loadData()

	print(json_data)

	time.sleep(2)

	
	for A in range(json_data['A'], 256):

		for B in range(json_data['B'], 256):

			for C in range(json_data['C'], 256):

				for D in range(json_data['D'], 256):

					json_data['A'] = A
					json_data['B'] = B
					json_data['C'] = C
					json_data['D'] = D

					saveData(json_data)

					print('Target >> ', A,".",B,".",C,".",D ,sep='')

					ip = str(A)+"."+str(B)+"."+str(C)+"."+str(D)

					scanServer(ip)
	