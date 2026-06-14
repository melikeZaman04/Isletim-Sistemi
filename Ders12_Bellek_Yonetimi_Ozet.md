# Ders 12 - Bellek Yönetimi: Sınav Odaklı Özet

> Kaynak slayt: **Ders12_Bellek Yönetimi.pdf**  
> Ana fikir: Bellek yönetimi, CPU'nun ürettiği adresleri güvenli, hızlı ve verimli biçimde gerçek belleğe yerleştirme işidir.

---

## 1. Giriş: Bellek Neden Merkezi Konuda?

Modern sistemlerde **ana bellek**, çalışan programların komutlarını ve verilerini tuttuğu yerdir. CPU bir programı çalıştırırken sürekli şu döngüyü yapar:

1. **Fetch:** Program counter'a göre komutu bellekten getirir.
2. **Decode:** Komutu çözer.
3. **Execute:** Gerekirse operandları bellekten alır, işlemi yapar.
4. **Write back:** Sonucu belleğe geri yazabilir.

Bellek birimi, adresin komut mu veri mi olduğunu bilmez. Sadece CPU'dan gelen **adres akışını** görür.

**Günlük benzetme:** CPU aşçı, bellek mutfak deposu gibidir. Aşçı tarife göre sürekli depodan malzeme ister. Depo, gelen isteğin tatlı için mi yemek için mi olduğunu bilmez; sadece raf numarasına bakar.

**CPU doğrudan şunlara erişebilir:**

- **Register'lar:** CPU içindedir, çok hızlıdır.
- **Ana bellek:** CPU'nun doğrudan erişebildiği genel depolama alanıdır.

Disk doğrudan CPU komutlarının operandı değildir. Veri diskteyse önce belleğe alınmalıdır.

<span style="color:red">**KRİTİK UYARI / TUZAK:** CPU disk adresiyle doğrudan işlem yapmaz. Çalışacak komut ve veri ya register'da ya da ana bellekte olmalıdır.</span>

### Sınavdan Önce Kesin Bak

Hoca burada genelde şu mantığı sorar: **"CPU neden belleğe ihtiyaç duyar, disk neden yetmez?"** Cevap: CPU'nun doğrudan erişebildiği genel depolama alanları register ve ana bellektir; disk daha yavaş ve doğrudan operand olarak kullanılmaz.

---

## 2. Bellek Alanlarının Korunması

İşletim sistemi ve kullanıcı process'leri aynı fiziksel belleği paylaşır. Bu yüzden:

- İşletim sisteminin belleği kullanıcı process'lerinden korunmalıdır.
- Kullanıcı process'leri birbirinin belleğine erişememelidir.
- Bu koruma performans düşmesin diye **donanım tarafından** yapılmalıdır.

Slayttaki temel yöntem:

- **Base register:** Process'in erişebileceği legal fiziksel adres aralığının başlangıcını tutar.
- **Limit register:** Bu aralığın boyutunu tutar.

CPU, kullanıcı modunda üretilen her adresi bu register'larla karşılaştırır. Adres legal aralık dışındaysa işletim sistemi hata üretir.

**Günlük benzetme:** Otelde herkesin kendi odası vardır. **Base**, odanın başladığı kapı numarası; **limit**, sana ayrılan oda bloğunun uzunluğudur. Başkasının odasına girersen güvenlik devreye girer.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Base ve limit register'ları kullanıcı programı değiştiremez. Bunları sadece işletim sistemi, çekirdek modunda yükleyebilir.</span>

### Sınavdan Önce Kesin Bak

Klasik soru: **"Base ve limit register ne işe yarar?"**  
Base başlangıç adresidir, limit erişilebilir aralığın boyutudur. Birlikte hem **koruma** hem de **adres sınırı kontrolü** sağlarlar.

---

## 3. Adres Bağlama (Address Binding)

Bir program önce diskte binary dosya olarak bulunur. Çalışabilmesi için belleğe alınmalıdır. Diskte bekleyen process'ler **input queue** içinde düşünülebilir.

Adresler programın yaşam döngüsünde farklı biçimlerde olabilir:

- Kaynak kodda: **sembolik adres**  
  Örnek: `count`
- Derleme sonrası: **relocatable address**  
  Örnek: "modülün başından itibaren 14. bayt"
