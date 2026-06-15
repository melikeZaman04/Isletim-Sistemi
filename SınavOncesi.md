# 🚀 İşletim Sistemleri Sınavına Hazırlık & Özet Notları

Bu doküman, sınavda kesinlikle soru gelen **Bellek Yönetimi**, **CPU Zamanlaması**, **Thread Yapıları** ve **Eşzamanlılık** konularına ait çıkmış sınav sorularının çözümlerini ve kritik konu özetlerini içerir.

---

## 📘 Bölüm 1: Bellek Yönetimi (Memory Management)

### 1. Sayfalama (Paging) Temelleri & Adres Çevrimi
* **Mantıksal Bellek (Logical Memory):** Programcının gördüğü, sanal adres alanıdır. **Sayfalara (Page)** bölünür.
* **Fiziksel Bellek (Physical Memory):** Gerçek RAM alanıdır. Sayfa boyutuyla aynı boyutta olan **Çerçevelere (Frame)** bölünür.
* **Sayfa Tablosu (Page Table):** Hangi sayfanın hangi çerçevede durduğunu tutan haritadır.
* **Adres Yapısı:** Mantıksal adres iki kısımdan oluşur: Sayfa Numarası ($m$ biti) ve Ofset ($n$ biti).
    * **Ofset ($n$):** Sayfa boyutunun $2$'lik tabandaki üssüdür ($2^{\text{Ofset}} = \text{Sayfa Boyutu}$). Sayfa içindeki satır numarasını (uzaklığı) verir.

> **💡 Adres Çevrim Formülü (Kısa Yol):**
> Aranan adresi **Sayfa Boyutuna** böl:
> * **Bölüm:** Hangi sayfada ($p$) olduğunu verir.
> * **Kalan:** Sayfa içi uzaklığı, yani **Ofseti ($d$)** verir.
> * **Fiziksel Adres:** (Sayfa Tablosundan bulunan Çerçevenin Başlangıç Adresi) + Ofset

---

### 2. İç ve Dış Parçalanma (Fragmentation)
Bellek tahsisi sırasında ziyan olan boş alan problemleridir.

* **İç Parçalanma (Internal Fragmentation):** Bellek **sabit boyutlu** bloklara (Paging gibi) bölündüğünde oluşur. Prosese ihtiyacından büyük bir blok verilir; bloğun içi tam dolmaz ve içeride kullanılmayan boş alan kalır.
    * *En Kötü Senaryo (Worst Case):* Bir prosesin $[n \times \text{Sayfa Boyutu} + 1 \text{ bayt}]$ alana ihtiyacı olmasıdır. Bu durumda son açılan sayfanın neredeyse tamamı boş kalır. Oluşabilecek en büyük iç parçalanma: $\text{Sayfa Boyutu} - 1$ bayttır.
    * *Ortalama Durum:* Proses başına ortalama $\frac{\text{Page Size}}{2}$ kadar iç parçalanma beklenir.
* **Dış Parçalanma (External Fragmentation):** Bellek **değişken boyutlu** (Segmentation gibi) bölündüğünde oluşur. Prosesler RAM'e girip çıktıkça aralarda irili ufaklı boşluklar kalır. Toplamda yeni bir prosesi alacak kadar boş yer vardır ama yan yana (ardışık) olmadıkları için büyük proses içeri alınamaz.
    * *Çözümü:* **Sıkıştırma (Compaction / Defragmentation)** işlemidir. RAM'deki tüm dolu alanlar bir tarafa toplanarak boşluklar birleştirilir.

---

### 3. Dinamik Depolama Tahsisi Stratejileri
Bir prosesi RAM'deki boş bloklardan birine yerleştirirken kullanılan yöntemlerdir:
* **First-Fit (İlk Uygun):** Yukarıdan aşağıya tararken prosesin sığabileceği **İLK** gördüğü boş bloğa yerleşir. EN HIZLI çalışan stratejidir.
* **Best-Fit (En Uygun):** Tüm belleği tarar, prosesin sığabileceği **EN KÜÇÜK** (ucu ucuna yeten) bloğu seçer. Hafıza ziyanını azaltmayı amaçlar.
* **Worst-Fit (En Kötü Uygun):** Tüm belleği tarar, prosesi kasıtlı olarak **EN BÜYÜK** boş bloğa yerleştirir. Geriye büyük bir parça kalsın mantığı güder; en büyük iç parçalanmayı bu yaratır.
* **Next-Fit (Sonraki Uygun):** First-Fit gibidir ancak aramaya her seferinde baştan başlamaz, **en son kaldığı yerden** devam eder.

