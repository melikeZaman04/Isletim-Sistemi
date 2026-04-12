# İşletim Sistemleri - Sınav Soruları ve Detaylı Çözümleri

Gönderdiğiniz görsellerde yer alan ara sınav kağıdındaki tüm klasik, boşluk doldurma ve çoktan seçmeli test sorularını okuyup detaylı cevap anahtarlarıyla beraber bir çalışma dokümanı haline getirdim.

---

## BÖLÜM 1: ÇOKTAN SEÇMELİ TEST SORULARI (Test Bölümü)

**Soru 1:** Bir process geçici olarak bellekten diske (secondary memory) yer değiştirilebilir ve daha sonra yürütmeye devam etmek için tekrar belleğe alınabilir. Buradaki ilgili ikincil hafıza birimi ve gerçekleşen işlemin doğru tanımlama çifti aşağıdakilerden hangisidir?
*   **Cevap:** **e) backing store, swapping**
*   *Açıklama:* İşletim sistemlerinde süreçlerin ana bellek (RAM) ve disk arasında yer değiştirmesine Swapping (Takaslama) denir. Bu geçici disk alanına da Backing Store adı verilir.

**Soru 2:** Dinamik depolama tahsisi probleminin çözümünde hangi bellek ayırma stratejisi, bir işlemi ona barındıracak kadar büyük olan ilk kullanılabilir bellek bloğuna yerleştirmeye çalışır?
*   **Cevap:** **d) First fit**
*   *Açıklama:* First-fit algoritması belleği baştan tarar ve sığdığı ilk (first) boşluğa (hole) yerleşim yapar.

**Soru 3:** Bir process bir kaynağı kullanmak istediğinde sırasıyla gerçekleştirdiği sistem çağrılarının sıralaması hangi seçenekte doğru verilmiştir?
*   **Cevap:** **a) Request - Use - Release**
*   *Açıklama:* Yaşam döngüsü: Önce kaynak talep edilir (Request), tahsis edilirse kullanılır (Use), iş bitince serbest bırakılır (Release).

**Soru 4:** Aşağıda verilen processler Shortest Remaining Time First (SRTF) algoritmasına göre yürütüldüğünde elde edilen ortalama waiting (bekleme) ve turnaround (geri dönüş) değerleri hangi seçenekte verilmiştir? (P1: Arrival=0, Burst=7 | P2: Arr=2, Burst=4 | P3: Arr=4, Burst=1 | P4: Arr=5, Burst=4)
*   **Cevap:** **b) 3, 7** (Ortalama Bekleme: 3, Ortalama Geri Dönüş: 7)
*   *Açıklama:*
    *   0-2 arası P1 çalışır (P1 kalan:5).
    *   2'de P2 gelir, kalan süresi (4), P1'den (5) küçük olduğu için CPU'yu alır (Preemption). 2-4 arası P2 çalışır (P2 kalan:2).
    *   4'te P3 (süre:1) gelir, P2'den (2) küçük olduğu için P3 çalışır ve 5'te biter.
    *   5'te P4 gelir (süre:4). Kalanlar: P1(5), P2(2), P4(4). En kısa P2 seçilir, 5-7 arası çalışır ve biter.
    *   7-11 arası P4 çalışır ve biter.
    *   11-16 arası P1 çalışır ve biter.
    *   *Turnaround:* P1(16-0=16), P2(7-2=5), P3(5-4=1), P4(11-5=6). Toplam=28, Ort=28/4=7.
    *   *Wait:* Turnaround - Burst = P1(16-7=9), P2(5-4=1), P3(1-1=0), P4(6-4=2). Toplam=12, Ort=12/4=3.

**Soru 5:** Hangi modül CPU'nun kontrolünü short-term scheduler (kısa vadeli zamanlayıcı) tarafından seçilen sürece verir?
*   **Cevap:** **a) Dispatcher**
*   *Açıklama:* Scheduler (zamanlayıcı) kimi çalıştıracağını seçer, **Dispatcher (Dağıtıcı)** ise o süreci CPU'ya bizzat bindiren ve context switch'i yapan modüldür.

**Soru 6:** Paylaşımsız kaynak bir process tarafından tutulurken başka bir processin bu kaynağa istek yapması durumunda ikinci processin kaynak boşalıncaya kadar beklemesi aşağıdakilerden hangisi ile açıklanır?
*   **Cevap:** **b) Tut ve bekle (Hold and wait)**

