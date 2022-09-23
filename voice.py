import speech_recognition as sr
import smtplib



# import pyaudio
# import platform
# import sys






from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
import datetime



path_of_files = "assets/"

sender_mail_address='development2001nr@gmail.com'
password_of_sender = "oajvbingbwowgsvr"
#maillist to restrict send address
validMailList = ["nitinraj2001"]

def main():

    #speak project name

    tts = gTTS(text="Project: Voice based Email for blind", lang='en')
    ttsname=(path_of_files+"project_name.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)



    #choices choice 1
    print("1. composed a mail.")
    tts = gTTS(text="option 1. composed a mail.", lang='en')
    ttsname=(path_of_files+"opt1_compose_mail.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)






    #choices choice 2
    print ("2. Check your inbox")
    tts = gTTS(text="option 2. Check your inbox", lang='en')
    ttsname=(path_of_files+"check_your_inbox.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)













    #this is for input choices
    tts = gTTS(text="Speak your choice ", lang='en')
    ttsname=(path_of_files+"/enter_your_choice.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

    #voice recognition part
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Speak your choice:")
        audio=r.listen(source)
        print ("ok done!!")

    try:
        text=r.recognize_google(audio)
        print ("You said : "+text)
        tts = gTTS(text="You said "+text, lang='en')
        ttsname=(path_of_files+"/you_said_choice.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    if text == '1' or text == 'One' or text == 'one':
        compose()
    elif text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To':
        readMail()
    else:
        tts = gTTS(text="Invalid Choice please try again.", lang='en')
        ttsname = (path_of_files + "/invalid_choice_please.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        main()


#choices details
#if text == '1' or text == 'One' or text == 'one':
def compose():
    r = sr.Recognizer() #recognize
    with sr.Microphone() as source:
        print ("Your message : ")
        tts = gTTS(text="Speek your message", lang='en')
        ttsname=(path_of_files+"/your_msg.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        
        audio=r.listen(source)
        print ("ok done!")
        tts =gTTS(text="ok done",lang='en')
        ttsname=(path_of_files+"/done_msg.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        
    try:
        text1=r.recognize_google(audio)
        print ("You said : "+text1)
        
        tts = gTTS(text="You said "+text1, lang='en')
        ttsname=(path_of_files+"/your_speaked_msg.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        
        msg = text1
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))    

    r = sr.Recognizer() #recognize email address
    with sr.Microphone() as source:
        print ("Mail address to send :")
        tts = gTTS(text="Speek Mail address to send", lang='en')
        ttsname=(path_of_files+"/mail_address_to_send.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

        audio=r.listen(source)
        print ("ok done!!")

    try:
        text1=r.recognize_google(audio)
        print ("You said : "+text1)

        textMailAddress = text1.replace(" ", "")
        textMailAddress = textMailAddress.lower()
        print ("Refined address : "+textMailAddress)

        tts = gTTS(text="Mail address is "+textMailAddress, lang='en')
        ttsname=(path_of_files+"/you_said.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)

        correct = False
        for madd in validMailList:
            if madd == textMailAddress:
                mailaddress = madd
                correct = True

        if not correct:
            tts = gTTS(text="Mail address is not exist in mail list please try again", lang='en')
            ttsname=(path_of_files+"/mailaddnotex.mp3")
            tts.save(ttsname)

            music = pyglet.media.load(ttsname, streaming = False)
            music.play()
            time.sleep(music.duration)
            exit()

      
        #mailaddress = text1
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))    
    
    
    
    mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
    mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
    mail.starttls() #security connection
    
    
    mailaddress+="@gmail.com"
    recipient =  mailaddress
    

    mail.login(sender_mail_address,password_of_sender) #login part
    
    content= msg
    mail.sendmail(sender_mail_address, recipient, content)
   
    print ("Congrates! Your mail has send. ")
    tts = gTTS(text="Congrates! Your mail has send. ", lang='en')
    ttsname=(path_of_files+"/congrets_mail_send.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()   
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
#reading inbox
    
    
    
    
    
    
    
    
#elif text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' :
def readMail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
    
    mail.login(sender_mail_address,password_of_sender)  #login
    
    
    stat, total = mail.select('Inbox')  #total number of mails in inbox
    print ("Number of mails in your inbox :"+str(total))
    
    str_total_mail = "Total mails are :"+str(total)
    
    str_total_mail = str_total_mail.replace("[b'"," ")
    str_total_mail = str_total_mail.replace("']","")
    
    tts = gTTS(text="Total mails are :"+str(total), lang='en') #voice out
    ttsname=(path_of_files+"/total.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    
    #unseen mails
    unseen = mail.search(None, 'UnSeen') # unseen count
    print ("Number of UnSeen mails :"+str(unseen))
    
    #tts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
    #ttsname=(path_of_files+"/unseen.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    #tts.save(ttsname)
    #music = pyglet.media.load(ttsname, streaming = False)
    #music.play()
    #time.sleep(music.duration)
    #os.remove(ttsname)
    
    #search mails
    
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    
    print("New :"+str(new))
    
    result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
    
    
    raw_email = email_data[0][1].decode("utf-8") #decode
    
    msg_str = email.message_from_string(raw_email)
    
    
    
    
    
    
    mail_from = msg_str['From']
    
    mail_from = "Mail From :" + mail_from
    mail_from = mail_from.replace("<","")
    mail_from = mail_from.replace(">","")
    
    print("====================  Mail From start =============================")
    print(mail_from)
    tts = gTTS(text=mail_from, lang='en')
    ttsname=(path_of_files+"/mail_from.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("====================  Mail From end  ==============================")
    
    
    
    
    mail_subject = 'Subject is : %s' % (msg_str['Subject'])
    
    print("==================== subject start =============================")
    print(mail_subject)
    tts = gTTS(text=mail_subject, lang='en')
    ttsname=(path_of_files+"/mail_subject.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("==================== subject end   =============================")
    
    
    
    
    #print ('Raw Date:', msg_str['Date'])
    date_tuple = email.utils.parsedate_tz(msg_str['Date'])
    if date_tuple:
        local_date = datetime.datetime.fromtimestamp(
            email.utils.mktime_tz(date_tuple))
        #print( "Local Date:", \
        #    local_date.strftime("%a, %d %b %Y %H:%M:%S"))
        
        date_and_time_str = local_date.strftime("%a, %d %b %Y %H:%M:%S")
        
        date_and_time_str = "Date and time is : "+date_and_time_str
            
    
    
    
    print("==================== date and time start =============================")
    print(date_and_time_str)
    tts = gTTS(text=date_and_time_str, lang='en')
    ttsname=(path_of_files+"/date_and_time_str.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("==================== date and time end   =============================")
    
    
    
    
    soup = BeautifulSoup(raw_email, 'html.parser')
    row = soup.find('div') 
    str_message = row.get_text()
    
    str_message = "Message is : " +str_message
    
    print("==================== message start =============================")
    print(str_message)
    tts = gTTS(text=str_message, lang='en')
    ttsname=(path_of_files+"/str_message.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("==================== message end   =============================")
    
   

    
    

    
   
  
    mail.close()
    mail.logout()
    
    
    

main()
"""else:
    tts = gTTS(text="Invalid Choice please try again.", lang='en')
    ttsname=(path_of_files+"/invalid_choice_please.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    """