---

### 4. Sayfalama (Paging) vs. Bölütleme (Segmentation)
* **Paging:** Belleği programın içeriğine bakmaksızın **sabit boyutlu** fiziksel parçalara böler. Sadece **İç Parçalanma** görülür.
* **Segmentation:** Belleği programcının gözüyle, kodun **mantıksal işlevlerine göre** (Main, Stack, Metotlar vb.) **değişken boyutlu** parçalara ayırır. Sadece **Dış Parçalanma** görülür. Başlangıç ve sınır adreslerini **Segment Table (Base/Limit)** üzerinde tutar.

---

### 5. Sanal Bellek (Virtual Memory) & Sayfa Değiştirme (Page Replacement)
* **Sanal Bellek:** Fiziksel RAM yetersiz kaldığında, sabit diskin (Hard Disk/SSD) bir bölümünün RAM gibi kullanılmasıdır. Programın tamamı yerine sadece o an ihtiyaç duyulan sayfaları RAM'de tutar (**Demand Paging**).
* **Belady'nin Anomalisi (Belady's Anomaly):** FIFO (İlk Giren İlk Çıkar) sayfa değiştirme algoritmasında, prosese tahsis edilen çerçeve (frame) sayısı artırılmasına rağmen sayfa hatası (page fault) oranının düşeceği yerde **artan anormal durumdur**.
* **Optimal (OPT) Algoritması:** Gelecekte en uzun süre kullanılmayacak olan sayfayı bulup yer değiştiren, teorik olarak **en düşük sayfa hatası oranına** sahip hayali algoritmadır.

---

## 🖥️ Bölüm 2: Proses ve CPU Zamanlaması (Scheduling)

### 1. Bir Prosesin RAM Üzerindeki Anatomisi
Bir proses çalışırken bellek alanı temelde şu bölümlere ayrılır:
* **Stack (Yığın):** Fonksiyon çağrıldığında parametreler, geri dönüş (return) adresleri ve yerel (lokal) değişkenler gibi **geçici verilerin** saklandığı dinamik bölümdür. İş bitince temizlenir.
* **Heap (Öbek):** Çalışma zamanında (runtime) programcının `new` veya `malloc` ile dinamik olarak genişlettiği verilerin tutulduğu yerdir.
* **Data & Text:** Global değişkenler (Data) ve programın derlenmiş makine kodları (Text) burada durur.

---

### 2. Kesintisiz (Non-preemptive) vs. Kesintili (Preemptive) Zamanlama
* **Non-preemptive (Kesintisiz):** CPU bir prosese verildikten sonra, o proses kendi isteğiyle sonlanıncaya veya bir I/O (girdi/çıktı) beklemek için bekleme durumuna geçinceye kadar **CPU'yu asla bırakmaz**, zorla elinden alınamaz.
* **Preemptive (Kesintili):** İşletim sistemi, önceliği yüksek bir iş geldiğinde veya prosesin süresi bittiğinde onu CPU koltuğundan **zorla kaldırabilir**.
* **Ready Queue (Hazır Kuyruğu):** RAM'de CPU'ya girmek için hazır bekleyen tüm proseslerin dizildiği sıradır.
* **Short-Term Scheduler (CPU Scheduler):** Ready Queue'daki proseslerden sıradakini seçip milisaniyeler içinde CPU'ya fırlatan işletim sistemi bileşenidir.
* **PCB (Process Control Block):** Bir prosesin ID'si, durumu, register değerleri gibi tüm kimlik bilgilerini tutan veri yapısıdır.
* **Context Switch (Bağlam Değişme):** CPU'nun bir prosesi çalıştırırken onu bırakıp diğerine geçmesi esnasında; eski prosesin durumunu PCB'ye kaydedip, yeni prosesin durumunu yüklemesi işlemidir. Saf bir ek yüktür (overhead), bu esnada yararlı bir iş yapılmaz.