- Yükleme sonrası: **absolute address**  
  Örnek: `74014`

**Binding**, bir adres alanından başka bir adres alanına eşlemedir.

### Binding Zamanları

| Binding zamanı | Mantık | Kritik sonuç |
|---|---|---|
| **Derleme zamanı** | Programın bellekte nereye yerleşeceği önceden bilinir. | **Absolute code** oluşur. Yer değişirse yeniden derleme gerekir. |
| **Yüklenme zamanı** | Yerleşim derlemede bilinmez. | **Relocatable code** oluşur. Başlangıç değişirse yeniden yükleme yeterlidir. |
| **Yürütme zamanı** | Process çalışırken bile taşınabilir. | Özel donanım gerekir. Modern genel amaçlı OS'lerde yaygındır. |

<span style="color:red">**KRİTİK UYARI / TUZAK:** Derleme ve yüklenme zamanı binding'de mantıksal ve fiziksel adresler aynı olabilir; yürütme zamanı binding'de genellikle farklıdır.</span>

### Sınavdan Önce Kesin Bak

Hoca "process bellekte başka yere taşınabiliyorsa hangi binding gerekir?" diye sorarsa cevap: **Yürütme zamanı binding**. Çünkü adres dönüşümü çalışma sırasında yapılmalıdır.

---

## 4. Mantıksal ve Fiziksel Adres Alanı

**Mantıksal adres (logical address):** CPU tarafından üretilen adrestir. Gerçek fiziksel belleği doğrudan göstermek zorunda değildir. **Sanal adres (virtual address)** olarak da geçer.

**Fiziksel adres (physical address):** Bellek biriminin gördüğü gerçek adrestir.

**MMU (Memory Management Unit):** Mantıksal adresi fiziksel adrese çeviren donanım birimidir.

**Mantıksal adres alanı:** Programın ürettiği tüm mantıksal adresler kümesi.  
**Fiziksel adres alanı:** Bu mantıksal adreslerin karşılık geldiği fiziksel adresler kümesi.

Basit MMU şemasında **relocation register** kullanılır:

```text
Fiziksel adres = Mantıksal adres + Relocation register
```

**Günlük benzetme:** Bir apartmanda "3. daire" demek mantıksal adres gibidir. Apartmanın şehirdeki gerçek konumu eklendiğinde fiziksel adres bulunur.

<span style="color:red">**KRİTİK UYARI / TUZAK:** CPU'nun ürettiği adres fiziksel adres değildir; CPU mantıksal adres üretir, fiziksel adresi MMU oluşturur.</span>

### Sınavdan Önce Kesin Bak

Kesin soru kalıbı: **"CPU hangi adresi üretir, bellek hangi adresi görür?"**  
Cevap: CPU **mantıksal/sanal adres** üretir; bellek **fiziksel adres** görür.

---

## 5. Dinamik Yükleme ve Dinamik Bağlama

### Dinamik Yükleme (Dynamic Loading)

Bir routine çağrılana kadar belleğe yüklenmez. Tüm routine'ler yeniden yüklenebilir formatta diskte tutulur.

Avantajı:

- Büyük programlarda belleği daha verimli kullanır.
- İşletim sisteminden özel destek gerektirmez.
- Programcı veya kütüphane yordamları tarafından yönetilebilir.

### Dinamik Bağlama ve Paylaşılan Kütüphaneler

**Dynamically linked libraries (DLL)**, çalışırken programa bağlanan sistem kütüphaneleridir.

Dinamik bağlamada programa küçük bir **stub** eklenir.

**Stub ne yapar?**

- Gerekli kütüphane routine'i bellekte mi kontrol eder.
- Yoksa yüklenmesini sağlar.
- Sonra kendini gerçek routine adresiyle değiştirir.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Dynamic loading ve dynamic linking aynı şey değildir. Loading, routine'in belleğe ne zaman alınacağıdır; linking, kütüphanenin programa ne zaman bağlanacağıdır.</span>

### Sınavdan Önce Kesin Bak

"Stub nedir?" sorusu kısa cevapta gelebilir. Net cevap: **Dinamik bağlamada kütüphane routine'ini bulmaya/yüklemeye yarayan küçük kod parçasıdır.**

---

## 6. Swapping (Yer Değiştirme)

