# Yaz Lab 2 Proje 2
 Yazılım Geliştirme Laboratuvarı 2 - 2. Proje: Sıralama Algortitmaları
 <br>
 201307061 Edanur Yazıcı - 201307067 Ela Karaoğlu
 <br>
 Proje Raporu Linki: 
 
<b>Proje Özeti</b>
<br>
Bu proje Pyhton programlama dili ve wx.Pyhton vb. kütüphaneler kullanılarak PyCharm aracılığıyla, kullanıcıların etkileşimli olarak sıralama algoritmalarını ve görsel temsilleri keşfedebilecekleri bir sol panel ve bir ana panelden oluşan bir ara yüz tasarlamayı amaçlamaktadır. Sol panel, kaydırılabilir bir kontrol ile boyut ve hız seçeneklerini ayarlamak için çubuklar içermektedir. Bu seçeneklerin altındaki radyo düğmeleri, kullanıcıların Seçimli Sıralama, Kabarcık Sıralama, Ekleme Sıralama, Birleştirme Sıralama ve Hızlı Sıralama gibi sıralama algoritmalarını seçmesine olanak tanır. Ek olarak, Dağılım Grafiği, Çubuk Grafiği ve Kök Grafiği dâhil olmak üzere grafik türlerini seçmek için bir açılır liste sağlanacaktır.
Ana panel, kullanıcının sol paneldeki seçimlerine göre dinamik olarak görsel bir ara yüz sunacaktır. Bir sıralama algoritması seçildiğinde, ara yüz seçilen algoritmaya göre sıralama işlemlerini gerçekleştirecektir. Sonuçlar, sıralama sürecinin anlaşılmasını geliştirmek için renk kodlu temsiller kullanılarak görselleştirilecek ve sol panelden kullanıcının belirlediği hız değeri ile renk kodları birleştirilip bir akış sağlanmaktadır.
<br>
<b>Projenin Geliştirilme Ortamı</b>
<br>
Bu proje, Python programlama dili ve wxPython vb. kütüphaneleri kullanarak PyCharm IDE'si üzerinden tasarlanmıştır. 
PyCharm sürümü olarak: Pycharm-community-2023.1.2
Pyhton sürümü olarak: pyhton-3.10.9 amd64
wxPython sürümü olarak: wxpyhton 4.0.4
<br>
Projenin Çalışır Hale Getirilmesi
<br>
Projenin bilgisayarınız üzerinde sorunsuz çalışması için ilk öncelikle “Projenin Geliştirilme Ortamı” başlığı altında sürümleri de verilmiş programları indirmeniz gerekmektedir. İndirme işlemlerini tamamladıktan sonra ilk öncelikle Pyhton kurulumunu sağlamalısınız. Daha sonrasında Pycharm kurulumunu gerçekleştirmelisiniz. Bu aşamada proje kodlarını açabilir ve inceleyebilirsiniz ama etkin bir şekilde çalışması için PyCharm üzerinden projenize wxPyhton kütüphanesini dahil etmeniz gerekir. Pycharm üzerinde proje klasörü açıkken sol yukarıda ki 4 çizgi üzerine basıp:
File--> Settings--> Project: proje_adınız--> Pyhton Interpreter seçeneğine basın buradan sonra sağ paneldeki listeden devam edin.
Sağ paneldeki listeden: pip --> arama kısmına: wxpyhton yazın ve aşağıda gözükecek olan ‘install’ butonuna basınız. Eğer sürüm 4.0.4 olarak seçili değilse ‘Specify Version’ yazan kısmın tikini işaretleyin ve açılan listeden 4.0.4 sürümünü seçerek ‘install’ butonuna basın.
Bu aşamaları sorunsuz bir şekilde tamamladığınızda Sıralama Algoritmaları projesini başarılı ve etkin bir şekilde kendi bilgisayarınızda da çalıştırabilirsiniz.

<br>
<b>Proje Ekranları</b>

