import os

# Title : Ukiyo Setup
# Date : 31/12/2021
# Author : https://github.com/1x12

if os.name == "posix":
	os.system('python3 -m pip install -U colorama\n')
	os.system('python3 -m pip install -U requests\n')
	os.system('python3 -m pip install -U psutil\n')
	os.system('python3 -m pip install -U lxml\n')
elif os.name == "nt":
	os.system('py -3 -m pip install -U colorama\n')
	os.system('py -3 -m pip install -U requests\n')
	os.system('py -3 -m pip install -U psutil\n')
	os.system('py -3 -m pip install -U lxml')
else:
	print("Unsupported operating system.")
