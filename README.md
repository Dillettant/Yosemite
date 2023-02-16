# Yosemite

This python script will query whether there is released ticket of Yosemite Entry. Once release tickets are found, it will pop up an alter window.

## Env Setup

### Python Env
Please run this like to install python-tk:
```
brew install python-tk
```

### Twilio
Setup the twilio account to enable text message or phone call notification.
* Get to https://console.twilio.com/ to register an account
* In the account console, you can request a phone number
* Save `Account SID`, `Auth Token`, `My Twilio phone number`, and your personal phone number as environment variables in your local machine like this:
```
export TWILIO_ACCT_SID="<Account SID>"
export TWILIO_AUTH_TOKEN="<Auth Token>"
export TWILIO_PHONE_NUM="<My Twilio phone number>"
export PERSONAL_PHONE_NUM="<personal phone number>"
```
* Save the environment variables into a file as `~/.twilio_creds.env`
* Set appropriate file permissions: `chmod 600 ~/.twilio_creds.env` This means the file should be readable only by the user that needs access to the credentials, and not by other users on the system.
* Run the following line in command-line shell so environement variables can be exported to terminal automatically:
```
echo "# twilio credentials" >> ~/.zshrc
echo "source ~/.twilio_creds.env" >> ~/.zshrc
source ~/.zshrc
```

## Run the Script
Simple run the script in the terminal as:
```
python ./query_remaining_tickets.py
```
Please keep the terminal window open.

If you want to run the script in the background, use `nohup`:
```
nohup <python-absolute-path> ./query_remaining_tickets.py > yosemite.out &
```

To check if the script is still running, use `ps` command to list all running processes:
```
ps aux | grep query_remaining_tickets.py
```