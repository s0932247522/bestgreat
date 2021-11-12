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

line_bot_api = LineBotApi('IOmxiatB18j0urE8jbRQGxi4Kbrf7ZjVpfVk2svFCh+JoRF45vRe9/wanzNb4j54T8TuCICf7rhl7OPypV2qnCpa6l8PrSUUzoR4O4nSEOXbdyGIoN+Isn5ezMtcn7GkYUJjNQjqDVv+Fc34fTVUVgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('92f35de5943c5deeb8b57bff35e1b3b0')



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

def personal(name,ws):
    tt = ws.get_values('A1','G56')
    for cel in range(1,len(tt)):
         #0:隊別、 1:name、 2:goal、 3:now、 4:achieve、 5:disparity、 6:rate
        if tt[cel][1].split('-')[1].lstrip() == name:
            goal = tt[cel][3]
            now = tt[cel][2]
            achieve = tt[cel][4]
            disparity = tt[cel][5]
            rate = tt[cel][6]
            return goal, now, achieve, disparity, rate

def personal_5(name,ws):
    tt = ws.get_values('A1','H56')
    for cel in range(1,len(tt)):
         #0:隊別、 1:name、 2:goal、 3:now、 4:achieve、 5:disparity、 6:rate
        if tt[cel][1].split('-')[1].lstrip() == name:
            goal = tt[cel][4]
            now = tt[cel][2]
            achieve = tt[cel][5]
            disparity = tt[cel][6]
            rate = tt[cel][7]
            task = tt[cel][3]
            return goal, now, achieve, disparity, rate, task
        


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
        
    

    if (event.message.text.split('-')[0] == '#') and(event.message.text.split('-')[2] == '超跑隊') and (len(event.message.text.split('-')) == 3):
        super_week = {'1':'3', '2':'6', '3':'9', '4':'12', '5':'15', '6':'18' }
        gc = pygsheets.authorize(service_account_file='superrun.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1mk9luUpS0h2XHZ1p2gKECADIMc-hdAjXQlxPM-9F40U/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title('imm_total')
        tt = ws.get_values('A' + super_week[event.message.text.split('-')[1]],'I'+ super_week[event.message.text.split('-')[1]]) 
        g = tt[0][2]
        n = tt[0][3]
        g_r = tt[0][4]
        a = tt[0][5]
        d = int(g) - int(n)
        rate = tt[0][8]
        peo_num = tt[0][7] + '  /  ' + tt[0][6]
        val = event.message.text.split('-')[2] + ' ：\t第 '+ event.message.text.split('-')[1] + ' 週' +  '\n'
        val += '目前步數：\t'+ n + '步\n'
        val += '本週目標：\t'+ g + '步\n'
        val += '是否達標：\t'+ a + '\n'
        val += '剩餘步數：\t'+ str(d) + '步\n'
        val += '步數達成率：\t'+ g_r + '\n'
        val += '人數達成率：\t'+ rate + '\n'
        val += '已達成人數：\t'+ peo_num
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    elif (event.message.text.split('-')[0] == '#') and(event.message.text.split('-')[2] == '百億隊') and (len(event.message.text.split('-')) == 3):
        money_week = {'1':'2', '2':'5', '3':'8', '4':'11', '5':'14', '6':'17' }
        gc = pygsheets.authorize(service_account_file='superrun.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1mk9luUpS0h2XHZ1p2gKECADIMc-hdAjXQlxPM-9F40U/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title('imm_total')
        tt = ws.get_values('A' + money_week[event.message.text.split('-')[1]],'I'+ money_week[event.message.text.split('-')[1]]) 
        g = tt[0][2]
        n = tt[0][3]
        g_r = tt[0][4]
        a = tt[0][5]
        d = int(g) - int(n)
        rate = tt[0][8]
        peo_num = tt[0][7] + '  /  ' + tt[0][6]
        val = event.message.text.split('-')[2] + ' ：\t第 '+ event.message.text.split('-')[1] + ' 週' +  '\n'
        val += '目前步數：\t'+ n + '步\n'
        val += '本週目標：\t'+ g + '步\n'
        val += '是否達標：\t'+ a + '\n'
        val += '剩餘步數：\t'+ str(d) + '步\n'
        val += '步數達成率：\t'+ g_r + '\n'
        val += '人數達成率：\t'+ rate + '\n'
        val += '已達成人數：\t'+ peo_num
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    elif (event.message.text.split('-')[0] == '#') and(event.message.text.split('-')[2] == '超跑隊未達成') and (len(event.message.text.split('-')) == 3):
        week_grades = {'1':'week1_find', '2':'week2_find', '3':'week3_find', '4':'week4_find', '5':'week5_find', '6':'week6_find' }
        task = {'0':'未完成', '1':'已完成', '':'未完成', '2':'已完成', '3':'已完成'}
        gc = pygsheets.authorize(service_account_file='superrun.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1mk9luUpS0h2XHZ1p2gKECADIMc-hdAjXQlxPM-9F40U/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title(week_grades[event.message.text.split('-')[1]])
        if event.message.text.split('-')[1] == '5':
            tt = ws.get_values('K:K','Q:Q')
            val = ''
            for cel in range(0,len(tt)):
                val +=  tt[cel][6] + '\t' + task[tt[cel][2]] + '\t' + tt[cel][0].split('-')[1].lstrip() +  '\n'
        else:
            tt = ws.get_values('K:K','P:P')
            val = ''
            for cel in range(0,len(tt)):
                val += tt[cel][0].split('-')[1].lstrip() + '\t' + tt[cel][5] + '\n'


        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    elif (event.message.text.split('-')[0] == '#') and(event.message.text.split('-')[2] == '百億隊未達成') and (len(event.message.text.split('-')) == 3):
        week_grades = {'1':'week1_find', '2':'week2_find', '3':'week3_find', '4':'week4_find', '5':'week5_find', '6':'week6_find' }
        task = {'0':'未完成', '1':'已完成', '':'未完成', '2':'已完成', '3':'已完成'}
        gc = pygsheets.authorize(service_account_file='superrun.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1mk9luUpS0h2XHZ1p2gKECADIMc-hdAjXQlxPM-9F40U/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title(week_grades[event.message.text.split('-')[1]])
        if event.message.text.split('-')[1] == '5':
            tt = ws.get_values('S:S','Y:Y')
            val = ''
            for cel in range(0,len(tt)):
                val +=  tt[cel][6] + '\t' + task[tt[cel][2]] + '\t' + tt[cel][0].split('-')[1].lstrip() +  '\n'
        else:
            tt = ws.get_values('S:S','X:X')
            val = ''
            for cel in range(0,len(tt)):
                val += tt[cel][0].split('-')[1].lstrip() + '\t' + tt[cel][5] + '\n'

        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    elif event.message.text == '#上傳':
        val = '超跑隊感謝您的每一步,也別忘了提醒您的好夥伴上傳哦！\n'
        val += '上傳網址：\n'
        val += 'https://reurl.cc/YWrEYO'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    elif event.message.text == '#超跑隊個人未達成次數':
        gc = pygsheets.authorize(service_account_file='superrun.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1mk9luUpS0h2XHZ1p2gKECADIMc-hdAjXQlxPM-9F40U/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title('no_accomplish')
        tt = ws.get_values('A:A','I:I')
        val = '超跑隊個人未達成次數\n'
        for cel in range(0,len(tt)):
            if tt[cel][0] == '【超跑隊】':
                val += tt[cel][8] + '\t' + tt[cel][1].split('-')[1].lstrip() + '\n'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    elif event.message.text == '#百億隊個人未達成次數':
        gc = pygsheets.authorize(service_account_file='superrun.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1mk9luUpS0h2XHZ1p2gKECADIMc-hdAjXQlxPM-9F40U/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title('no_accomplish')
        tt = ws.get_values('A:A','I:I')
        val = '百億隊個人未達成次數\n'
        for cel in range(0,len(tt)):
            if tt[cel][0] == '＄百億隊＄':
                val += tt[cel][8] + '\t' + tt[cel][1].split('-')[1].lstrip() + '\n'


        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
    elif (event.message.text.split('-')[0] == '#') and (len(event.message.text.split('-')) == 3):
        week_grades = {'1':'week1_find', '2':'week2_find', '3':'week3_find', '4':'week4_find', '5':'week5_find', '6':'week6_find' }
        gc = pygsheets.authorize(service_account_file='superrun.json')
        gs_url = 'https://docs.google.com/spreadsheets/d/1mk9luUpS0h2XHZ1p2gKECADIMc-hdAjXQlxPM-9F40U/edit#gid=0'
        sh = gc.open_by_url(gs_url)
        ws = sh.worksheet_by_title(week_grades[event.message.text.split('-')[1]])
        # val = ws.get_value('F3')
        if event.message.text.split('-')[1] == '5':
            task = {'0':'未完成', '1':'已完成', '':'未完成'}
            g, n, a, d, r ,t = personal_5(event.message.text.split('-')[2], ws)
            val = event.message.text.split('-')[2] + ' ：\t第 '+ event.message.text.split('-')[1] + ' 週' +  '\n'
            val += '本週目標：\t'+ g + '步\n'
            val += '目前步數：\t'+ n + '步\n'
            val += '是否達標：\t'+ a + '\n'
            val += '剩餘步數：\t'+ d + '步\n'
            val += '週達成率：\t'+ r + '\n'
            val += '本週任務：\t'+ task[t]
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))
        else:
            g, n, a, d, r = personal(event.message.text.split('-')[2], ws)
            val = event.message.text.split('-')[2] + ' ：\t第 '+ event.message.text.split('-')[1] + ' 週' +  '\n'
            val += '本週目標：\t'+ g + '步\n'
            val += '目前步數：\t'+ n + '步\n'
            val += '是否達標：\t'+ a + '\n'
            val += '剩餘步數：\t'+ d + '步\n'
            val += '週達成率：\t'+ r 
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=val))



        
        


if __name__ == "__main__":
    app.run()