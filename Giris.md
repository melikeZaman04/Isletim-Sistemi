
# İşletim Sistemlerine Giriş ve Temel Kavramlar (Bölüm 1)

## 1. İşletim Sistemi Nedir? (Tarihsel ve Genel Tanım)
İlk bilgisayarlarda işlemler, delikli **kartlarla (punch cards)** manuel olarak yüklenerek yapılırdı. Daha sonra bu rutin ve yavaş işleri takip eden, donanımı otomatikleştiren bir yazılım (İşletim Sistemi) oluşturuldu.

**Günümüzde İşletim Sistemi:** Bilgisayarın sabit diskinde (HDD/SSD) depolanan ve bilgisayar açıldığında belleğe (RAM) otomatik olarak yüklenen ana programdır. (Operating System Concepts – 10th Edition 1.6 Silberschatz, Galvin and Gagne ©2018)

> 💡 **En Genel Tanım:** İşletim Sistemi (OS), bilgisayarın donanımını yöneten; bilgisayar kullanıcısı ile donanımı arasında **aracı görevi gören** ve programları çalıştırarak donanımın verimli kullanılmasını sağlayan yazılımdır.

---

## 2. İşletim Sisteminin Amaçları ve Rolleri
İşletim sistemi, her zaman arka planda çalışan ve sistemi organize eden yazılımdır. Temel 3 ana amacı vardır:

1.  **Ortam Sağlamak:** Bir bilgisayar kullanıcısının, programlarını en uygun, kolay ve verimli şekilde yürütebilmesi için platform oluşturmak.
2.  **Kaynak Tahsisi (Resource Allocator):** Gerekli görevleri gerçekleştirmek için bilgisayarın donanım kaynaklarını adil, düzenli ve verimli bir şekilde tahsis etmek (dağıtmak).
3.  **Kontrol Programı Olmak (Control Program):** İki ana işleve hizmet eder:
    *   Bilgisayarın uygunsuz kullanımını ve hataları önlemek için kullanıcı programlarının yürütülmesini denetler.
    *   I/O (Giriş/Çıkış) cihazlarıyla ilgili işlemleri yönetir ve I/O cihazlarının kontrolünü sağlar.

> ❓ **Hoca Sorabilir (Boşluk Doldurma / Açıklama):** "İşletim sistemi kaynak dağıtıcısı (____) ve denetleyici (____) olarak iki ana görev üstlenir."
> ✅ **Cevap:** **Resource Allocator** (Kaynak Paylaştırıcı) ve **Control Program** (Kontrol Programı).

### Öğrenilmesi Gereken İki Kritik Tanım:
*   **Resource Allocator:** İşletim sistemi, bilgisayarın CPU zamanı, bellek (RAM) alanı, disk alanı gibi sınırlı kaynaklarını yönetir ve bunları kullanıcı programlarına tahsis eder. Bu süreç, kaynakların adil ve verimli bir şekilde kullanılmasını sağlar.
*   **Control Program:** OS, bilgisayarın uygunsuz kullanımını ve hataları önlemek için kullanıcı programlarının yürütülmesini denetler. I/O cihazlarının kontrolünü sağlar. Bu, bilgisayarın güvenli ve stabil (kararlı) bir şekilde çalışmasına olanak tanır.

---

## 3. Bilgisayar Sisteminin Bileşenleri (4 Mantıksal Yapı)
Bir bilgisayar sistemi temelden kullanıcıya doğru 4 ayrı katmana ayrılır:

| Katman | İşlevi | Örnek |
| :--- | :--- | :--- |
| **1. Donanım (Hardware)** | Temel bilgi işlem kaynaklarını sağlar. Tüm sistemin fiziksel varlığıdır. | CPU, Bellek (RAM), Diskler, Klavye, Ekran |
| **2. İşletim Sistemi (OS)** | Donanımı kontrol eder ve uygulamalar arasında bölüştürür (Aracı katman). | Windows, Linux, Android |
| **3. Uygulama Programları** | Kullanıcının spesifik problemlerini çözen sistemin görünen yüzüdür. | Word, Chrome, Oyunlar, Derleyiciler |
| **4. Kullanıcılar (Users)** | Sistemi kullanan taraftır. | İnsanlar, makineler, başka bilgisayarlar |

![Bilgisayar Sisteminin Soyut Görünümü](image-1.png)

---

## 4. Çekirdek (Kernel), Sistem ve Uygulama Programları

> 🚨 **'Soru Gelir' Alarmı (Kısa Cevap / Boşluk Doldurma):** "Bilgisayarda her zaman, sistem açılışından kapanışına kadar durmadan çalışan işletim sisteminin kalbine (ana programa) ne ad verilir?"
> ✅ **Cevap:** **Çekirdek (Kernel)** denir.

İşletim sistemi ortamında bulunan programlar:
1.  **Kernel (Çekirdek):** Her zaman çalışan ana kısımdır.
2.  **Sistem Programları:** İşletim sistemiyle birlikte gelir (gönderilir), sistemi idare etmeni sağlarlar ancak çekirdeğin (kernel) *kendisinin bir parçası DEĞİLDİRLER*.
3.  **Uygulama Programları:** İşletim sistemiyle direkt ilişkisi olmayan tüm dış (sonradan kurulan) programlardır.

