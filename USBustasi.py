import os, sys, time

class rənglər:

    cyan = '\033[0;36m'
    magenta = '\033[0;95m'

isoyolu = input("ISO faylını terminal pəncərəsinə dartıb buraxın.\nISO-ya gedən Yol: " )

print(rənglər.magenta, "Aşağıdaki siyahıdan ISO faylını yazmaq istədiyiniz USB-ni seçin. ")
məsləhət = "\n Lazım olan USB yaddaşı tapmağın ən rahat yolu USB-ni çıxardıb yenidən taxmaq\
\n və ikinci dəfə görünən əlavə USB-ni seçməkdir :)" 
print(rənglər.cyan, məsləhət)

xodda = input(" USB-ni çıxardın və <enter> düyməsinə basın: ");
os.system('sudo -S ls -l /dev/disk/by-id/*usb*')
ekşın = input(" İndi USB-ni qoşun və <enter> düyməsinə basın: ")
time.sleep(2)
os.system('sudo -S ls -l /dev/disk/by-id/*usb*')
print(rənglər.magenta)
usb = input(" İndi isə ISO faylını yazmaq istədiyiniz USB yaddaşı seçin.\
            \n Unutmayın ki, seçdiyiniz USB drive format olunacaq!\
            \n Buna görə də, düzgün seçim edin!\
            \n QEYD: Seçiminizi /dev/sdf şəklində daxil edin. sd-dən sonrakı hərfi\
            \n USB-ə uyğun dəyişin. sdX-dən sonra rəqəm(1, 2) yazmayın: ")

print(rənglər.magenta, "\n Hardasa bitdi. İndi kofenizi hazırlayın və \
əməliyyatın bitməsini gözləyin :)")

os.system('sudo dd if=%s of=%s' %(isoyolu, usb))
