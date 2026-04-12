# Donanımsal Senkronizasyon Çözümleri (Hardware Synchronization) - Sınav Hazırlık Özeti

Bu bölüm, yazılımsal çözümlerin yetersiz kaldığı veya performans sorunu yarattığı yerlerde, **doğrudan işlemci (CPU) ve bellek mimarisi seviyesinde** sunulan donanımsal çözümleri inceler. 

Hocalar bu bölümden özellikle **"Hangi çözüm hangi sistemde işe yarar/yaramaz?"** tarzı karşılaştırma soruları ile **Bounded-Waiting TestAndSet** kodunu sormayı çok severler.

---

## 1. Kesmeleri Kapatmak (Interrupt Disable) - "Balyoz Yöntemi"
Bir proses Kritik Bölge'de (CS) çalışırken, işlemcinin dışarıdan gelen (saat kesmesi vb.) tüm uyarıları (interrupts) dinlemeyi reddetmesidir. İşlemci adeta "kapıyı kilitler".

*   **Nasıl Çalışır?** İşlemci, kesmeleri kapattığında hiçbir şekilde onu yarıda kesip (preempt edip) bağlam değişimi (context switch) yapamaz. Bu yapı **Non-preemptive** (araya girilemez) mantığı benimser.

### 🚨 Sınav Sorusunun Geleceği Yer: Single-Processor vs Multi-Processor

| Sistem Türü | Kesmeleri Kapatma (Interrupt Disable) İşe Yarar mı? Neden? |
| :--- | :--- |
| **Tek İşlemcili (Single Processor)** | ✅ **Evet, harika çalışır.** Tek bir işlemci olduğu için, o işlemciyi dış dünyaya kapatmak başka hiçbir kodun araya girmemesini (Mutual Exclusion) kesin olarak sağlar. |
| **Çok İşlemcili (Multi-processor)** | ❌ **Uygun Değildir.** Kesmeleri kapat emrini diğer TÜM işlemcilere / çekirdeklere mesaj olarak göndermek inanılmaz **vakit alır (gecikme yaratır)**. Her CS girişinde bu yapıldığı için sistem verimliliği ve hızı (efficiency) yerle bir olur. |

---

## 2. Bellek Modelleri ve Bariyerleri (Memory Barriers)
Farklı işlemciler, performansı artırmak adına arka planda komutların sırasını (instruction reordering) değiştirebilir. Bu, özellikle ortak bellek kullanan thread'ler arasında ölümcül hatalar doğurur.

### A) Bellek Modelleri (Memory Models)
1.  **Strongly Ordered (Güçlü Sıralı):** Bir işlemcinin bellekte yaptığı değişiklik, diğer tüm işlemciler tarafından **ANINDA (hemen)** görülür.
2.  **Weakly Ordered (Zayıf Sıralı):** Bir işlemcinin bellek değişikliği, diğerleri tarafından **hemen görülmeyebilir**. 

### B) Memory Barrier (Bellek Bariyeri) Nedir?
Bellekteki bir değişikliğin **diğer tüm işlemcilere yayılmasını ve görünür kılınmasını ZORLAYAN** özel donanımlara has komuttur.

> 💡 **Kod Örneğinin Mantığı (Hoca Ne Demek İstiyor?):**
> Görseldeki `x = 100` ve `flag = true` örneğinde, zayıf sıralı (weakly ordered) bir işlemci hız kazanmak için `flag = true` işlemini hafızaya daha önce yazabilir. Eğer Thread 1, `flag`'in true olduğunu görüp döngüden çıkar ve `x`'i ekrana basarsa (ama `x` henüz `100` güncellenmediyse) HATA ÇIKAR. 
> Bu yüzden araya `memory_barrier();` konur. Bu komut der ki: *"Önce üstteki `x=100`'ü belleğe kesin olarak yaz, o load/store bitmeden ASLA alt satıra (`flag=true`) geçme!"*
> 
> **Not:** Memory Barrier çok düşük seviyeli bir donanım kodudur, genelde sıradan programcılar değil, **İşletim Sistemi (Kernel) geliştiricileri** Mutual Exclusion sağlamak için kullanır.

