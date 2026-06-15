# Virtual Memory Ders 13-14 - Sinav Mentor Notu

Kaynak slaytlar:
- `Ders13_Virtual memory1.pdf`
- `Ders14_Virtual memory2.pdf`

Bu not slayt sirasina bagli kalir. Amac: sinavdan once "hocanin sorabilecegi" tanimlari, formulleri, karsilastirmalari ve islem mantigini sade dille yakalamak.

---

## 1. Background ve Virtual Memory Mantigi

### 1. Teknik Dili Sadelestir

Bir programi otelde kalan bir misafir gibi dusun. Misafirin butun esyalarini odasina yigmana gerek yoktur; sadece o anda kullanacagi valiz, kiyafet ve belgeler odada dursa yeter. Geri kalan esyalar depoda bekleyebilir.

Virtual memory de ayni mantiktir: Programin tamamini fiziksel RAM'e almak zorunda degiliz. O anda gerekli olan parcalar RAM'de, diger parcalar disk/swap alaninda durabilir.

Programci buyuk bir mantiksal bellek varmis gibi dusunur; isletim sistemi bunu daha kucuk fiziksel bellekle idare eder.

### 2. Hocalar Sever / Sinavda Cikar

Sanal bellek tanimi:

```text
Virtual memory = mantiksal belleğin fiziksel bellekten ayrilmasidir.
```

Sınavda buradan vururlar:
- Programin tumu ayni anda gerekli olmayabilir.
- Program fiziksel RAM boyutu ile sinirli kalmaz.
- Daha az RAM kullanildigi icin ayni anda daha fazla program calisir.
- CPU utilization ve throughput artabilir.
- Daha az I/O yapilabilir, cunku gereksiz kisimlar yuklenmez.

### 3. Ozet: Aklinda Kalsin

- Virtual memory, programciya buyuk bellek varmis hissi verir.
- Fiziksel bellekte sadece gereken page'ler tutulur.
- Mantiksal adres alani fiziksel adres alanindan buyuk olabilir.
- Daha fazla process ayni anda calisabilir.

### 4. Beni Test Et

1. Virtual memory neyi neyden ayirir?
   - Cevap: Mantiksal bellegi fiziksel bellekten ayirir.
2. Programin tamamini RAM'e yuklememenin bir avantaji nedir?
   - Cevap: Ayni anda daha fazla program calisir / daha az I/O olur.
3. Virtual memory sayesinde mantiksal adres alani fiziksel adres alanindan nasil olabilir?
   - Cevap: Daha buyuk olabilir.

---

## 2. Virtual Address Space

### 1. Teknik Dili Sadelestir

Virtual address space'i bir sehir haritasi gibi dusun. Haritada yollar duzgun, sirali ve bitisik gorunur. Ama gercekte sehrin altindaki altyapi parca parca farkli yerlere dagilmis olabilir.

Process kendi bellegini bitisik ve duzenli gorur. Gercekte fiziksel RAM page frame'lere bolunmustur ve process'in page'leri RAM'in farkli yerlerinde olabilir.

Stack ve heap'i de iki kisinin ayni koridorda birbirine dogru yurumesi gibi dusun:
- Heap yukari dogru buyur.
- Stack asagi dogru buyur.
- Aradaki bos alan hole'dur.

### 2. Hocalar Sever / Sinavda Cikar

Sınavda buradan vururlar:
- Virtual address space, process'in bellekte nasil depolandigina iliskin mantiksal/sanal gorunumdur.
- Process 0 gibi belirli bir mantiksal adresten basliyormus gibi gorunebilir.
- Stack maksimum mantiksal adresten baslar ve asagi buyur.
- Heap yukari buyur.
- Stack ile heap arasindaki kullanilmamis kisim hole'dur.
- Sanal bellek page sharing ile system library, shared memory ve process olusturmayi verimli hale getirir.

### 3. Ozet: Aklinda Kalsin

- Process belleği bitisik gorur, RAM'de parca parca olabilir.
- Stack asagi, heap yukari buyur.
- Aradaki bosluk hole'dur.
- Paylasilan kutuphaneler ve shared memory sanal bellekle kolaylasir.

### 4. Beni Test Et

1. Stack hangi yonde buyur?
   - Cevap: Asagi dogru.
2. Heap hangi yonde buyur?
   - Cevap: Yukari dogru.
3. Stack ile heap arasindaki kullanilmamis alana ne denir?
   - Cevap: Hole.

---

## 3. Demand Paging

### 1. Teknik Dili Sadelestir

Demand paging'i kargo sirketi gibi dusun. Magazadaki her urunu eve tasimazsin; ne zaman ihtiyacin olursa o urun depodan gelir.

Page'ler de boyle: Program baslarken tum page'ler RAM'e yuklenmez. Sadece process bir page'e ihtiyac duydugunda o page diskten RAM'e getirilir.

### 2. Hocalar Sever / Sinavda Cikar

Demand paging tanimi:

```text
Page sadece ihtiyaç duyulduğunda belleğe getirilir.
```

