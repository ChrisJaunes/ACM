#!/usr/bin/env python
# -*- coding:utf-8 -*-
import telegram
import logging
import requests
import random
import datetime
from telegram.error import NetworkError, Unauthorized
from time import sleep
from bot_config  import *
from bot_sqlite  import *
from bot_crawler import *

help_message = '''
<table>
  <tr> <th>help      </th> <th> tell you some operation about the bot </th> </tr>
  <tr> <th>get_todo  </th> <th> [default] get your task; [(e.g : /get_todo#TA)] get TA todo</th> </tr>
  <tr> <th>set_todo  </th> <th> [(e.g: /set_todo#TA#todo)] set TA todo </th> </tr>
  <tr> <th>get_done  </th> <th> [default] get your do in todolist; [(e.g: /get_done#TA) ] get TA do in todolist</th> </tr>
  <tr> <th>set_done  </th> <th> [(e.g: /set_done#do or /set_done#do#todo_id] set your do </th> </tr>
</table>
'''
cf_pro = {'hjj' : '', 'wzk' : '', 'zys' : ''}

# 初始化 update_id
update_id = None
#初始化 date_set
date_set = set()
# 定义主函数
def main():
    global update_id
    ## 创建Bot类的对象，下方填入自己的TOKEN
    bot = telegram.Bot(TG_TOKEN)

    # 获取第一个挂起的update_id，这样我们可以跳过它以防万一
    # 得到一个 "Unauthorized" 异常.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
    # 主函数功能
    while True:
        try:
            if(datetime.date.today() not in date_set) :
                date_set.add(datetime.date.today())
                res = get_date_todo()
                bot.send_message(chat_id = scut_gugugu_chat_id, text = res, parse_mode = telegram.ParseMode.HTML)
            operation(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # 用户已屏蔽或取消了与机器人对话时
            update_id += 1
        except Exception as e:
            print(e)

def operation(bot):
    global update_id
    # 在最后一个update_id之后请求更新
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        print(update.message)
        msg_argv = update.message.text.split('#')
        res = ''
        if(update.message.text.startswith('/help')):
            res = help_message
        elif(update.message.text.startswith('/get_todo')):
            if(len(msg) == 1) : msg.append(update.message.from_user.username)
            res = get_todo(msg_argv)
        elif(update.message.text.startswith('/set_todo')):
            res = set_todo(msg_argv)
        elif(update.message.text.startswith('/get_done')):
            if(len(msg) == 1) : msg.append(update.message.from_user.username)
            res = get_todo(msg_argv)
        elif(update.message.text.startswith('/set_done')):
            msg_argv[0] = update.message.from_user.username
            res = get_todo(msg_argv)
        elif(update.message.text.startswith('/get_contest')):
            get_context(update.message)
        elif(update.message.text.startswith('/set_contest')):
            set_context(update.message)
        else: update.message.reply_text(update.message.text)
        res = '<html><body>' + res + '</body></html>'
        update.message.reply_text(res, parse_mode = telegram.ParseMode.HTML)


def get_cf_pro(tag) :
    url = 'https://codeforces.com/api/problemset.problems?tags=' + str(tag)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    res = 'https://codeforces.com/problemset/problem'
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        p = random.choice(json.loads(r.text) ['result']['problems'])
        return (str(p['name']),str(res)+'/'+str(p['contestId'])+'/'+str(p['index']))
    except requests.HTTPError as e:
        print(e)
    except requests.RequestException as e:
        print(e)
    except Exception as e:
        print(e)

def get_date_todo() :
    def get_todo_pro(_name):
        resc = get_todo_res(_name)
        if(resc[0] == 'Err') return resc[1][0]
        tresc = []
        for i in resc[1] :
            if(i[4] == 'no') :
                tresc.append('<p>' + str(i[1])+'&nbsp;'+str(i[0]) + '&nsbp;' + str(i[2])+'&nbsp;'+str(i[3])+'</p><br/>'
        res = random.choice(tresc) +'</div>'
        return res
    
    res = '<div> <p>' + str(datetime.today()) + 'todo list:</p><br/>'
    res = res + set_todo_pro(['hjj'])
    res = res + set_todo_pro(['wzk'])
    res = res + set_todo_pro(['zys'])
    cf_pro['hjj'], pro_link = get_cf_pro(random.choice(HJJ_TAG))
    res = res + '<p>[hjj]' + str(cf_pro['hjj']) + '&nbsp;' + pro_link + '</p><br/>'
    cf_pro['wzk'], pro_link = get_cf_pro(random.choice(WZK_TAG))
    res = res + '<p>[wzk]' + str(cf_pro['wzk']) + '&nbsp;' + pro_link + '</p><br/>'
    cf_pro['zys'], pro_link = get_cf_pro(random.choice(ZYS_TAG))
    res = res + '<p>[zys]' + str(cf_pro['zys']) + '&nbsp;' + pro_link + '</p><br/>'
    res = re + '</div>'
    return res

# 定义程序的入口
if __name__ == '__main__':
    main()
