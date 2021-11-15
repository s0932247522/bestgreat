from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import pygsheets
app = Flask(__name__)

line_bot_api = LineBotApi('vixzEpnS9sDjYhGz+CQx54mRmIzVSvG3PwsVa0nj+dA9RYG01WeejkJoEZm9Eo3q/4odGV7jghHg9zPMfQtdvDUY+op5VRdXV/hs3oXdukHiWfo3Sn2awMtMBN5IisqVm0fBHpcZaAPM5x0jlpOinQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5b8be3b8730f373648e646bfc4b6c1ed')
#已改機器人位置


# def personal(name,ws):
#     for cell in range(2,60):
#         cel = 'B' + str(cell)
#         if ws.get_value(cel).split('-')[1].lstrip() == name:
#             goal = ws.get_value('C' + str(cell))
#             now = ws.get_value('D' + str(cell))
#             achieve = ws.get_value('E' + str(cell))
#             disparity = ws.get_value('F' + str(cell))
#             rate = ws.get_value('G' + str(cell))
#             return goal, now, achieve, disparity

# def personal(name,ws):
#     tt = ws.get_values('A1','G56')
#     for cel in range(1,len(tt)):
#          #0:隊別、 1:name、 2:goal、 3:now、 4:achieve、 5:disparity、 6:rate
#         if tt[cel][1].split('-')[1].lstrip() == name:
#             goal = tt[cel][3]
#             now = tt[cel][2]
#             achieve = tt[cel][4]
#             disparity = tt[cel][5]
#             rate = tt[cel][6]
#             return goal, now, achieve, disparity, rate

# def personal_5(name,ws):
#     tt = ws.get_values('A1','H56')
#     for cel in range(1,len(tt)):
#          #0:隊別、 1:name、 2:goal、 3:now、 4:achieve、 5:disparity、 6:rate
#         if tt[cel][1].split('-')[1].lstrip() == name:
#             goal = tt[cel][4]
#             now = tt[cel][2]
#             achieve = tt[cel][5]
#             disparity = tt[cel][6]
#             rate = tt[cel][7]
#             task = tt[cel][3]
#             return goal, now, achieve, disparity, rate, task
        


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
        
    

    # if (event.message.text.split('-')[0] == '#') and(event.message.text.split('-')[2] == '超跑隊') and (len(event.message.text.split('-')) == 3):
    #     super_week = {'1':'3', '2':'6', '3':'9', '4':'12', '5':'15', '6':'18' }
    #     gc = pygsheets.authorize(service_account_file='superrun.json')
    #     gs_url = 'https://docs.google.com/spreadsheets/d/1mk9luUpS0h2XHZ1p2gKECADIMc-hdAjXQlxPM-9F40U/edit#gid=0'
    #     sh = gc.open_by_url(gs_url)
    #     ws = sh.worksheet_by_title('imm_total')
    #     tt = ws.get_values('A' + super_week[event.message.text.split('-')[1]],'I'+ super_week[event.message.text.split('-')[1]]) 
    #     g = tt[0][2]
    #     n = tt[0][3]
    #     g_r = tt[0][4]
    #     a = tt[0][5]
    #     d = int(g) - int(n)
    #     rate = tt[0][8]
    #     peo_num = tt[0][7] + '  /  ' + tt[0][6]
    #     val = event.message.text.split('-')[2] + ' ：\t第 '+ event.message.text.split('-')[1] + ' 週' +  '\n'
    #     val += '目前步數：\t'+ n + '步\n'
    #     val += '本週目標：\t'+ g + '步\n'
    #     val += '是否達標：\t'+ a + '\n'
    #     val += '剩餘步數：\t'+ str(d) + '步\n'
    #     val += '步數達成率：\t'+ g_r + '\n'
    #     val += '人數達成率：\t'+ rate + '\n'
    #     val += '已達成人數：\t'+ peo_num
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    if (event.message.text.split('-')[0] == '#') and(event.message.text.split('-')[1] == '尚讚') and (len(event.message.text.split('-')) == 2):

        gc = pygsheets.authorize(service_account_file='bestgreat.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1UwEf2DLgod9Gb1Oe6SK2BOgvddWbNt-3y6eUnogaIRw/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title('imm_total')
        tt = ws.get_values('A:A','E:E')
        a1 = tt[3][3]
        b1 = tt[3][4]
        date1 = tt[6][2]
        date2 = tt[7][2]
        total = tt[4][3]
        val = '尚讚隊\n'
        val += '今天日期：\t'+ date1 + '\n'
        val += '倒數天數：\t'+ date2 + '\t天\n'
        val += '個人賽道：\t'+ a1 + '\t分\n'
        val += '團隊賽道：\t'+ b1 + '\t分\n'
        val += '總計分數：\t'+ total + '\t分\n'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    elif (event.message.text.split('-')[0] == '#') and(event.message.text.split('-')[1] == '紅不讓') and (len(event.message.text.split('-')) == 2):

        gc = pygsheets.authorize(service_account_file='bestgreat.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1UwEf2DLgod9Gb1Oe6SK2BOgvddWbNt-3y6eUnogaIRw/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title('imm_total')
        tt = ws.get_values('A:A','E:E')
        a1 = tt[3][1]
        b1 = tt[3][2]
        date1 = tt[6][2]
        date2 = tt[7][2]
        total = tt[4][1]
        val = '紅不讓隊\n'
        val += '今天日期：\t'+ date1 + '\n'
        val += '倒數天數：\t'+ date2 + '\t天\n'
        val += '個人賽道：\t'+ a1 + '\t分\n'
        val += '團隊賽道：\t'+ b1 + '\t分\n'
        val += '總計分數：\t'+ total + '\t分\n'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    elif (event.message.text.split('-')[0] == '#') and(event.message.text.split('-')[1] == '尚讚') and (event.message.text.split('-')[2] == 'detail') and (len(event.message.text.split('-')) == 3):

        gc = pygsheets.authorize(service_account_file='bestgreat.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1UwEf2DLgod9Gb1Oe6SK2BOgvddWbNt-3y6eUnogaIRw/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title('now')
        tt = ws.get_values('A:A','G:G')
        val = '隊員\t 個人\t 團隊\t'
        for cel in range(5,len(tt)):
            val +=  tt[cel][4] + '\t' + tt[cel][5] + '\t' + tt[cel][6] + '\n' 



        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
        
        
        
            
            


if __name__ == "__main__":
    app.run()