Sınavda buradan vururlar:
- Page'e referans verilirse ve page RAM'de degilse page fault olur.
- Gecersiz referans varsa process sonlandirilir.
- Page diskteyse RAM'e getirilir.
- Pure demand paging: Process hicbir page'i RAM'de olmadan baslar; ilk komut bile page fault yaratir.
- Pager tum process'i degil, sadece gerekli page'leri getirir.

### 3. Ozet: Aklinda Kalsin

- Demand paging: Gerektikce getir.
- RAM'de olmayan page'e erisim page fault'tur.
- Pure demand paging'de baslangicta hic page RAM'de olmayabilir.
- Amaç gereksiz I/O ve RAM kullanimini azaltmaktir.

### 4. Beni Test Et

1. Demand paging'de page ne zaman RAM'e getirilir?
   - Cevap: Ihtiyac duyuldugunda.
2. RAM'de olmayan ama gerekli olan page'e erisim ne olusturur?
   - Cevap: Page fault.
3. Pure demand paging ne demektir?
   - Cevap: Process baslarken page'lerinin hicbiri RAM'de olmayabilir.

---

## 4. Valid-Invalid Bit ve Page Fault Isleme

### 1. Teknik Dili Sadelestir

Valid-invalid bit'i otel oda karti gibi dusun:
- Kart yesilse oda hazir: valid.
- Kart kirmiziysa oda hazir degil ya da oraya giremezsin: invalid.

Process bir page'e erismek ister. Page table'a bakilir. Eger page bellekteyse valid. Bellekte degilse invalid ve page fault olusur.

### 2. Hocalar Sever / Sinavda Cikar

```text
v = in-memory / memory resident
i = not-in-memory
```

Page fault proseduru:
1. Referans gecerli mi, gecersiz bellek erisimi mi kontrol edilir.
2. Referans gecersizse process sonlandirilir.
3. Gecerliyse bos frame bulunur.
4. Istenen page diskten frame'e okunur.
5. Page table ve dahili tablolar guncellenir.
6. Kesilen komut yeniden baslatilir.

Sınavda buradan vururlar:
- Baslangicta page table girisleri invalid olabilir.
- Page fault her zaman hata anlamina gelmez; page'in RAM'de olmamasi da page fault yaratir.
- Page fault'tan sonra komut restart edilebilmelidir.

### 3. Ozet: Aklinda Kalsin

- Valid: page RAM'de.
- Invalid: page RAM'de degil veya erisim gecersiz.
- Page fault gelirse once referansin legal olup olmadigi kontrol edilir.
- Page geldikten sonra instruction restart gerekir.

### 4. Beni Test Et

1. Valid bit neyi gosterir?
   - Cevap: Page'in bellekte oldugunu.
2. Invalid referans kesinlikle neye yol acar?
   - Cevap: Process sonlandirilir.
3. Page fault'tan sonra kesilen komut ne yapilmalidir?
   - Cevap: Yeniden baslatilmalidir.

---

## 5. Demand Paging Donanim Destegi, Free-Frame List ve Zero-Fill

### 1. Teknik Dili Sadelestir

Free-frame list'i bos otel odalari listesi gibi dusun. Yeni misafir gelince resepsiyon once bos oda listesine bakar.

Page fault olunca OS, diskten gelen page'i koymak icin bos frame arar. Bu bos frame'ler free-frame list'te tutulur.

Zero-fill-on-demand ise yeni verilen odayi once temizlemek gibidir. Eski misafirin bilgileri kalmasin diye frame sifirlanir.

### 2. Hocalar Sever / Sinavda Cikar

Demand paging icin gereken destek:
- Page table: valid-invalid bit veya koruma biti kullanir.
- Secondary memory: RAM'de olmayan page'ler burada tutulur.
- Swap device / swap space: Page'lerin tutuldugu disk alani.
- Free-frame list: Bos frame havuzu.
- Zero-fill-on-demand: Bos frame verilmeden once sifirlanir.

### 3. Ozet: Aklinda Kalsin

- Page fault cozumunde bos frame gerekir.
- Bos frame'ler free-frame list'te tutulur.
- Swap space RAM'de olmayan page'leri tutar.
- Zero-fill-on-demand guvenlik ve temizlik icindir.

### 4. Beni Test Et

1. RAM'de olmayan page'ler diskte hangi alanda tutulur?
   - Cevap: Swap space.
2. Bos frame havuzuna ne denir?
   - Cevap: Free-frame list.
3. Zero-fill-on-demand ne yapar?
   - Cevap: Frame'i kullanmadan once sifirlar.

---

## 6. Demand Paging Performansi ve EAT

### 1. Teknik Dili Sadelestir

Page fault'u markette kasaya gelince urunun depoda oldugunu fark etmeye benzet. Normalde kasadan gecmek 2 saniye surecekti; ama urun depodan gelirse dakikalarca beklersin.

Bellek erisimi cok hizlidir, page fault ise disk I/O yuzunden cok yavas olabilir. Bu yuzden cok kucuk page fault orani bile sistemi yavaslatir.

### 2. Hocalar Sever / Sinavda Cikar

Formul:

```text
EAT = (1 - p) x memory access time + p x page fault time
```

Slayt ornegi:

```text
Memory access time = 200 ns
Page fault service time = 8 ms = 8,000,000 ns

EAT = (1 - p) x 200 + p x 8,000,000
EAT = 200 + p x 7,999,800
```

