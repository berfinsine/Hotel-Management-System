import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from uygulama_giris import*
from uygulama_odaekleme import*
from uygulama_musteriekleme import*
from rezervasyon import*
from datetime import datetime
import time
import re
import datetime
from suds.client import Client
import sys
from PyQt5 import QtWidgets,QtGui

#ana giriş sayfası
uygulama=QApplication(sys.argv)
pencere=QMainWindow()
ui1=Ui_MainWindow3()
ui1.setupUi(pencere)
pencere.show()

#misafir kayıt sayfası
uygulama2=QApplication(sys.argv)
pencere2=QMainWindow()
ui2=Ui_MainWindow()
ui2.setupUi(pencere2)

##veritabanı işlemleri
import sqlite3

con=sqlite3.connect("proje_odalar_denemetarih.db")
cursor=con.cursor()
con.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS odalar(odatipi text,odano int PRIMARY KEY,kisisayisi int,ucret int,odaaciklama text)")
con.commit()



#oda düzennleme sayfası
uygulama3=QApplication(sys.argv)
pencere3=QMainWindow()
ui3=Ui_MainWindow2()
ui3.setupUi(pencere3)


#rezervasyon sayfası
uygulama4=QApplication(sys.argv)
pencere4=QMainWindow()
ui4=Ui_MainWindow4()
ui4.setupUi(pencere4)


def Misafir_sayfasi_ac():
    pencere.close()
    pencere3.close()
    pencere2.close()
    pencere2.show()

def Oda_Düzenleme_ac():
    pencere.close()
    pencere3.show()

def Anaekranadon_misafirden():
    pencere2.close()
    pencere.show()

def Anaekranadon_odadan():
    pencere3.close()
    pencere.show()
def rezervasyon_ac():
    pencere.close()
    pencere4.show()

def Anaekranadon_rezervasyondan():
    pencere4.close()
    pencere.show()


## odalarla alakalı kısım
def oda_ekle():
    OdaTipi=ui3.lineEdit.text()
    OdaNo=ui3.lineEdit_2.text()
    KisiSayisi=ui3.lineEdit_3.text()
    Ucret=ui3.lineEdit_4.text()
    OdaAciklama=ui3.lneOdaAciklama.text()

    try:
        ekle="INSERT INTO odalar(odatipi,odano,kisisayisi,ucret,odaaciklama) VALUES (?,?,?,?,?)"
        cursor.execute(ekle,(OdaTipi,OdaNo,KisiSayisi,Ucret,OdaAciklama))
        con.commit()
        kayit_listele()
        ui3.lineEdit.clear()
        ui3.lineEdit_2.clear()
        ui3.lineEdit_3.clear()
        ui3.lineEdit_4.clear()
        ui3.lneOdaAciklama.clear()

        ui3.statusbar.showMessage("Kayıt ekleme işlemi başarılı",5000)

    except Exception as error:
        ui3.statusbar.showMessage("Kayıt ekleme sırasında hata oluştu=== "+str(error))

def kayit_listele():
    ui3.tableWidget.clear()
    ui3.tableWidget.setHorizontalHeaderLabels(("Oda Tipi","Oda No","Kişi Sayısı","Ücret","Oda Açıklaması"))
    ui3.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    sorgu="SELECT * FROM odalar "
    cursor.execute(sorgu)

    for indexSatir, kayitnumarasi in enumerate(cursor):
        for indexSutun,KayitSutun in enumerate(kayitnumarasi):
            ui3.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(KayitSutun)))


def kategoriye_gore_listele():
    listelenecek_odatipi=ui3.cmbOdaKategori.currentText()

    sorgu="SELECT * FROM odalar WHERE odatipi= ?"
    cursor.execute(sorgu,(listelenecek_odatipi,))
    ui3.tableWidget.clear()
    for indexSatir, kayitnumarasi in enumerate(cursor):
        for indexSutun,KayitSutun in enumerate(kayitnumarasi):
            ui3.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(KayitSutun)))


def oda_sil():
    sil_mesaj=QMessageBox.question(pencere,"Silme Onayı","Silmek istediğinizden emin misiniz?",QMessageBox.Yes,QMessageBox.No)

    if sil_mesaj== QMessageBox.Yes:
        secilen_oda= ui3.tableWidget.selectedItems()
        silinecek_oda= secilen_oda[1].text()

        sorgu="DELETE FROM odalar WHERE odano=?"
        try:
            cursor.execute(sorgu,(silinecek_oda,))
            con.commit()
            ui3.statusbar.showMessage("Kayıt başarıyla silindi",5000)
            kayit_listele()

        except Exception as error:
            ui3.statusbar.showMessage("Silme İşlemi Başarısız === "+str(error))
    else:
        ui3.statusbar.showMessage("Silme işlemi iptal edildi.",5000)


