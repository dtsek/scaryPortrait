#Enable on crontab: */20 * * * *    /usr/bin/python3 /home/pi/Desktop/projectScaryPortrait/sendMail.py

import shutil
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def checkSpace():

	videoPath = '/home/pi/Desktop/projectScaryPortrait/videos'

	total, used, free = shutil.disk_usage(videoPath)
	totalGB = total // (2**30)
	usedGB = used // (2**30)
	freeGB = free // (2**30)

	path, dirs, files = next(os.walk(videoPath))
	videoCount = len(files)

	reportStr = 'Total: %d GB, Used: %d GB, Free %d GB \n\nNumber of video files: %d' % (totalGB, usedGB, freeGB, videoCount)
	sendMailReport(reportStr)

def sendMailReport(reportMsg):
	gmailUser = ''
	gmailPasswd = ''

	fromAddr = 'lovelyLady@raspberry.pi'
	toAddr = ''

	msg = MIMEMultipart()
	msg['From'] = fromAddr
	msg['To'] = toAddr
	msg['Subject'] = 'Space report on Raspberry Pi'
	body = reportMsg
	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(gmailUser, gmailPasswd)
	text = msg.as_string()
	server.sendmail(fromAddr, toAddr, text)
	server.quit()


if __name__ == '__main__':
        checkSpace()