Eger 1000 erisimden 1'i page fault ise:

```text
p = 0.001
EAT = 200 + 0.001 x 7,999,800
EAT = 8,199.8 ns = yaklasik 8.2 mikrosaniye
```

Sınavda buradan vururlar:
- p = 0 ise page fault yok.
- p = 1 ise her referans page fault.
- EAT page fault oraniyla dogru orantilidir.

### 3. Ozet: Aklinda Kalsin

- Page fault disk I/O yuzunden pahali.
- EAT formulu kesin bilinmeli.
- p cok kucuk olsa bile EAT buyuk artabilir.
- Page fault orani artarsa performans duser.

### 4. Beni Test Et

1. EAT formulu nedir?
   - Cevap: `(1-p) x bellek erisimi + p x page fault suresi`
2. p = 0 ne demektir?
   - Cevap: Page fault yoktur.
3. Slayt orneginde p = 0.001 iken EAT yaklasik kac olur?
   - Cevap: 8.2 mikrosaniye.

---

## 7. Swap Space Optimizasyonlari

### 1. Teknik Dili Sadelestir

Dosya sistemini sehir ici trafik, swap space'i ise direkt otoyol gibi dusun. Swap space daha duz, daha az arama gerektiren, daha hizli bir alandir.

### 2. Hocalar Sever / Sinavda Cikar

Swap space I/O neden dosya sistemi I/O'dan hizli olabilir?
- Daha buyuk bloklarla tahsis edilir.
- File lookup yoktur.
- Indirect allocation gibi dosya sistemi ek maliyetleri yoktur.

Iki yaklasim:
1. Process basinda dosya goruntusunu swap space'e kopyala, sonra demand paging'i swap space'ten yap.
   - Dezavantaj: Baslangicta kopyalama maliyeti.
   - Eski BSD Unix'te kullanilmis.
2. Baslangicta dosya sisteminden demand page yap, page degistirilecekse swap space'e yaz.

### 3. Ozet: Aklinda Kalsin

- Swap space genelde dosya sistemi I/O'dan hizlidir.
- Baslangicta tum image'i swap'a kopyalamak hizli paging saglar ama ilk maliyeti vardir.
- Alternatif: Once file system'den getir, sonra gerekirse swap'a yaz.

### 4. Beni Test Et

1. Swap space I/O neden hizlidir?
   - Cevap: Buyuk bloklar ve daha az dosya sistemi ek maliyeti.
2. Eski BSD Unix hangi yaklasimi kullanmistir?
   - Cevap: Baslangicta dosya goruntusunu swap space'e kopyalama.
3. Swap space hangi tur bellek alanidir?
   - Cevap: Diskte RAM'de olmayan page'ler icin kullanilan alan.

---

## 8. Copy-on-Write

### 1. Teknik Dili Sadelestir

Copy-on-write'i fotokopi makinesi gibi dusun. Iki kisi ayni belgeyi sadece okuyacaksa iki ayri kopya cikarmaya gerek yok. Ama biri belgeye not yazmaya baslarsa, o kisiye ayri kopya verilir.

`fork()` ile child process olusunca parent'in tum page'lerini hemen kopyalamak pahali olabilir. COW der ki: "Once paylasin; biri yazmaya kalkarsa o page'i kopyalariz."

### 2. Hocalar Sever / Sinavda Cikar

Sınavda buradan vururlar:
- COW hizli process olusturma saglar.
- Yeni child process'e atanacak page sayisini azaltir.
- Parent ve child baslangicta ayni page'leri paylasir.
- Paylasilan page'ler copy-on-write olarak isaretlenir.
- Process'lerden biri paylasilan page'e yazarsa o page'in kopyasi olusturulur.
- `fork()`tan sonra child genellikle `exec()` cagirabilir; bu durumda tum adres alanini bastan kopyalamak gereksizdir.

### 3. Ozet: Aklinda Kalsin

- COW = yazana kadar kopyalama yok.
- Parent-child baslangicta page'leri paylasir.
- Yazma olursa sadece ilgili page kopyalanir.
- `fork()` performansini iyilestirir.

### 4. Beni Test Et

1. COW ne zaman kopya olusturur?
   - Cevap: Paylasilan page'e yazma oldugunda.
2. COW en cok hangi sistem cagrisiyla iliskilidir?
   - Cevap: `fork()`.
3. COW neden hizlidir?
   - Cevap: Baslangicta tum adres alanini kopyalamaz.

---

## 9. Page Replacement Temeli

### 1. Teknik Dili Sadelestir

RAM'i dolu bir kitaplik gibi dusun. Yeni kitap gelecek ama raflar dolu. Bir kitabi secip depoya kaldirman gerekir. Iste page replacement bu "hangi kitabi kaldiralim?" sorusudur.

### 2. Hocalar Sever / Sinavda Cikar

Over-allocation:

```text
Process'lerin ihtiyac duydugu frame sayisi fiziksel belleği asarsa over-allocation olur.
```

Bos frame yoksa:
1. Istenen page'in diskteki konumu bulunur.
2. Bos frame aranir.
3. Bos frame varsa kullanilir.
4. Yoksa victim frame secilir.
5. Victim page gerekiyorsa diske yazilir.
6. Page table guncellenir.
7. Yeni page frame'e getirilir.