Bir process çalışmak için bellekte olmalıdır. Ama geçici olarak:

- Bellekten diske çıkarılabilir: **swap out**
- Sonra tekrar belleğe alınabilir: **swap in**

Bu disk alanına **backing store** denir. Genellikle hızlı disk olmalıdır ve tüm bellek görüntülerini tutabilecek kadar büyük olmalıdır.

**Swapping'in amacı:** Fiziksel belleğin yetmediği durumda daha fazla process'i sistemde tutabilmek, yani **multiprogramming kabiliyetini artırmak**.

**Roll out, roll in:** Öncelik tabanlı scheduling'de düşük öncelikli process'in çıkarılıp yüksek öncelikli process'in belleğe alınmasıdır.

Swapping süresinin büyük kısmı **transfer süresidir** ve swap edilen bellek miktarıyla doğru orantılıdır.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Swapping context switch süresini çok büyütebilir. Çünkü sıradaki process bellekte değilse swap out + swap in gerekir.</span>

### I/O ve Swapping Tuzağı

Bir process I/O bekliyorsa ve I/O buffer'ı process'in kullanıcı belleğine erişiyorsa process'i swap etmek tehlikelidir. Çünkü process çıkarılıp yerine başka process gelirse I/O yanlış process'in belleğine yazabilir.

Çözümler:

- I/O bekleyen process swap edilmez.
- I/O sadece işletim sistemi buffer'larında yapılır; sonra kullanıcı belleğine kopyalanır.

### Mobil Sistemlerde Swapping

Mobil sistemlerde klasik swapping genellikle desteklenmez:

- Flash bellekte yazma ömrü sınırlıdır.
- Alan sınırlıdır.
- Main memory ile flash arasındaki throughput düşüktür.

iOS ve Android, yeterli bellek yoksa uygulamalardan bellek bırakmalarını isteyebilir veya process sonlandırabilir. Buna rağmen her ikisi de **paging** destekler.

### Sınavdan Önce Kesin Bak

Hoca "swapping neden pahalıdır?" diye sorarsa cevap: **Disk transferi yavaştır; süre, swap edilen bellek miktarıyla doğru orantılıdır.**

---

## 7. Bitişik Bellek Tahsisi (Contiguous Memory Allocation)

Bu yöntemde bellek iki ana parçaya ayrılır:

- İşletim sisteminin bulunduğu kısım
- Kullanıcı process'lerinin bulunduğu kısım

Her process bellekte **tek ve bitişik bir blokta** yer alır.

### Sabit ve Değişken Bölmelendirme

**Fixed partition:** Bellek sabit boyutlu bölmelere ayrılır. Aynı anda çalışabilecek program sayısı bölüm sayısına bağlıdır.

**Variable partition:** Belleğin boş ve dolu parçaları tabloyla tutulur. Process ihtiyacı kadar yer alır, bu yüzden daha verimlidir.

Boş kullanılabilir bellek bloklarına **hole** denir.

Process geldiğinde işletim sistemi yeterince büyük bir hole arar. Hole büyükse bölünür; process çıkınca alan tekrar hole listesine döner. Yan yana hole'ler birleşebilir.

### Dynamic Storage Allocation Yöntemleri

| Yöntem | Mantık |
---|---|
| **First fit** | Yeterli büyüklükteki ilk hole seçilir. |
| **Best fit** | Yeterli hole'ler içinde en küçüğü seçilir. |
| **Worst fit** | Yeterli hole'ler içinde en büyüğü seçilir. |

Simülasyonlara göre **first fit** ve **best fit**, zaman ve depolama kullanımı açısından genelde **worst fit'ten iyidir**.

<span style="color:red">**KRİTİK UYARI / TUZAK:** "Best fit her zaman en iyidir" diye düşünme. Slaytın söylediği: first fit ve best fit, worst fit'ten daha iyidir. Best fit'in tüm listeyi araması gerekebilir.</span>

### Sınavdan Önce Kesin Bak

"Hole nedir?" sorusu kolay görünür ama gelir: **Kullanılabilir boş bellek bloğudur.**  
"First/best/worst fit farkı nedir?" tabloyu ezber değil, hole seçme mantığıyla bil.

---

## 8. Fragmentation: İç ve Dış Parçalanma