### Mobil İşletim Sistemleri ve Middleware (Ara Yazılım)
İşletim sistemlerinin özellikleri günümüzde sürekli artmaktadır. Özellikle mobil işletim sistemleri (iOS, Android vb.) yalnızca bir Kernel'den ibaret değildir. 
*   **Middleware (Ara Yazılım):** Aynı zamanda uygulama geliştiricilerine doğrudan veritabanları, multimedya işleme veya grafik hesaplamaları gibi ek hizmetler sağlayan bir dizi yazılım framework'ü (kütüphane altyapısı) içeren **ara yazılımdır (middleware)**.

---

## 5. Ders-1 İçin Hocanın Sorabileceği İlave Kritik Konular (Sınavlık Kavramlar)
İşletim Sistemlerine giriş derslerinin (Ders 1) klasik konuları bağlamında sorulabilecek en temel kavramlar:

### A) Kesmeler (Interrupts) ve Traps
İşletim sistemi **"Kesme Odaklı" (Interrupt-driven)** çalışır. 
*   **Donanım Kesmesi (Hardware Interrupt):** Mouse hareket ettiğinde veya diske veri geldiğinde donanımın CPU'ya gönderdiği "Bana bak, iş geldi!" elektrik sinyalidir.
*   **Yazılım Kesmesi (Trap / Exception):** Kod çalışırken yanlış işlem yapıldığında (Örn: sıfıra bölme, yetkisiz belleğe erişim), yazılımın ürettiği bir uyarıdır (exception). OS devreye girip o programı kapatır.

### B) Çift Modlu Çalışma (Dual-Mode Operation) - Güvenliğin Temeli
Hocaların çok önemsediği konudur. Sistemin çökmesini engellemek için OS iki farklı yetki modunda donanımsal bir "Mode Bit" ile yönetilir:
1.  **User Mode (Kullanıcı Modu - Bit: 1):** Sınırlı yetkiyle çalışılan moddur. Sıradan bir uygulama donanıma (disk, RAM'in geneli) kendisi doğrudan erişemez.
2.  **Kernel Mode (Çekirdek Modu - Bit: 0):** Tam yetkili (Privileged) moddur. Kritik işletim sistemi komutları ve I/O işlemleri burada yapılır.

> ❓ **Hoca Sorabilir (Açıklama):** Kullanıcı bir uygulamada (örn: Word) dosyayı kaydet dediğinde yetki süreci nasıl işler?
> ✅ **Cevap:** Uygulama (Bit:1) User Mode'da iken diske kendi yazamaz. Bunun için OS'ye bir **Sistem Çağrısı (System Call)** yapar. Donanım bunu algılayıp modu Kernel Mode'a (Bit:0) geçirir. OS işlemi güvenlik kontrolünden geçirip kalıcı diske kaydeder ve normal moda (User Mode) geri döner.

### C) Bellek Hiyerarşisi (Memory Hierarchy) Standartları
Hız, maliyet ve kalıcılık açısından hocalar bu sıralamayı testte/boşluk doldurmada sever. Kapasite büyüdükçe hız düşer.

| Bellek Türü | Hız | Kapasite / Depolama | Kalıcılık Durumu (Power Off) |
| :--- | :--- | :--- | :--- |
| **Registers (Yazmaçlar)** | En Hızlı (CPU İçi) | Çok Küçük (Byteler) | Silinir (Uçucu / **Volatile**) |
| **Cache (Önbellek)** | Çok Hızlı (SRAM) | Küçük (MB seviyesi) | Silinir (Uçucu / **Volatile**) |
| **Main Memory (RAM)** | Orta Hızlı (DRAM) | Orta Boyut (GB seviyesi)| Silinir (Uçucu / **Volatile**) |
| **SSD / Manyetik Disk** | Yavaş | Büyük (TB seviyesi) | **Kalıcı (Non-Volatile)** |

### D) Doğrudan Bellek Erişimi (DMA - Direct Memory Access)
*   **Neden Kullanılır?** Büyük miktardaki I/O verilerinin (örneğin devasa bir disk kopyalaması veya yüklemesinin) işlemciyi (CPU) sürekli meşgul etmesini önlemek içindir. 
*   **Nasıl Çalışır?** Cihaz kontrolcüsü (Device Controller) veriyi CPU'ya uğramadan DOĞRUDAN ana belleğe (RAM'e) bloklar halinde aktarır. Sadece blok bittiğinde işlemciye tek bir Kesme (Interrupt) atılır.

---

## 6. Özet: Niye İşletim Sistemine İhtiyacımız Var?
İşletim sistemleri, bilgisayarın donanımını yönetmenin yanı sıra, kullanıcıların bilgisayarı daha kolay ve verimli bir şekilde kullanmalarını sağlar.
*   Kullanıcıların **dosyaları yönetmelerine**,
*   Çeşitli **programları çalıştırmalarına**,
*   Aynı anda çalışırken (Concurrency) **bilgisayarın kaynaklarını paylaşmalarına** olanak tanır.
*   Ayrıca, donanımın birbirine girmemesi ve programların birbirini bozmaması için **çeşitli güvenlik önlemleri** içerir (Mode Bit, Memory Protection).