**Soru 7:** Bir process'in (işlemin) sunulduğu andan tamamlanma zamanına kadar geçen süre ____ olarak adlandırılır.
*   **Cevap:** **c) turnaround (geri dönüş) süresi**

**Soru 8:** Thread oluşturma işinin uygulama geliştiriciler yerine derleyici (compiler) tarafından yapılması aşağıdakilerden hangisi ile açıklanır?
*   **Cevap:** **d) Dolaylı thread oluşturma (Implicit threading)**

**Soru 9:** Aşağıdakilerden hangisi kernel (çekirdek) tarafından programlanamaz (schedule edilemez)?
*   **Cevap:** **e) User-level threads**
*   *Açıklama:* İşletim sistemi çekirdeği yalnızca Kernel Thread'leri ve Processleri tanır ve çizelgeler. Kullanıcı seviyesi iş parçacıkları görünmezdir.

**Soru 10:** Starvation ve deadlock farkı?
*   **Cevap:** **c) Starvation, bir sürecin zamanlama veya öncelik sorunları nedeniyle gerekli kaynakları elde edememesi nedeniyle süresiz olarak ertelenmesi durumudur. Deadlock ise iki veya daha fazla sürecin her biri bir başkası tarafından tutulan kaynağı beklediği için kilitlenmesidir.**

---

## BÖLÜM 2: KLASİK SORULAR

**Soru 1: Multithreading modelleri nelerdir, nasıl çalıştığını birer örnek vererek açıklayınız.**
*   **Cevap:**
    1.  **Many-to-One (Çoktan Bire):** Birçok User Thread (Kullanıcı İş Parçacığı), arka planda tek bir Kernel Thread ile eşleştirilir. Eğer içlerinden birisi bloke olursa tüm süreç kilitlenir. Kötü bir modeldir.
    2.  **One-to-One (Bire Bir):** Her bir User Thread, kendi Kernel Thread'ine sahip olacak şekilde eşleşir. Gerçek eşzamanlılık (concurrency) sağlar, biri bloke olsa bile diğeri çalışır. Linux ve Windows'un mevcut modelidir.
    3.  **Many-to-Many (Çoktan Çoğa):** İşletim sistemindeki User threadler belli (daha az veya eşit) sayıdaki Kernel Thread'e havuz şeklinde paylaştırılır. Hem esnek hem performanslıdır ama yönetimi oldukça karmaşıktır.

**Soru 2: Hangi dört durum aynı anda oluştuğunda deadlock ortaya çıkabilir, maddeler halinde yazınız.**
*   **Cevap:**
    1. Mutual Exclusion (Karşılıklı Dışlama)
    2. Hold and Wait (Tut ve Bekle)
    3. No Preemption (Zorla Alamama / Engellenememezlik)
    4. Circular Wait (Döngüsel Bekleme)

**Soru 3: Bellek tahsisi ile ilgili parçalanma sorunları (fragmentation) nelerdir?**
*   **Cevap:** İki tür parçalanma sorunu vardır:
    *   **Internal Fragmentation (İç Parçalanma):** İşletim sistemi prosese sabit tam bir blok (örn. 4KB) ayırır ancak proses bunun sadece bir kısmını kullanır. Kalan kısım o blok içerisinde "boş ama tahsisli" kalarak israf olur.
    *   **External Fragmentation (Dış Parçalanma):** Bellekte, yeni gelen büyük bir süreci sığdırmaya yetecek kadar *toplamda* boşluk vardır, ancak bu boşluklar bütünleşik (ardışık) olmadığı için tahsis edilemez.

**Soru 4: Sanal Bellek (Virtual Memory) nedir, avantajları nelerdir?**
*   **Cevap:** Sanal bellek, gerçekte olan fiziksel RAM kapasitesinden çok daha büyük programların (diskteki bir alan olan paging file yardımıyla) çalıştırılabilmesini sağlayan teknolojidir. 
    *   *Çalışma Prensibi:* Sadece o an için acil gerekli olan kısımlar (sayfalar) hazır belleğe (RAM) yüklenirken geri kalanı diskte bekletilir (Demand Paging).
    *   *Avantajları:* Sisteme RAM miktarından çok daha büyük yazılımların entegre edilebilmesini sağlar, aynı anda daha fazla programın belleğe yüklenip CPU kullanımının (Multiprogramming) artmasını sağlar.

---

## BÖLÜM 3: BOŞLUK DOLDURMA (Fill in the blanks)