### External Fragmentation (Dış Parçalanma)

Toplam boş bellek yeterlidir ama boş alanlar bitişik değildir. Bu yüzden istek karşılanamaz.

**Benzetme:** Otelde toplam 5 boş oda var ama hepsi farklı katlarda tek tek dağılmış. 5 kişilik yan yana oda isteyen aileyi yerleştiremiyorsun.

Çözüm olarak **compaction** yapılabilir:

- Process'ler belleğin bir ucuna taşınır.
- Boşluklar diğer uçta büyük tek blok yapılır.

Ama compaction pahalıdır ve sadece **dinamik relocation** varsa yürütme zamanında yapılabilir.

### Internal Fragmentation (İç Parçalanma)

Process'e ayrılan bellek, istediğinden biraz büyüktür. Aradaki fark ayrılmıştır ama kullanılmaz.

**Benzetme:** 7 kişilik grup için 10 kişilik masa ayırmak. Masa senin ama 3 sandalye boş kalır.

<span style="color:red">**KRİTİK UYARI / TUZAK:** External fragmentation = boşluklar dışarıda dağınık. Internal fragmentation = ayrılan bloğun içinde kullanılmayan alan.</span>

### Sınavdan Önce Kesin Bak

Kısa cevapta "hangisi paging ile çözülür?" diye sorulabilir: **Paging external fragmentation ve compaction ihtiyacını ortadan kaldırır; internal fragmentation yine olabilir.**

---

## 9. Segmentation (Bölütleme)

Programcı belleği genellikle düz bir bayt dizisi gibi düşünmez. Programı şu parçalar halinde düşünür:

- Main program
- Fonksiyonlar
- Prosedürler
- Nesneler
- Diziler
- Stack
- Değişkenler

**Segmentation**, programcının gördüğü bu mantıksal parçaları fiziksel belleğe eşler.

Mantıksal adres iki parçadan oluşur:

```text
<segment number, offset>
<s, d>
```

Segment tablosundaki her girişte:

- **Segment base:** Segmentin fiziksel bellekteki başlangıç adresi.
- **Segment limit:** Segmentin uzunluğu.

Ek register'lar:

- **STBR (Segment-table base register):** Segment tablosunun bellekteki konumunu gösterir.
- **STLR (Segment-table length register):** Programın kullandığı segment sayısını gösterir.

### Segmentation'da Koruma

Her segment girişi:

- Valid/invalid biti
- Okuma/yazma/yürütme izinleri

içerebilir.

Segmentler değişken boyutlu olduğu için bellek tahsisi yine **dynamic storage allocation** problemidir.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Segmentation bitişik olmayan tahsis avantajı sağlar ama external fragmentation'ı tamamen ortadan kaldırmaz. Paging bunu yapar.</span>

### Sınavdan Önce Kesin Bak

"Segmentation adres yapısı nedir?" cevabı net: **`<segment number, offset>`**.  
"Segment table entry ne tutar?" cevabı: **base ve limit**.

---

## 10. Paging (Sayfalama)

**Paging**, process'in fiziksel bellekte bitişik olmak zorunda kalmadan yerleşmesini sağlar.

Paging ile:

- **External fragmentation ortadan kalkar.**
- **Compaction ihtiyacı kalkar.**
- Process'in page'leri herhangi boş frame'lere yerleştirilebilir.
- Ancak **internal fragmentation** hala olabilir.

### Page ve Frame

- **Frame:** Fiziksel belleğin sabit boyutlu bloklarıdır.
- **Page:** Mantıksal belleğin frame ile aynı boyuttaki bloklarıdır.

Page/frame boyutu genellikle **2'nin kuvvetidir**.

Bir process'in `N` page'i varsa çalışması için `N` boş frame gerekir.

### Paging Adres Yapısı

CPU'nun ürettiği mantıksal adres ikiye ayrılır:

```text
page number | page offset
     p      |      d
```

- **Page number (p):** Page table içinde indeks olarak kullanılır.
- **Page offset (d):** Frame içindeki yer değiştirmedir.

Eğer mantıksal adres alanı `2^m`, page boyutu `2^n` bayt ise:

- Yüksek öncelikli `m - n` bit: **page number**
- Düşük öncelikli `n` bit: **page offset**

```text
Mantıksal adres = p + d
p = m - n bit
d = n bit
```

