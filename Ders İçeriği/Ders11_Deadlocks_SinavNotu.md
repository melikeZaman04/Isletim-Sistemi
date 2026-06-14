# 🔒 DEADLOCKS (Ders 11) – TAM ÇALIŞMA & SINAV NOTU

> **Kaynak:** `Ders11_Deadlocks.pdf` (78 slayt) — Dr. Öğr. Üyesi Ertan Bütün
>
> 🎯 **İşaretler:** 🔴 = slaytta **kırmızı** (terim/madde) · ⬛ = **siyah koyu/bold** · 📝 = boşluk doldurma · 🧮 = işlem/tablo sorusu · ⚠️ = tuzak
>
> **Yapı:** ① Kavramlar açık anlatım → ② Sınav notu → ③ Çıkabilecek sorular → ④ Çözümlü örnekler

---

# ① BÖLÜM: KAVRAMLARIN ANLAŞILIR ANLATIMI

## 🧩 Deadlock (Kilitlenme) Nedir?

Hayal et: İki kişi tek bir kapıdan geçmeye çalışıyor ama her ikisi de "önce sen geç" diyerek diğerinin hareket etmesini bekliyor. İkisi de sonsuza kadar bekler → **kimse geçemez.** İşte bu **deadlock**'tır.

🔴 **Tanım:** Çoklu programlama (multiprogramming) ortamında, **bekleyen bir process'in talep ettiği kaynaklar, başka kaynakları bekleyen process'ler tarafından tutulduğu için bir daha asla durumunu değiştiremediği** duruma **deadlock** denir.

> 💡 **Önemli not:** İşletim sistemleri (Linux, Windows) genellikle deadlock önleme mekanizması **sağlamaz** → **program geliştiricinin** deadlock oluşmayacak şekilde kod yazması gerekir.

## 🔧 Sistem Modeli – Kaynak Kullanımı

Sistemde farklı türde **kaynaklar (resources)** vardır: CPU cycle, dosya, I/O cihazları (yazıcı, DVD). Bunlar R₁, R₂, …, Rₘ ile gösterilir. Her kaynak türünün **bir veya birden fazla örneği (instance)** olabilir.

🔴 Bir process kaynağı **3 adımda** kullanır:
1. 🔴 **Request (İstek):** Kaynak ister; uygun değilse **bekler.**
2. 🔴 **Use (Kullan):** Kaynak üzerinde işlemini yapar.
3. 🔴 **Release (Serbest bırak):** Kaynağı geri bırakır.

> 📌 Bu işlemlerin gerçek karşılıkları: cihaz → `request()/release()`, dosya → `open()/close()`, hafıza → `allocate()/free()`, semafor → `wait()/signal()`, mutex → `acquire()/release()`.

---

## ⭐ Deadlock'ın 4 GEREKLİ KOŞULU (EN ÖNEMLİ KONU!)

Deadlock oluşması için aşağıdaki **4 koşulun AYNI ANDA** gerçekleşmesi gerekir. Birini bile engellersen deadlock olmaz.

| # | Koşul | Açık Anlatım |
|---|-------|--------------|
| 1 | 🔴 **Mutual Exclusion** (Karşılıklı dışlama) | En az bir kaynak **paylaşılamaz** modda olmalı → bir anda **sadece 1 process** kullanabilir. (Örn: yazıcı) |
| 2 | 🔴 **Hold and Wait** (Tut ve bekle) | Bir process **bir kaynağı tutarken**, başka bir process'in tuttuğu **başka kaynağı da bekliyor** olmalı. |
| 3 | 🔴 **No Preemption** (Zorla alınamama) | Kaynak, tutan process'ten **zorla alınamaz**; ancak process **gönüllü** olarak (işi bitince) bırakır. |
| 4 | 🔴 **Circular Wait** (Dairesel bekleme) | {P₀, P₁, …, Pₙ} process'leri **dairesel** bekler: P₀→P₁'i, P₁→P₂'yi, …, Pₙ→P₀'ı bekler. |

