# 🧠 CPU SCHEDULING (Ders 10) – SINAV ODAKLI TAM NOT

> **Kaynak:** `Ders10_CPU_Scheduling 3.pdf` (73 slayt)
> **Hoca:** Dr. Öğr. Üyesi Ertan Bütün — *soruları DOĞRUDAN slayttan soruyor!*
>
> 🎯 **İşaretler:**
> - 🔴 = Slaytta **kırmızı** yazılmış (terim/başlık) → tanım sorusu çok olası
> - ⬛ = Slaytta **siyah koyu/bold** yazılmış → vurgulu, sorulur
> - 📝 = **Boşluk doldurma** sorusu
> - 🧮 = **İşlem / Gantt şeması** sorusu (kesin gelir!)
> - ⚠️ = Tuzak / sık karıştırılan nokta

---

## 📋 KONULAR (Bu PDF'in işlediği başlıklar)
1. Thread Scheduling
2. Multiple-Processor Scheduling
3. Real-Time CPU Scheduling
4. İşletim Sistemlerinde Scheduling Örnekleri (Linux, Windows, Solaris)
5. Bir Scheduling Algoritması Nasıl Seçilir?

---

# 1️⃣ THREAD SCHEDULING

- 🔴 Thread'lerin desteklendiği OS'lerde **process'ler yerine THREAD'ler schedule edilir.**
- 🔴 **User-level thread'ler** bir **thread kütüphanesi** tarafından yönetilir; **kernel bunların farkında değildir.**
- User-level ve kernel-level thread'ler **farklı şekilde** schedule edilir.

## 🟦 User-Level Thread Scheduling → PCS
- User-level thread'in CPU'da çalışması için **kernel-level bir thread'le eşleşmesi** gerekir (dolaylı olabilir → **LWP = lightweight process** kullanılır).
- 🔴⬛ **Process-Contention Scope (PCS):** CPU için rekabet, **AYNI process'e ait thread'ler arasında** gerçekleşir.
- **many-to-one** ve **many-to-many** modellerinde kullanılır.
- PCS **önceliğe (priority) göre** yapılır → en yüksek öncelikli thread seçilir.
- ⚠️ User-level thread öncelikleri **PROGRAMCI tarafından** belirlenir.

## 🟦 Kernel-Level Thread Scheduling → SCS
- 🔴⬛ **System-Contention Scope (SCS):** CPU için rekabet, **SİSTEMDEKİ TÜM thread'ler arasında** gerçekleşir.
- 🔴 **one-to-one** modeli kullanan **Windows, Linux, Solaris** → **yalnızca SCS** kullanır.

### 📝 BOŞLUK DOLDURMA
- Aynı process'in thread'leri arasındaki rekabet ________ (**PCS / Process-Contention Scope**).
- Sistemdeki tüm thread'ler arasındaki rekabet ________ (**SCS / System-Contention Scope**).
- Windows, Linux, Solaris ________ (**one-to-one**) modelini kullanır ve ________ (**SCS**) ile schedule eder.

## 🟦 Pthread Scheduling (POSIX)
- POSIX Pthread API, thread oluştururken PCS veya SCS belirlemeye izin verir:
  - 🔴 **`PTHREAD_SCOPE_PROCESS`** → **PCS** kullanır
  - 🔴 **`PTHREAD_SCOPE_SYSTEM`** → **SCS** kullanır
- ⚠️ **Linux ve macOS yalnızca `PTHREAD_SCOPE_SYSTEM`'e izin verir.**

### 📝 BOŞLUK DOLDURMA
- `PTHREAD_SCOPE_PROCESS` → ________ (**PCS**), `PTHREAD_SCOPE_SYSTEM` → ________ (**SCS**).

---

# 2️⃣ MULTIPLE-PROCESSOR SCHEDULING

- Multi-processor'da scheduling, **yük paylaşımı (load sharing)** kullanır ama **çok daha karmaşıktır.**
- 🔴 Modern "multiprocessor" tanımı şunları kapsar:
  - ⬛ **Multicore CPUs**
  - ⬛ **Multithreaded cores**
  - ⬛ **NUMA systems**
  - ⬛ **Heterogeneous multiprocessing**