---

### 3. CPU Zamanlama Algoritmaları & Performans Kriterleri
* **Turnaround Time (Dönüş Süresi):** Bir prosesin sisteme sunulduğu (girdiği) andan tamamen bittiği ana kadar geçen **toplam** süredir. (Beklemeler + Çalışma süresi dahildir).
* **Response Time (Yanıt Süresi):** Proses sisteme verildikten sonra işlemciden aldığı **ilk** tepkiye/yanıta kadar geçen süredir.
* **Throughput (İş Çıkarma Oranı):** İşlemcinin birim zamanda (örn: 1 dakikada) bitirebildiği toplam proses sayısıdır.
* **Round-Robin (RR) Algoritması:** Her prosese **Quantum** adı verilen sabit bir zaman dilimi verir. Süresi biten proses CPU'dan indirilir ve Ready Queue'nun en arkasına gönderilir (Preemptive mimaridir).

---

## 🧵 Bölüm 3: Thread Yapıları & Eşzamanlılık (Concurrency)

### 1. Çoklu İş Parçacığı (Multithreading) Modelleri
Kullanıcı alanındaki thread'ler (User Thread) ile çekirdeğin (Kernel Thread) eşleşme modelleridir:
* **Many-to-One:** Birçok kullanıcı thread'i tek bir kernel thread'ine bağlanır. Bir thread kilitlenirse (block) tüm sistem donar. Kernel thread'lerin varlığından haberdar değildir.
* **One-to-One:** Her kullanıcı thread'i için arkada resmi bir kernel thread'i yaratılır (Modern Windows/Linux). Biri donarsa diğerleri çalışmaya devam eder.
* **Many-to-Many:** Birçok kullanıcı thread'i, sayıca kendilerinden daha az veya eşit kernel thread havuzuna dinamik olarak eşlenir.

### 2. Thread Oluşturma Yöntemleri
* **Explicit Threading:** Thread oluşturma ve kapatma işçiliğini tamamen kod yazan **geliştirici** elle yapar.
* **Implicit Threading:** Thread yönetim yükünü **derleyiciye (compiler)** veya çalışma zamanı kütüphanelerine bırakma işidir.
    * **Fork-Join Modeli:** Ana thread çalışırken paralel bir iş geldiğinde otomatik olarak kollara ayrılır (**Fork**), işler bitince tekrar ana thread ile birleşir (**Join**). **OpenMP** kütüphanesi derleyici yönergeleriyle bu modeli otomatik yürütür.

### 3. Kritik Bölge (Critical Section) & Deadlock (Ölümcül Kilit)
* **Critical Section (Kritik Bölge):** Birden fazla prosesin/thread'in aynı anda erişip değiştirmeye çalıştığı paylaşılan ortak veri/kod alanıdır. Aynı anda sadece biri girmelidir (**Mutual Exclusion**). 
    * *Kritik Bölge Çözümleri:* **Mutex Locks, Semaphore (Semafor) ve Monitors** gibi kilit sistemleridir.
    * *Sınırlı Bekleme (Bounded Waiting):* Bir proses kritik bölgeye girmek istedikten sonra, diğerlerinin ondan önce içeri kaç kez girebileceğine dair bir limit olmalıdır (Sonsuza kadar aç kalmamalıdır).

* **Deadlock (Ölümcül Kilit):** İki veya daha fazla prosesin, birbirlerinin elinde tuttukları kaynakları dairesel olarak beklemesi ve sistemin tamamen kilitlenmesi durumudur.
    * **Deadlock İçin Gerekli 4 Şart (Aynı anda oluşmalıdır):**
        1.  *Mutual Exclusion:* Kaynaklar paylaşılamaz olmalı (tek kişilik).
        2.  *Hold and Wait:* Proses elindekini bırakmadan yenisini beklemeli.
        3.  *No Preemption:* Bir prosesin kaynağı zorla elinden alınamamalı.
        4.  *Circular Wait:* Prosesler birbirini döngüsel bir zincir şeklinde beklemeli.

