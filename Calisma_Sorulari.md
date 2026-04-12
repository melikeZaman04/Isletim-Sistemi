# İşletim Sistemleri - Sınav Öncesi Çalışma Soruları (Deneme Sınavı)

Hocanızın soru tarzına (çoktan seçmeli, boşluk doldurma ve klasik sorulara dengeli ağırlık veren) ve bugüne kadar çalıştığımız tüm notlara (Giriş, Prosesler, Threadler, Senkronizasyon, Donanım Çözümleri ve Deadlock) dayanarak kendinizi test edebileceğiniz harika bir deneme sınavı hazırladım.

---

## BÖLÜM 1: ÇOKTAN SEÇMELİ SORULAR (Her soru 5 Puan)

**1.** Bir process (süreç) çalışırken dinamik olarak büyüyüp küçülebilen ve `malloc()` gibi fonksiyonlarla bellekte çalışma zamanında (run-time) tahsis edilen verilerin tutulduğu bellek bölgesi aşağıdakilerden hangisidir?
a) Text (Kod)
b) Stack (Yığın)
c) Heap (Öbek) 
d) Data 
e) Registers

**2.** İşletim sisteminin User Mode'da (Kullanıcı Modu) çalışan bir uygulamanın donanıma erişebilmesi için Kernel Mode'a (Çekirdek Moduna) geçişini sağlayan "yasal kapı" aşağıdakilerden hangisidir?
a) Interrupt (Kesme)
b) System Call (Sistem Çağrısı)
c) API
d) Bootstrap
e) Dispatcher

**3.** "Sınırlı Bekleme (Bounded Waiting)" koşulunu sağlamak amacıyla standart `TestAndSet` gibi atomik donanım talimatlarına çoğunlukla (slayttaki örnekteki gibi) hangi veri yapısı entegre edilir?
a) Boolean değişkenli bir kuyruk/dizi (`waiting[i]`)
b) Turn değişkeni
c) Mutex Kilidi
d) Bir adet Binary Semaphore
e) Sayıcı Semafor (Counting Semaphore)

**4.** Aşağıdaki multithreading eşleşme modellerinden hangisinde, programcı tarafından atanan kullanıcı iş parçacıklarının (user threads) her biri arka planda ayrı bir donanım iş parçacığına (kernel thread) kilitlenir ve birbirlerini hiç bloke etmezler?
a) Implicit Threading
b) Many-to-One (Çoktan Bire)
c) Many-to-Many (Çoktan Çoğa)
d) One-to-One (Bire Bir)
e) Thread Pool (İş parçacığı havuzu)

**5.** Deadlock (Kilitlenme) oluşması için dört şartın eşzamanlı olarak gerçekleşmesi zorunludur. Bir prosesin elindeki kaynağı yalnızca kendi işi bittiğinde veya kendi isteğiyle serbest bırakması, bu süre zarfında kaynağın **zorla alınamaması** kuralına ne ad verilir?
a) Mutual Exclusion
b) Circular Wait
c) No Preemption
d) Hold and Wait
e) Busy Waiting

**6.** Çok çekirdekli (Multi-processor) bir sistemde kritik bölgeyi (Critical Section) korumak için aşağıdaki yöntemlerden hangisini kullanmak **en büyük sistem gecikmesine ve performans kaybına** yol açar?
a) Interruptları kapatmak (Interrupt Disable)
b) Mutex Kilitleri
c) Semafor kullanımı
d) Compare and Swap mimarisi
e) Monitör (Monitor) yapısı

---

## BÖLÜM 2: BOŞLUK DOLDURMA (Her Boşluk 4 Puan)

1. Bir prosesin çalışırken beklenmedik bir hata verip sonlandırılması sonrasında, hatanın sebebini bulmak (debug) amacıyla bellek alanının kaydedilmesine **[ ___________________ ]** denir.
2. İşletim sistemlerinde iki prosesin hafızada ortak bir alan üzerinden haberleştiği, çok hızlı olan ancak mutlaka senkronizasyon gerektiren IPC (Interprocess Communication) yöntemine **[ ___________________ ]** denir.
3. Kilitli bir kritik bölgenin kapısında "tamamen uykuya dalmak yerine" sürekli döngüde kontrol ederek CPU zamanını israf eden mekanizmalara genel adıyla **[ ___________________ ]** denir.
4. Sistemlerin Deadlock'tan (Ölümcül kilitlenmeden) dinamik olarak kaçınmasını sağlayan ve her kaynak tahsisi öncesinde "Safe State (Güvenli Durum)" hesabı yapan meşhur algoritmaya **[ ___________________ ]** adı verilir.
5. Bir child (çocuk) proses işini bitirip sonlandığında, eğer parent (baba) proses henüz `wait()` çağrısı yapıp sonucunu almamışsa, işletim sistemi listesinde giriş kaplamaya devam eden bu çocuğa **[ ___________________ ]** proses denir.

---

## BÖLÜM 3: KLASİK VE UZUN CEVAPLI SORULAR