## 🟦 İki Temel Yaklaşım (TANIM SORUSU!)

| Yaklaşım | Özellik |
|----------|---------|
| 🔴 **Asymmetric multiprocessing** | Tüm scheduling/I/O kararlarını **TEK bir işlemci (master CPU)** verir; diğer CPU'lar kullanıcı kodu çalıştırır. **Basittir** (tek çekirdek veriye erişir). ⚠️ **Dezavantaj:** master CPU **darboğaz (bottleneck)** olabilir. |
| 🔴 **Symmetric multiprocessing (SMP)** | Her işlemcinin **kendi scheduling algoritması** vardır. **Master CPU YOKTUR.** |

### 🔴 SMP'de 2 Strateji (kuyruk yaklaşımı):
1. **Common ready queue (ortak hazır kuyruğu):** Tüm thread'ler ortak kuyrukta.
   - ⚠️ **Race condition olabilir** → **locking** gerekir → kilit darboğaz oluşturur, **performans düşebilir.**
2. **Per-core run queues (her işlemcinin kendi kuyruğu):**
   - ✅ Performans kaybı yok → 🔴 **SMP'de EN YAYGIN yaklaşım.**
   - ⚠️ **Sorun:** işlemciler arası **değişken iş yükü** → **dengeleme algoritmaları** gerekir.

- 🔴 Windows, Linux, macOS + **Android, iOS** mobil OS'ler **SMP'yi destekler.**

### 📝 BOŞLUK DOLDURMA
- Tek master CPU'lu yaklaşım ________ (**asymmetric multiprocessing**).
- Her işlemcinin kendi algoritması olan ________ (**symmetric multiprocessing / SMP**).
- SMP'de en yaygın strateji ________ (**her işlemcinin kendi kuyruğu / per-core run queue**).

## 🟦 Processor Affinity (İşlemci Yakınlığı)
- Process **başka işlemciye** taşınınca: eski işlemcideki **cache geçersiz olur**, yeni işlemcide **cache yeniden yüklenir** → **yüksek maliyet.**
- 🔴 Bu yüzden SMP, process'i **AYNI işlemcide** tutmaya çalışır → **processor affinity.**
- 🔴 **Soft affinity:** Process bir işlemciye atanır ama aynı işlemcide çalışması **GARANTİ EDİLMEZ.**
- 🔴 **Hard affinity:** Process bir işlemciye atanır ve her zaman aynı işlemcide çalışması **GARANTİ EDİLİR.**
- 🔴 **Linux hem soft hem hard affinity destekler.**

### 📝 BOŞLUK DOLDURMA
- Aynı işlemcide çalışma garanti EDİLMEZ → ________ (**soft affinity**).
- Aynı işlemcide çalışma garanti EDİLİR → ________ (**hard affinity**).

## 🟦 NUMA (Non-Uniform Memory Access)
- Her CPU'nun **kendi belleğine erişimi HIZLI (fast access)**, diğer CPU'nun belleğine erişimi **YAVAŞ (slow access)**.

## 🟦 Load Balancing (Yük Dengeleme)
- 🔴 SMP'de tüm işlemcilere iş yükü dağıtarak **verimi artırır.**
- ⚠️ **Ortak kuyruk** kullanan sistemlerde yük dengelemeye **GEREK YOK.**
- ⚠️ **Her işlemcinin kendi kuyruğu** olan sistemlerde yük dengeleme **GEREKLİDİR.**

### 🔴 2 Yöntem (TANIM/karşılaştırma sorusu!):
| Yöntem | Mantık |
|--------|--------|
| 🔴 **Push migration** | Periyodik kontrol; **aşırı yüklü** işlemciden boş/az meşgul işlemciye process **İTİLİR (push).** |
| 🔴 **Pull migration** | **Boş kalan** işlemci, dolu işlemcideki bekleyen process'i kendine **ÇEKER (pull).** |

- ⚠️ Push ve pull **birbirini dışlamaz**, genellikle **paralel** uygulanır.

### 📝 BOŞLUK DOLDURMA
- Aşırı yüklü işlemciden process itme ________ (**push migration**).
- Boş işlemcinin process çekmesi ________ (**pull migration**).

