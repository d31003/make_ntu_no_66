from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

user_id = 'U43dd60475a2c8f1af6c07fb0f20e301f'
channel_access_token = 'v4nBwDMkqdXr7wjbKON42g0G8pvWoGcaDdHxF+RTPqWeA+jI7z+tAc/xMkAnMd4r5yIomV0+Okqdp6+LW/HdYNGqgFDpWZTBJyJukqTKl3KWMZpK6oIyjKr6jcqWrOjsrPBQ/NMZPsdccLcDUApOAwdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
line_bot_api.push_message(user_id, TextSendMessage(text='偵測到陌生人！'))