def oda_guncelle():
    guncelle_mesaj=QMessageBox.question(pencere,"Güncelleme Onayı","Bu odayı güncellemek istiyor musunuz?",QMessageBox.Yes,QMessageBox.No)

    if guncelle_mesaj==QMessageBox.Yes:
        try:
            OdaTipi=ui3.lineEdit.text()
            Odano=ui3.lineEdit_2.text()
            KisiSayisi=ui3.lineEdit_3.text()
            Ucret=ui3.lineEdit_4.text()
            OdaAciklama=ui3.lneOdaAciklama.text()

            cursor.execute("UPDATE odalar SET odatipi=?,kisisayisi=?,ucret=?,odaaciklama=? WHERE odano=?",(OdaTipi,KisiSayisi,Ucret,OdaAciklama,Odano))
            con.commit()
            kayit_listele()
            ui3.lineEdit.clear()
            ui3.lineEdit_2.clear()
            ui3.lineEdit_3.clear()
            ui3.lineEdit_4.clear()
            ui3.lneOdaAciklama.clear()
            ui3.statusbar.showMessage("Oda bilgileri başarıyla güncellendi",5000)

        except Exception as error:
            ui3.statusbar.showMessage("kayıt güncelleme sırasında hata oluştu ==="+str(error))
    else:
        ui3.statusbar.showMessage("oda güncelleme iptal edildi.")


### müşterilerle alakalı kısım

cursor.execute("CREATE TABLE IF NOT EXISTS musteriler(isim text,soyisim text,ıd int PRIMARY KEY,adres text,dogum_gunu text,telefon int,cinsiyet text,kayit_tarihi text)")
con.commit()



def musteri_ekle():
    Musteri_isim=ui2.lneIsim_3.text()
    Musteri_soyisim=ui2.lneSoyisim_3.text()
    Musteri_id = ui2.lneId_3.text()
    Musteri_adres=ui2.lneAdres_3.text()
    Musteri_tarih=ui2.dateEdit_3.date().toPyDate()
    Musteri_telefon=ui2.lneTelefon_3.text()
    Musteri_cinsiyet=ui2.comboBox.currentText()
    def tc_validation():
        TCURL = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?WSDL"
        client = Client(TCURL)
        a=ui2.dateEdit_3.date().toPyDate().year
        args = {"TCKimlikNo": ui2.lneId_3.text(), "Ad": ui2.lneIsim_3.text(), "Soyad": ui2.lneSoyisim_3.text(), "DogumYili": int(a)}
        return client.service.TCKimlikNoDogrula(**args) == True
    if tc_validation()==True:
        try:

            ekle = "INSERT INTO musteriler(isim,soyisim,ıd,adres,dogum_gunu,telefon,cinsiyet,kayit_tarihi) VALUES(?,?,?,?,?,?,?,?)"
            zaman = time.time()
            kayit_tarihi_getirme = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
            cursor.execute(ekle, (
            Musteri_isim, Musteri_soyisim, Musteri_id, Musteri_adres, Musteri_tarih, Musteri_telefon, Musteri_cinsiyet,
            kayit_tarihi_getirme))
            con.commit()
            musteri_kayit_listele()
            ui2.statusbar.showMessage("Müşteri kaydı oluşturuldu", 5000)

        except Exception as error:
            ui2.statusbar.showMessage("Müşteri kaydı oluşturulamadı=== " + str(error))
    else:
        ui2.statusbar.showMessage("TC,İsim veya Soyadı hatalı ",5000)

    tc_validation()
    ui2.lneIsim_3.clear()
    ui2.lneSoyisim_3.clear()
    ui2.lneId_3.clear()
    ui2.lneAdres_3.clear()
    ui2.lneTelefon_3.clear()




def musteri_kayit_listele():
    ui2.tblMusteri.clear()
    ui2.tblMusteri.setHorizontalHeaderLabels(("İSİM", "SOYİSİM", "TC KİMLİK", "ADRES", "DOĞUM TARİHİ","TELEFON","CİNSİYET","KAYIT TARİHİ"))
    ui2.tblMusteri.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



    sorgu="SELECT * FROM musteriler"
    cursor.execute(sorgu)
    for indexSatir_2, kayitnumarasi_2 in enumerate(cursor):
        for indexSutun_2,KayitSutun_2 in enumerate(kayitnumarasi_2):
            ui2.tblMusteri.setItem(indexSatir_2,indexSutun_2,QTableWidgetItem(str(KayitSutun_2)))


