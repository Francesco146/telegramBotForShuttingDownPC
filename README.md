# telegramBotForShuttingDownPC
A telegram bot that allow to shutdown your pc remotely.

# Setup guide
- set `telegram_API_Key` to your telegram api key. [Get yours at this address](https://core.telegram.org/bots)
- in the following if statement
```
if str(message.from_user.id) == "{YOUR PROFILE ID}" and 
   str(message.from_user.first_name) == "{YOUR FIRST NAME}" and 
   str(message.from_user.last_name) == "{YOUR LAST NAME}" and 
   str(message.from_user.username) == "{YOUR NICKNAME}":
```
replace the value with your value. Get those info [Here](https://t.me/userinfobot)

Then simply run the script with `python shutdown.py` and sent your bot `/start` and `/spegni` for shutting down your pc from anywhere.

# Tip
If you want to get this running at startup of your pc, in the background, make a .bat file that execute this command:
`START /B pythonw shutdown.py`. Then put the .bat and the .py file in the same folder and make a shortcut of the .bat file in this location (on Windows):
`C:\Users\%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
