# from twilio.rest import Client
# from secret import accountSID, authToken, myNumber, herNumber

# twilioCli = Client(accountSID, authToken)
# message = twilioCli.messages.create(body="Amy, it's Paul, scream to me if you got this text", from_=myNumber, to=herNumber)

# # Enabling the GMAIL API. After activating, token.json comes into directory
# import ezgmail, os
# os.chdir(r'C:/path/to/credentials_json_file')

# ezgmail.init()


# To send app link each morning when app is called
def send_link(url):
	import ezgmail
	ezgmail.send('7326162029@vtext.com','', f'Fill form for nanny: {url}')

# Create public URL for localhost:5000 so phone can access undeployed app
def start_ngrok():
    from pyngrok import ngrok
    url = ngrok.connect(5000).public_url
    return url

send_link(start_ngrok())