Modify bit:
- Page degistirilmemisse diske yazmaya gerek yoktur.
- Degistirilmisse page out gerekir.
- Modify bit page fault servis maliyetini azaltir.

Sınavda buradan vururlar:
- Bos frame yoksa iki aktarim gerekebilir: page out + page in.
- Bu page fault suresini ikiye katlayabilir.

### 3. Ozet: Aklinda Kalsin

- Page replacement: Bos frame yoksa kurban page secme isidir.
- Victim page degistirilmisse diske yazilir.
- Modify bit gereksiz disk yazmayi engeller.
- Page replacement demand paging'in temelidir.

### 4. Beni Test Et

1. Victim frame ne demektir?
   - Cevap: Yer acmak icin secilen kurban frame.
2. Bos frame yoksa page fault servisinde hangi iki aktarim olabilir?
   - Cevap: Page out ve page in.
3. Modify bit ne ise yarar?
   - Cevap: Page degismediyse diske yazmayi engeller.

---

## 10. Page Replacement Algoritmalari: FIFO, OPT, LRU

### 1. Teknik Dili Sadelestir

Uc farkli kutuphane gorevlisi dusun:

- FIFO gorevlisi: "Rafa ilk gelen kitap ilk gider."
- OPT gorevlisi: "Gelecegi biliyorum; en gec kullanilacak kitabi kaldiririm."
- LRU gorevlisi: "Gecmise bakarim; en uzun suredir kullanilmayan kitabi kaldiririm."

### 2. Hocalar Sever / Sinavda Cikar

#### FIFO

```text
FIFO = ilk gelen page ilk cikar.
```

Slayt uyarisi:
- FIFO basit ama kotu karar verebilir.
- Belady's Anomaly gorulebilir.

Belady's Anomaly:

```text
Bazi page replacement algoritmalarinda frame sayisi artinca page fault sayisi azalmak yerine artabilir.
```

Slayt ornegi:

```text
Reference string: 1,2,3,4,1,2,5,1,2,3,4,5
3 frame -> 9 page fault
4 frame -> 10 page fault
```

#### OPT

```text
OPT = gelecekte en uzun sure kullanilmayacak page'i cikarir.
```

Sınavda buradan vururlar:
- En dusuk page fault oranina sahiptir.
- Belady anormalliginden etkilenmez.
- Uygulamada zordur; cunku gelecek referans string'i bilinmelidir.
- Karsilastirma/benchmark icin kullanilir.
- Slayt orneginde 3 frame ile 9 page fault verir.

#### LRU

```text
LRU = en uzun suredir kullanilmayan page'i cikarir.
```

Sınavda buradan vururlar:
- Gelecege degil gecmise bakar.
- Slayt orneginde 12 page fault verir.
- FIFO'dan iyi, OPT'den kotu olabilir.
- Genellikle iyi sonuc verir.
- Donanim destegi gerekebilir.
- Belady anormalliginden etkilenmez.

LRU uygulama yontemleri:
1. Counter implementation:
   - Her page entry'sinde sayac vardir.
   - Page'e referans verilince saat sayaca kopyalanir.
   - Degisimde en kucuk sayac aranir.
2. Stack implementation:
   - Page'e referans verilince stack'in tepesine tasinir.
   - En son kullanilan tepede, en az kullanilan alttadir.
   - Double linked list ile uygulanabilir.

### 3. Ozet: Aklinda Kalsin

- FIFO: Ilk giren ilk cikar, Belady olabilir.
- OPT: En iyi ama gelecegi bilmek gerekir.
- LRU: Gecmise bakar, Belady yoktur.
- OPT ve LRU stack algorithms sinifindadir.

### 4. Beni Test Et

1. Belady's Anomaly nedir?
   - Cevap: Frame sayisi artinca page fault sayisinin artabilmesi.
2. OPT hangi page'i cikarir?
   - Cevap: Gelecekte en uzun sure kullanilmayacak page'i.
3. Slayt orneginde LRU kac page fault verir?
   - Cevap: 12.

---

## 11. LRU Approximation ve Additional-Reference-Bits

### 1. Teknik Dili Sadelestir

Gercek LRU'yu tutmak pahaliysa, bunu yoklama listesiyle tahmin edersin. "Bu kitap son zamanlarda kullanildi mi?" diye isaret koyarsin.

Referans biti bu isaret gibi calisir. Page'e her erisimde bit 1 olur. Sonra sistem zaman zaman bu bitleri inceleyerek hangi page'lerin yakin zamanda kullanildigini tahmin eder.

### 2. Hocalar Sever / Sinavda Cikar

Reference bit:
- Baslangic degeri 0.
- Page'e referans verildiginde donanim tarafindan 1 yapilir.
- Kullanilma sirasi tam bilinmez ama yakin zamanda kullanildi mi anlasilir.

Additional-Reference-Bits:
- Her page icin ornegin 8 bitlik bilgi tutulur.
- Bu 8 bit son 8 zaman dilimindeki kullanim gecmisidir.
- Page'e referans yapilinca en anlamli bit 1 yapilir.
- Her zaman araligi sonunda bitler saga kaydirilir, en anlamli bit 0 yapilir.
- En kucuk bit degerine sahip page LRU'ya en yakin kabul edilir.
- Ayni en kucuk degere sahip page'ler varsa FIFO ile secilebilir.

