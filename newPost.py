#!/usr/bin/env python3

import os
import time
import string
import pyperclip

def askTitle(lastDir, relative_path):
	title = str(input("Enter the title of the blog: "))
	title = title.strip()
	urled = title.replace(' ','-')
	urled = urled.lower()
	htmled = urled + ".html"
	filePath = os.path.join(lastDir, htmled)
	if(os.path.exists(filePath)):
		print("\nSorry! The file: ", htmled, " already exists. Pleae consider a new title")
		askTitle(lastDir, relative_path)
	else:
		header = "<html>\n<head>\n<title>"+title+" | Cipher's Blog</title>\n"
		ender = "	<hr><br>\n<div id=\"someWhat-main-Banner\">"+title+"</div>\n</body>\n</html>"
		fh = open(filePath, "w")
		fhr = open(os.path.join(os.getcwd(),"site.template"), "r")
		site = fhr.read()
		fhr.close()
		tobeWritten = header + site + ender
		fh.write(tobeWritten)
		fh.close()
		tocpy = "<a href=\""+relative_path+"/"+htmled+"\"><li>"+title+"</li></a>";
		return tocpy;
#askTitle



def makeDir(dateList):
	path = os.getcwd();
	dirYear = os.path.join(path, dateList[0])
	dirMonth = os.path.join(dirYear, dateList[1])
	dirDay = os.path.join(dirMonth, dateList[2])
	if(os.path.isdir(dirYear)):
		if(os.path.isdir(dirMonth)):
			if(os.path.isdir(dirDay)):
				pass
			else:
				os.makedirs(dirDay)
			#isDay
		else:
			os.makedirs(dirMonth)
			os.makedirs(dirDay)
		#isMonth
	else:
		os.makedirs(dirYear)
		os.makedirs(dirMonth)
		os.makedirs(dirDay)
	#isYear
	return dirDay
#makeDir


##MAIN##
customDate = str(input("Do you want to use Current Date for your post(Y/N)?"))
dateArray = []
if(customDate.lower() == "no"):
	newDate = str(input("Please Enter New Date: (YYYY/MM/DD)"))
	dateArray = string.split(newDate, "/")
else: 
	dateArray = time.strftime("%Y/%m/%d").split("/");
cpyStr = askTitle(makeDir(dateArray), dateArray[0]+"/"+dateArray[1]+"/"+dateArray[2])
pyperclip.copy(cpyStr);
print("The following string: \n\n\t"+ cpyStr+"\n\nhas been copied to clipboard! Paste in where it suits.");