#First_Name:Mirheybet
#Last_Name:Hasanov
#Proqram mahiyyeti:Sade bank islerini goren console interface'li bir proqram



def userBankinformationGENERATOR(userİnformationdictionary):
   
    print(f"Salam,{userİnformationdictionary['Istifadeci adi=>']} {userİnformationdictionary['Istifadeci soyadi=>']}")
    print('Oz shexsi bank hesabiniza dair melumatlari gormek isteyirsinizmi(+/-)*:')
    userPERSONALINFOAnswer=input('>>>   ')

  
    if(userPERSONALINFOAnswer=='+'):
        
        import random
        userSECURITY=random.randint(100000,1000000)

        print("Tehlukesizliyini qorumaq ucun aktiv telefon nomrenizi daxil edin:")
        userphone=input('AZE => +994')
        print('Bize guvendiyiniz ucun minnetdariq... ^-^ ')

        print('MIRIbank platformasindan telefonunuza gonderilen kod:' )
        print('>>>   ',userSECURITY)
        print(f'Zehmet olmasa,{userphone} nomresine gonderilen mesaj kodunu daxil edesiniz.Yanlis daxil etdiniz halda ,emeliiyat sonlanacaq ve prosesleri yeniden baslatmali olacaqsiz...')
        useraddSECURITY=int(input('>>>   '))
        if(userSECURITY==useraddSECURITY):
            print(userİnformationdictionary)
            print("Bank hesabiniz uzre hansisa emeliyyat icra etmek isteyirsinizmi(+/-)*?")
            usertoSYStemanswer=input('>>>   ')

            if(usertoSYStemanswer=='-'):
                print("Emeliyyat basa catdi!")
                print("Qeyd*:Yeni bir emeliyyat aparmaq isteyirsinizse,yeniden prosesleri basladin...")
            
            if(usertoSYStemanswer=='+'):
                print('Hesaba pul elave etmek isteyirsinizse,(1) duymesine klikleyin:')
                print('Hesabinizdan pul cekmek isteyirsinizse,(2) duymesine klikleyin:')
                userMONEYanswer=input('>>>   ')

                if(userMONEYanswer=='1'):
                    MONEYadd=int(input('Elave edeceyiniz pulu daxil edin(AZN): '))
                    print('Hesabiniz haqqinizda melumat:')
                    
                    print('Cari balans(AZN): ',userİnformationdictionary['Istifadecinin aktiv balansi(AZN)=>']+userİnformationdictionary['Istifadecinin rezerv balansi(AZN)=>']+MONEYadd)
                    print('Aktiv balans(AZN): ',userİnformationdictionary['Istifadecinin aktiv balansi(AZN)=>']+MONEYadd)
                    print('Rezerv balans(AZN): ',userİnformationdictionary['Istifadecinin rezerv balansi(AZN)=>'])
                    print('Emeliyyat ugurla basa catdi!')
                if(userMONEYanswer=='2'):
                    MONEYremove=int(input('Hesabdan cekeceyiniz pulu  qeyd edin(AZN): '))
                    if(MONEYremove>userİnformationdictionary['Istifadecinin umumi balansi(AZN)=>']):
                        print('Emeliyyat ugursuz oldu.Yeniden emeliyyat aparmaq ucun prosesleri yeniden basladin...')
                        print("QEYD:Bank hesabinizdan cekeceyiniz mebleg hazirki balansdan coxdur!")
                    
                    if(MONEYremove<=userİnformationdictionary['Istifadecinin umumi balansi(AZN)=>']):
                        print('Zehmet olmasa hesabdan pul cekmeyinizle bagli isteyinizi son olaraq bir daha tesdiqleyesiniz:(+/-)')
                        userENDanswer=input('>>>   ')
                        if(userENDanswer=='-'):
                            print('Emeliyyat sonlandirildi!')
                            print("Yeniden emeliyyat aparmaq ucun ,prosesleri yeniden basladin...")
                        if(userENDanswer=='+'):
                            print(f'Hesabinizdan {MONEYremove} AZN cixildi! ')
                            print('Cari balans(AZN): ',userİnformationdictionary['Istifadecinin aktiv balansi(AZN)=>']+userİnformationdictionary['Istifadecinin rezerv balansi(AZN)=>']-MONEYremove)
                            print('Rezerv balans(AZN): ',userİnformationdictionary['Istifadecinin rezerv balansi(AZN)=>'])
                            print('Emeliyyat ugurla basa catdi!')
        
        if(userSECURITY!=useraddSECURITY):
            print('!!!Yanlis daxiletme!!!')
            print("Emeliyyat sona catdi!")
            print("Qeyd*:Yeni bir emeliyyat aparmaq isteyirsinizse,yeniden prosesleri basladin...")
            False
    
    if(userPERSONALINFOAnswer=='-'):
        print("Emeliyyat sona catdi!")
        print("Qeyd*:Yeni bir emeliyyat aparmaq isteyirsinizse,yeniden prosesleri basladin...")
        False

    

                                                      
print('###############################################')

print("               ^ _ ^                    ")
print('Salam,MIRIbank-in platformasina xos gelmisiz...')
print('Qeyd edek ki,platformamizda hesablar uzre tehlukesizlik TCP protokolu uzerinden aparilir.')
print('TCP protokolu pul kocurmeleri,bank hesablari uzerinde emeliyyatlar aparilan zaman istifade olunan bir sebeke protokoludur.')
print('Davam etmek ucun asagidaki melumatlari doldurun...')
print("Istifadeci adini daxil edin: ")
userName=input(">>>   ")

print('Zehmet olmasa,cinsiyyetinizi daxil edin(K/Q)*: ')
gender=input('>>>   ')

if(gender.upper()=='K'):
    print(f'{userName} bey, zehmet olmasa,soyadinizi daxil edin: ')
    lastName=input(">>>   ")

if(gender.upper()=='Q'):
    print(f'{userName} xanim, zehmet olmasa,soyadinizi daxil edin: ')
    lastName=input(">>>   ")
    

import random
userBankBalance=random.randint(2000,10000)
userAddBalance=random.randint(2000,10000)
userWHOLEBankBalance=userBankBalance+userAddBalance

userİnformationdictionary={
    'Istifadeci adi=>' : userName,
    'Istifadeci soyadi=>': lastName,
    'Istifadecinin aktiv balansi(AZN)=>': userBankBalance,
    'Istifadecinin rezerv balansi(AZN)=>':userAddBalance,
    'Istifadecinin umumi balansi(AZN)=>':userWHOLEBankBalance
}


userBankinformationGENERATOR(userİnformationdictionary)