---

## 3. Atomik Özel Donanım Komutları (Hardware Instructions)
İşletim sistemleri, Kritik Bölge problemini aşmak için yürütülmesi sırasında **ASLA kesintiye (interrupt'a) uğramayan, "Atomik" (bölünemez)** özel donanım komutları sunar. Multiprocessor bir sistemde iki çekirdek aynı anda bu komutu çağırsalar dahi, donanım onları araya sadece biri girecek şekilde tek tek alır.

**İki Soyut Donanım Komutu:**
1.  `test_and_set()` : İçeriği (genelde byte/word) okur ve hemen ardından değerini true (kilitleme) yapar.
2.  `compare_and_swap()` (CAS) : İki veriyi atomik şekilde karşılaştırır, eşitse yerlerini değiştirir.

> ❓ **Hoca Testte Sorabilir (Tuzak Soru):** `TestAndSet` ve `CompareAndSwap` donanımsal özellikleri sayesinde tek başlarına CS'nin 3 altın kuralını da sağlar mı?
> ✅ **Cevap:** HAYIR! **Mutual Exclusion (Karşılıklı Dışlama)**'yı ve ilerlemeyi çok iyi sağlarlar. Ancak saf (sade) halleriyle kullanıldıklarında **Bounded-Waiting (Sınırlı Bekleme)** şartını sağlayamazlar, Starvation (Açlık) doğurabilirler.

---

## 4. 🚨 GÖRSELDEKİ KODUN DEŞİFRESİ: "Bounded-Waiting with TestAndSet"
*(İşte hocanın slaytta "Bu karmaşık kod nə yapar???" diye vuracağı kısım tam olarak burası!)*

Eklediğiniz görselde karmaşık gibi duran, tablolu bir **"Bounded wait solution with TestAndSet"** kodu var. Hoca "Mutex exclusion sağlıyor mu??" diye not düşmüş.

### Soru 1: Bu kod NEDEN bu kadar uzadı? Sade TestAndSet yetmiyor muydu?
Yukarıda dediğimiz gibi: Sade bir `TestAndSet` kodu, iki prosesten sadece birisinin içeri girmesine izin verir **(Mutual Exclusion SAĞLAR)**. İlerlemeyi de sağlar. 
❌ **ANCAK, Bounded-Waiting (Sınırlı Bekleme) ŞARTINI SAĞLAYAMAZ!** Kapıda bekleyen P0, P1, P2, P3 varken, P0 çıkıp CS'yi açtığında kimin daha hızlı davranıp içeri gireceği tamamen donanım hızında rastgeledir. Şanssız bir proses "Açlık (Starvation)" yaşayabilir, sonsuza dek içeri giremeyebilir.

✅ **Çözüm (Görseldeki Kod):** Starvation'u önlemek ve "Sınırlı Bekleme" kuralını sağlamak için koda `waiting[n]` (bekleyenler) isimli bir dizi (array) eklenmiştir.

### Soru 2: Entry Section (Giriş) Adım Adım Ne Yapıyor?
Görseldeki `while` döngüsü olan kısım:
```c
waiting[i] = true;             // Adım 1: "Ben (Pi) kapıya geldim, içeri girmek için kuyruktayım" (Bayrak Kaldır).
key = true;                    // Adım 2: Elimize sanal bir kilit anahtarı (key) alıyoruz.
while (waiting[i] && key)      // Adım 3: Pi hem "bekliyor" pozisyonundaysa hem de "anahtar henüz bende" değilse dönmeye (spin) devam et.
    key = TestAndSet(&lock);   // Adım 4: KİLİDİ ZORLA. Eğer açık (lock=false) ise TestAndSet onu (true) kilitler ve kendisi false döner! false dönerse while kırılır!
waiting[i] = false;            // Adım 5: Artık kilidi kırdım içeriye giriyorum. "Bekliyorum" bayrağımı false (F) yaparak CS'ye daldım.

// ---> BURASI KRİTİK BÖLGE (CS) <--- 
```
*Görseldeki tablonun açıklaması:*
P0, P1, P2 gibi prosesler var. Tabloda P0 kapıya gelip `waiting[0]=T` yapmış, `key=T` ayarlamış ve TestAndSet kapısını dövmektedir. Başardığında `waiting[0]` tablosu `F` olacak.

### Soru 3: Exit Section Algoritması Nasıl Adalet Sağlıyor? (Çıkış Kısmı)
Bencilce çıkıp `lock = false` yapıp kaçılmaz. Bir j prosesi çıkarılır (i+1 mod n şeklinde). Eğer kapıda `waiting[j] == true` olan biri varsa, direk onun `waiting[j]` değerini false yapar! Bu sayede onu döngüden manuel olarak kurtarıp kilidi bizzat ona hediye etmiş olur. İşte **Sınırlı Bekleme (Bounded Waiting)** garanti altına alınmış olur!

> 🔥 **En Net Cevap ("Mutex exclusion sağlıyor mu??" notuna):** 
> Evet kesinlikle sağlıyor. Çünkü `TestAndSet(&lock)` fonksiyonu donanım tabanlı Atomik (Bölünemez) bir fonksiyondur. İki proses P0 ve P1 döngü içerisinde aynı milisaniyede `lock`'a saldırsalar bile, işlemci donanımı yalnızca P0'a `false` döner ve hemen kapıyı kapatır. P1 `true` okuyarak kapıda beklemeye devam eder. O yüzden **Mutual Exclusion Kesinlikle Sağlanır**.

---

## 🎯 5. SINAV PROVASI: KELİME AVI VE TESPİT SORULARI

**1. Boşluk Doldurma:**
Bir değişkenin belleğe yazılması ve diğer işlemciler tarafından da görülmesinin arka planda gecikmeli olarak sağlanabildiği bellek mimarilerine **[ Weakly Ordered (Zayıf Sıralı) ]** bellek modeli denir. Yazılım ve donanım senkronizasyon kaymasını engellemek ve işlem sırasını zorunlu tutmak için **[ Memory Barrier (Bellek Bariyeri) ]** komutları kullanılır.

**2. Klasik Doğru/Yanlış Yanıltmacası:**
* *"Tek işlemcili bir sistemde (Single Processor), dış kesmeleri (interrupt) kapatmak Kritik Bölge problemini çözmek için harika ve tam garantili (Non-preemptive olduğu için) bir yoldur."* -> **DOĞRU!** Başka hiçbir komut/görev (timer dahil) araya giremeyeceği için CS güvenlidir.
* *"Mükemmel çalıştığı için, Çok çekirdekli (Multiprocessor) sistemlerde de kesmeleri kapatmak en iyi çözümdür."* -> **YANLIŞ!** Multi-process sistemlerde kesmeleri kapattırma sinyalini tüm çekirdeklere iletmek zaman alır, aşırı performans düşüşü yaratır.

**3. Görselle Alakalı / Kod Klasik Senaryo Sorusu:**
*Soru:* İşletim sistemlerinde sunulan `TestAndSet` veya `CompareAndSwap` donanım talimatlarının tek başlarına kullanıldığında yetersiz kaldığı/çözemeyebileceği Kritik Bölge şartı hangisidir? Yukarıdaki görselde bu eksiği kapatmak için nasıl bir yaklaşım sergilenmiştir?
*Cevap:* Atomik donanım talimatları tek başlarına **Bounded Waiting (Sınırlı Bekleme)** kuralını garanti edemez ve **Starvation (Açlığa)** yol açıp bir prosesin sonsuza dek kuyrukta beklemesine neden olabilirler. Görseldeki çözümde bu boşluğu kapatmak için, koda kapıda bekleyenleri adaletli sıraya koyan `waiting[i]` boolean dizisi eklenmesi yaklaşımı sergilenmiştir. Bu sayede çıkış yapan proses, bencilce kilidi fırlatıp atmak yerine kendinden sonra sırası gelen ilk bekleyen prosese kilidi bizzat teslim eder.Donanım Seviyesinde (Hardware) en kaba ama en etkili çözüme geldik. Bu yöntem, özellikle tek işlemcili (single-processor) sistemlerde "balyoz" etkisi yaratır.