### 3. Ozet: Aklinda Kalsin

- Gercek LRU pahali olabilir.
- Reference bit, LRU tahmini icin kullanilir.
- Additional-reference-bits, son kullanim gecmisini bitlerle tutar.
- En dusuk bit degeri en iyi kurban adayidir.

### 4. Beni Test Et

1. Reference bit ne zaman 1 olur?
   - Cevap: Page'e referans verildiginde.
2. Additional-reference-bits algoritmasinda en kucuk bit degeri neyi gosterir?
   - Cevap: LRU'ya en yakin page'i.
3. 8 bitlik deger neyi temsil eder?
   - Cevap: Son 8 zaman araligindaki kullanim gecmisini.

---

## 12. Second-Chance ve Enhanced Second-Chance

### 1. Teknik Dili Sadelestir

Second-chance'i sinavda son anda yoklama alan hoca gibi dusun:
- "Bu ogrenci yakin zamanda derse katildi mi?"
- Katildiysa hemen silmiyor, bir sans daha veriyor.
- Katilmadiysa listeden cikiyor.

Clock algoritmasi ise bu listeyi dairesel bir saat gibi dolasir.

### 2. Hocalar Sever / Sinavda Cikar

Second-chance:
- FIFO'ya benzer ama page'e ikinci sans verir.
- Clock algorithm olarak da adlandirilir.
- Reference bit kontrol edilir:

```text
Reference bit = 0 -> page degistirilir.
Reference bit = 1 -> ikinci sans verilir, bit 0 yapilir, sonraki page'e gecilir.
```

Dairesel kuyruk:
- Pointer sonraki kurban adayini gosterir.
- Pointer reference bit 0 bulana kadar ilerler.
- Ilerlerken reference bitleri temizler.

Enhanced Second-Chance:

Reference bit ve modify bit birlikte kullanilir:

```text
(0,0) -> yakin zamanda kullanilmadi, degistirilmedi: en iyi kurban
(0,1) -> kullanilmadi ama degistirildi: diske yazmak gerekir
(1,0) -> kullanildi, degistirilmedi
(1,1) -> kullanildi ve degistirildi: en kotu kurban adaylarindan
```

En dusuk sinif degeriyle karsilasilan ilk page degistirilir.

### 3. Ozet: Aklinda Kalsin

- Second-chance = FIFO + reference bit.
- Reference bit 1 ise ikinci sans alir.
- Clock algoritmasi dairesel kuyrukla uygulanir.
- Enhanced second-chance hem reference hem modify bit'e bakar.

### 4. Beni Test Et

1. Second-chance algoritmasinin diger adi nedir?
   - Cevap: Clock algorithm.
2. Reference bit 1 ise ne olur?
   - Cevap: Page ikinci sans alir, bit 0 yapilir.
3. Enhanced second-chance'te en iyi kurban sinifi hangisidir?
   - Cevap: `(0,0)`.

---

## 13. Counting-Based, Page Buffering ve Raw I/O

### 1. Teknik Dili Sadelestir

Counting-based algoritmalari kutuphanede kitaplarin kac kez odunc alindigini saymaya benzet. Az alinan kitabi kaldirmak LFU, cok alinan kitabi kaldirmak MFU mantigidir.

Page buffering ise mutfakta hazir tabak bulundurmak gibi: Misafir gelince once tabak yikamayi beklemezsin, hazir tabagi verirsin.

Raw I/O ise restoranda garsonu atlayip direkt mutfaktan almak gibi: Dosya sistemi hizmetlerini atlar.

### 2. Hocalar Sever / Sinavda Cikar

Counting-based:
- LFU: Least Frequently Used. En az kullanilan page degistirilir.
- MFU: Most Frequently Used. En cok kullanilan page degistirilir; cunku dusuk sayacli page yeni gelmis ve henuz kullanilmamis olabilir varsayimi vardir.
- Bu algoritmalar yaygin degildir, uygulanmasi pahalidir.

Page-buffering:
- Bos frame havuzu tutulur.
- Page fault olunca istenen page, victim disk'e yazilmadan once bos frame'e yerlestirilebilir.
- Process daha hizli devam eder.
- Modified page list tutulabilir.
- Disk bosta iken degistirilmis page'ler diske yazilir, modify bit sifirlanir.
- Bos frame havuzunda page'in eski icerigi duruyorsa tekrar I/O gerekmeden kullanilabilir.

Applications and page replacement:
- Veritabanlari gibi uygulamalar kendi bellek yonetimini OS'ten daha iyi bilebilir.
- OS I/O buffer ve uygulama buffer ayni page'in iki kopyasini tutabilir.
- Raw disk / raw I/O dosya sistemi hizmetlerini atlar.
- Raw I/O; demand paging, file locking, prefetching gibi dosya sistemi hizmetlerini bypass eder.

### 3. Ozet: Aklinda Kalsin