> ⚠️ **Çok kritik bağlantı:** Bu koşullar tamamen bağımsız değildir. **Circular wait oluştuğunda, hold and wait da otomatik olarak vardır.**

---

## 📊 Kaynak Tahsisi Grafı (Resource-Allocation Graph)

Deadlock'ı görselleştirmek için **yönlü graf (directed graph)** kullanılır.

- **Düğümler (V):** İki gruba ayrılır → **P** = process'ler (○ daire), **R** = kaynaklar (▭ dikdörtgen).
- Kaynağın **birden fazla örneği** varsa → dikdörtgen içinde **her örnek bir nokta (•)** ile gösterilir.

🔴 **İki kenar (edge) türü:**
- 🔴 **Request edge (İstek kenarı):** `Pi → Rj` → Pi, Rj'yi **istiyor ve bekliyor.**
- 🔴 **Assignment edge (Atama kenarı):** `Rj → Pi` → Rj kaynağı Pi'ye **atanmış.**

> İstek karşılanınca: istek kenarı → atama kenarına dönüşür. Kaynak bırakılınca: atama kenarı **silinir.**

### 🎯 Döngü (Cycle) ile Deadlock İlişkisi — KRİTİK KURAL!

| Durum | Sonuç |
|-------|-------|
| 🔴 Grafta **döngü YOK** | ✅ **Deadlock YOK** (kesin) |
| 🔴 Döngü VAR + her kaynağın **TEK örneği** | ❌ **Deadlock VAR** (döngü → gerekli VE yeterli koşul) |
| 🔴 Döngü VAR + kaynakların **birden fazla örneği** | ⚠️ **Deadlock OLABİLİR** (döngü → gerekli ama YETERLİ DEĞİL) |

---

## 🛠️ Deadlock ile Başa Çıkma – 3 Genel Yol

🔴 Deadlock problemine **3 farklı yaklaşım:**
1. 🔴 **Önleme/Kaçınma protokolü kullan** → sistem **hiçbir zaman** deadlock'a düşmez.
2. 🔴 **Deadlock'a izin ver, sonra algıla ve çöz.**
3. 🔴 **Problemi tamamen yok say** ("deadlock hiç olmayacak" gibi davran).

> ⚠️ **3. yaklaşım** işletim sistemlerinde **en yaygın** kullanılır (**Linux, Windows**) → deadlock yönetimini **uygulama geliştiriciye** bırakırlar.

İki ana yöntem grubu:
- 🔴 **Deadlock Prevention (Önleme):** Kaynak isteklerini **sınırlandırarak** 4 koşuldan birini engeller.
- 🔴 **Deadlock Avoidance (Kaçınma):** Her process'in **maksimum ihtiyacını önceden bildirmesini** ister, kaynak tahsis durumunu **dinamik** inceler.

---

## 🚫 DEADLOCK ÖNLEME (Prevention) – 4 Koşulu Tek Tek Kırmak

### 1️⃣ Mutual Exclusion'ı Kır
- Paylaşılabilir kaynaklar (örn. **read-only dosya**) zaten deadlock oluşturmaz.
- ⚠️ **AMA genelde işe yaramaz** → bazı kaynaklar **özünde paylaşılamaz** (örn. mutex lock aynı anda paylaşılamaz).

### 2️⃣ Hold and Wait'i Kır (2 protokol)
- 🔴 **Protokol 1:** Process **çalışmaya başlamadan ÖNCE TÜM kaynaklarını** talep eder.
  - ⚠️ Dezavantaj: Kaynağı sonradan kullanacaksa bile **tüm süre boyunca tutar → verimsiz kullanım.**