def Musteri_sil():
    sil_mesaj=QMessageBox.question(pencere2,"Silme Onayı","Silmek istediğinizden emin misiniz?",QMessageBox.Yes,QMessageBox.No)
    if sil_mesaj== QMessageBox.Yes:
        secilen_kisi= ui2.tblMusteri.selectedItems()
        silinecek_kisi= secilen_kisi[2].text()

        sorgu="DELETE FROM musteriler WHERE ıd=?"
        try:
            cursor.execute(sorgu,(silinecek_kisi,)) ## VİRGÜL UNUTMA
            con.commit()
            ui2.statusbar.showMessage("Kayıt başarıyla silindi",5000)
            musteri_kayit_listele()

        except Exception as error:
            ui2.statusbar.showMessage("Silme İşlemi Başarısız === "+str(error))
    else:
        ui2.statusbar.showMessage("Silme işlemi iptal edildi.",5000)

def Musteri_kayit_guncelle():
    guncelle_mesaj = QMessageBox.question(pencere2, "Güncelleme Onayı", "Bu kişinin bilgilerini güncellemek istiyor musunuz?",QMessageBox.Yes, QMessageBox.No)

    if guncelle_mesaj==QMessageBox.Yes:
        try:
            Musteri_isim = ui2.lneIsim_3.text()
            Musteri_soyisim = ui2.lneSoyisim_3.text()
            Musteri_id = ui2.lneId_3.text()
            Musteri_adres = ui2.lneAdres_3.text()
            Musteri_tarih = ui2.dateEdit_3.date().toPyDate()
            Musteri_telefon = ui2.lneTelefon_3.text()
            Musteri_cinsiyet = ui2.comboBox.currentText()

            cursor.execute("UPDATE musteriler SET adres=?,telefon=?,cinsiyet=? WHERE isim=? and soyisim=? and ıd=? and dogum_gunu= ? ",(Musteri_adres,
            Musteri_telefon,Musteri_cinsiyet,Musteri_isim,Musteri_soyisim,Musteri_id,Musteri_tarih))
            con.commit()
            musteri_kayit_listele()
            ui2.lneIsim_3.clear()
            ui2.lneSoyisim_3.clear()
            ui2.lneId_3.clear()
            ui2.lneAdres_3.clear()
            ui2.lneTelefon_3.clear()


            ui2.statusbar.showMessage("Kayıt Başarıyla güncellendi",5000)

        except Exception as error:
            ui2.statusbar.showMessage("Kayıt güncellenirken hata oluştu=== "+str(error))


### rezervasyonla alakalı kısımlar

def oda_bosluk_kontrol():
    Musteri_oda2=ui4.lneOda.text()
    cursor.execute("Select COUNT(id) FROM rezervasyon WHERE odano=? ",(Musteri_oda2,))
    sayi=cursor.fetchone()
    print(sayi)

    cursor.execute("select kisisayisi from odalar where odano=?",(Musteri_oda2,))
    kapasite=cursor.fetchall()

    cursor.execute("select cikis_tarihi from rezervasyon where odano=?",(Musteri_oda2,))
    kalinan_sayi=cursor.fetchall()
    print(kalinan_sayi)

    return kapasite >= sayi ==True


def rezervasyon_yap():
    def oda_bosluk_kontrol():
        global cikis4
        try:
            Musteri_oda2 = ui4.lneOda.text()
            cursor.execute("Select COUNT(id) FROM rezervasyon WHERE odano=? ", (Musteri_oda2,))
            sayi = cursor.fetchone()

            cursor.execute("select kisisayisi from odalar where odano=?", (Musteri_oda2,))
            kapasite = cursor.fetchone()

            cursor.execute("select distinct ciks from rezervasyon where odano=?", (Musteri_oda2,))
            cikis = cursor.fetchall()

            Giris_tarih2=ui4.giris_tarihi.date().toPyDate()
            print(type(Giris_tarih2))

            if len(cikis)>0:
                cikis2=cikis[0]
                cikis3=cikis2[0]
                y=int(cikis3[0:4])
                m=int(cikis3[5:7])
                d=int(cikis3[8:])
                cikis4=datetime.date(y,m,d)

                if Giris_tarih2>cikis4:
                    cursor.execute("Select COUNT(id) FROM rezervasyon WHERE odano=? and giris_tarihi=? ", (Musteri_oda2,Giris_tarih2,))
                    sayi2 = cursor.fetchone()
                    return (kapasite > sayi2) == True


            return(kapasite >sayi)  == True
        except Exception as error:
            ui4.statusbar.showMessage("Hata Var ==="+str(error))


    Musteri_isimsoyisim=ui4.lneisimsoyisim.text()
    Musteri_id=ui4.lneID.text()
    Musteri_oda=ui4.lneOda.text()
    Giris_tarih=ui4.giris_tarihi.date().toPyDate()
    Cikis_tarihi=ui4.cikis_tarihi.date().toPyDate()



    #giriş çıkış fark
    f=(Cikis_tarihi-Giris_tarih).days

    # CURSOR KISIMLARI
    cursor.execute('Select ıd from musteriler')
    ıdler=cursor.fetchall()
    cursor.execute('select odano from odalar')
    odalar1=cursor.fetchall()


    # ücret hesaplama
    if oda_bosluk_kontrol()==True:
        try:
            for k in odalar1:
                if int(Musteri_oda) in k:
                    sorgu='select ucret from odalar where odano=?'
                    cursor.execute(sorgu,(int(Musteri_oda),))
                    fiyat=cursor.fetchone()
                    fiyat1=fiyat[0]
                    odenecek_tutar = fiyat1 * f
                else:
                    ui4.statusbar.showMessage("oda bulunamadi",5000)
        except Exception as error:
            ui4.statusbar.showMessage("hata var ==="+str(error))

        try:
            for i in ıdler:
                for j in odalar1:
                    if int(Musteri_id) in i and int(Musteri_oda) in j:

                        ekle = "insert into rezervasyon(bilgi,id,odano,giris_tarihi,cikis_tarihi,tutar,giris,ciks) values(?,?,?,?,?,?,?,?)"
                        cursor.execute(ekle, (Musteri_isimsoyisim, Musteri_id, Musteri_oda,Giris_tarih,Cikis_tarihi,odenecek_tutar,Giris_tarih,Cikis_tarihi))
                        con.commit()
                        rezervasyon_listele()
                        ui4.statusbar.showMessage("Rezervasyon yapıldı", 5000)



        except Exception as error:
            ui4.statusbar.showMessage("Rezervasyon yapılamadı==="+str(error),5000)
    else:
        ui4.statusbar.showMessage("Oda Kapasitesi Dolu ",5000)

