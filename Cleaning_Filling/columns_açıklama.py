# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:35:56 2022

@author: hp
"""
--------
1-url:
*null değer yok 
*15919 unique değer var:
*url linkleri araç bilgilerini getiren sayfayı açması gerekiyor,fakat linklerden 
sayfalara ulaşılmıyor 
dtype: object
*satır içinde 0 dan başlayarak numaralar verilmiş,bu temizlenebilir yada index 
numaraları olarak düzenlenebilir.

----

2-make_model:
Audi A3           3097
Audi A1           2614
Opel Insignia     2598
Opel Astra        2526
Opel Corsa        2219
Renault Clio      1839
Renault Espace     991
Renault Duster      34
Audi A2              1
Name: make_model, dtype: int64

*3 farklı marka var Audi,Opel,Renault
*markalar kendi aralarında nominal,kendi içlerinde ise ordinal değerlendirilebilir
*null değer yok 
*dtype: object


------
3-short_description:
*Araçlarla ilgili kısa açıklamalar yapılmış
*TDI,FSI,TFSI,TSI,GDI  En çok bu ifadeler geçiyor 
*46 null değer var

TDI: Turbocharged Direct Injection (Turbo Beslemeli Direkt Enjeksiyonlu):
    
Volkswagen’in kullandığı turbo dizel motorun adıdır.Turbo şarj sistemine sahip
olan bu motorlar, dünyadaki ilk seri üretim turbo dizel motorlardandır. 
Dünya çapında düşük yakıt tüketimi ve uzun kilometre dayanıklılığı ile ün salmıştır

FSI: Fuel Stratified Injection (Direkt Benzin Enjeksiyonu):

*Fsi motorlarda, yakıt standart motorlardaki gibi manifolda değil,
direkt yanma odasına püskürtme yapılır.
*Asıl amacı, düşük yakıt tüketimi.
*FSI teknolojine sahip motorlarda yakıt,
çok ince partiküllerden oluşan sprey şeklinde doğrudan yanma odasına püskürtülür.
Bu sayede yanmadan atılacak olan yakıtın önüne geçilmiş ve yakıt tasarrufu sağlanmış,
motordan alınan verim artmıştır.

TFSI: Turbo Fuel Stratified Injection.(Turbo Beslemeli Direkt Benzin Enjeksiyonlu Motor.):

Tfsi motorda yakıt, talebe bağlı olarak kontrol edilen yüksek basınçlı bir pompa
ile sağlanan bir ortak yakıt sistemi yoluyla püskürtülür. Emme supaplarının 
arasında yer alan bir enjektörle yakıt doğrudan yanma odasına milisaniyelik 
hassasiyetle ve 110 bara varan basınçla püskürtülüyor. Yakıt/hava karışımı 
yanma odasında bütünüyle homojen bir şekilde dağıtılır. Bu da TFSI motoru 
diğer motorlardan ayıran ve bütün motor devirlerinde yüksek performans 
sağlayan en önemli özelliktir.

TSI: Çift Şarjlı (Turbo Ve Supercharger) Direkt Enjeksiyonlu Motor:

TSI (Turbo Supercharger Injection), küçük hacimli motora (1.4 lt gibi)
Turbo ve kompresörün eklenmesiyle oluşmuş bir teknolojidir. 
İlk kalkıştan itibaren emrinize hazır bekleyen motorda turbo devreye girene
kadar kompresör size eşlik ediyor. Bu sayede turbo motorlu araçların büyük bir
kısmında yaşanan “Turbo Boşluğu” kompresörün varlığıyla ortadan kalkmış olmaktadır.
TSI motorun az yakmasının nedeni kompresör sayesinde turbo çalışıncaya kadar
turbo boşluğunu kapatması ve böylece düşük devirlerde vites atılabilmesidir.



GDI Motor:
‘Gasoline direct injection’ kelimelerinin kısaltılmasıdır. 
‘Doğrudan benzin püskürtmeli’ motor anlamına gelir.
Mitsubishi’nin ürettiği bir motor teknolojisidir.
Bu tip motorlara, düşük yakıt tüketimi ve yüksek güç sağlayan özellikler ; 
dik ve düz emme borusu, eğimli piston başı, yüksek basınçlı yakıt pompası
ve yüksek basınçlı, döndürme hareketi sağlayan enjektörlerdir. 
GDI motorun iki farklı çalışma modu vardır. Motorun ekonomik çalışma modunda, 
yakıt, sıkıştırma zamanı sırasında silindire püskürtülür ve ekonomik bir şekilde 
normal güç elde edilir. Motorun güç modunda ise, yakıtın küçük bir bölümü emme 
zamanı sırasında püskürtülür ve geri kalanı kısmı da sıkıştırma zamanında püskürtülür.
Böylece daha iyi yanma ve daha yüksek güç elde edilir
(ama ekonomik moda göre daha fazla yakıt tüketilir).
detaylı link:
https://www.tech-worm.com/araclardaki-tdi-fsi-tfsi-tsi-gdi-nedir/#:~:text=TDI%3A%20Turbocharged%20Direct%20Injection%20(Turbo,seri%20%C3%BCretim%20turbo%20dizel%20motorlardand%C4%B1r.

-------------------------------------------------------------------

4-Body Type:
Sedans           7903
Station wagon    3553
Compact          3153
Van               783
Other             290
Transporter        88
Off-Road           56
Coupe              25
Convertible        8

*9 unique değer var
*60 null değer içeriyor 
*Nominal kategori 
*dtype: object

Gövde Tipi; Kasa yapılarına göre gövde tipleri;  
Hatchback : Arkası Kambur (Örn: Golf),   
Sedan : Arkası Çıkıntılı (Fiat Linea),   
Coupe : İki Kapılı/Arkası Dar (Scirocco),  
SUV : Arazi Aracı (BMW X5),  
MPV : Çok Amaçlı (Renault Scenic),
Cabrio : Üstü Açılır/İki kapılı (Opel Cascada),  
Roadster : Üstü Açılır/2 Kişilik (BMW Z4), 
Kombi : Geniş Bagaj/Çift Kabin (VW Caddy),  
St.Wagon : Arkası Uzun (Passat Variant).

Sedans:
Sedan, iki yada dört kapılı, en az dört kişilik, sabit şaseli ve dörtten
fazla penceresi olan kapalı binek taşıtlardır. Kısacası iki veya dört kapılı
dörtten fazla kişinin seyahat edebildiği uzun şaseli araçlardır. 
Sedan araçların iç konforları  da oldukça ileri düzeydedir.  

Station wagon:
Gövdesi kapalı, arka şekli daha geniş bir iç hacim sağlayacak şekilde 
dizayn edilmiş, üst tavanı sabit ve sert tavanlı, bununla birlikte tavanın 
bir kısmının açılma özelliği olabilen, sürücüden başka en az 3 oturma yeri 
ve en az iki sırası bulunan (sıra ve sıralar öne yatmak veya çeşitli 
şekillerde hareket ettirilmek        

Coupe:

Gövde kapalı, genellikle daratılmış arka hacimli, üst tavanı sabit,
sert tavanlı, bununla birlikte bazı modellerde açılabilir tavanı olan,
sürücü oturma yerinden başka en az bir oturma yeri ve enaz bir sırası bulunan,
iki taraflı kapılara sahip, ayrıca arka kapağıda açılabilen 2 
eya daha fazla kenar pencereli otomobillerdir.    


Van:
Sürücü bölmesi ve yükleme alanı tek bir birimde olan kamyon,
yük taşımaya meyillidir ve içinde yolcu taşıyamazsınız ayrıca yolcu koltuğu yoktur
*ruhsat kamyonet olarak işlendiği için vergileri genel anlamda transporterlara 
göre yüksektir
*Bu gövde, malların taşınması için tamamen uyarlanmıştır. 
*Minibüsler, arabalar ve kamyonlar arasında bir geçiş seçeneğidir. 
*Geniş bir yüksek kargo alanı ile donatılmış arka kapı, pencere yok

Transporter:
Koltuk bulunur ve yolcu taşınabilir. 

Off-Road:
4*4 özel arazi araçlarıdır


Convertible:
Üstü açık otomobil kategorisi, yalnızca dünyaca ünlü üstü açık araba değil,
aynı zamanda roadster, brogam, targa, fayton, örümcek ve diğerleri de dahil
olmak üzere çeşitli modelleri içerir.




---------------------------------------------------------------------------------
5-Price:
*Araç fiyatları belirtildi
*Null değer yok 
*dtype: float64
*Para birimini bu column a bakarak anlayamıyoruz


-------------------------------------------------------------------------------- 
6-Vat:
VAT deductible      10980
Price negotiable      426
*dtype: object
*4513 null değer 
*2 kategori var (Nominal)
Devletlerin kazançlarını ve ekonomiyi arttırmak için kullandığı vergi türüne 
Value Added Tax denmektedir. 
Türkçe adı ile Vat numarası Katma Değer Vergisi anlamına gelmektedir. 

VAT deductible :İndirilebilir KDV, KDV'nin tamamını (veya bir kısmını) geri
talep edebileceğiniz ticari amaçlı harcamaları ifade eder.
Satın alma işlemi yalnızca işletmeniz içinse, 
KDV'nin tamamını geri talep edebilirsiniz.
Hem ticari hem de özel kullanımın bir karışımıysa, 
KDV'nin ticari kısmını talep edebilirsiniz.
Örneğin, cep telefonunuzu %50'si iş amaçlı, %50'si kişisel kullanım için
kullanıyorsanız, satın alma fiyatının %50'sini ve aylık faturanızı talep edebilirsiniz

Price negotiable:
Pazarlık, bir malın fiyatını veya kesin olarak kurulmamış bir sözleşmeyi 
tanımlamak için kullanılır, yani şartlar değiştirilebilir.
Pazarlık, şartların tamamının veya bir kısmının ilgili taraflarca 
ayarlanabileceği yasal bir sözleşmeye atıfta bulunabilir.


-------------------------------------------------------------------------------------------
7-km:
*null değer yok
*dtype: object   verildi.
*veriler "56,013" km formatında girildi km ler temizlenip dtype float olarak 
değiştirilebilir
*Araçların yaptıkları total km yi belirtir.

---------------------------------------------------------------------------------------
8-registration:
*Ruhsat tarihini belirtmiş 
*dtype: object
*06/2016 formatında tarihler girildi düzenlenip date formatına dönüştürülebilir
*Bu column un aynısı "First Registration" olarak var.veriler [\n, 2017, \n]
şeklinde girildi. 
df_[["registration","First Registration"]] şeklinde incelendiğinde her satırın 
tarihlerinin aynı olduğu görülüyor
*null deger gozukmuyor fakat -/- seklinde girdiler var 
*bunlar diger columnda null olarak girilmis

--------------------------------------------------------------------------------------
9-prev_owner:
*Aracı önceden kaç kişi kullandığı belirtilmiş
*1 previous owner     8294
*2 previous owners     778
*3 previous owners      17
*4 previous owners       2
*dtype: object
*Ordinal kategori?
*6828 null değer var 


--------------------------------------------------------------------------------------------
10-kW
*Kw bir birimdir ve uzun ifadesi kilowatt olan enerji biriminin kısaltılmış halidir.
Kilowatt elektrikle ilgili bir birim olup, enerjinin saate bölünmesiyle hesaplanır.
Uluslararası bir birim olan araç kw değeri elektrik faturalarında ve
motorlu taşıtlarda beygir gücünün hesaplanmasında kullanılır.
*Tüm değerler null 
*column datadan direkt çıkartılabilir?
*hP column u verilmiş hP den kw hesaplanabilir yada sade hP ile devam edilebilir
*araç beygir gücü değeri ise 0,745 kw yapmaktadır.
*yani hP*0.745 bize kW ı verecektir 
*araç Kw değeri 1,341 ile çarpılarak araç Hp değeri elde edilir.
---------------------------------------------------------------------------------
11-hP
* araç beygir gücü(Horse Power) belli bir zamanda belli bir yükün yer 
değiştirmesi aşamasında gerekli olan güç miktarıdır.

*Araçların kalkması, hız alması ve erişebileceği azami hız değerini elde 
edebilmek için çok önemli olan motor gücü genelde beygir gücü ile ifade edilir.
Beygir gücü, bir atın 75 kg lık bir yükü 1 metre yer değiştirmesi için harcadığı güçtür. 
hp=kW*1341

*nul değer gözükmüyor fakat "-" olarak girdiler var bunlar düzenlenecek
*dtype: object veriler 125 kW formatında girilmiş kw temizlenip dtype int a 
çevrilebilir

----------------------------------------------------------------------------------
12-Type
--------------------------------------------
13-Previous Owners:
*muhtepelen "prev_owner" column u ile aynı
*veriler "\n1\n " formatında çok kirli girilmiş
*df_[["prev_owner","Previous Owners"]] incelemesi yapıldığında iki column verilerinin
tamamen aynı olduğu görülüyor.

*1 previous owner      n1
*2 previous owners     n2
*3 previous owners     n3
*4 previous owners     n4

*iki columndan herhangi biri temizlenip diğeri çıkartılabilir.Kolaylık açısından
"prev_owner" columnu daha temiz gözüküyor.
*6640 null değer var . "prev_owner" columun dan daha az.çünkü "prev_owner" da 
gözüken bazı null değerler burada n0 olarak girilmiş 


------------------------------------------------------------------------
14-"Next Inspection"
*Sıradaki araç muayenesini belirtiyor 
*12384 null değer var
* girilen veriler "[\n03/2020\n, \n99 g CO2/km (comb)\n] " şeklinde girildi.
*buradaki 99 g CO2/km (comb),aracın km deki co2 salımınını gösteriyor
*03/2020 formatında ise muane tarihi belirtilmiş 


-----------------------------------------------------------------------------
15-"Inspection new"
*son muanenin yapılma durumunu belirtiyor olabilir 
*11987 null değer var 
*veriler genel olarak "[\nYes\n, \n99 g CO2/km (comb)\n]" formatında girildi
*yes muanesi yapıldı bilgisi olabilir 


--------------------------------------------------------------------------------
16-Warranty
*5420 null deger var
*veriler genellikle '[\n6 months\n, \n103 g CO2/km (comb)\n]' formatinda girilmis
*buradan 6 months gibi girilen kisim garanti suresi olabilir 

--------------------------------------------------------------------------------
17-Full Service
*Aracin yillik servis bakiminin yaptirilmasi
*Detayli arac bakimi icerir
*7704 null deger var 
*veriler genellikle '[\n, \n, \n124 g CO2/km (comb)\n]' formatinda girilmis
*Anlasilir ortak veri cok gozukmuyor 
*124 g CO2 gibi girdiler araci km basi co2 salinim miktari olabilir 

-------------------------------------------------------------------------
18-'Non-smoking Vehicle'

*Aracta sigara kullanilip kullanilmadigi bilgisi 
*8742 null deger var 
*veriler genellikle '[\n, \n, \n4 (Green)\n]'  ve ' [\n, \n]'
*girilen bilgiler anlasilir degil null olabilecek baska girdiler var 


---------------------------------------------------------------------------
19-null
*null deger gozukmuyor fakat tum girdiler null 
* [] formatinda girildi 

--------------------------------------------------------------------------
20-Make
*3 arac markasi girilmis 
*null deger yok
*Nominal kategori 
*veriler  \nAudi\n formatinda girildi temizlenmesi gerekiyor
\nOpel\n       7343
\nAudi\n       5712
\nRenault\n    2864

-------------------------------------------------------------------------
21-Model

[\n, A3, \n]          3097
[\n, A1, \n]          2614
[\n, Insignia, \n]    2598
[\n, Astra, \n]       2526
[\n, Corsa, \n]       2219
[\n, Clio, \n]        1839
[\n, Espace, \n]       991
[\n, Duster, \n]        34
[\n, A2, \n]             1

*null deger yok 
*df_[["make_model","Make","Model"]]  incelendiginde 'make_model' bilgisi 
diger iki column un tum bilgilerini iceriyor 
*'Make' ve 'Model' columnlari silinerek 'make_model' uzerinden devam edilebilir


-------------------------------------------------------------------------------

22-Offer Number

*3175 null deger var 
* veriler genellikle "[\nSL0500396\n]" formatinda girilmis 

-------------------------------------------------------------------------------
23-First Registration 
**Ruhsat tarihini belirtmiş 
*dtype: object
*06/2016 formatında tarihler girildi düzenlenip date formatına dönüştürülebilir
*Bu column un aynısı "Registration" olarak var.
df_[["registration","First Registration"]] şeklinde incelendiğinde her satırın 
tarihlerinin aynı olduğu görülüyor
*1597 null deger var


-------------------------------------------------------------------------------
24-Body Color
*govde renkleri bilgisi var
*597 null deger var
*veriler " [\n, Grey, \n]" formatinda girildi,temizleme yapildiktan sonra 
duzgun bir gorunum olusacak

[\n, Black, \n]     3745
[\n, Grey, \n]      3505
[\n, White, \n]     3406
[\n, Silver, \n]    1647
[\n, Blue, \n]      1431
[\n, Red, \n]        957
[\n, Brown, \n]      289
[\n, Green, \n]      154
[\n, Beige, \n]      108
[\n, Yellow, \n]      51
[\n, Violet, \n]      18
[\n, Bronze, \n]       6
[\n, Orange, \n]       3
[\n, Gold, \n]         2

-------------------------------------------------------------------------------
25-Paint Type
[\nMetallic\n]       9794
[\nUni/basic\n]       347
[\nPerl effect\n]       6

*3 Farkli tip girdileri var Nominal kategori 
*5772 null deger var 

------------------------------------------------------------------------------------

26-Body Color Original
*3759 null deger var
*1927 unique renk var 
*"[\nKokosnuss braun\n]" genel girilen format 


-------------------------------------------------------------------------------
27-Upholstery(Doseme) 
*46 unique deger var
*3720 null deger var 
* veriler genel olarak [\nCloth, Black\n] formatinda girildi




-----------------------------------------------------------------
# 28 Body	            : 4. sütundaki açıklamaya bakınız
# 29 Nr. of Doors	    : Kapı sayısı(Bagajla birlikte) --> int
# 30 Nr. of Seats	    : Koltuk sayısı -- int
# 31 Model Code	        : Araba model kodu -- object(nominal) -- ATILABİLİR AYTEKIN HOCAM : ATALIM GİTSİN DİYOR
# 32 Gearing Type	    : Vites türü --> Categorik(Ordinal)
# 33 Displacement	    : Motor hacmi(cc türünden) -- categorik değişkene çevirilip aralık belirlenebilir
# 34 Cylinders	        : Kaç silindirli olduğu -- categorik(ordinal) -- bazı unique değerler atılabilir. 5 silindir hangi markaya ait incelenebilir. Belki sadece belli bir marka 5 silindir
# 35 Weight	            : Araç ağırlığı  -- int
# 36 Drive chain	    : Ön takım zincir türü -->object(nominal)
# 37 Fuel	            : Yakıt tipi(Motorin vs) --> Object(ordinal) -- sıkıntılı
# 38 Consumption	    : Yakıt tüketim miktarı(100km de)(Şehir içi, Şehir dışı(comb??))
# 39 CO2 Emission	    : Arabalardan ne kadar CO2 saldığı km başına gr cinsinden -- int
	# Dizel motorlu taşıtlarda, absorpsiyon katsayısı Normal emişli dizel motorlarda 2,5 m-1, Aşırı doldurmalı dizel motorlarda ( Turbo Şarjlı ) 3,0 m-1, 2010 yılından sonra üretilmiş dizel motorlarda 1,5 m-1 sınır değeri geçemeyecek
# 40 Emission Class     :  ----------
# 41 \nComfort & Convenience\n	 : Araç içi özellikler(Comfort & Convenience açısından) --> categorik(nominal) -- unique değerler birleştirebilir
# 42 \nEntertainment & Media\n	 : Araç içi özellikler(Entertainment & Media açısından) --> categorik(nominal) -- unique değerler birleştirebilir
# 43 \nExtras\n	                 : Extra araç özellikleri --> category(ordinal)
# 44 \nSafety & Security\n	 : Araç özellikleri(Safety & Security açısından) --> category(ordinal)
# 45 description	                 : Araç tanımı -- category(nominal) -- AYTEKIN HOCAM: çöp diyebiliriz
# 46 Emission Label		 : ------------
# 47 Gears	                 : Vites sayısı  -- categorik(nominal)
# 48 Country version	         : (Sanırım) hangi ülkede üretildiği -- category(nominal)
# 49 Electricity consumption	 : Elektrik tüketim miktarı(Elektirikli arabalar için değerler olabilir- NaN ları atmak mantıklı olmayabilir) -- categorik(nominal)
# 50 Last Service Date	         : Son muayene tarihi -- object ama 2 ayrı sütun yapılabilir içindeki bilgilerden ama çok fazla nan var
# 51 Other Fuel Types	         : Bu veride NAN haricindeki değerler saçma yazım hataları, bir anlamı olmayabilir. Bunu direk atabiliriz
# 52 Availability	             : Satın alındıktan sonra kaç günde ulaştığı(Sanırım) -- categorik -- aralık belirlenip dummy ye atılabilir
# 53 Last Timing Belt Service Date : Son Triger kayışı servis tarihi :D :D :D --> string olabilir(Date harici değerler var) -- Ama direk atacağız heralde
# 54 Available from                : Piyasaya gireceği tarih -- nominal -- diğer değerlere unknown yazmak mantıklı mı ???

# Yarın
    # Drop edilecek sütunları drop edelim(benzer olanlar, null değerler, karışık olduğundan dolayı)
    # 