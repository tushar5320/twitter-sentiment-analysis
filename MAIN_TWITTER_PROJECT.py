from textblob import TextBlob
from tkinter import *
from PIL import ImageTk,Image
import tweepy,requests
'''access_key="739126373692932100-hLi1AxaCjYbSDjaPGHtPFc4vUOptpU3"
access_key_secret="FBQE0ZluJyjmcZdYqPaOhw4boAMwltWawwVZuXdT1uNNa"
consumer_key="sYrDmZXDLaKD16ZbVPbb7g7PT"
consumer_secret="W24arlFbeAUq0Qlxs7dF2MjF6QlX7MKfWtRwc81MeqRxpULk6D"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_key_secret)
api=tweepy.API(auth)
api.update_status('tweepy + oauth!')'''

root = Tk()
image = Image.open("C:\\Users\\tusha\\Desktop\\back.jpg")
image = image.resize((2200, 2200), Image.ANTIALIAS)

#C = Canvas(root, bg="blue", height=250, width=300)
filename = ImageTk.PhotoImage(image)
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
allow=False
a=None
img=None
def onClick():
    global allow,a,img
    inputt=E1.get("1.0",'end-1c')
    innt=int(E2.get("1.0",'end-1c'))
    access_key="739126373692932100-hLi1AxaCjYbSDjaPGHtPFc4vUOptpU3"
    access_key_secret="FBQE0ZluJyjmcZdYqPaOhw4boAMwltWawwVZuXdT1uNNa"
    consumer_key="sYrDmZXDLaKD16ZbVPbb7g7PT"
    consumer_secret="W24arlFbeAUq0Qlxs7dF2MjF6QlX7MKfWtRwc81MeqRxpULk6D"
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_key_secret)
    api=tweepy.API(auth)
    print(innt)
    #api.update_status('tweepy + oauth!')
    #tweets=tweepy.Cursor(api.search,q=inputt,lang="English").items(innt)
    tweets=api.search(inputt,count=innt)
    print(tweets)

    p=0.00
    n=0.00
    nu=0.00
    avg=0.00
    c=0
    for tweet in tweets:
        print(tweet.text,"   =>   ",c)
        c+=1
        b=TextBlob(text=tweet.text)
        print(b.sentiment.polarity)
        if b.sentiment.polarity>0.00:
            p+=1
            avg+=b.sentiment.polarity
        elif b.sentiment.polarity<0.00:
            n+=1
            avg+=b.sentiment.polarity
        else:
            nu+=1
            avg+=b.sentiment.polarity



    if avg==0 :
        img=ImageTk.PhotoImage(Image.open('C:\\Users\\tusha\Downloads\\neutral.png'))
    elif avg>0.00 :
        img=ImageTk.PhotoImage(Image.open('C:\\Users\\tusha\Downloads\\happy.png'))
    elif avg<0.00 :
        img=ImageTk.PhotoImage(Image.open('C:\\Users\\tusha\Downloads\\sad.png'))
    icon=Label(root,image=img,width=img.width(),height=img.height())
    icon.place(relx=0.5,rely=0.5)
    q=Label(root,text=avg)
    q.place(relx=0.5,rely=0.1)
    #a.sentiment.polarity
    #print(a," = ",a.sentiment.polarity)
    #q=Label(root,text=avg)
    #q.place(relx=0.5,rely=0.1)

w = Label(root, text='Enter Keyword here :',bg="white")
w.place(relx=0.18,rely=0.20)
x = Label(root, text='Enter number of tweets to be searched :',bg="white")
x.place(relx=0.18,rely=0.23)
E1 = Text(root,width=25,height=1)
E1.place(relx=0.26,rely=0.20 )
E2 = Text(root,width=25,height=1)
E2.place(relx=0.32,rely=0.24 )
button=Button(root,text="Submit",command=onClick)
button.place(relx=0.40,rely=0.27)
root.mainloop()