## 🟦 Multicore Processors
- 🔴 **Aynı fiziksel yonga üzerine birden çok çekirdek** yerleştirme = multicore.
- Her çekirdek OS'e **ayrı fiziksel işlemci** olarak görünür.
- ⬛ Multicore SMP, ayrı yongalı sistemlerden **daha hızlıdır ve daha az güç tüketir.**

### 🔴 Memory Stall (Bellek Durması)
- İşlemci belleğe erişince veri gelene kadar **bekler** = **memory stall**.
- Sebep: önbellekte (cache) olmayan veriye erişim.
- ⚠️ İşlemci zamanının **%50'sini** bekleyerek geçirebilir.
- **Çözüm:** 🔴⬛ **Her çekirdeğe 2+ donanım thread'i atanan multithreaded çekirdekler** → bir thread beklerken çekirdek **diğer thread'e geçer.**
- ⚠️ **İŞLEM SORUSU:** Her donanım thread'i OS'e **mantıksal işlemci** olarak görünür.
  - 🧮 **dual-threaded + dual-core sistem = OS açısından `4` (dört) mantıksal işlemci!**

### 📝 BOŞLUK DOLDURMA
- İşlemcinin veri beklemesi ________ (**memory stall**).
- dual-threaded, dual-core sistem ________ (**4**) mantıksal işlemci olarak görünür.

---

# 3️⃣ REAL-TIME CPU SCHEDULING

## 🔴 İki Tür Real-Time Sistem (TANIM SORUSU – kesin gelir!)

| Tür | Özellik |
|-----|---------|
| 🔴 **Soft real-time** | Kritik process'in **ne zaman** çalışacağı garanti EDİLMEZ; sadece **diğerlerine göre öncelikli** çalışması garanti edilir. |
| 🔴 **Hard real-time** | **Daha katı.** Görev **deadline'a kadar MUTLAKA** hizmet almalı. ⚠️ **Deadline'dan sonra verilen hizmet = HİÇ hizmet verilmemesiyle aynıdır.** |

### 📝 BOŞLUK DOLDURMA
- Sadece öncelik garantisi veren ________ (**soft real-time**).
- Deadline'ı mutlaka karşılaması gereken ________ (**hard real-time**).

## 🟦 Latency (Gecikme) Türleri
- 🔴 **Event latency:** Bir olay oluştuktan sonra **cevap verilene kadar** geçen süre.
- 🔴 Real-time performansını **2 tür gecikme** etkiler:
  1. 🔴 **Interrupt latency:** CPU'ya **interrupt gelmesi** ile **istenen işleme başlaması** arasındaki süre.
  2. 🔴 **Dispatch latency (sevk gecikmesi):** Bir process'in **durdurulup** diğerinin **başlatılması** için geçen süre.

### 🔴 Dispatch Latency 2 Aşamadan Oluşur:
1. 🔴 **Conflict aşaması** (2 kısım):
   - Çekirdekte çalışan process'in **durdurulması**
   - Yüksek öncelikli process'in ihtiyacı olan kaynakların **düşük öncelikli process'lerce serbest bırakılması**
2. 🔴 **Dispatch aşaması:** Yüksek öncelikli process uygun CPU'ya **schedule edilir.**

### 📝 BOŞLUK DOLDURMA
- Interrupt gelmesi ile işleme başlama arası ________ (**interrupt latency**).
- Process durdurulup diğerinin başlaması arası ________ (**dispatch latency**).
- Dispatch latency aşamaları ________ (**conflict**) ve ________ (**dispatch**).

## 🟦 Priority-Based Scheduling
- 🔴 Real-time OS'in en önemli özelliği: process CPU'ya ihtiyaç duyduğu an **ANINDA YANIT vermesidir.**
- 🔴 Scheduler **preemption + önceliğe dayalı (priority-based)** algoritma desteklemeli.
- ⬛ Preemptive sistemde **yüksek öncelikli process gelince** çalışan process **askıya alınır.**
- ⚠️ Preemptive + priority-based scheduler → **soft real-time garanti** edilir, AMA **deadline garantisi YOKTUR.**
- ⬛ **Hard real-time** ek schedule özellikleri gerektirir.