**Örnek mantık:** Page table sana "page 0, frame 5'te" diyorsa, frame 5'in başlangıcına offset eklenir.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Page number fiziksel adresin kendisi değildir. Page table'da frame numarasını bulmak için kullanılan indekstir.</span>

### Paging'de İç Parçalanma Örneği

Slayttaki örnek:

```text
Page size = 2048 bayt
Process size = 72766 bayt
```

Hesap:

```text
72766 = 35 page + 1086 bayt
36. page'e 1086 bayt yerleşir.
Boş kalan = 2048 - 1086 = 962 bayt
```

En kötü durumda iç parçalanma:

```text
Page size - 1
```

2048 bayt page için:

```text
2047 bayt
```

Ortalama iç parçalanma yaklaşık **page boyutunun yarısıdır**.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Page boyutu küçülürse iç parçalanma azalır ama page table giriş sayısı ve ek yük artar.</span>

### Sınavdan Önce Kesin Bak

Hoca sayısal sorabilir: **"m ve n bit verilirse page number/offset kaç bit?"**  
Formül: page size `2^n` ise offset `n` bit, page number `m-n` bit.

---

## 11. Page Table ve TLB

**Page table**, her page'in hangi fiziksel frame'e karşılık geldiğini tutar.

Page table ana bellekte tutulur.

- **PTBR (Page Table Base Register):** Page table'ın başlangıcını gösterir.
- **PTLR (Page Table Length Register):** Page table boyutunu gösterir.

Bu basit şemada her komut/veri erişimi için iki bellek erişimi gerekir:

1. Page table'a erişim
2. Gerçek veri/komuta erişim

Bu sorunu azaltmak için **TLB (Translation Look-aside Buffer)** kullanılır.

### TLB Nedir?

**TLB**, page number -> frame eşleşmelerini tutan hızlı donanım önbelleğidir.

Her TLB girişi:

- Anahtar: **page number**
- Değer: **frame number**

**Hit ratio:** Page numarasının TLB'de bulunma yüzdesidir.

Bazı TLB'lerde:

- **Wired down** girişler olabilir; bunlar TLB'den çıkarılamaz.
- **ASID (Address-Space Identifier)** bulunabilir; process'i benzersiz tanımlar.

ASID yoksa context switch sırasında yanlış adres dönüşümünü önlemek için TLB temizlenmelidir.

<span style="color:red">**KRİTİK UYARI / TUZAK:** TLB page table'ın yerine geçmez; page table erişimini hızlandıran önbellektir.</span>

### Sınavdan Önce Kesin Bak

"Hit ratio nedir?" cevabı: **Aranan page numarasının TLB'de bulunma oranıdır.**  
"ASID ne işe yarar?" cevabı: **Process'lerin adres alanlarını ayırt eder; TLB'nin yanlış process dönüşümünü kullanmasını engeller.**

---

## 12. Paging'de Bellek Koruması

Page tablosundaki girişlere koruma bitleri eklenebilir:

- Read-only
- Read-write
- Execute-only
- Valid-invalid

**Valid bit:** Page process'in mantıksal adres alanındadır.  
**Invalid bit:** Page process'in mantıksal adres alanında değildir.

İhlal olursa çekirdekte hata oluşur.

Alternatif olarak **PTLR**, adresin geçerli aralıkta olup olmadığını kontrol etmek için kullanılabilir.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Invalid page, "page diskte" anlamına gelmek zorunda değildir. Bu slayt bağlamında process'in mantıksal adres alanında olmayan/geçersiz page demektir.</span>

### Sınavdan Önce Kesin Bak

Valid-invalid biti sorulursa: **Adres erişiminin process için legal olup olmadığını gösterir.**

---

## 13. Paylaşılan Sayfalar

Paging'in önemli avantajlarından biri **shared pages** desteğidir.

Özellikle **reentrant / read-only code** process'ler arasında paylaşılabilir.

Örnek:

- 40 kullanıcı aynı text editor'ü çalıştırıyor.
- Kod 150 KB, veri 50 KB.
- Kod read-only ise tek kopya paylaşılır.
- Her process'in kendi data page'i olur.

Bu, bellek tasarrufu sağlar.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Paylaşılan kod genellikle read-only/reentrant olmalıdır. Her process'in veri alanı ayrı kalır.</span>