- 🔴 **Protokol 2:** Process **hiç kaynak tutmuyorken** yeni istek yapabilir. Yeni istek öncesi **elindekilerin hepsini bırakır.**
- ⚠️ **Her iki protokolde de STARVATION mümkündür** (popüler kaynak bekleyen process süresiz bekleyebilir).

> 📌 **DVD örneği:** Process: DVD→disk kopyala, sırala, yazıcıya yazdır.
> - Protokol 1: DVD + disk + yazıcıyı **baştan** ister (yazıcıyı sonda kullansa bile tutar = verimsiz).
> - Protokol 2: Önce DVD+disk ister → kopyalar → bırakır → sonra disk+yazıcı ister.

### 3️⃣ No Preemption'ı Kır (2 protokol)
- 🔴 **Protokol 1:** Process kaynak tutarken alamadığı yeni kaynak isterse → **elindeki tüm kaynaklar preempt edilir** (dolaylı serbest bırakılır), bekleme listesine eklenir. Eski + yeni kaynakları alabilince yeniden başlar.
- 🔴 **Protokol 2:** İstenen kaynağı tutan process **başka kaynak bekliyorsa** → kaynak ondan alınıp (preempt) **yeni isteyene verilir.** Beklemiyorsa → **isteyen bekletilir.**

### 4️⃣ Circular Wait'i Kır (EN PRATİK YÖNTEM)
- 🔴 Her kaynak türüne **farklı bir tam sayı (F fonksiyonu)** atanır → kaynaklar **sıralanır.**
- 🔴 Process kaynak isteğini **yalnızca ARTAN sırada** yapabilir.
- 🔴 Pi'ye Ri atandıysa, ancak **F(Rj) > F(Ri)** koşulunu sağlayan Rj'yi isteyebilir.
- ⬛ **İspat:** Eğer circular wait olsaydı → F(R₀) < F(R₁) < … < F(Rₙ) < F(R₀) çelişkisi çıkar. **F(Rₙ) < F(R₀) olamayacağı için circular wait OLUŞAMAZ.**

---

## ⚠️ DEADLOCK'TAN KAÇINMA (Avoidance)

🔴 **Temel fikir:** Her process **maksimum kaynak ihtiyacını önceden bildirir.** Sistem, kaynak tahsis durumunu **dinamik** inceleyerek **circular wait'in asla oluşmayacağından** emin olur.

> ⚠️ Önleme yöntemleri cihazlardan **az faydalanmaya ve düşük throughput'a** neden olur; kaçınma bu yüzden alternatiftir.

### 🔑 Safe State (Güvenli Durum) – ÇOK ÖNEMLİ KAVRAM

🔴 **Safe State:** Sistem, kaynakları process'lere **belirli bir sırayla (safe sequence)** maksimum ihtiyaçları kadar atayıp **deadlock olmadan** hepsini tamamlayabiliyorsa, sistem **güvenli durumdadır.**

🔴 **Safe Sequence `<P₁, P₂, …, Pₙ>`:** Her Pi'nin ihtiyacı, **mevcut boş kaynaklar + ondan önceki tüm Pj'lerin (j<i) tuttuğu kaynaklar** ile karşılanabiliyorsa geçerlidir. Pi tamamlanınca kaynaklarını iade eder, sıradaki Pi+1 çalışır...

🔴 **Temel kurallar:**
| Durum | Sonuç |
|-------|-------|
| Sistem **safe state** | ✅ **Deadlock YOK** |
| Sistem **unsafe state** | ⚠️ **Deadlock OLMA İHTİMALİ VAR** |