## 🟦 Periyodik Process Karakteristikleri (İŞLEM için ŞART!)
- Process'ler **periyodik** kabul edilir → CPU'ya **sabit periyotlarla** ihtiyaç duyar.
- 🔴 **t** = işlem süresi (CPU burst), **d** = deadline, **p** = periyot
- 🔴 İlişki: **0 ≤ t ≤ d ≤ p**
- 🔴 Periyodik görevin **rate** değeri = **1/p**
- Deadline = bir sonraki periyodun başlama zamanı.

### 📝 BOŞLUK DOLDURMA
- İşlem süresi ________ (**t**), deadline ________ (**d**), periyot ________ (**p**).
- İlişki ________ (**0 ≤ t ≤ d ≤ p**), rate ________ (**1/p**).

---

## 🔴 3 Hard Real-Time Algoritması
1. **Rate-Monotonic Scheduling**
2. **Earliest-Deadline-First Scheduling**
3. **Proportional Share Scheduling**

---

## 🧮 3.1 RATE-MONOTONIC SCHEDULING (RMS) — İŞLEM SORUSU KESİN!

- 🔴 **Preemptive, priority-based** algoritma.
- 🔴⬛ Her process **periyot süresiyle TERS ORANTILI öncelik** alır.
  - **Periyot kısaldıkça → öncelik ARTAR** (CPU'yu sık isteyene yüksek öncelik).
- ⚠️ **STATİK öncelik** (periyoda göre baştan belirlenir, değişmez).
- Varsayım: CPU burst süresi her seferinde **aynıdır.**

### 🧮 CPU Kullanımı Hesabı
- Bir process'in CPU kullanımı = **t / p**
- **Örnek 1:** P1(p=50, t=20), P2(p=100, t=35)
  - P1: 20/50 = **0.40**
  - P2: 35/100 = **0.35**
  - **Toplam = 0.75 (%75)** → schedule edilebilir ✅

### 🧮 GANTT ŞEMASI – Örnek 1 (P1 öncelikli, doğru sıralama)
- P1 periyodu kısa (50 < 100) → **P1 öncelikli.**
```
0──P1──20──P2──50  (P1 deadline'ı=50, t1=20 tamamlandı ✅)
P1 ilk 20ms, sonra P2 çalışır
```
- **P1 deadline'ı sağladı** (50'den önce 20ms tamamlandı).
- ⚠️ Olaylar: "P1 öncelikli olduğundan P2 kesildi", "P1 ve P2 aynı anda geldi".

### 🧮 ⚠️ TUZAK Örnek: P2'ye yanlışlıkla yüksek öncelik verilirse
- P1(p=50,t=20), P2(p=100,t=35), **P2 önce çalışır:**
```
0────P2────35────P1────55
```
- P2, 0-35 arası çalışır. P1, 35'te başlar, **55'te biter.**
- ⚠️ **Ama P1'in deadline'ı 50'ydi → P1 DEADLINE'I KAÇIRDI!**
- 💡 **Ders:** RMS'de **mutlaka periyodu kısa olan öncelikli olmalı.**