---
**💡 Sınav Tüyosu:** Bilgisayar ilk açıldığında ROM bellekte yer alan ve işletim sistemini diskten RAM'e yükleyip başlatan o ilk minik koda **Bootstrap (veya Bootloader)** denir. Sözel boşluk doldurmalarda çok sık gelir!


# 📝 BMÜ-314 İşletim Sistemleri Final Sınavı Çözümleri

## 1) Deadlock (Ölümcül Kilit) Oluşması İçin Gerekli 4 Şart
Bir sistemde deadlock meydana gelebilmesi için aşağıda belirtilen 4 şartın **aynı anda** gerçekleşmesi gerekir. Herhangi birinin engellenmesi deadlock'ı çözer:

1. **Mutual Exclusion (Karşılıklı Dışlama):** En az bir kaynak paylaşılamaz modda olmalıdır. Yani bir kaynak aynı anda sadece tek bir proses tarafından kullanılabilir.
2. **Hold and Wait (Tut ve Bekle):** Bir proses, halihazırda en least bir kaynağı elinde tutarken, diğer proseslerin elinde bulunan ve ihtiyaç duyduğu yeni kaynakları almak için bekleme durumunda olmalıdır.
3. **No Preemption (Zorla Geri Alamama):** Kaynaklar, proseslerin elinden zorla alınamaz. Bir kaynak ancak onu tutan proses işini bitirdiğinde gönüllü olarak bırakılabilir.
4. **Circular Wait (Döngüsel Bekleme):** Proseslerin birbirlerinin kaynaklarını zincirleme bir döngü halinde beklemesi durumudur. (Örn: $P_0$ prosesi $P_1$'in kaynağını beklerken, $P_1$ de $P_0$'ın elindeki kaynağı bekler).

---

## 2) Paging (Sayfalama) Modelinde Adres Eşleştirme (Çevrimi)
Paging modelinde bellek yönetimi, programcının gördüğü **Mantıksal Bellek (Logical Memory)** ile fiziksel donanım olan **Fiziksel Bellek (Physical Memory)** arasındaki eşlemeyi sabit boyutlu bloklar üzerinden yürütür.

* **Sayfa (Page) ve Çerçeve (Frame):** Mantıksal bellek sabit boyutlu **Page**'lere, fiziksel bellek ise aynı boyuttaki **Frame**'lere bölünür.
* **Adres Yapısı:** CPU tarafından üretilen mantıksal adres iki bileşenden oluşur: **Sayfa Numarası ($p$)** ve **Ofset ($d$)**.
* **Eşleştirme Süreci:** 1. CPU bir mantıksal adres üretir.
  2. Donanımsal olan **Bellek Yönetim Birimi (MMU)**, bu adresteki sayfa numarasını ($p$) alır ve **Sayfa Tablosuna (Page Table)** gider.
  3. Sayfa tablosunda o sayfa numarasının karşılık geldiği fiziksel **Çerçeve Numarası ($f$)** bulunur.
  4. Bulunan çerçeve numarası ($f$) ile sayfa içi yer değişimi gösteren ofset ($d$) değeri birleştirilerek nihai **Fiziksel Adres** elde edilir ve RAM'e erişim sağlanır. Ofset ($d$) değeri çevrim esnasında asla değişmez.

---

## 3) SRTF (Shortest Remaining Time First) Sayısal CPU Zamanlama Sorusu

### 📊 Proses Tablosu
| Process | Varış Zamanı (Arrival Time) | CPU Burst Süresi |
| :---: | :---: | :---: |
| **P1** | 0 ms | 9 ms |
| **P2** | 2 ms | 6 ms |
| **P3** | 5 ms | 5 ms |
| **P4** | 4 ms | 3 ms |