> 💡 **Görsel mantık:** deadlock ⊂ unsafe ⊂ tüm durumlar. Deadlock'tan kaçınma = sistemin **asla unsafe state'e girmemesini** sağlamak. (Unsafe = OS artık deadlock'ı engelleyemeyebilir.)

### 📐 Kaynak Tahsisi Graf Algoritması (TEK örnekli kaynaklar için)
- 🔴 İstek/atama kenarlarına ek olarak **claim edge (niyet kenarı)** eklenir → `Pi --→ Rj` (noktalı çizgi): "Pi ileride Rj'yi isteyebilir."
- Process çalışmaya başlamadan **tüm niyet kenarları** grafta olmalı.
- 🔴 **Kural:** Pi, Rj'yi isterse → istek kenarını atama kenarına çevirmek **döngü oluşturmuyorsa** izin verilir (safe). **Döngü oluşuyorsa → unsafe → Pi bekler.**

### 🏦 Banker's Algorithm (Banker Algoritması) – ÇOK örnekli kaynaklar için

🔴 Graf algoritması **çok örnekli kaynaklarda çalışmaz** → **Banker algoritması** kullanılır.

> 💡 **İsmin mantığı:** Banka, parasını **hiçbir zaman tüm müşterilerin ihtiyacını karşılayamayacak şekilde** dağıtmaz. Yeni process maksimum ihtiyacını bildirir; istek ancak sistemi **safe state'te bırakacaksa** kabul edilir.

🔴 **4 veri yapısı** (n=process sayısı, m=kaynak türü sayısı):
| Yapı | Boyut | Anlamı |
|------|-------|--------|
| 🔴 **Available** | m vektör | Her kaynaktan kaç **boş** örnek var |
| 🔴 **Max** | n×m matris | Her process'in **maksimum** talebi |
| 🔴 **Allocation** | n×m matris | Her process'in **şu an kullandığı** kaynak |
| 🔴 **Need** | n×m matris | **Kalan ihtiyaç** = ⬛ **Need = Max − Allocation** |

#### 🔍 İki Alt Algoritma:
**A) Safety Algorithm (Güvenlik Algoritması)** – sistem güvenli mi?
```
1. Work = Available;  Finish[i] = false (tüm i)
2. Şu koşulu sağlayan i bul:  Finish[i]==false  VE  Need_i ≤ Work
      → varsa adım 3'e, yoksa adım 4'e
3. Work = Work + Allocation_i ;  Finish[i] = true ;  → adım 2'ye dön
4. Tüm Finish[i]==true ise → SİSTEM GÜVENLİ
```

**B) Resource-Request Algorithm** – Pi'nin Request isteği onaylanır mı?
```
1. Request_i ≤ Need_i  ?  değilse → HATA (maksimumu aştı)
2. Request_i ≤ Available ?  değilse → Pi BEKLER (kaynak yok)
3. Geçici tahsis yap:
      Available = Available − Request_i
      Allocation_i = Allocation_i + Request_i
      Need_i = Need_i − Request_i
   → Güvenlik algoritmasını çalıştır:
      Güvenli ise → tahsis et;  Değilse → Pi bekler, eski duruma dön
```

---

## 🔍 DEADLOCK ALGILAMA (Detection)

Sistem önleme/kaçınma kullanmıyorsa deadlock olabilir → algılamak için iki durum:

### A) Her kaynaktan TEK örnek → Wait-For Graph
- 🔴 **Wait-for grafı:** Kaynak tahsisi grafından **kaynak düğümleri çıkarılır**, sadece process'ler kalır.
- 🔴 `Pi → Pj` kenarı: "Pi, Pj'yi bekliyor."
- 🔴 **Wait-for grafında DÖNGÜ varsa → DEADLOCK var.**
- Periyodik olarak döngü arayan algoritma çalıştırılır.