- LFU az kullanilani, MFU cok kullanilani cikarir.
- Page buffering page fault bekleme suresini azaltmaya yardim eder.
- Modified page list, diske yazma maliyetini onde yapar.
- Raw I/O ozel uygulamalar icin dosya sistemi katmanini atlar.

### 4. Beni Test Et

1. LFU hangi page'i degistirir?
   - Cevap: En az referans almis page'i.
2. Page buffering'in amaci nedir?
   - Cevap: Page fault sonrasi process'i daha hizli devam ettirmek.
3. Raw I/O neyi atlar?
   - Cevap: Dosya sistemi hizmetlerini.

---

## 14. Allocation of Frames

### 1. Teknik Dili Sadelestir

Frame allocation'i apartmandaki oda paylasimi gibi dusun. Her aileye en az yasayabilecegi kadar oda vermen gerekir. Cok az oda verirsen herkes surekli esya tasir, hayat yavaslar.

### 2. Hocalar Sever / Sinavda Cikar

Process'lere minimum frame verilmelidir.
- Frame sayisi azalirsa page fault orani artar.
- Page fault orani artarsa process yavaslar.
- Minimum frame sayisi mimari tarafindan belirlenir.
- Maksimum frame sayisi fiziksel bellekle sinirlidir.

Fixed allocation:
1. Equal allocation:

```text
m frame, n process varsa her process m/n frame alir.
```

2. Proportional allocation:

```text
S = toplam process boyutu = toplam si
ai = (si / S) x m
```

Slayt ornegi:

```text
m = 62 frame
s1 = 10
s2 = 127
S = 137

a1 = (10 / 137) x 62 = 4
a2 = (127 / 137) x 62 = 57
```

### 3. Ozet: Aklinda Kalsin

- Her process'e yeterli frame verilmezse page fault artar.
- Equal allocation herkes esit alir.
- Proportional allocation process boyutuna gore dagitir.
- Formul: `ai = (si / S) x m`

### 4. Beni Test Et

1. Frame sayisi azalirsa page fault orani ne olur?
   - Cevap: Artar.
2. Equal allocation formulu nedir?
   - Cevap: `m/n`.
3. Proportional allocation'da `ai` nasil hesaplanir?
   - Cevap: `(si / S) x m`.

---

## 15. Global vs Local Allocation ve Reclaiming Pages

### 1. Teknik Dili Sadelestir

Global allocation'i okul kantinindeki ortak sandalye sistemi gibi dusun. Her sinif diger siniftan sandalye alabilir.

Local allocation ise her sinifin kendi sandalyesi olmasidir. Daha duzenlidir ama bazi siniflarda bos sandalye varken diger sinif sikisabilir.

### 2. Hocalar Sever / Sinavda Cikar

Global replacement:
- Tum frame'ler arasindan kurban secilebilir.
- Bir process baska process'in frame'ini alabilir.
- Process performansi dis kosullardan etkilenebilir.
- Genellikle daha yuksek system throughput saglar.
- Daha yaygindir.

Local replacement:
- Process sadece kendi frame'leri arasindan kurban secer.
- Process basina daha tutarli performans saglar.
- Bellek verimsiz kullanilabilir.

Reclaiming pages:
- OS bos frame listesinin sifira dusmesini beklemez.
- Minimum esik altina dusunce page reclaim baslar.
- Maksimum esige ulasana kadar page'ler geri alinir.
- Maksimum esikte reclaim durur.

### 3. Ozet: Aklinda Kalsin

- Global: baskasinin frame'i alinabilir, throughput yuksek.
- Local: sadece kendi frame'in, performans tutarli.
- Reclaiming bos frame listesini esikler arasinda tutar.
- Minimum altinda reclaim baslar, maksimumda durur.

### 4. Beni Test Et

1. Global replacement'ta bir process baskasinin frame'ini alabilir mi?
   - Cevap: Evet.
2. Local replacement'in avantaji nedir?
   - Cevap: Process basina daha tutarli performans.
3. Reclaiming ne zaman baslar?
   - Cevap: Bos frame listesi minimum esigin altina dusunce.

---

## 16. NUMA ve Frame Tahsisi

### 1. Teknik Dili Sadelestir

NUMA'yi kampuste farkli yemekhaneler gibi dusun. Sana en yakin yemekhane hizli, uzaktaki yemekhane yavas. Bellek de bazi CPU'lara yakin, bazi CPU'lara uzaktir.

### 2. Hocalar Sever / Sinavda Cikar

NUMA:
- Non-Uniform Memory Access.
- Tum bellek bolgelerine erisim suresi esit degildir.
- Belirli CPU, belleğin bazi bolgelerine daha hizli erisir.
- Amaç process'in calistigi CPU'ya mumkun oldugunca yakin frame tahsis etmektir.

Solaris:
- `lgroups` yani locality groups kullanir.
- CPU ve bellekleri gecikme yakinligina gore gruplar.
- Process'in thread'lerini ve bellek tahsisini ayni grup icinde tutmaya calisir.
- Mümkün degilse yakin gruplari secer.

### 3. Ozet: Aklinda Kalsin

- NUMA'da bellek erisim sureleri esit degildir.
- Yakindaki bellek daha hizlidir.
- NUMA-aware VM, CPU'ya yakin frame verir.
- Solaris lgroups kullanir.