**Soru 1 (15 Puan):** Thread (İş parçacığı) kullanmanın, yeni bir tam Process (Süreç) oluşturmaya göre getirdiği 3 temel avantajı maddeler halinde yazınız.
**Cevap 1:**



**Soru 2 (15 Puan):** Kritik Bölge (Critical Section) probleminin çözülmesi için bir algoritmanın sağlaması gereken 3 mutlak şart nedir? İsimlerini yazıp sacede "Mutual Exclusion (Karşılıklı Dışlama)" şartını kısaca açıklayınız.
**Cevap 2:**



**Soru 3 (10 Puan):** "Deadlock Prevention (Önleme)" ile "Deadlock Avoidance (Kaçınma)" mekanizmaları birbirinden tamamen farklıdır. İkisinin sisteme yaklaşım şekli arasındaki felsefi farkı kısaca açıklayınız.
**Cevap 3:**



<br><br><br><br>

---

# CEVAP ANAHTARI VE AÇIKLAMALAR 
*(Cevaplarınızı üst tarafa yazdıktan sonra buradan kontrol edin)*

### Bölüm 1: Test Çözümleri
1. **c) Heap** -> Dinamik olarak çalışma zamanında büyüyen bölgedir. Stack geçici adreslerdir.
2. **b) System Call** -> Donanıma doğrudan müdahalenin güvenilir yoludur. API'ler System Call çağırır ancak asıl geçiş aracı System Call'dur.
3. **a) Boolean değişkenli bir kuyruk/dizi (`waiting[i]`)** -> TestAndSet kendi başına donanımsaldır ve Bounded Waiting sağlamaz. Hocanın slaytındaki tablolu çözümde "kuyruk" için `waiting[i]` kullanılıyordu.
4. **d) One-to-One** -> Gerçek donanım paralelitesi sunan ancak sistem limitlerine dayanan standart (Linux/Windows) modelidir.
5. **c) No Preemption** -> Zorla almaya preemption denir, zorla alınamamasına no preemption.
6. **a) Interruptları kapatmak** -> Tek çekirdekte hayat kurtarır ama çok çekirdekte diğer çekirdeklere mesaj iletmek donanımı felç eder.

### Bölüm 2: Boşluk Doldurma Çözümleri
1. **[ Core Dump ]** -> İşletim sisteminin kendi çökmesine Crash Dump denirken, proses çökmesine Core Dump denir.
2. **[ Shared Memory (Paylaşılan Bellek) ]** -> Diğer yöntem Message Passing'dir ama yavaştır.
3. **[ Spinlock (veya Busy Waiting / Meşgul Bekleme) ]** -> Sürekli dönerek CPU'yu yoran kilitlerdir.
4. **[ Banker Algoritması (Banker's Algorithm) ]** -> Dijkstra'nın ünlü kaçınma (avoidance) formülüdür.
5. **[ Zombie (Zombi) ]** -> Eğer baba ölseydi yetim (orphan) olurdu. Çocuk ölür baba alırsa zombi olur.

### Bölüm 3: Klasik Soru Çözümleri
**Test-Cevap 1:**
1. Ekonomi: Yeni bir proses oluşturmak bellek ayırmayı gerektirdiği için pahalıdır. Thread'ler anaprosese ait kaynakları paylaştığından Context Switch çok daha ucuz ve hızlıdır.
2. Kaynak Paylaşımı: Threadler IPC'ye (Message Passing vb.) ihtiyaç duymadan kod ve data alanını otomatik paylaşırlar.
3. Ölçeklenebilirlik / Cevap Verebilirlik: Çok işlemcilikli yapılardan tam fayda sağlar. Bir thread bloklansa bile diğeri akıcı şekilde arayüzü kontrol edebilir.

**Test-Cevap 2:**
Üç Şart: 1) Mutual Exclusion, 2) Progress (İlerleme), 3) Bounded Waiting (Sınırlı Bekleme).
Açıklama (Mutual Exclusion): Eğer bir proses kendi kritik bölgesinde işlem yapıyor/kodu çalıştırıyorsa, eş zamanlı olarak başka hiçbir prosesin o kritik bölgeye dahi girmesine izin verilmemesi prensibidir. Asla paylaşılamaz.

**Test-Cevap 3:**
*Prevention (Önleme)*, daha sistem kurulurken Deadlock için şart olan 4 koşuldan (Mutual exclusion, hold and wait vb.) en az birisini kati suretle imkansız hale getirecek katı kurallar ile sistemi çalıştırmaktır. Kaynak tüketimi israflıdır. 
*Avoidance (Kaçınma)* ise, kuralsızlıktır fakat ileri görüşlülüktür. Bankacı algoritması gibi dinamik hesaplar kurarak, arka planda "Ben bu sürece bu kaynağı verirsem ileride deadlock yaşanabilme ihtimali olan bir Unsafe duruma düşer miyim?" diye hesap yapmasıdır. Durum safe ise kaynak verir, değilse red eder.