### Sınavdan Önce Kesin Bak

"Kod paylaşılır mı, veri paylaşılır mı?" diye gelirse: **Read-only kod güvenle paylaşılır; her process'in kendi verisi ayrı tutulur.**

---

## 14. Page Table Yapıları

Basit page table çok büyük olabilir.

Örnek:

```text
32-bit logical address
Page size = 4 KB = 2^12
Page table entry sayısı = 2^32 / 2^12 = 2^20
```

Yani yaklaşık **1 milyon giriş**. Her giriş 4 bayt ise process başına yaklaşık **4 MB page table** gerekir.

Bu yüzden farklı page table yapıları kullanılır:

- **Hierarchical Paging**
- **Hashed Page Tables**
- **Inverted Page Tables**

---

## 15. Hierarchical Paging

Mantıksal adres alanı birden çok page tablosuna bölünür.

En yaygın örnek: **Two-level paging**

32-bit adres ve 4 KB page için:

- Offset: `12 bit`
- Page number: `20 bit`
- Page number ikiye bölünebilir:
  - `p1`: dış page table indeksi
  - `p2`: iç page table indeksi

Adres yapısı:

```text
p1 | p2 | d
```

Bu şemaya **forward-mapped page table** da denir.

64-bit adres alanlarında iki seviyeli paging yeterli olmayabilir; dış page table çok büyür. Daha fazla seviye gerekir ama bu da karmaşıklık ve erişim maliyeti getirir.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Hierarchical paging page table'ı küçültmek için page table'ın kendisini de sayfalar; ama seviye arttıkça adres çevirme maliyeti artabilir.</span>

### Sınavdan Önce Kesin Bak

"Two-level paging'de p1 ve p2 neyi gösterir?"  
**p1 dış page table indeksi, p2 iç page table indeksi, d offsettir.**

---

## 16. Hashed Page Tables

32 bitten büyük adres alanlarında yaygın bir yaklaşımdır.

Sanal page numarası hash fonksiyonuyla tabloya yerleştirilir. Her hash girişinde bağlı liste olabilir.

Her eleman üç alan içerir:

1. **Virtual page number**
2. **Eşlenen physical frame**
3. **Sonraki elemanı gösteren pointer**

Arama mantığı:

- Sanal page number hashlenir.
- Listedeki elemanların virtual page number alanı karşılaştırılır.
- Eşleşme varsa frame değeri alınır ve offset ile fiziksel adres oluşturulur.

**Clustered page table** varyasyonu, tek girişte birden fazla page-frame eşlemesini tutabilir. Sparse adres alanları için faydalıdır.

### Sınavdan Önce Kesin Bak

"Hashed page table elemanı hangi alanlardan oluşur?" sorusu gelebilir: **virtual page number, frame value, pointer.**

---

## 17. Inverted Page Tables

Standart paging'de her process'in kendi page table'ı vardır. Bu tablolar çok büyüyebilir.

**Inverted page table** yaklaşımında:

- Sistemde yalnızca **tek page table** vardır.
- Fiziksel bellekteki her gerçek frame için bir giriş bulunur.
- Her girişte ilgili **process** ve **page** bilgisi tutulur.

IBM RT örneğinde sanal adres:

```text
<process-id, page-number, offset>
```

Tabloda eşleşme bulunursa, örneğin `i`. satır eşleşirse fiziksel adres:

```text
<i, offset>
```

Avantaj:

- Page table için gereken bellek azalır.

Dezavantaj:

- Arama süresi artar.
- Aramayı hızlandırmak için hash table ve TLB kullanılabilir.
- Paylaşılan belleği uygulamak zorlaşır.

<span style="color:red">**KRİTİK UYARI / TUZAK:** Inverted page table fiziksel frame başına giriş tutar; process başına ayrı page table tutmaz.</span>

### Sınavdan Önce Kesin Bak

"Inverted page table avantaj/dezavantaj?"  
Avantaj: **Bellek tasarrufu.**  
Dezavantaj: **Arama maliyeti artar, shared memory zorlaşır.**

---

## Mini Karşılaştırma Tablosu