### 4. Beni Test Et

1. NUMA acilimi nedir?
   - Cevap: Non-Uniform Memory Access.
2. NUMA-aware sistem page fault'ta hangi frame'i tercih eder?
   - Cevap: Process'in calistigi CPU'ya yakin frame'i.
3. Solaris bu problemi hangi yapıyla cozer?
   - Cevap: lgroups / locality groups.

---

## 17. Thrashing

### 1. Teknik Dili Sadelestir

Thrashing'i surekli esya tasiyan ama hic ders calismayan ogrenci gibi dusun. Ogrenci zamaninin cogunu kitaplari odadan depoya, depodan odaya tasimakla geciriyor; ders calismaya vakit kalmiyor.

Process de komut calistirmak yerine surekli page getirip goturuyorsa thrashing vardir.

### 2. Hocalar Sever / Sinavda Cikar

Thrashing tanimi:

```text
Bir process, komutlarini yurutmekten daha fazla zamani paging yaparak geciriyorsa thrashing olmustur.
```

Sınavda buradan vururlar:
- Page fault orani muazzam artar.
- EAT artar.
- CPU utilization duser.
- CPU scheduler dusuk CPU kullanimi gorunce multiprogramming derecesini artirmaya calisabilir.
- Bu daha fazla page fault yaratir ve durum kotulesir.
- Thrashing durdurmak icin multiprogramming derecesi dusurulmelidir.

Grafik mantigi:
- Multiprogramming derecesi artinca CPU utilization once artar.
- Bir noktadan sonra thrashing baslar.
- CPU utilization keskin duser.

### 3. Ozet: Aklinda Kalsin

- Thrashing = is yapmak yerine page tasimak.
- Page fault orani ve EAT artar.
- CPU utilization duser.
- Cozum: Process'lere yeterli frame vermek / multiprogramming'i azaltmak.

### 4. Beni Test Et

1. Thrashing ne zaman olur?
   - Cevap: Process paging'e komut calistirmaktan daha cok zaman harcarsa.
2. Thrashing CPU utilization'i nasil etkiler?
   - Cevap: Keskin sekilde dusurur.
3. Thrashing'i durdurmak icin multiprogramming derecesi ne yapilmalidir?
   - Cevap: Dusurulmelidir.

---

## 18. Locality Model, Working-Set Model ve PFF

### 1. Teknik Dili Sadelestir

Locality model'i ders calisma masasi gibi dusun. Bir konuda calisirken ayni 5-10 sayfayi surekli acarsin. Konu degisince baska sayfa grubuna gecersin.

Working set ise "son zamanlarda masanda aktif duran sayfalar"dir.

PFF ise alarm sistemi gibidir:
- Page fault coksa daha fazla frame ver.
- Page fault azsa fazla frame'i geri al.

### 2. Hocalar Sever / Sinavda Cikar

Locality model:
- Process, bir locality'den diger locality'ye hareket eder.
- Locality = birlikte aktif kullanilan page kumesi.
- Fonksiyon cagrisi yeni locality olusturabilir.

Working-set model:
- Locality varsayimina dayanir.
- `Delta` working-set window'dur.
- En son page referanslarindaki page grubu working set'tir.
- Page aktif kullaniliyorsa working set'tedir.
- Son referansindan sonra bir working-set window boyunca kullanilmadiysa working set'ten cikar.

Slayt ornegi:

```text
Delta = 10
t1 aninda working set = {1,2,5,6,7}
t2 aninda working set = {3,4}
```

Delta secimi:
- Delta cok kucukse tum locality'yi kapsamaz.
- Delta cok buyukse birden fazla locality'yi kapsar.
- Delta sonsuzsa process'in kullandigi tum page'ler working set olur.

Formul:

```text
WSSi = i process'inin working-set size degeri
D = toplam talep frame'i = sum WSSi
```

Kritik kosul:

```text
D > m ise thrashing meydana gelir.
```

PFF:
- Page fault rate ust siniri asarsa process'e frame verilir.
- Page fault rate alt sinirin altina duserse process'ten frame alinir.

### 3. Ozet: Aklinda Kalsin

- Locality = aktif birlikte kullanilan page grubu.
- Working set = son Delta referans icindeki aktif page'ler.
- D = tum process'lerin WSS toplami.
- D > m ise thrashing olur.
- PFF page fault oranini kontrol ederek frame verir veya alir.

### 4. Beni Test Et

1. Working-set window hangi sembolle gosterilir?
   - Cevap: Delta.
2. `D > m` ise ne olur?
   - Cevap: Thrashing meydana gelir.
3. Page fault rate ust siniri asarsa ne yapilir?
   - Cevap: Process'e ek frame tahsis edilir.

---

## 19. Linux Virtual Memory Ornegi

### 1. Teknik Dili Sadelestir

Linux'u iki sepetli bir kutuphane gibi dusun:
- Active sepet: yakin zamanda kullanilan kitaplar.
- Inactive sepet: uzun suredir kullanilmayan, kaldirilmaya aday kitaplar.

### 2. Hocalar Sever / Sinavda Cikar

Linux:
- Demand paging kullanir.
- Second-chance / clock benzeri genel page replacement politikasi vardir.
- Iki liste tutar:

