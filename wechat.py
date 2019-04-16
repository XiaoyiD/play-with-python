import itchat, time
import random
import datetime as dt
#from apscheduler.schedulers.background import BackgroundScheduler
from itchat.content import *

lib_set = {'rb', 'gs', 'RB', 'gerstain', '图书馆', '约馆'}
gotobed_set = {'早睡', '早点睡', '熬夜', '不睡', '没睡', '睡了'}
eat_set = {'饿', '吃', '食堂', '饭', '烤肉'}
study_set = {'学习', '作业', 'ddl', 'due', 'hw', 'assignmant', 'a4'}
question_set = {'做什么呢', '干嘛'}
set419 = {'约炮', '炮友', '上床', '做爱', '419', '一夜情', '床上', '蹦迪'}
reply_counter = 0
msg_mode = False
reply_lst = [ "请您听到'哔'声后留言_____ ",
             "您好，您所呼叫的用户不知道在忙啥呢，稍后回复您",
             #"小一同学沉迷于学习中，无法自拔😅", \
             #"为什么天这么安静______", \
             #"本人现在不在呀，一会儿回复", "正在写作业，稍后回复哦，如有急事请打call 6479785060",\
             #"知道你想我，可我现在真的不在😶", "Auto_Reply，本人稍后闪现。", \
             "这里是自动回复哦，您先留言好不好呀😀", 
             "（可能手机被我扔了hhh）一会就捡回来啦"] 
             #"感受到了你的呼唤，可我不在手机旁边，请您稍等一段时间😉",
             #"call 6479785060 if u miss me, or 911 for emergency."]

def keywords_checker(msg, keywords_set):
    ''' str, set -> boolean
    check if msg contains the keyword from keywords_set, 
    @msg: the Text of received message, msg['Text'] in main
    @keywords_set: a set of similar attributes
    '''
    for word in keywords_set:
        if word in msg:
            return True
    return False


'''自动回复'''
@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
    #print(msg['Type'])
    # print(msg['Text'])
    counter = 0
    if msg['Type'] == 'Text' and msg_mode:
        if msg['Text'] == '屏蔽自动回复':
            #reply_counter = 1
            itchat.send('自动回复关闭功能还在建设中', toUserName=msg['FromUserName'])
        elif '小一' in msg['Text']:
            itchat.send('感受到了你的呼唤，可我不在手机旁边，请您稍等一段时间，抱歉。', toUserName=msg['FromUserName'])
        elif '夕阳' in msg['Text'] or '遗憾' in msg['Text'] or '错过' in msg['Text']:
            itchat.send('夕阳下我多少次回望着你的眼，谁料遗憾苍茫了爱恋。', toUserName=msg['FromUserName'])
        elif '死' in msg['Text'] or '身亡' in msg['Text'] or '卒' in msg['Text']:
            itchat.send('愿死如秋叶之静美', toUserName=msg['FromUserName'])
        elif keywords_checker(msg['Text'], study_set):
            itchat.send('我看黄历了，今天不适合学习，说吧去哪嗨？', toUserName=msg['FromUserName'])
        elif 'ba' in msg['Text'] or 'BA' in msg['Text'] or 'Ba' in msg['Text']:
            itchat.send('BA？嘿！怎么又要去BA，是觉得黑夜不够美，还是嫌黑眼圈不够黑。', toUserName=msg['FromUserName'])                        
        elif 'code' in msg['Text']:
            itchat.send('I heard u mention code, any bugs?', toUserName=msg['FromUserName'])
        elif '想你' in msg['Text']:
            itchat.send('白茶清欢别无事，我在等风也在想你、', toUserName=msg['FromUserName'])
        elif keywords_checker(msg['Text'], gotobed_set):
            itchat.send('我在熬夜，熟了叫你', toUserName=msg['FromUserName']) 
        elif '晚安' in msg['Text']:
            itchat.send('晚安我爱你', toUserName=msg['FromUserName'])
        elif '爱你' in msg['Text']:
            itchat.send('漫天的我落在枫叶上雪花上，你再不来，我就要下雪了', toUserName=msg['FromUserName'])
        elif '游戏' in msg['Text']:
            itchat.send('我觉得吹泡泡是最好玩的游戏，尽管大家都说那不是游戏。', toUserName=msg['FromUserName'])
        elif '雨' in msg['Text'] or '最美' in msg['Text']:
            itchat.send('最美的不是下雨天，是和你一起躲雨的屋檐', toUserName=msg['FromUserName'])
        elif '伤心' in msg['Text'] or '难过' in msg['Text'] or '想哭' in msg['Text']:
            itchat.send('悲伤有很多种，能加以抑制的悲伤，未必称得上悲伤。', toUserName=msg['FromUserName'])
        elif '午后' in msg['Text']:
            itchat.send('想孤身前往去看一场花事。如果午后微雨突袭，你恰好渡船而过，不妨让我们在春柳拂面的桥头相见。', toUserName=msg['FromUserName'])
        elif '累' in msg['Text']:
            itchat.send('人生就是电梯啊，就算自己静止，也还是会前行', toUserName=msg['FromUserName'])
        elif keywords_checker(msg['Text'], eat_set):
            itchat.send('少吃点，肉啊！', toUserName=msg['FromUserName'])
        elif '酒' in msg['Text']:
            itchat.send('浊酒情深有闲致，亦是盼月、亦是盼你', toUserName=msg['FromUserName'])
        elif '等你' in msg['Text'] or '等会' in msg['Text']:
            itchat.send('在等风、也在等你', toUserName=msg['FromUserName'])
        elif '666' in msg['Text']:
            itchat.send('我也觉得很6', toUserName=msg['FromUserName'])
        elif keywords_checker(msg['Text'], lib_set):
            itchat.send('世界上最快乐的事莫过于，和你在图书馆肩并肩，手牵手，潇潇洒洒做完一套又一套题。', toUserName=msg['FromUserName'])
        elif keywords_checker(msg['Text'], set419):
            itchat.send('一夜雨如一夜情，蓦然回首，人去楼空。', toUserName=msg['FromUserName'])
        elif keywords_checker(msg['Text'], question_set):
            itchat.send("在想你，多希望此刻吹一阵风把'我想你'带到有你的那边，可今天吹南风，那就你想我吧～", toUserName=msg['FromUserName'])
        else:
            itchat.send("在熬夜，熟了叫你。", toUserName=msg['FromUserName'])
    else:
        itchat.send(random.choice(reply_lst), toUserName=msg['FromUserName'])
        #itchat.send("在熬夜，熟了唤你", toUserName=msg['FromUserName'])
        #reply_counter += 1
        #if reply_counter >= 5:
            #itchat.send("是自动回复的啦，发这么多消息是不是喜欢我呀😊", toUserName=msg['FromUserName'])
            #counter = 0
    
    users = itchat.search_friends(userName=msg['FromUserName'])
   # print(users)
    if users['NickName'] != 'Xiaoyi':
        print('%s : %s' % (users['NickName'], msg['Text']))

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('很高兴遇见你', msg['RecommendInfo']['UserName'])

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run() # 启动微信