### 🧮 RATE-MONOTONIC — MISSING DEADLINE örneği (ÇOK ÖNEMLİ!)
- P1(p=50, t=25), P2(p=80, t=35)
- Toplam kullanım = (25/50)+(35/80) = **0.50 + 0.4375 = 0.94 (%94)** → CPU %6 boşta görünür.
- P1 öncelikli (periyot kısa).
```
0──P1──25──P2──50──P1──75──P2──80
```
- **P2 deadline'ı KAÇIRDI!** P2'nin 80ms'de tamamlanması gerekiyordu ama tamamlanamadı.
- 🔴⬛ **SONUÇ: RMS'de toplam kullanım %100'ün altında olsa bile deadline kaçırılabilir!** (RMS'nin en büyük dezavantajı/kısıtı)

### 📝 BOŞLUK DOLDURMA
- RMS'de öncelik ________ (**periyotla ters orantılı / statik**).
- CPU kullanımı ________ (**t/p**) formülüyle.
- RMS, kullanım %100'ün altında olsa bile ________ (**deadline kaçırabilir**).

---

## 🧮 3.2 EARLIEST-DEADLINE-FIRST (EDF) SCHEDULING

- 🔴⬛ **DİNAMİK** olarak her process'e **deadline'a göre öncelik** atanır.
- 🔴 **Deadline'ı KISA olanın önceliği YÜKSEK.**
- ⚠️ RMS (statik) ↔ EDF (dinamik) **— en önemli fark budur!**

### 🧮 EDF, RMS'in kaçırdığı deadline'ı KURTARIR!
- Aynı örnek: P1(p=50,t=25), P2(p=80,t=35)
- RMS'de P2 deadline'ı kaçırmıştı; **EDF ile her ikisi de deadline'ı sağlar.**
```
0──P1──25──P2──60──P1──80──P2──90──P1──125──P2──145
```
- "deadline'ı daha kısa olan process devam etti" → öncelik dinamik değişir.

### 📝 BOŞLUK DOLDURMA
- EDF'de öncelik atama ________ (**dinamik**).
- EDF'de ________ (**deadline'ı kısa**) olanın önceliği yüksektir.
- RMS = ________ (**statik**) öncelik, EDF = ________ (**dinamik**) öncelik.

---

## 🟦 3.3 Proportional Share Scheduling
- 🔴 Toplam **T payı** tüm uygulamalara dağıtılır. Uygulama **N pay** alırsa → işlemci süresinin **N/T'sine** sahip olur.
- 🧮 **Örnek:** T=100, A=50 pay, B=15 pay, C=20 pay → A %50, B %15, C %20 işlemci süresi alır.
- 🔴⬛ **Admission control policy (kabul-kontrol politikası)** ile çalışmalı → yalnızca **yeterli pay varsa** talebi kabul eder.

### 📝 BOŞLUK DOLDURMA
- N pay alan uygulama işlemci süresinin ________ (**N/T**) kadarını alır.
- Yeterli pay varsa talebi kabul eden politika ________ (**admission control policy**).

## 🟦 POSIX Real-Time Scheduling
- 🔴 POSIX.1b standardı, real-time thread'ler için **2 scheduling sınıfı** tanımlar:
  1. 🔴 **`SCHED_FIFO`:** **FCFS** stratejisi, **FIFO** kuyruk. ⚠️ **Eşit öncelikli thread'ler için time-slicing YOK.**
  2. 🔴 **`SCHED_RR`:** SCHED_FIFO gibi AMA **eşit öncelikli thread'ler için time-slicing VAR.**
- Fonksiyonlar: `pthread_attr_getsched_policy()` / `pthread_attr_setsched_policy()`

### 📝 BOŞLUK DOLDURMA
- Time-slicing OLMAYAN ________ (**SCHED_FIFO**), time-slicing OLAN ________ (**SCHED_RR**).

---

# 4️⃣ İŞLETİM SİSTEMLERİNDE SCHEDULING ÖRNEKLERİ

## 🟦 4.1 Linux Scheduling

### Version 2.5'e kadar
- 🔴 **O(1) scheduler:** Görev sayısından **bağımsız sabit zamanda** çalışır.
- **Preemptive, priority-based.**
- ⬛ 2 priority range: **time-sharing** ve **real-time.**
- ⬛ **Sayısal olarak düşük değer = yüksek öncelik.**
- ⬛ **active** (zaman kalmış) / **expired** (zaman bitmiş) iki priority array. Active bitince array'ler **takas edilir.**
- ⬛ **runqueue:** per-CPU veri yapısı.

### 🔴 Version 2.6.23+ → CFS (Completely Fair Scheduler)
- 🔴⬛ **CFS = varsayılan Linux scheduling algoritması.**
- 🔴 Scheduling **sınıflara (scheduling classes)** dayalı; her sınıfın bir önceliği var.
- Scheduler, **en yüksek öncelikli sınıftaki en yüksek öncelikli görevi** seçer.
- 🔴 **2 scheduling class:**
  1. **Default scheduling class → CFS algoritması**
  2. **Real-time scheduling class**

