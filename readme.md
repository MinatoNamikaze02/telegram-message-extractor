# Telegram chat history exporter
* A simple python script using the telethon library to extract message history of the specified telegram channel
## Requirements
* Telethon 1.24.0
* dotenv
## Environment variables
* check the env.example file in the task1 directory and follow the same format to create the actual env file. Once done, you can run the code.
* Note: The env file needs the api_id and api_hash which can be obtained by creating a developer account on telegram.
## Process
* Enter the link of a channel or its ID. The link is available on the description (mostly). The ID can be obtained from the url while using
  telegram desktop.
* Make sure the channel isn't private.
* Enter the limit (number of messages to download)
## Output
* Output is printed as well as stored in a JSON file
* It is stored as a dict ({'user_id': ID', 'message': MESSAGE})
## Side Notes
* You will be asked to login for the first session.
* You would have to enter your phone number in an international format like `+91XXXXXXXXXX`.
* Followed by this, you'd have to enter a code that was sent to you through telegram.
* You're good to go now. If any queries, feel free to contact me!