def rezervasyon_listele():
    ui4.tblrezervasyon.clear()
    ui4.tblrezervasyon.setHorizontalHeaderLabels(("İSİM SOYİSİM","ID","ODA NO","GİRİŞ TARİHİ","ÇIKIŞ TARİHİ","ÜCRET"))
    ui4.tblrezervasyon.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    sorgu = "SELECT bilgi,id,odano,giris_tarihi,cikis_tarihi,tutar FROM rezervasyon"
    cursor.execute(sorgu)
    for indexSatir_5, kayitnumarasi_5 in enumerate(cursor):
        for indexSutun_5, KayitSutun_5 in enumerate(kayitnumarasi_5):
            ui4.tblrezervasyon.setItem(indexSatir_5, indexSutun_5, QTableWidgetItem(str(KayitSutun_5)))


def rezervasyon_sil():
    sil_mesaj = QMessageBox.question(pencere4, "Silme Onayı", "Silmek istediğinizden emin misiniz?", QMessageBox.Yes,
                                     QMessageBox.No)
    if sil_mesaj== QMessageBox.Yes:
        secilen_rezervasyon= ui4.tblrezervasyon.selectedItems()
        silinecek_rezervasyon= secilen_rezervasyon[0].text()

        sorgu="DELETE FROM rezervasyon WHERE bilgi=?"

        try:
            cursor.execute(sorgu,(silinecek_rezervasyon,))
            con.commit()
            ui4.statusbar.showMessage("Kayıt başarıyla silindi",5000)
            rezervasyon_listele()

        except Exception as error:
            ui4.statusbar.showMessage("Silme İşlemi Başarısız === "+str(error))
    else:
        ui4.statusbar.showMessage("Silme işlemi iptal edildi.",5000)



#odalarla alakalı butonlar
ui3.pbEkle.clicked.connect(oda_ekle)
ui3.pushButton_4.clicked.connect(kayit_listele) #pblistele
ui3.pbKategori.clicked.connect(kategoriye_gore_listele)
ui3.pbSil.clicked.connect(oda_sil)
ui3.pbGuncelle.clicked.connect(oda_guncelle)


##müşterilerle alakalı butonlar
ui2.pbMusterikayit_4.clicked.connect(musteri_ekle)
ui2.pushButton_8.clicked.connect(musteri_kayit_listele)
ui2.pbMusteriSil_4.clicked.connect(Musteri_sil)
ui2.pushButton_7.clicked.connect(Musteri_kayit_guncelle)


##rezervasyon butonlar
ui4.pbkaydet.clicked.connect(rezervasyon_yap)
ui4.pblistele.clicked.connect(rezervasyon_listele)
ui4.pbsil.clicked.connect(rezervasyon_sil)
ui4.pbanaekran.clicked.connect(Anaekranadon_rezervasyondan)


#butonlar
ui1.PbMisafirkayit.clicked.connect(Misafir_sayfasi_ac)
ui1.PbOdaduzenleme.clicked.connect(Oda_Düzenleme_ac)
ui2.pushButton_9.clicked.connect(Anaekranadon_misafirden)
ui3.pushButton.clicked.connect(Anaekranadon_odadan)
ui1.pushButton.clicked.connect(rezervasyon_ac)




sys.exit(uygulama.exec())