```text
active_list   = kullanildigi dusunulen page'ler
inactive_list = yakin zamanda basvurulmamis, reclaim'e uygun page'ler
```

Accessed bit:
- Page'e her basvuruda 1 yapilir.
- Page ilk tahsis edildiginde accessed bit 1 olur ve active_list arkasina eklenir.
- Active_list icindeki page'e basvurulursa accessed bit 1 olur ve page listenin arkasina tasinir.
- Active_list'teki accessed bitler periyodik olarak sifirlanir.
- Zamanla en az kullanilan page active_list'in onune gelir.
- Inactive_list'teki page'e basvurulursa active_list'in arkasina geri doner.
- Active_list cok buyurse, onundeki page'ler inactive_list'e tasinir.
- Bos bellek esik altina duserse kernel inactive_list'i tarar ve frame'leri reclaim eder.

### 3. Ozet: Aklinda Kalsin

- Linux demand paging + clock benzeri replacement kullanir.
- active_list ve inactive_list vardir.
- Accessed bit page kullanildiginda 1 olur.
- Inactive_list reclaim icin adaydir.

### 4. Beni Test Et

1. Linux hangi iki page listesini tutar?
   - Cevap: active_list ve inactive_list.
2. active_list neyi tutar?
   - Cevap: Kullanildigi dusunulen page'leri.
3. Bos bellek azalinca Linux hangi listeyi tarar?
   - Cevap: inactive_list.

---

## 20. Windows Virtual Memory Ornegi

### 1. Teknik Dili Sadelestir

Windows'u akilli bir depo gorevlisi gibi dusun. Sadece istedigin kutuyu degil, yakinindaki kutulari da getirir; cunku muhtemelen birazdan onlara da ihtiyacin olur. Buna clustering denir.

### 2. Hocalar Sever / Sinavda Cikar

Windows 10:
- Demand paging kullanir.
- Clustering stratejisi vardir.
- Page fault olunca sadece hatali page degil, onceki ve sonraki bazi page'ler de getirilebilir.
- Working set management onemlidir.

Working set:
- Working set minimum: Process'in bellekte sahip olmasi garanti edilen minimum page sayisi.
- Working set maximum: Yeterli bellek varsa process'e atanabilecek maksimum page sayisi.
- Yeterli bellek varsa process maximum'u asabilir.
- Bellek talebi yuksekse minimum altina bile dusebilir.

Replacement:
- Local ve global page replacement karisimi kullanir.
- Second-chance / clock algoritmasi kullanir.
- Bos page frame listesi ve esik degeri vardir.
- Process working set maximum altindaysa page fault'ta bos listeden page alabilir.
- Process maximum'daysa ve bos bellek yeterliyse maximum'un otesine gecebilir.
- Bos bellek yetersizse kernel local LRU ile process'in working set'inden page secer.

Automatic working-set trimming:
- Bos bellek esik altina dusunce kullanilir.
- Process'lerin page sayilari degerlendirilir.
- Working set minimum'dan fazla page'i olan process'lerden page kaldirilir.
- Yeterli bellek bulunana veya process minimum'a ulasana kadar devam eder.

### 3. Ozet: Aklinda Kalsin

- Windows demand paging + clustering kullanir.
- Clustering hatali page'in komsularini da getirir.
- Working set minimum ve maximum kavramlari onemli.
- Bos bellek azalinca automatic working-set trimming yapar.

### 4. Beni Test Et

1. Windows clustering ne yapar?
   - Cevap: Hatali page ile birlikte yakin page'leri de getirir.
2. Working set minimum nedir?
   - Cevap: Process'in bellekte sahip olmasi garanti edilen minimum page sayisi.
3. Automatic working-set trimming ne zaman devreye girer?
   - Cevap: Bos bellek esik altina dustugunde.

---

## 21. Son Tekrar: Hocanin En Sevdigi Tuzaklar

```text
Virtual memory = logical memory ile physical memory ayrimi.
Demand paging = page sadece ihtiyac olunca gelir.
Page fault = RAM'de olmayan page'e erisim; her zaman illegal access demek degildir.
Valid bit = page RAM'de.
Invalid bit = page RAM'de degil veya erisim gecersiz.
EAT = (1-p) x memory access + p x page fault time.
COW = yazana kadar kopyalama yok.
FIFO = Belady anomaly olabilir.
OPT = en iyi, gelecegi bilmek ister, Belady yok.
LRU = gecmise bakar, Belady yok.
Second-chance = FIFO + reference bit.
Enhanced second-chance = reference bit + modify bit.
LFU = en az kullanilani atar.
MFU = en cok kullanilani atar.
Equal allocation = m/n.
Proportional allocation = (si/S) x m.
Global replacement = baskasinin frame'i alinabilir.
Local replacement = sadece kendi frame'lerinden secilir.
NUMA = bellek erisim sureleri esit degil.
Thrashing = process is yapmaktan cok paging yapar.
Working set = son Delta referans icindeki aktif page grubu.
D = sum WSSi.
D > m ise thrashing.
PFF ust sinir asilirsa frame ver, alt sinir altina inerse frame al.
Linux = active_list / inactive_list.
Windows = clustering + working set management.
```

