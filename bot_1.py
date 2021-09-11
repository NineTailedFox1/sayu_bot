from random import choice
import tweepy
import time

consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

A = ['The journey is no fun if you know where you are going. - Soma Yukihira']
B = ['Do me a favour and stop deciding other people’s happiness for them. – Soma Yukihira']
C = ['If you want to grow, just look above you. There are plenty of people perfect to serve as fodder for your growth. – Kojiro Shinomiya']
D = ['It’s just pathetic to give up on something before you even give it a shot. – Reiko Mikami']
E = ['You can die anytime, but living takes true courage. – Kenshin Himura']
F = ['Life is not a game of luck. If you wanna win, work hard. – Sora']
G = ['If your life can change once, your life can change again. – Sanae']
H = ['It’s more important to master the cards you’re holding than to complain about the ones your opponent was dealt. – Grimsley']
I = ['A teacher doesn’t give up on her students just because things get tough. – Harumi Kiyama']
J = ['If you just submit yourself to fate, then that’s the end of it. – Keiichi Maebara']
K = ['Whatever you do, enjoy it to the fullest. That is the secret of life. – Rider']
L = ['Sometimes I do feel like I’m a failure. Like there’s no hope for me. But still I don\'t think I am gonna give up. Ever! – Izuku Midoriya']
M = ['You can’t always hold on to the things that are important. By letting them go we gain something else. – Kunio Yaobi']
N = ['If you don’t like your destiny, don’t accept it. Instead, have the courage to change it the way you want it to be. – Naruto Uzumaki']
O = ['You can’t win a game by doing nothing. And if someone else wins it for you then you haven’t accomplished anything. Life is the same way. – Junichirou Kagami']
P = ['If you can’t find a reason to fight, then you shouldn’t be fighting. – Akame']
Q = ['You should never give up on life, no matter how you feel. No matter how badly you want to give up. – Canaan']
R = ['People who can’t throw something important away, can never hope to change anything. – Armin Arlelt']
S = ['We can’t waste time worrying about the what if’s. – Ichigo Kurosaki']
T = ['No matter how hard or impossible it is, never lose sight of your goal. – Monkey D Luffy']
U = ['That’s why I can’t make a change. Everything I do is so… Half-assed. – Hiroshi Kido']
V = ['Sometimes it’s necessary to do unnecessary things. – Kanade Jinguuji']
W = ['Just like games, no matter how well you have things lined up in your life, there’s always something to keep you on your toes. – Junichirou Kagami']
X = ['If you can’t do something, then don’t. Focus on what you can do. – Shiroe']
Y = ['The moment you think of giving up, think of the reason why you held on so long. – Natsu Dragneel']
Z = ['You don’t like who you are now, so you go. Even if you’re scared, you want to change the self you hate. – Neiru Aonuma']
AA = ['It’s a dream. It’s a bad dream. – Ai Ohoto']
AB = ['Crosswalks are still scary even when you move with the crowd. I’m done pretending not to see. – Ai Ohto']
AC = ['Unless someone makes the first move, nothing will happen. – Misa Amane']
AD = ['Being alone is better than being with the wrong person. – L Lawliet']
AE = ['Learn to treasure your life because unfortunately, it can be taken away from you anytime. – L Lawliet']
AF = ['Humans aren’t made perfectly. Everyone lies. Even so… I’ve been careful not to tell lies that hurt others. – Light Yagami ']
AG = ['Sometimes, the questions are complicated – and the answers are simple. – L Lawliet']
AH = ['You can’t ever win if you’re always on the defensive. To win, you have to attack! – Light Yagami']
AI = ['New experiences are what make life worth living. – Leticia Draculea']
AJ = ['Don’t live your life making up excuses. The one making your choices is yourself. – Mugen']
AK = ['Whatever your thoughts may be, if you don’t say them, none of it will be acknowledged by others. – Tomoyo Daidouji']
AL = ['Life is like a pencil that will surely run out, but will leave the beautiful writing of life. – Nami']
AM = ['The future is something that you build by yourself. – Ami Mizuno']
AN = ['Nothing’s perfect, the world’s not perfect, but it’s there for us, trying the best it can. That’s what makes it so damn beautiful. – Roy Mustang']
AO = ['If you have anything you wanna say, you better spit it out while you can. Because you’re all going to die sooner or later.- Zero Two']
AP = ['If you don’t belong here, just a build a place where you do. If you don’t have a partner, just find another one. – Zero Two']

data_quotes = list(A + B + C + D + E + F + G + H + I + J + K + L + M + N + O + P + Q + R + S + T + U + V + W + X + Y + Z + AA + AB + AC + AD + AE + AF + AG + AH + AI + AJ + AK + AL + AM + AN + AO + AP)

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#noticeme' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + ' ~ ' + choice(data_quotes), tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(10)