| Kavram | En kısa akılda kalma hali |
---|---|
| **Logical address** | CPU'nun ürettiği adres |
| **Physical address** | Belleğin gördüğü gerçek adres |
| **MMU** | Logical -> physical çeviren donanım |
| **Swapping** | Process'i bellekten diske çıkarıp geri alma |
| **Contiguous allocation** | Process tek bitişik blokta durur |
| **External fragmentation** | Toplam boşluk var ama bitişik değil |
| **Internal fragmentation** | Ayrılan bloğun içinde kullanılmayan alan |
| **Segmentation** | Programı mantıksal bölütlere ayırır |
| **Paging** | Mantıksal page'leri fiziksel frame'lere eşler |
| **TLB** | Page table dönüşümlerinin hızlı önbelleği |
| **Page table** | Page -> frame eşlemesini tutar |

---

# Sınav Provası: Boşluk Doldurma ve Kısa Cevap

## A) Boşluk Doldurma

1. CPU tarafından üretilen adrese __________ adres denir.
2. Bellek biriminin gördüğü gerçek adrese __________ adres denir.
3. Mantıksal adresi fiziksel adrese çeviren donanım birimi __________ olarak adlandırılır.
4. Bir process'in geçici olarak bellekten diske çıkarılmasına __________ denir.
5. Bitişik bellek tahsisinde kullanılabilir boş bellek bloklarına __________ denir.
6. Toplam boş bellek yeterli olduğu halde bitişik olmadığı için isteğin karşılanamamasına __________ parçalanma denir.
7. Ayrılan bellek bloğunun içinde kullanılmayan alan kalmasına __________ parçalanma denir.
8. Paging'de fiziksel bellek bloklarına __________, mantıksal bellek bloklarına __________ denir.
9. Page numarasının TLB'de bulunma oranına __________ denir.
10. Segment tablosunda her giriş segmentin başlangıcını ve uzunluğunu gösteren __________ ve __________ bilgilerini tutar.

## B) Kısa Cevap

1. Derleme zamanı binding ile yürütme zamanı binding arasındaki temel fark nedir?
2. Base register ve limit register birlikte neyi sağlar?
3. Dynamic loading ile dynamic linking arasındaki farkı bir cümleyle yaz.
4. Swapping neden context switch süresini artırabilir?
5. Paging external fragmentation'ı nasıl ortadan kaldırır?
6. Page size küçülürse avantaj ve dezavantaj nedir?
7. TLB neden kullanılır?
8. ASID ne işe yarar?
9. Hashed page table elemanının üç alanı nelerdir?
10. Inverted page table'ın en büyük avantajı ve en büyük dezavantajı nedir?

---

# Cevap Anahtarı

## A) Boşluk Doldurma Cevapları

1. **Mantıksal / logical / sanal**
2. **Fiziksel / physical**
3. **MMU**
4. **Swap out / swapping**
5. **Hole**
6. **External fragmentation / dış parçalanma**
7. **Internal fragmentation / iç parçalanma**
8. **Frame, page**
9. **Hit ratio / isabet oranı**
10. **Base, limit**

## B) Kısa Cevap Cevapları

1. Derleme zamanı binding'de adresler program belleğe yerleşmeden belirlenir; yürütme zamanı binding'de process çalışırken taşınabilir ve adres dönüşümü çalışma sırasında yapılır.
2. Process'in yalnızca kendisine ait legal bellek aralığına erişmesini sağlar.
3. Dynamic loading routine'i çağrılınca belleğe alır; dynamic linking kütüphaneyi çalışırken programa bağlar.
4. Sıradaki process bellekte değilse bir process swap out, diğeri swap in yapılır; disk transferi yavaştır.
5. Process'in page'leri fiziksel bellekte herhangi boş frame'lere yerleştirilebilir; bitişik alan gerekmez.
6. Avantaj: iç parçalanma azalır. Dezavantaj: page table giriş sayısı ve yönetim ek yükü artar.
7. Page table erişimini hızlandırmak ve iki bellek erişimi maliyetini azaltmak için kullanılır.
8. Process'lerin adres alanlarını ayırt eder, TLB'de yanlış process'e ait dönüşümün kullanılmasını engeller.
9. Virtual page number, physical frame value, pointer.
10. Avantajı page table belleğini azaltmasıdır; dezavantajı arama süresini artırması ve shared memory'yi zorlaştırmasıdır.
