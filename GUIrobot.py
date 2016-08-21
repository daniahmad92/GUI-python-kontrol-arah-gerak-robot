import serial           # import libarary serial
import time             # import library pewaktu
import msvcrt           # import libarary keyboard
from Tkinter import *   # import library Tkinter untuk membuat GUI
	

def maju():
	arduino.write('K')
	
def mundur():
	arduino.write('M')
	

def kiri():
	arduino.write('Z')
	

def kanan():
	arduino.write('A')
	

def stop():
	arduino.write('O')


print 'Proses Koneksi...'
arduino = serial.Serial("COM4", 9600)
time.sleep(3)
print 'Telah Terkoneksi dengan Baik'

GUI_kontrol = Tk() # membuat aplikasi GUI
GUI_kontrol.wm_title("GUI KONTROL ROBOT") #Membuat Judul GUI Di Bagian Kiri Atas
GUI_kontrol.config(bg = "#828481")


# Kontrol Frame GUI
controlFrame = Frame(GUI_kontrol, width=150, height = 150, bg="#037481",\
                     highlightthickness=2, highlightbackground="#111")
# mendefinisikan kontrol frame
controlFrame.grid() #posisi kontrol frame

btnFrame = Frame(controlFrame, width=150, height = 150, bg="white")
# mendefinisikan tombol Button
btnFrame.grid() #posisi frame button

about = "GUI KONTROL ROBOT"
name = Label(btnFrame, width=20, height=1, text=about, font="bold", \
             justify=CENTER, bg="white")
name.grid(row=0, column=2)

button_maju = Button(btnFrame, text="MAJU", command=maju, bg="green")
#mendefinisikan button maju
button_maju.grid(row=2, column=2, padx=5, pady=5)
#posisi button maju

button_mundur = Button(btnFrame, text="MUNDUR", command=mundur, bg="green")
#mendefinisikan button mundur
button_mundur.grid(row=4, column=2, padx=5, pady=5)
#posisi button mundur

button_kiri = Button(btnFrame, text="KIRI", command=kiri, bg="green")
#mendefinisikan button kiri
button_kiri.grid(row=3, column=0, padx=5, pady=5)
#posisi button kiri

button_kanan = Button(btnFrame, text="KANAN", command=kanan, bg="green")
#mendefinisikan button kanan
button_kanan.grid(row=3, column=3, padx=5, pady=5)
#posisi button kanan

button_stop = Button(btnFrame, text="STOP", command=stop, bg="red")
#mendefinisikan button stop
button_stop.grid(row=3, column=2, padx=5, pady=5)
#posisi button stop

GUI_kontrol.mainloop()# membentuk looping program