### 🕒 Adım Adım Zaman Analizi (Preemptive)
* **t = 0:** Sadece **P1** geldi. CPU'ya girer ve çalışır.
* **t = 2:** **P2** geldi (Süre: 6). P1 o ana kadar 2 ms çalıştı, kalan süresi: $9 - 2 = 7$. Karşılaştırma: P2'nin süresi daha kısa ($6 < 7$) olduğu için **P2, P1'i kesintiye uğratır (preempt eder) ve CPU'yu alır.**
* **t = 4:** **P4** geldi (Süre: 3). P2 o ana kadar 2 ms çalıştı ($2 \rightarrow 4$ arası), kalan süresi: $6 - 2 = 4$. Karşılaştırma: P4'ün süresi daha kısa ($3 < 4$) olduğu için **P4, P2'yi kesintiye uğratır ve CPU'yu alır.**
* **t = 5:** **P3** geldi (Süre: 5). P4 o ana kadar 1 ms çalıştı ($4 \rightarrow 5$ arası), kalan süresi: $3 - 1 = 2$. Karşılaştırma: P4 hala en kısa süreye sahip ($2 < 5$) olduğu için **P4 çalışmaya devam eder.**
* **t = 7:** **P4 tamamen bitti (Süresi: 0).** Hazır kuyruğundaki proseslerin kalan süreleri incelenir: 
  * P1: 7 ms, P2: 4 ms, P3: 5 ms. 
  * En kısa olan **P2** CPU'yu alır ve kalan 4 ms'lik işini kesintisiz tamamlayarak **t = 11** anında biter.
* **t = 11:** Kalanlar: P1 (7 ms) ve P3 (5 ms). En kısa olan **P3** CPU'ya girer, 5 ms çalışarak **t = 16** anında biter.
* **t = 16:** Son kalan **P1** CPU'ya girer, kalan 7 ms'lik işini tamamlar ve **t = 23** anında sistem tüm işleri bitirir.

### 📊 Gantt Şeması (Gantt Chart)

+------+------+------+------+------+------+
|  P1  |  P2  |  P4  |  P2  |  P3  |  P1  |
+------+------+------+------+------+------+
0      2      4      7      11     16     23



# 🎯 BMÜ-314 İşletim Sistemleri Dönem Sonu Deneme Sınavı

**Süre:** 90 Dakika  
**Not:** Soruların puan değerleri yanlarında belirtilmiştir. Başarılar brom!

---

## 📝 BÖLÜM 1: Klasik ve Sayısal Sorular (50 Puan)

### S1) (10 Puan) Bir prosesin veya thread'in sistem kaynaklarını güvenli bir şekilde kullanabilmesi için uyması gereken işletim sistemi kaynak kullanım sırasını (protokolünü) yazarak açıklayınız.

#### 🔑 Cevap ve Sınav Detayı:
Bir proses, sistemdeki herhangi bir donanımsal veya yazılımsal kaynağı kullanırken sırasıyla şu 3 aşamadan geçmek zorundadır:
1. **Request (İstek):** Proses ihtiyaç duyduğu kaynağı işletim sisteminden talep eder. Eğer kaynak o an başka bir proses tarafından kullanılıyorsa, istekte bulunan proses kaynak serbest kalana kadar hazır/bekleme kuyruğunda bekletilir.
2. **Use (Kullanım):** Kaynak prosese tahsis edildikten sonra, proses kaynak üzerinde gerçekleştireceği işlemleri yürütür (Örn: Yazıcıdan çıktı alma, dosyaya yazma).
3. **Release (Serbest Bırakma):** Prosesin kaynakla işi bittiğinde, kaynağı sisteme geri iade eder. Böylece kuyrukta bekleyen diğer proseslerin kaynağa erişiminin önü açılır.

---

### S2) (15 Puan) Paylaşılan Bellek (Shared Memory) mimarisinde, "Producer-Consumer" (Üretici-Tüketici) problemi üzerinden "Race Condition" (Yarış Durumu) kavramını açıklayınız. Ortak `count` değişkeninin güncellenmesi sırasında neden en son yazan prosesin değerinin kalıcı olduğunu işlemci seviyesinde ifade ediniz.

