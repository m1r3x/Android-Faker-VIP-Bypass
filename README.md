
## Requirements:
- Rooted Android device
- Android Faker latest version
- PC (tested on Windows)
- Python
- Proxy app (tested on Burpsuite)


## Instructions:

### On PC:
1. Run:
	- pip install flask
	- python .\server.py 
	- password: 1234

2. Edit hosts file on the PC like this:
\<your local ip\>	android1500.com

3. Enable the proxy app on all interfaces. On Burpsuite, after enabling all interfaces, go to Options > Miscellaneous, and enable the HTTP/1.0 fields

### On android:
1. Connect the phone to the PC proxy (using tools such as ProxyDroid)

2. Start the app, tap on 3 dots > User info > Refresh

3. Enjoy the VIP features :D