### 🔴 CFS Detayları (ÇOK ÖNEMLİ!)
- Sabit quantum YERİNE → her göreve CPU zamanının bir **oranını** atar.
- 🔴⬛ **nice value:** -20 ile +19 arası.
  - 🔴 **Düşük nice value = YÜKSEK öncelik** (daha fazla CPU zamanı).
- 🔴 **target latency:** Her çalıştırılabilir görevin **en az bir kez** çalışması gereken zaman aralığı. Görev sayısı artarsa target latency **artabilir.**
- 🔴⬛ **vruntime (sanal çalışma süresi):** CFS önceliği doğrudan atamaz, vruntime tutar.
  - Normal öncelikli görev 200ms çalışırsa → vruntime = 200ms
  - ⚠️ **Düşük öncelikli** görev 200ms çalışırsa → vruntime **200ms'den FAZLA**
  - ⚠️ **Yüksek öncelikli** görev 200ms çalışırsa → vruntime **200ms'den AZ**
- 🔴⬛ **Scheduler EN KÜÇÜK vruntime'lı görevi seçer.**
- CFS Performance: vruntime'a göre **red-black tree** (dengeli ikili arama ağacı), en soldaki düğüm en küçük vruntime = en yüksek öncelik. `rb_leftmost` cache'lenir → O(1).

### 🔴 Linux Öncelik Aralıkları (sayısal!)
- 🔴 **Real-time görevler: 0–99** (statik öncelik)
- 🔴 **Normal görevler: 100–139**
- ⬛ Düşük değer = yüksek öncelik.
- ⚠️ **nice -20 → 100'e**, **nice +19 → 139'a** eşittir.

### 📝 BOŞLUK DOLDURMA
- Varsayılan Linux algoritması ________ (**CFS / Completely Fair Scheduler**).
- Düşük ________ (**nice value**) = yüksek öncelik.
- CFS, en ________ (**küçük**) vruntime'lı görevi seçer.
- Real-time görev aralığı ________ (**0–99**), normal görev ________ (**100–139**).
- CFS, vruntime için ________ (**red-black tree**) kullanır.

## 🟦 4.2 Windows Scheduling
- 🔴 **Priority-based preemptive** scheduling. En yüksek öncelikli thread çalışır.
- 🔴⬛ **Dispatcher = scheduler.**
- Thread çalışır ta ki: (1) **bloke olur**, (2) **time slice biter**, (3) **yüksek öncelikli thread tarafından preempt edilir.**
- Real-time thread'ler non-real-time'ı preempt edebilir.
- 🔴 **32 seviyeli** öncelik şeması:
  - 🔴⬛ **Variable class: 1–15**
  - 🔴⬛ **Real-time class: 16–31**
  - ⬛ **Priority 0 = memory-management thread.**
- Çalıştırılabilir thread yoksa → 🔴⬛ **idle thread** çalışır.

### 🟦 Windows Priority Classes
- 🔴 **6 priority class:** REALTIME, HIGH, ABOVE_NORMAL, NORMAL, BELOW_NORMAL, IDLE.
  - ⚠️ **REALTIME hariç hepsi "variable".**
- Thread'in **relative priority**: TIME_CRITICAL, HIGHEST, ABOVE_NORMAL, NORMAL, BELOW_NORMAL, LOWEST, IDLE.
- ⬛ **Base priority = sınıf içindeki NORMAL.**
- Quantum biterse öncelik düşer ama **asla base'in altına inmez.**
- Wait olursa öncelik **boost** edilir. **Foreground pencere 3x boost** alır.
- 🔴⬛ **Windows 7 → user-mode scheduling (UMS):** Uygulamalar thread'leri kernel'den bağımsız yönetir; çok thread için verimli. (örn. C++ **ConcRT** kütüphanesi)

### 📝 BOŞLUK DOLDURMA
- Windows'ta scheduler ________ (**dispatcher**).
- Variable class ________ (**1–15**), real-time class ________ (**16–31**).
- Priority 0 ________ (**memory-management thread**).
- Foreground pencere ________ (**3x**) öncelik boost alır.

## 🟦 4.3 Solaris Scheduling
- 🔴 **Priority-based**, **6 sınıf:**
  - **TS** (Time sharing - **varsayılan**), **IA** (Interactive), **RT** (Real time), **SYS** (System), **FSS** (Fair Share), **FP/FX** (Fixed priority)