**a.** **[ Round Robin (RR) ]** CPU scheduling algoritması hazır kuyruğundaki her proses için CPU'yu kullanacağı sabit bir zaman dilimi (quantum) tahsis eder...
**b.** **[ Bölümlendirme (Segmentation) ]** belleği sabit boyutlu sayfaların aksine bir programın mantıksal bölümlerine dayalı olarak değişken boyutlu bölümlere ayırmak için kullanılan bir bellek tahsisi yöntemidir.
**c.** Paging yönteminde bir bellek erişimi sırasında, CPU'nun ilk olarak page tablosunu kullanarak **[ mantıksal (logical) ]** adresi, fiziksel adrese çevirmesi gerekir.
**d.** Paging yönteminde fiziksel bellek, **[ frame (çerçeve) ]** adı verilen küçük bloklara bölünür. Mantıksal bellek ise aynı boyutta **[ page (sayfa) ]** adı verilen bloklara bölünür.
**e.** Bazı page replacement algoritmaları için prosese tahsis edilen frame'lerin sayısı arttıkça page hatası oranı düşmesi beklenirken artabilir, bu duruma **[ Belady's Anomaly (Belady'nin Anomalisi) ]** denir.
**f.** **[ Optimal ]** page replacement algoritmasında, uzun süre kullanılmayacak olan page ile yer değiştirme yapılır, tüm algoritmalar arasında en düşük page hatası oranına sahiptir.
**g.** Kritik Bölge (CS) probleminin çözümünde olması gereken özelliklerden **[ Sınırlı Bekleme (Bounded Waiting) ]** özelliğine göre bir process CS'ye girmek için istekte bulunduktan sonra diğer processlerin bu processten önce CS'yi kaç kez ele geçirebileceği sayısında bir limit olmalıdır.
**h.** Bir proses CPU'da yürütülürken başka bir prosesin CPU'ya geçmesi gerektiğinde mevcut prosesin durum bilgilerinin kaydedilip CPU'dan çıkarılması ve sonraki prosesin... **[ Context Switch (Bağlam Değişimi) ]** denir.
**i.** Bilgisayar açılırken veya yeniden başlatılırken işletim sistemini başlatmak için kullanılan programa **[ Bootstrap (veya Bootloader) ]** programı denir.
**j.** Bir prosesin **[ Stack (Yığın) ]** bileşeni, fonksiyonlar çağrıldığında fonksiyon parametreleri, return adresleri, lokal değişkenler vb. geçici verileri saklamak için kullanılır.
**k.** **[ Non-preemptive (Kesintiye Uğratılamayan) ]** scheduling'te, CPU bir process'e tahsis edildiğinde, process sonlanıncaya veya bekleme durumuna geçinceye kadar process CPU'da kalır. CPU her boşta kaldığında işletim sisteminin **[ Ready (Hazır) ]**'dan bir process'i yürütmek üzere seçmesi gerekir. Bu seçme işlemi **[ Short-Term Scheduler (Kısa Vadeli Zamanlayıcı) ]** tarafından gerçekleştirilir. Kuyruk içindeki processler ile ilgili çeşitli kayıtlar **[ PCB (Process Control Block) ]** tarafından tutulur.

---

## BÖLÜM 4: EK TEST (Kâğıdın Sonundaki Bölüm)

**Soru A:** Critical section (Kritik bölge) probleminin çözümü için aşağıda verilen yöntem çiftlerinden hangisi **kullanılamaz**?
*(Not: Soru A'nın şıkları, CPU Scheduling terimleriyle karışık yazılmıştır)*
*   **Cevap Olasılıkları (Hatalı Şıklar):** c, d, e seçeneklerinde verilen "Throughput", "Waiting", "Turnaround" gibi terimlerin CS ile alakası yoktur. Bunlar CPU Scheduling (Zamanlama) kriterleridir. Mutex Logs, Semaphore ve Monitors kritk bölge probleminde kullanılır!

**Soru B:** Aşağıda verilen CPU scheduling algoritmalarına ait karşılaştırma kriterleri çiftlerinden hangisi **yanlıştır**?
a- Waiting, Turnaround 
b- CPU utilization, Swapping 
c- Throughput, Response 
d- CPU utilization, Waiting 
e- Turnaround, Response
*   **Cevap:** **b- CPU utilization, Swapping**
*   *Açıklama:* Geri kalan tüm şıklar CPU algoritmalarında hesaplanan performans kriterleridir. Ancak "Swapping" bir bellek (memory management) işlemidir, CPU scheduling algoritma başarısı ölçüm kriteri değildir.