#### 🔑 Cevap ve Sınav Detayı:
* **Race Condition (Yarış Durumu):** Birden fazla prosesin veya thread'in paylaşılan ortak bir veriye (Örn: `count` değişkeni) aynı anda erişip onu değiştirmeye çalışması ve nihai sonucun, bu proseslerin **yürütülme/yazma sırasına** bağlı olarak değişmesi hatasıdır.
* **En Son Yazan Prosesin Kazanma Nedeni:** Yazılım dilindeki `count++` veya `count--` gibi işlemler işlemci (CPU) seviyesinde tek bir adımda gerçekleşmez (Atomic değildir). İşlemci arkada şu 3 adımı koşturur:
  1. Bellekteki `count` değerini işlemci register'ına yükle (`register = count`).
  2. Register değerini 1 artır veya azalt (`register = register + 1`).
  3. Register'daki yeni değeri belleğe geri yaz (`count = register`).
  
  İki proses aynı anda bu adımları koştururken, işlemci aralarında geçiş (Context Switch) yaparsa, proseslerden biri kendi lokal register'ındaki değeri RAM'deki ortak `count` alanına **en son yazar ve bir önceki prosesin RAM'e yazmış olduğu güncel değeri ezerek havaya uçurur**. Bu yüzden "en son yazanın dediği olur" ve veri tutarsızlığı doğar.

---

### S3) (15 Puan) Aşağıda 3 frame'lik (çerçeve) boş bir fiziksel belleğe sahip sistemde, sayfa referans dizisi verilmiştir. **Optimal (OPT) Sayfa Değiştirme Algoritmasını** kullanarak hangi adımlarda Page Fault (Sayfa Hatası) oluştuğunu bulunuz ve toplam Page Fault sayısını hesaplayınız.

* **Referans Dizisi:** `7, 0, 1, 2, 0, 3, 0, 4`
* **Fiziksel Bellek Boyutu:** 3 Çerçeve (Boş)

#### 🔑 Cevap ve Sınav Detayı:
Optimal (OPT) algoritması, RAM dolduğunda **gelecekte en uzun süre kullanılmayacak (en geç lazım olacak)** sayfayı RAM'den dışarı atar.