- Bir thread aynı anda **tek sınıfta** olabilir; her sınıfın **kendi algoritması** var.
- 🔴 **Time sharing = multi-level feedback queue.**
- Scheduler, sınıfa özel öncelikleri **global önceliğe** çevirir; en yüksek öncelikli çalışır.
- Aynı öncelikli thread'ler **RR (Round-Robin)** ile seçilir.

### 📝 BOŞLUK DOLDURMA
- Solaris varsayılan sınıfı ________ (**TS / Time sharing**).
- Solaris time sharing ________ (**multi-level feedback queue**) kullanır.

---

# 5️⃣ BİR SCHEDULING ALGORİTMASI NASIL SEÇİLİR?

- İlk problem: **kriterlerin tanımlanması.** Genelde: 🔴 **CPU utilization, response time, throughput.**
- Örnek kriterler:
  - Max response time 1sn iken **CPU utilization'ı maksimize etmek**
  - Turnaround süresi yürütme süresiyle orantılı olacak şekilde **throughput'u maksimize etmek**

## 🔴 4 Değerlendirme Yöntemi (ezberle!)
1. **Deterministic Modeling**
2. **Queueing Models**
3. **Simulations**
4. **Implementation**

---

## 🧮 5.1 Deterministic Modeling
- 🔴 Bir tür **analitik değerlendirme (analytic evaluation).**
- Önceden belirlenmiş bir iş yükü alır, her algoritmanın performansını **tanımlar.**
- ✅ **Basit ve hızlı.** ⚠️ Kesin sayı gerektirir, yanıtlar **yalnızca o duruma** geçerli.

