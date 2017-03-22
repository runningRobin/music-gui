# coding:utf8
from Tkinter import *
import tkMessageBox
import urllib
import mp3play
import json
import time
import threading


def music():
    word = entry.get().encode('utf-8')
    if not word:
        tkMessageBox.showinfo("提示：",'请输入歌曲名再搜索')
        return
    word = urllib.quote(word)
    html = urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=20'%(word)).read()

    js = json.loads(html)

    listbox.delete(0, END)
    global data
    data = js['result']['songs']
    for i in data:
        listbox.insert(END, i['album']['name']+"("+i['artists'][0]['name']+")")


def play():
    sy = listbox.curselection()[0] #获取点击索引
    url = data[sy]['audio']
    urllib.urlretrieve(url, 'music.mp3')
    mp3 = mp3play.load('music.mp3')
    mp3.play()
    mp3.seconds(time.sleep(100))
    mp3.stop()


def doplay():
    t = threading.Thread(play())
    t.start()


if __name__ == '__main__':
    root = Tk()
    root.geometry('+800+200')
    root.title('音乐播放器')
    entry = Entry(root)
    entry.pack()
    Button(root, text='搜 索', command=music).pack()
    var = StringVar()
    listbox = Listbox(root, width=50, listvariable=var)
    listbox.bind('<Double-Button-1>', play)
    listbox.pack()
    Label(root, text='欢迎使用Robin在线音乐播放器', fg="red").pack()
    root.mainloop()
