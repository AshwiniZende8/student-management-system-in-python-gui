from tkinter import*
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from sqlite3 import*
import requests
import  matplotlib.pyplot as plt
import bs4

def f1():
	root.withdraw()
	add_st.deiconify()
def f2():
	add_st.withdraw()
	root.deiconify()
	add_st_entrno.delete(0,END)
	add_st_entname.delete(0,END)
	add_st_entmarks.delete(0,END)
def f3():
	root.withdraw()
	view_st.deiconify()
	view_st_data.delete(1.0, END)
	con = None
	try:
		con = connect("studentdata.db")
		sql = "select * from student"
		cursor = con.cursor()
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "rno:-" + str(d[0])+ "   name:-" + str(d[1]) +"   marks:-"+str(d[2])+ "\n"
		view_st_data.insert(INSERT, info)
	except Exception  as e:
		showerror("issue", e)
	finally:
		if con is not None:
			con.close()
def f4():
	view_st.withdraw()
	root.deiconify()
def f5():
	con = None
	try:
		con = connect("studentdata.db")
		sql = "insert into student values('%s', '%s','%s')"
		cursor = con.cursor()
		rno = add_st_entrno.get()
		name = add_st_entname.get()
		marks= add_st_entmarks.get()
		if len(rno)==0:
			showerror("ISSUE","ROLL NO CANNOT BE EMPTY")
		else:
			if int(rno) > 0:
				if len(name)==0:
					showerror("ISSUE","NAME CANNOT BE EMPTY")
				else:
					if name.isalpha():
						if len(name)>=2:
							if len(marks)==0:
								showerror("ISSUE","MARKS CANNOT BE EMPTY")
							else:
								if 0 < int(marks) <= 100:
									cursor.execute(sql % (rno, name,marks))
									con.commit()
									showinfo("success", "Record Added")
								else:
									showerror("ISSUE","MARKS SHOULD BE IN RANGE BETWEEN 0-100")
						else:
							showerror("ISSUE","LENGTH OF NAME SHOULD BE GREATER THAN 1")
					else:
						showerror("ISSUE","NAME SHOULD CONTAIN ONLY ALPHABETS")
			else:
				showerror("ISSUE","ROLL NUMBER SHOULD BE GREATER THAN 0")
	except Exception as e:
		showerror("FAILURE",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
def f6():
	root.withdraw()
	update_st.deiconify()
			
def f7():	
	con=None
	try:
		con=connect("studentdata.db")
		sql="update student set name='%s',marks='%s' where rno='%s' "
		cursor=con.cursor()
		rno=update_st_entrno.get()
		name=update_st_entname.get()
		marks=update_st_entmarks.get()
		cursor.execute(sql % (name,marks,rno))
		if len(rno)==0:
			showerror("ISSUE","ROLL NO CANNOT BE EMPTY")
		else:
			if int(rno) > 0:
				if len(name)==0:
					showerror("ISSUE","NAME CANNOT BE EMPTY")
				else:
					if name.isalpha():
						if len(name)>=2:
							if len(marks)==0:
								showerror("ISSUE","MARKS CANNOT BE EMPTY")
							else:
								if 0 < int(marks) <= 100:
									cursor.execute(sql % (rno, name,marks))
									con.commit()
									showinfo("success", "Record updated")
								else:
									showerror("ISSUE","MARKS SHOULD BE IN RANGE BETWEEN 0-100")
						else:
							showerror("ISSUE","LENGTH OF NAME SHOULD BE GREATER THAN 1")
					else:
						showerror("ISSUE","NAME SHOULD CONTAIN ONLY ALPHABETS")
			else:
				showerror("ISSUE","ROLL NUMBER SHOULD BE GREATER THAN 0")
	except Exception as e:
		showerror("issue",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
def f8():
	update_st.withdraw()
	root.deiconify()
	update_st_entrno.delete(0,END)
	update_st_entname.delete(0,END)
	update_st_entmarks.delete(0,END)
def f9():
	root.withdraw()
	delete_st.deiconify()
def f10():
	con=None
	try:
		con=connect("studentdata.db")
		sql="delete from student where rno='%s' "
		cursor=con.cursor()
		rno=delete_st_entrno.get()
		cursor.execute(sql %(rno))
		if cursor.rowcount==1:
			con.commit()
			showinfo("SUCCESS", "RECORD DELETED")
		else:
			showerror("FAILURE","RECORD NOT EXISTS")
	except Exception as e:
		showerror("issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close 
def f11():
	delete_st.withdraw()
	root.deiconify()
	delete_st_entrno.delete(0,END)
def f12():
	con=connect("studentdata.db")
	sql="select name ,cast( marks as integer) from student"
	cursor=con.cursor()
	cursor.execute(sql)
	name = [ ]
	marks = [ ]
	data=cursor.fetchall()
	for row in data:
		name.append(row[0])
		marks.append(row[1])
	plt.bar(name,marks)
	plt.xticks(name)
	plt.title("Students Performance")
	plt.xlabel("Name of the student")
	plt.ylabel("Marks of the student")
	plt.show()
def location():
	web_address= "https://ipinfo.io/"
	res= requests.get(web_address)
	data=res.json()
	city_name=data['city'].upper()

	a1 = "https://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city_name
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	web_add = a1+ a2+ a3
	res= requests.get(web_add)
	result = res.json()
	at = result['main']['temp']	
	msg="\t" + "\t"+"LOCATION:" + city_name+"\t"+ "\t" + "\t" +"TEMP:"+str(at)+ "\t" + "\t"+ "\t"+ "\t"+"\n"
	return msg
def qotd():
	web_add = "https://www.brainyquote.com/quote_of_the_day"
	res = requests.get(web_add)	
	data = bs4.BeautifulSoup(res.text, "html.parser")
	info = data.find("img", {"class":"p-qotd"})
	quote = info['alt']
	msg="\t"+"\t"+"QOTD:"+str(quote)+"\t"+"\t"+"\n"
	return msg
root=Tk()
root.title("ASHWINI MANAGEMENT SYSTEM")
root.geometry("465x400+400+200")
root.configure(background="lavender")
#mainwindow
btnAdd=Button(root, text="Add",width=10,font=('arial',15,'bold'),command=f1)
btnView=Button(root, text="View",width=10,font=('arial',15,'bold'),command=f3)
btnUpdate=Button(root, text="Update",width=10,font=('arial',15,'bold'),command=f6)
btnDelete=Button(root, text="Delete",width=10,font=('arial',15,'bold'),command=f9)
btnCharts=Button(root, text="Charts",width=10,font=('arial',15,'bold'),command=f12)
lblLocation=Label(root,text=location(), font=('arial',10,'bold'),borderwidth=1,relief="solid")
lblQotd=Label(root, text=qotd(), font=('arial',10,'bold'),borderwidth=1,relief="solid")
#show
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnCharts.pack(pady=10)
lblLocation.pack(anchor="w")
lblQotd.pack(anchor="sw")

#addwindow
add_st=Toplevel(root)
add_st.title("ADD STUDENT INFORMATION")
add_st.geometry("400x400+400+200")
add_st.configure(background="light blue")

add_st_lblrno=Label(add_st, text="enter rno", font=('arial',15,'bold'))
add_st_entrno=Entry(add_st,bd=5,font=('arial',15,'bold'))
add_st_lblname=Label(add_st,text="enter name",font=('arial',15,'bold'))
add_st_entname=Entry(add_st,bd=5,font=('arial',15,'bold'))
add_st_lblmarks=Label(add_st,text="enter marks",font=('arial',15,'bold'))
add_st_entmarks=Entry(add_st,bd=5,font=('arial',15,'bold'))
add_st_btnsave=Button(add_st,text="Save",font=('arial',15,'bold'),command=f5)
add_st_btnback=Button(add_st,text="Back",font=('arial',15,'bold'),command=f2)

add_st_lblrno.pack(pady=10)
add_st_entrno.pack(pady=5)
add_st_lblname.pack(pady=10)
add_st_entname.pack(pady=5)
add_st_entname.delete(0,END)
add_st_lblmarks.pack(pady=10)
add_st_entmarks.pack(pady=5)
add_st_btnsave.pack(pady=10)
add_st_btnback.pack(pady=10)
add_st.withdraw()

#viewwindow
view_st = Toplevel(root)
view_st.title("VIEW STUDENT INFORMATION")
view_st.geometry("500x400+400+200")
view_st.configure(background="#FFE4C4")

view_st_data = ScrolledText(view_st, width=41, height=10, font=('arial', 18, 'bold'))
view_st_btnback =Button(view_st, text="Back", font=('arial', 18, 'bold'), command=f4)

view_st_data.pack(pady=10)
view_st_btnback.pack(pady=10)
view_st.withdraw()


#updatewindow
update_st=Toplevel(root)
update_st.title("UPDATE STUDENT INFORMATION")
update_st.geometry("400x400+400+200")
update_st.configure(background="pink")

update_st_lblrno=Label(update_st, text="enter rno", font=('arial',15,'bold'))
update_st_entrno=Entry(update_st, bd= 5, font=('arial',15,'bold'))
update_st_lblname=Label(update_st, text="enter name", font=('arial',15,'bold'))
update_st_entname=Entry(update_st, bd=5, font=('arial',15,'bold'))
update_st_lblmarks=Label(update_st, text="enter marks", font=('arial',15,'bold'))
update_st_entmarks=Entry(update_st,bd=5, font=('arial',15,'bold'))
update_st_btnsave=Button(update_st,text="Save",font=('arial',15,'bold'),command=f7)
update_st_btnback=Button(update_st,text="Back",font=('arial',15,'bold'),command=f8)

update_st_lblrno.pack(pady=10)
update_st_entrno.pack(pady=5)
update_st_lblname.pack(pady=10)
update_st_entname.pack(pady=5)
update_st_lblmarks.pack(pady=10)
update_st_entmarks.pack(pady=5)
update_st_btnsave.pack(pady=10)
update_st_btnback.pack(pady=10)
update_st.withdraw()

#deletewindow
delete_st=Toplevel(root)
delete_st.title("DELETE STUDENT INFORMATION")
delete_st.geometry("400x300+400+200")
delete_st.configure(background="light blue")

delete_st_lblrno=Label(delete_st, text="enter rno", font=('arial',15,'bold'))
delete_st_entrno=Entry(delete_st, bd= 5, font=('arial',15,'bold'))
delete_st_btnsave=Button(delete_st,text="Save",font=('arial',15,'bold'),command=f10)
delete_st_btnback=Button(delete_st,text="Back",font=('arial',15,'bold'),command=f11)

delete_st_lblrno.pack(pady=10)
delete_st_entrno.pack(pady=10)
delete_st_btnsave.pack(pady=10)
delete_st_btnback.pack(pady=10)
delete_st.withdraw()

root.mainloop()