### B) Her kaynaktan ÇOK örnek → Banker'a benzer algoritma
🔴 Veri yapıları: **Available, Allocation, Request** (Request[i][j]=k → Pi, Rj'den k tane daha istiyor).
```
1. Work = Available
   Allocation_i ≠ 0 ise Finish[i]=false, değilse Finish[i]=true
2. Finish[i]==false VE Request_i ≤ Work olan i bul → varsa 3, yoksa 4
3. Work = Work + Allocation_i ; Finish[i]=true ; → 2'ye dön
4. BAZI Finish[i]==false ise → SİSTEM DEADLOCK'TA
```
> ⚠️ **Safety vs Detection farkı:** Safety'de **Need** kullanılır; Detection'da **Request** kullanılır. Detection'da Allocation=0 olanlar baştan Finish=true.

### ⏰ Algılama Algoritması NE ZAMAN Çalışmalı?
🔴 İki faktöre bağlı: **(1)** Deadlock ne sıklıkta olur? **(2)** Kaç process etkilenir?
- Sık deadlock → sık çalıştır.
- ⚠️ Her istekte çalıştırmak **pahalı (yüksek ek yük).**
- 🔴 Ucuz alternatif: **belirli aralıklarla** çalıştır (örn. saatte bir, veya **CPU kullanımı %40'ın altına düşünce**).

---

## 🔓 DEADLOCK'TAN KURTULMA (Recovery)

🔴 Deadlock algılanınca: ya **operatöre bildir** (manuel), ya **otomatik kurtul.** İki seçenek:

### Seçenek 1: Process Sonlandırma (Abort)
🔴 İki yöntem:
1. 🔴 **Tüm deadlock process'lerini sonlandır** → sonuçlar kaybolur (pahalı ama kesin).
2. 🔴 **Döngü kırılana kadar birer birer sonlandır** → her sonlandırmada **döngü kontrolü** yapılır.

⚠️ **Abort riski:** Process dosya güncellemenin/mutex tutmanın ortasındaysa → **veri tutarsızlığı** oluşabilir.

🔴 **Hangi process sonlandırılmalı?** = ekonomik/maliyet sorunu. Etkileyen **6 faktör:**
1. Önceliği · 2. Ne kadar çalıştığı / kalan süresi · 3. Kullandığı kaynak sayısı-türü · 4. Tamamlanması için gereken kaynak · 5. Kaç process sonlanmalı · 6. Etkileşimli (interactive) mi, toplu (batch) mu

### Seçenek 2: Kaynak Preemption (Zorla alma)
🔴 Döngü kırılana kadar kaynaklar **sırayla alınıp** başka process'e verilir. **3 konu:**
1. 🔴 **Selecting a victim (Kurban seçimi):** Maliyeti en aza indirecek sıra.
2. 🔴 **Rollback:** Kaynağı alınan process **güvenli duruma geri alınır**, oradan yeniden başlar.
3. 🔴 **Starvation:** Hep aynı process kurban seçilirse **açlık** olur → maliyet faktörüne **sonlandırma sayısını da kat** (önlem).

---

# ② BÖLÜM: SINAVA HAZIRLIK – ÖZET KARTLARI

## 🎯 Tanım Hızlı Tekrar
| Terim | Tek Cümle |
|-------|-----------|
| **Deadlock** | Process'lerin karşılıklı, sonsuz bekleyip ilerleyemediği durum |
| **Mutual Exclusion** | Kaynak paylaşılamaz, bir anda 1 process |
| **Hold and Wait** | Kaynak tutarken başkasını beklemek |
| **No Preemption** | Kaynak zorla alınamaz |
| **Circular Wait** | P₀→P₁→…→Pₙ→P₀ dairesel bekleme |
| **Request/Assignment edge** | Pi→Rj istek / Rj→Pi atama |
| **Claim edge** | Pi--→Rj niyet (noktalı, ileride isteyebilir) |
| **Wait-for graph** | Kaynaksız, sadece process'li graf; döngü=deadlock |
| **Safe state** | Safe sequence ile deadlocksuz tamamlanabilen durum |
| **Need** | Max − Allocation |
| **Banker's algorithm** | Çok örnekli kaynakta avoidance |

## 🔑 Ezberlenecek KESİN Kurallar
- **Döngü yok → deadlock yok** (her zaman)
- **Döngü + tek örnek → deadlock VAR** (gerekli+yeterli)
- **Döngü + çok örnek → deadlock OLABİLİR** (gerekli, yeterli değil)
- **Safe → deadlock yok** · **Unsafe → deadlock olabilir**
- **Need = Max − Allocation**
- 4 koşulun **HEPSİ aynı anda** olmalı; **circular wait → hold-and-wait içerir**
- Safety algoritması **Need** kullanır, Detection **Request** kullanır
- Linux & Windows → 3. yöntem (yok say), yönetimi geliştiriciye bırakır

## ⚠️ En Çok Karıştırılanlar
- **Prevention** (4 koşuldan birini kır) ↔ **Avoidance** (max ihtiyaç bilinir, dinamik kontrol)
- **Avoidance** (deadlock oluşmadan engelle) ↔ **Detection** (oluşmasına izin ver, sonra bul)
- **Graf algoritması** (tek örnek) ↔ **Banker** (çok örnek)
- Banker **Need** ↔ Detection **Request**
- Recovery: **Abort** (process öldür) ↔ **Preemption** (kaynak al)

---

# ③ BÖLÜM: ÇIKABİLECEK SORULAR

### Tanım/Kavram Soruları
1. Deadlock'ın 4 gerekli koşulunu yazıp **kısaca** açıklayınız. *(klasik soru!)*
2. Circular wait oluştuğunda hangi koşul da otomatik var olur? **(Hold and wait)**
3. Request edge ile assignment edge arasındaki fark nedir?
4. Kaynak tahsisi grafında döngü varsa kesinlikle deadlock var mıdır? Hangi durumda evet, hangisinde belki?
5. Safe state, unsafe state ve deadlock arasındaki ilişkiyi açıklayın. (deadlock ⊂ unsafe)
6. Deadlock prevention ile avoidance arasındaki fark nedir?
7. Wait-for grafı nasıl elde edilir, deadlock'ı nasıl gösterir?
8. Deadlock algılama algoritması ne zaman çalıştırılmalı?
9. Deadlock'tan kurtulmanın iki yolu nedir? (abort / preemption)
10. Kurban seçiminde (victim) starvation neden oluşur, nasıl önlenir?

### Boşluk Doldurma (📝)
- Bir anda sadece bir process'in kaynağı kullanması ________ (**mutual exclusion**).
- `Need = ________ − ________` (**Max − Allocation**).
- Tek örnekli kaynaklarda deadlock algılama için ________ grafı kullanılır (**wait-for**).
- Sistem ________ state'te ise deadlock yoktur (**safe**).
- Çok örnekli kaynakta kaçınma için ________ algoritması kullanılır (**Banker's**).
- İleride istenebilecek kaynağı gösteren kenar ________ (**claim edge / niyet kenarı**).

### İşlem Soruları (🧮) — *kesin gelir!*
- Bir kaynak tahsisi grafı verilip "deadlock var mı?" sorusu.
- Banker's algorithm: Need matrisini hesaplayıp **safe sequence** bulma.
- Resource-Request: bir Request'in onaylanıp onaylanmayacağı (safe mi?).
- Detection: verilen Allocation/Request tablosunda deadlock var mı?

---

# ④ BÖLÜM: ÇÖZÜMLÜ ÖRNEKLER

## 🧮 ÖRNEK 1: Kaynak Tahsisi Grafı – Deadlock var mı?

**Durum:** R₁(1 örnek), R₂(2), R₃(1), R₄(3). P₁ R₂'yi tutar R₁'i bekler; P₂ R₁ ve R₂ tutar R₃ bekler; P₃ R₃ tutar.
→ Bu durumda **döngü yok → DEADLOCK YOK.**

**Şimdi P₃, R₂'den bir örnek istesin.** İki döngü oluşur:
```
P₁ → R₁ → P₂ → R₃ → P₃ → R₂ → P₁
P₂ → R₃ → P₃ → R₂ → P₂
```
✅ **Sonuç: P₁, P₂, P₃ DEADLOCK olur.** (P₂, P₃'ün R₃'ünü bekler; P₃, R₂'yi bekler; P₁, P₂'nin R₁'ini bekler.)

> ⚠️ **Karşı örnek:** `P₁→R₁→P₃→R₂→P₁` döngüsü olsa bile, eğer **P₄, R₂'yi bırakırsa P₃ kullanabilir → döngü kırılır → DEADLOCK YOK.** (Çok örnekli kaynakta döngü ≠ kesin deadlock.)

---

## 🧮 ÖRNEK 2: BANKER'S ALGORITHM – Safe Sequence Bulma *(en önemli örnek!)*

**Sistem:** 5 process (P₀–P₄), 3 kaynak: **A(10), B(5), C(7)**. T₀ anı:

| Process | Allocation | Max | **Need = Max−Alloc** |
|---------|-----------|-----|------|
| P₀ | 0 1 0 | 7 5 3 | **7 4 3** |
| P₁ | 2 0 0 | 3 2 2 | **1 2 2** |
| P₂ | 3 0 2 | 9 0 2 | **6 0 0** |
| P₃ | 2 1 1 | 2 2 2 | **0 1 1** |
| P₄ | 0 0 2 | 4 3 3 | **4 3 1** |

**Available (boş) = (3 3 2)** → bu `Work`'ün başlangıcı.

**Adım adım Safety Algorithm:**
| Adım | Work | Kontrol | Sonuç |
|------|------|---------|-------|
| Başla | **3 3 2** | P₀ Need(7 4 3) ≤ (3 3 2)? **HAYIR** | P₀ atla |
| | 3 3 2 | P₁ Need(1 2 2) ≤ (3 3 2)? **EVET** | ✅ P₁ seç, Work += Alloc(2 0 0) |
| | **5 3 2** | P₃ Need(0 1 1) ≤ (5 3 2)? **EVET** | ✅ P₃ seç, Work += (2 1 1) |
| | **7 4 3** | P₄ Need(4 3 1) ≤ (7 4 3)? **EVET** | ✅ P₄ seç, Work += (0 0 2) |
| | **7 4 5** | P₀ Need(7 4 3) ≤ (7 4 5)? **EVET** | ✅ P₀ seç, Work += (0 1 0) |
| | **7 5 5** | P₂ Need(6 0 0) ≤ (7 5 5)? **EVET** | ✅ P₂ seç, Work += (3 0 2) |
| Bitti | **10 5 7** | Tüm Finish=true | 🎯 **GÜVENLİ** |

✅ **SAFE SEQUENCE = `<P₁, P₃, P₄, P₀, P₂>`** → Sistem güvenli durumda.

> 💡 **Çözüm ipucu:** Her adımda **Need ≤ Work** olan ilk process'i seç, onun Allocation'ını Work'e ekle. Hepsi bitince güvenli.

---

## 🧮 ÖRNEK 3: RESOURCE-REQUEST – İstek onaylanır mı?

**Soru:** P₁, `Request₁ = (1, 0, 2)` istiyor. (Available=3 3 2, Need₁=1 2 2)

**Adım 1:** Request₁ ≤ Need₁ → (1,0,2) ≤ (1,2,2)? **✅ true**
**Adım 2:** Request₁ ≤ Available → (1,0,2) ≤ (3,3,2)? **✅ true**
**Adım 3:** Geçici tahsis yapılır:
- Available = (3,3,2) − (1,0,2) = **(2, 3, 0)**
- Allocation₁ = (2,0,0) + (1,0,2) = **(3,0,2)** · Need₁ = **(0,2,0)**
- Güvenlik algoritması → `<P₁,P₃,P₄,P₀,P₂>` safe sequence bulunur.

✅ **Sonuç: Sistem güvenli → İstek DERHAL KABUL EDİLİR.**

---

## 🧮 ÖRNEK 4: REDDEDİLEN İstek

**Soru:** (Örnek 3 sonrası) P₄, `Request₂ = (3, 3, 0)` istiyor. (Available şimdi=2 3 0, Need₄=4 3 1)

**Adım 1:** (3,3,0) ≤ Need₄(4,3,1)? **✅ true**
**Adım 2:** (3,3,0) ≤ Available(2,3,0)? **❌ FALSE** (A'da 3 isteniyor ama 2 var)

❌ **Sonuç: Adım 2 sağlanmadı → kaynaklar yetersiz → İstek REDDEDİLİR (P₄ bekler).**

---

## 🧮 ÖRNEK 5: KAYNAKLAR VAR AMA UNSAFE → Reddedilir

**Soru:** P₀, `Request₃ = (0, 2, 0)` istiyor. (Available=2 3 0)
- Adım 1 ve 2 geçer (kaynaklar **kullanılabilir**), ama geçici tahsis sonrası **güvenlik algoritması safe sequence BULAMAZ → unsafe.**

❌ **Sonuç: Kaynaklar yeterli olsa bile yeni durum UNSAFE → İstek KABUL EDİLMEZ.**

> ⚠️ **Önemli ders:** Kaynak var olması yeterli değil; **tahsis sonrası safe state korunmalı!**

---

## 🧮 ÖRNEK 6: DEADLOCK DETECTION – Deadlock var mı?

**Sistem:** 5 process, kaynaklar **A(7), B(2), C(6)**, T₀ anı:

| Process | Allocation | Request | |
|---------|-----------|---------|---|
| P₀ | 0 1 0 | 0 0 0 | |
| P₁ | 2 0 0 | 2 0 2 | |
| P₂ | 3 0 3 | 0 0 0 | |
| P₃ | 2 1 1 | 1 0 0 | |
| P₄ | 0 0 2 | 0 0 2 | |

**Available = (0 0 0)**

**Detection çalıştır:** Request ≤ Work olanları sırayla bul:
- Work=(0 0 0): P₀ Request(0 0 0)≤(0 0 0)✅ → Work+=Alloc(0 1 0)=(0 1 0)
- P₂ Request(0 0 0)≤(0 1 0)✅ → Work+=(3 0 3)=(3 1 3)
- P₃ Request(1 0 0)≤(3 1 3)✅ → Work+=(2 1 1)=(5 2 4)
- P₄ Request(0 0 2)≤(5 2 4)✅ → Work+=(0 0 2)=(5 2 6)
- P₁ Request(2 0 2)≤(5 2 6)✅ → Work+=(2 0 0)=(7 2 6)

✅ **Tüm Finish=true → `<P₀,P₂,P₃,P₄,P₁>` → DEADLOCK YOK.**

### 🔄 Şimdi T₁'de P₂, `(0,0,1)` istesin → Request₂ = (0 0 1):
- Work=(0 0 0): Sadece **P₀** Request(0 0 0)≤(0 0 0)✅ → Work=(0 1 0)
- Diğer hiçbiri Request ≤ Work sağlamaz! (P₁ ister 2 0 2, P₂ ister 0 0 1 ama C'de 0 var, P₃ ister 1 0 0, P₄ ister 0 0 2...)

❌ **P₀ hariç hepsinin Finish=false → P₁, P₂, P₃, P₄ DEADLOCK olur!**

> 💡 **Sonuç:** Tek bir küçük istek (P₂'nin 1 tane C istemesi) bile sistemi deadlock'a sokabilir.

---

> 🍀 **Başarılar!** En sık gelenler: **4 koşul (tanım+açıklama)**, **döngü-deadlock ilişkisi**, **Banker safe sequence hesabı** ve **Resource-Request kabul/red analizi**. İşlem sorularında mutlaka **Need = Max − Allocation** ile başla ve her adımda **Need(veya Request) ≤ Work** kontrolünü tablo halinde yaz.