| Referans Adımı | Frame 1 | Frame 2 | Frame 3 | Durum (Fault / Hit) | Açıklama |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **7** | 7 | | | **Page Fault (1)** | İlk sayfa boş çerçeveye alındı. |
| **0** | 7 | 0 | | **Page Fault (2)** | Boş çerçeveye alındı. |
| **1** | 7 | 0 | 1 | **Page Fault (3)** | Tüm çerçeveler doldu. |
| **2** | 2 | 0 | 1 | **Page Fault (4)** | 2 geldi. Geleceğe bakıyoruz: 0 hemen lazım, 1 hiç yok, 7 hiç yok. İlk giren 7'yi kurban seçip yerine 2'yi alıyoruz. |
| **0** | 2 | 0 | 1 | Hit | 0 zaten RAM'de var. |
| **3** | 2 | 3 | 1 | **Page Fault (5)** | 3 geldi. Geleceğe bakıyoruz: 0 hemen lazım. 2 ve 1 ileride yok. En eski/uygun olan 0'ın yanındaki veya kurallara göre 0'ı koruyup 2 veya 1'den birini atarız. Gelecekte en geç lazım olana göre 0 elenmez; 2 veya 1'den biri (Örn: 0'ın yeri veya 1) yerine 3 gelir. |
| **0** | 2 | 3 | 0 | **Page Fault (6)** | 0 tekrar istendi, RAM'den atıldığı için tekrar fault oldu. |
| **4** | 4 | 3 | 0 | **Page Fault (7)** | 4 geldi, gelecekte hiçbiri yok, en uygun olan değiştirildi. |

* **Toplam Page Fault Sayısı:** 6 veya 7 (Hocanın referans dizisinin uzunluğuna göre geleceğe bakma adımında yaptığı kabule bağlıdır ama temel mantık gelecekte en geç lazım olanı fırlatmaktır).

---

### S4) (10 Puan) "Multitasking" (Çoklu Görev) nedir? Tek çekirdekli bir işlemcide birden fazla programın aynı anda çalışabilmesinin arkasındaki işletim sistemi mekanizmasını açıklayınız.

#### 🔑 Cevap ve Sınav Detayı:
* **Multitasking:** Kullanıcının bilgisayarda aynı zaman dilimi içerisinde birden fazla görevi/programı (Örn: Müzik dinleme, kod yazma, tarayıcıda gezinme) eşzamanlı olarak yürütebilmesi becerisidir.
* **Mekanizma:** Tek çekirdekli bir CPU fiziksel olarak aynı milisaniyede sadece TEK bir komut koşturabilir. Ancak işletim sistemi **Zaman Paylaşımı (Time-Sharing)** yöntemiyle her prosese çok küçük zaman dilimleri (Quantum) ayırır. CPU bu prosesler arasında o kadar yüksek bir hızda mekik dokur ki (**Context Switching / Bağlam Değişimi**), insan beyni bu geçişleri algılayamaz. Kullanıcı tüm programların aynı anda, kesintisiz çalıştığı illüzyonuna kapılır.

---

## 🕳️ BÖLÜM 2: Boşluk Doldurma Soruları (30 Puan)

*Her boşluk 6 puandır.*

1. CPU, RAM'den bir komutu getirdikten sonra komutun ne anlama geldiğini çözme aşamasına **Decode (Çözme)**, komutu donanım üzerinde koşturma aşamasına ise **Execute (Yürütme)** adı verilir.
2. Bilgisayar ilk açıldığında veya yeniden başlatıldığında, kalıcı ROM bellekte duran ve işletim sistemi çekirdeğini diskten bularak RAM'e yükleyen ilk minik koda **Bootstrap (veya Bootloader)** denir.
3. Sanal bellek mimarisinde, bir prosesin komut çalıştırmaktan ziyade sürekli olarak disk ile RAM arasında sayfa taşımakla (paging) uğraşıp sistemin kilitlenmesine neden olması durumuna **Thrashing (Sayfa Serpme / Çırpınma)** adı verilir.
4. İstekte bulunan bir prosesin, ihtiyaç duyduğu kaynakların diğer aktif prosesler tarafından sürekli olarak kapılmasından dolayı belirsiz/süresiz bir şekilde hazır kuyruğunda beklemesine **Starvation (Açlık)** denir.
5. Bir sayfa RAM'de bulunamadığında donanımsal bir kesme (trap) sinyali tetiklenir, bu duruma **Page Fault (Sayfa Hatası)** adı verilir.

---

## 🔘 BÖLÜM 3: Çoktan Seçmeli / Sıralama Sorusu (20 Puan)

### S5) Demand Paging (İsteğe Bağlı Sayfalama) kullanan bir işletim sisteminde, CPU'nun talep ettiği bir sayfanın RAM'de olmaması (Page Fault) durumunda, işletim sisteminin donanımsal ve yazılımsal olarak gerçekleştirdiği adımların DOĞRU sıralaması aşağıdakilerden hangisidir?

I. İlgili sayfa diskteki yerinden bulunarak RAM'deki boş bir çerçeveye (frame) yüklenir (I/O işlemi).  
II. Sayfa tablosu güncellenir ve geçerlilik biti (valid/invalid bit) "Valid" yapılır.  
III. CPU, sayfa tablosundaki invalid bitini görerek işletim sistemine bir "Page Fault Trap" (kesme sinyali) gönderir.  
IV. Kesintiye uğrayan ve yarıda kalan işlemci komutu en baştan tekrar başlatılır (Restart Instruction).  

A) I - III - II - IV  
B) III - I - II - IV  
C) III - II - I - IV  
D) I - II - III - IV  

#### 🔑 Doğru Cevap: B
**Neden?** Sıralama her zaman şöyledir: Önce hata fark edilir ve tuzak fırlatılır (III), ardından diskten RAM'e yükleme yapılır (I), yükleme bitince harita/tablo güncellenir (II) ve en son olarak donanım yarıda kalan o komutu sıfırdan tekrar çalıştırır (IV).
