import Tkinter
from functools import partial
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
import time
import notify2
import getpass
import thread


notify2.init("INTERNET_USAGE")



def somethingelse():
	p1=thread.start_new_thread(f2,tuple())
	p2=thread.start_new_thread(f1,tuple())
	

def f1():
	frame.pack_forget()
	label=Tkinter.Message(root,text="The notification of Your data will arrive at every 15s",width=200,font=('times', 13, 'italic'))
	label.pack()
	b3=Tkinter.Button(root,text="HIDE THIS WINDOW",command=root.iconify)
	b3.pack()



def f2():
	username=e1.get()
	password=e2.get()
	driver = selenium.webdriver.PhantomJS(service_args=['--ssl-protocol=tlsv1','--ignore-ssl-errors=true'])
	driver.set_window_size(1124, 850)
	while (1):
		driver.get('https://172.22.2.2/corporate/webpages/login.jsp')
	        elem=driver.find_element_by_name('username')
	        elem.send_keys(username)
	        elem=driver.find_element_by_name('password')
	        elem.send_keys(password)
	        elem=driver.find_element_by_name('logintype')
	        elem=elem.find_element_by_id('Language.MyAccount')
	        elem.click()
	        elem=driver.find_element_by_name('loginbutton')
	        elem.click()
	        time.sleep(5)
	        elem=driver.find_elements_by_tag_name('tr')
	        elem=elem[13].find_elements_by_tag_name('td')
	        notify2.Notification("INTERNET USAGE","Your Remaining daily balance is " + elem[25].text).show()
	        time.sleep(10)   
	driver.quit();



root=Tkinter.Tk()
root.title("Cyberoam Internet Usage")
root.geometry('300x100')
frame=Tkinter.Frame(root)
frame.pack()
frame1=Tkinter.Frame(frame,height=10,bd=5)
frame1.pack()
l1=Tkinter.Label(frame1, text="Username:")
l1.pack(side="left")
e1=Tkinter.Entry(frame1)
e1.pack(side="right")
frame2=Tkinter.Frame(frame,height=5,bd=1)
frame2.pack(pady=5)
l2=Tkinter.Label(frame2,text="Password:")
l2.pack(side="left",pady=2,padx=2)
e2=Tkinter.Entry(frame2,show="*")
e2.pack(side="right")
submit=Tkinter.Button(frame,text="SUBMIT",command=somethingelse)
submit.pack()
root.mainloop()









