
import urllib
import re
import time


def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getInfo(student_no):
	url = "https://z.seiee.com/scores/search?student_no=" + str(student_no)
	html = getHtml(url)
	p1 = r"<p>[0-9]+(.+?)</p>"
	pattern1 = re.compile(p1)
	f = open("b.txt", "w")
	array = re.findall(pattern1, html)
	result = ""
	for ele in array:
		ele = ele.split(" ")
		result = str(student_no) + " " + ele[1]

	return result

def main():
	f = open("b.txt", "a")
	seed = 0
	for i in range(515030910065, 515030910200):
		print i
		if seed == 1:
			seed = 0;
			time.sleep(1);

		seed += 1;
		result = getInfo(i)
		f.write(result + "\n")
	f.close()

if __name__ == '__main__':
	main()