### 🧮 ÖRNEK (kesin gelir!) — Min. ortalama waiting time hangi algoritma?
İş yükü (hepsi t=0'da gelir): P1=10, P2=29, P3=3, P4=7, P5=12
- 🔴 **FCFS = 28 ms** (sıra: P1,P2,P3,P4,P5)
- 🔴 **Non-preemptive SJF = 13 ms** (sıra: P3,P4,P1,P5,P2) → **EN İYİ!**
- 🔴 **RR (q=10) = 23 ms**
- 💡 **Bu örnekte SJF minimum waiting time verir (13ms).**

### 📝 BOŞLUK DOLDURMA
- Deterministic modeling bir ________ (**analitik değerlendirme**) türüdür.
- Örnekte en düşük waiting time veren ________ (**SJF, 13ms**).

---

## 🧮 5.2 Queueing Models
- Statik process yok → **CPU ve I/O burst dağılımları** kullanılır (genellikle **eksponansiyel**).
- 🔴⬛ **LITTLE'S FORMULA (çok önemli – işlem sorusu!):**

> ### 📐 **n = λ × W**
> - **n** = ortalama kuyruk uzunluğu (kuyruktaki process sayısı)
> - **λ** = ortalama varış hızı (saniyede gelen process)
> - **W** = kuyruktaki ortalama bekleme süresi

- 🔴 Herhangi bir scheduling algoritması ve varış dağılımında **geçerlidir.**

### 🧮 ÖRNEK İŞLEM (slayttan – aynısı gelebilir!)
- λ = 7 process/saniye, n = 14 process
- **W = n / λ = 14 / 7 = `2 saniye`** ← ortalama waiting time

### 📝 BOŞLUK DOLDURMA
- Little's formula ________ (**n = λ × W**).
- n=14, λ=7 ise W = ________ (**2 saniye**).
- Bu formül ________ (**herhangi**) bir scheduling algoritmasında geçerlidir.

### ⚠️ Queueing Models Sınırlamaları
- Karmaşık algoritma/dağılım matematiği **zor.**
- Gerçekçi olmayan varsayımlar gerekir → sonuçlar **yaklaşık**, doğruluk sorgulanabilir.

---

## 🟦 5.3 Simulations
- Daha doğru değerlendirme için kullanılır.
- **Saati temsil eden değişken** + sistem bileşenlerini temsil eden veri yapıları.
- Veri üretimi: **random number generator** (rastgele sayı üreteci).
- Dağılımlar: **uniform, exponential, Poisson** (matematiksel) veya **deneysel** olabilir.
- **trace tape:** Gerçek process yürütmesinden alınan iz kaydı → FCFS, SJF, RR simülasyonlarına aynı veri verilir.

## 🟦 5.4 Implementation
- 🔴 **Bir algoritmayı değerlendirmenin TAMAMEN DOĞRU tek yolu:** kodlamak, OS'e koymak, çalıştırmak.
- ⚠️ **En büyük zorluk: yüksek MALİYET** (kodlama + OS değişimi + kullanıcıların değişen OS'e tepkisi).
- ⚠️ Ortam değişince scheduler performansı değişir. Örn. kısa process'lere öncelik verilirse → kullanıcılar **process'leri küçük parçalara böler.**
- 🔴 En esnek algoritmalar: sistem yöneticisi/kullanıcı tarafından **ayarlanabilen (tunable)** algoritmalar. (Bazı UNIX sürümleri buna izin verir.)

### 📝 BOŞLUK DOLDURMA
- Bir algoritmayı değerlendirmenin tamamen doğru yolu ________ (**implementation / gerçek sisteme koymak**).
- Implementation'ın en büyük zorluğu ________ (**yüksek maliyet**).

---

# ⚡ SINAV ÖNCESİ HIZLI TEKRAR

## 🎯 En Kritik Tanım/Karşılaştırma Tablosu
| Kavram | Tek cümle |
|--------|-----------|
| **PCS** | Aynı process'in thread'leri arası rekabet |
| **SCS** | Sistemdeki tüm thread'ler arası rekabet (Windows/Linux/Solaris) |
| **Asymmetric MP** | Tek master CPU karar verir |
| **SMP** | Her işlemci kendi algoritması, master yok |
| **Soft affinity** | Aynı işlemci garanti EDİLMEZ |
| **Hard affinity** | Aynı işlemci garanti EDİLİR |
| **Push migration** | Yüklü işlemciden process İTİLİR |
| **Pull migration** | Boş işlemci process ÇEKER |
| **Soft real-time** | Sadece öncelik garantisi |
| **Hard real-time** | Deadline mutlak (sonrası = hiç) |
| **RMS** | STATİK, periyotla ters orantılı öncelik |
| **EDF** | DİNAMİK, kısa deadline = yüksek öncelik |
| **CFS** | Linux varsayılan, en küçük vruntime seçilir |
| **Little's Formula** | n = λ × W |

## 🔢 Ezberlenecek Sayılar
- Linux: real-time **0–99**, normal **100–139**; nice **-20…+19**
- Windows: variable **1–15**, real-time **16–31**, priority **0**=mem-mgmt, foreground **3x** boost
- RMS örnek kullanım: P1(20/50=0.40) + P2(35/100=0.35) = **0.75**
- RMS missing deadline: (25/50)+(35/80) = **0.94** ama P2 deadline kaçırır
- Little: λ=7, n=14 → **W=2sn**
- Deterministic örnek: FCFS=28, **SJF=13**, RR=23 ms
- dual-threaded+dual-core = **4 mantıksal işlemci**
- Periyodik: **0 ≤ t ≤ d ≤ p**, rate = **1/p**

## ⚠️ En Çok Karıştırılanlar
- **RMS = statik öncelik** ↔ **EDF = dinamik öncelik**
- **RMS**, kullanım %100 altında olsa bile **deadline kaçırabilir** (EDF kaçırmaz)
- **PCS** (aynı process) ↔ **SCS** (tüm sistem)
- **Push** (yüklü iter) ↔ **Pull** (boş çeker)
- **CFS:** düşük nice = yüksek öncelik, **en küçük vruntime** seçilir
- **Düşük sayısal değer = yüksek öncelik** (hem Linux hem Windows global şema)
- Implementation = **en doğru ama en pahalı** değerlendirme

---

> 🍀 **Başarılar!** Hoca özellikle: PCS/SCS, asymmetric vs SMP, soft/hard affinity, push/pull migration, soft/hard real-time, RMS & EDF Gantt şemaları (deadline kaçırma!), CFS/vruntime/nice, Windows-Linux öncelik aralıkları ve Little's Formula işleminden soruyor.
