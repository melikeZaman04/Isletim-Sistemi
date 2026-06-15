# CPU Scheduling Ders 9-10 - Sinav Oncesi Calisma Karti

Kaynaklar:
- `Ders Icerigi/ders_9_CPU_Scheduling2.pdf`
- `Ders Icerigi/Ders10_CPU_Scheduling 3.pdf`

Bu notun amaci: Sinavdan once iki slayttan hocanin sorabilecegi yerleri tek sayfalik tekrar mantigiyla toplamak. Ozellikle tanim, bosluk doldurma, karsilastirma ve kucuk islem sorularina odaklan.

---

## 1. Kesin Bak: En Cok Soru Gelebilecek Kavramlar

| Kavram | Sinavlik Kisa Cevap |
|---|---|
| PCS | Ayni process icindeki user-level thread'ler arasinda CPU rekabetidir. |
| SCS | Sistemdeki tum kernel-level thread'ler arasinda CPU rekabetidir. |
| Asymmetric multiprocessing | Tek master CPU scheduling ve I/O kararlarini verir. |
| Symmetric multiprocessing / SMP | Master CPU yoktur; her islemci kendi scheduling kararlarini verebilir. |
| Common ready queue | Tum thread'ler ortak hazir kuyruktadir; race condition ve locking problemi olabilir. |
| Per-core run queue | Her CPU'nun kendi hazir kuyrugu vardir; SMP'de en yaygin yaklasimdir. |
| Processor affinity | Process'i ayni islemcide calistirmaya calisma mantigidir. |
| Soft affinity | Ayni islemcide calisma garanti edilmez. |
| Hard affinity | Ayni islemcide calisma garanti edilir. |
| Push migration | Asiri yuklu CPU process'i baska CPU'ya iter. |
| Pull migration | Bos CPU, baska CPU'dan process ceker. |
| Memory stall | CPU'nun bellekten veri beklemesi durumudur. |
| Soft real-time | Sadece oncelikli calisma garantisi vardir; deadline garantisi yoktur. |
| Hard real-time | Deadline mutlaka karsilanmalidir. Deadline sonrasi hizmet = hic hizmet yoktur. |
| RMS | Statik oncelikli, periyotla ters orantili real-time scheduling algoritmasidir. |
| EDF | Dinamik oncelikli, deadline'i en yakin olani sectiren algoritmadir. |
| CFS | Linux'un varsayilan scheduler'idir; en kucuk vruntime'i secer. |
| Little's Formula | `n = lambda x W` |

---

## 2. Thread Scheduling

Thread destekleyen isletim sistemlerinde genellikle process'ler yerine thread'ler schedule edilir.

### PCS - Process-Contention Scope

- User-level thread scheduling icindir.
- Rekabet ayni process'e ait thread'ler arasindadir.
- Many-to-one ve many-to-many modellerinde gorulur.
- Thread oncelikleri programci tarafindan belirlenebilir.

### SCS - System-Contention Scope

- Kernel-level thread scheduling icindir.
- Rekabet sistemdeki tum thread'ler arasindadir.
- Windows, Linux ve Solaris one-to-one model kullandigi icin SCS ile schedule eder.

### POSIX Pthread

```text
PTHREAD_SCOPE_PROCESS -> PCS
PTHREAD_SCOPE_SYSTEM  -> SCS
```

Linux ve macOS genelde sadece `PTHREAD_SCOPE_SYSTEM` destekler.

### Hoca Sorabilir

1. Ayni process'in thread'leri arasindaki rekabete ne denir?
   - Cevap: PCS
2. Sistemdeki tum thread'ler arasindaki rekabete ne denir?
   - Cevap: SCS
3. Windows, Linux ve Solaris hangi modeli kullanir?
   - Cevap: One-to-one model ve SCS

---

## 3. Multiple-Processor Scheduling

Multi-processor scheduling daha karmasiktir cunku birden fazla CPU/cekirdek vardir ve yuk paylasimi gerekir.

Modern multiprocessor kapsami:
- Multicore CPUs
- Multithreaded cores
- NUMA systems
- Heterogeneous multiprocessing

### Asymmetric vs Symmetric Multiprocessing

| Ozellik | Asymmetric Multiprocessing | Symmetric Multiprocessing / SMP |
---|---|---|
| Master CPU | Vardir | Yoktur |
| Scheduling karari | Tek CPU verir | Her CPU verebilir |
| Avantaj | Basit | Modern sistemlerde yaygin ve esnek |
| Dezavantaj | Master CPU bottleneck olabilir | Kuyruk ve yuk dengeleme karmasik olabilir |

### SMP'de Kuyruk Yaklasimlari

1. Common ready queue:
   - Tum thread'ler ortak kuyruktadir.
   - Race condition olabilir.
   - Locking gerekir.
   - Locking performans kaybi yaratabilir.

2. Per-core run queue:
   - Her islemcinin kendi hazir kuyrugu vardir.
   - SMP'de en yaygin yaklasimdir.
   - Yuk dengesizligi olursa load balancing gerekir.

### Processor Affinity

Bir process baska CPU'ya tasininca eski CPU'daki cache bilgileri gecersizlesir, yeni CPU'da cache yeniden doldurulur. Bu pahali oldugu icin process ayni CPU'da tutulmaya calisilir.

```text
Soft affinity -> Garanti yok
Hard affinity -> Garanti var
```

Linux hem soft hem hard affinity destekler.

### Load Balancing

Ortak ready queue varsa genelde load balancing gerekmez. Her CPU'nun kendi kuyrugu varsa gerekir.

```text
Push migration -> Yuklu CPU process'i iter
Pull migration -> Bos CPU process'i ceker
```

Push ve pull ayni sistemde beraber kullanilabilir.

### Hoca Sorabilir

1. Tek master CPU'lu yaklasim hangisidir?
   - Cevap: Asymmetric multiprocessing
2. Master CPU olmayan yaklasim hangisidir?
   - Cevap: SMP
3. SMP'de en yaygin ready queue yaklasimi nedir?
   - Cevap: Per-core run queue
4. Ayni CPU'da calisma garantisi olmayan affinity nedir?
   - Cevap: Soft affinity
5. Bos CPU'nun process cekmesi nedir?
   - Cevap: Pull migration

---

## 4. Multicore, Multithreaded Core ve Memory Stall

Multicore processor: Ayni fiziksel yonga uzerinde birden fazla cekirdek bulunmasidir.

OS acisindan:
- Her cekirdek ayri fiziksel islemci gibi gorunur.
- Her hardware thread mantiksal islemci gibi gorunur.

### Memory Stall

Memory stall, CPU'nun bellekten veri gelmesini beklemesidir. Cache'te olmayan veriye erisim bu duruma neden olabilir.

Sorunun cozumu:
- Her cekirdege birden fazla hardware thread atanir.
- Bir thread bellek beklerken diger thread calisir.

Kesin islem:

```text
Dual-core + dual-threaded = 2 x 2 = 4 mantiksal islemci
```

---

## 5. Real-Time CPU Scheduling

### Soft Real-Time vs Hard Real-Time

| Kavram | Anlam |
---|---|
| Soft real-time | Kritik process'e oncelik verilir ama deadline garantisi yoktur. |
| Hard real-time | Deadline mutlaka karsilanir; deadline sonrasi hizmet anlamsizdir. |

### Latency Turleri

| Latency | Anlam |
---|---|
| Event latency | Olay olusmasi ile cevap verilmesi arasindaki sure. |
| Interrupt latency | Interrupt gelmesi ile interrupt'in islenmeye baslamasi arasindaki sure. |
| Dispatch latency | Bir process'in durdurulup digerinin baslatilmasi icin gecen sure. |

Dispatch latency iki asamadan olusur:

```text
1. Conflict phase
2. Dispatch phase
```

Conflict phase iki is icerir:
- Kernel'de calisan process'in durdurulmasi
- Yuksek oncelikli process'in ihtiyac duydugu kaynaklarin serbest birakilmasi

### Periyodik Process Karakteristikleri

```text
t = CPU burst / islem suresi
d = deadline
p = period / periyot

0 <= t <= d <= p
rate = 1 / p
```

Deadline genellikle bir sonraki periyodun baslama zamanidir.

---

## 6. Rate-Monotonic Scheduling / RMS

RMS sinavda islem ve Gantt semasi olarak gelebilir.

Temel ozellikler:
- Preemptive'dir.
- Priority-based'dir.
- Oncelik statiktir.
- Periyot kisa ise oncelik yuksektir.
- Oncelik periyotla ters orantilidir.
- Her CPU burst suresinin ayni oldugu varsayilir.

### CPU Kullanimi

```text
Bir process'in CPU kullanimi = t / p
Toplam kullanim = tum process'ler icin t / p toplami
```

### Ornek 1

```text
P1: p = 50,  t = 20
P2: p = 100, t = 35

P1 kullanimi = 20 / 50  = 0.40
P2 kullanimi = 35 / 100 = 0.35
Toplam = 0.75
```

P1'in periyodu daha kisa oldugu icin P1 daha yuksek onceliklidir.

Yanlis oncelik verilirse:

```text
P2 once calisirsa: 0-35 P2
P1 sonra calisirsa: 35-55 P1
P1 deadline = 50
Sonuc: P1 deadline kacirir.
```

### RMS Missing Deadline Ornegi

```text
P1: p = 50, t = 25
P2: p = 80, t = 35

Toplam kullanim = 25/50 + 35/80
Toplam kullanim = 0.50 + 0.4375 = 0.9375, yaklasik 0.94
```

CPU kullanimi %100'den dusuk gorunur ama RMS yine deadline kacirabilir.

Kesin ezber:

```text
RMS'de CPU kullanimi %100 altinda olsa bile deadline kacabilir.
```

---

## 7. Earliest-Deadline-First / EDF

EDF'de oncelik deadline'a gore dinamik atanir.

Temel ozellikler:
- Dinamik onceliklidir.
- Deadline'i en yakin olan process en yuksek onceligi alir.
- RMS'in deadline kacirdigi bazi durumlarda EDF deadline'i kurtarabilir.

En kritik fark:

```text
RMS -> statik oncelik, periyoda bakar
EDF -> dinamik oncelik, deadline'a bakar
```

Hoca bunu klasik karsilastirma olarak sorabilir.

---

## 8. Proportional Share Scheduling

Toplam `T` pay tum uygulamalara dagitilir. Bir uygulama `N` pay alirsa CPU zamaninin `N/T` kadarina sahip olur.

Ornek:

```text
T = 100
A = 50 pay -> %50 CPU
B = 15 pay -> %15 CPU
C = 20 pay -> %20 CPU
```

Bu algoritma admission control policy ile calismalidir.

```text
Admission control policy -> Yeterli pay varsa talebi kabul eder.
```

---

## 9. POSIX Real-Time Scheduling

| Sinif | Ozellik |
---|---|
| SCHED_FIFO | FCFS mantigi, FIFO kuyruk, esit oncelikte time-slicing yok. |
| SCHED_RR | FIFO'ya benzer, esit oncelikte time-slicing var. |

Kesin ezber:

```text
SCHED_FIFO -> time-slicing yok
SCHED_RR   -> time-slicing var
```

---

## 10. Linux Scheduling

### Linux 2.5'e kadar / O(1) Scheduler

- Preemptive ve priority-based.
- Gorev sayisindan bagimsiz sabit zamanda calisir.
- Iki priority range vardir:
  - Time-sharing
  - Real-time
- Active ve expired priority array kullanir.
- Per-CPU runqueue vardir.
- Dusuk sayisal deger daha yuksek oncelik demektir.

### Linux 2.6.23+ / CFS

CFS = Completely Fair Scheduler

Kesin ozellikler:
- Linux'un varsayilan scheduling algoritmasidir.
- Sabit quantum yerine CPU zamanindan oran verir.
- Nice value kullanir.
- Vruntime tutar.
- En kucuk vruntime'a sahip gorevi secer.
- Vruntime icin red-black tree kullanir.

### Nice Value

```text
nice araligi = -20 ... +19
Dusuk nice value = yuksek oncelik
```

### Vruntime

```text
Normal oncelik 200 ms calisirsa -> vruntime = 200 ms
Dusuk oncelik 200 ms calisirsa -> vruntime > 200 ms
Yuksek oncelik 200 ms calisirsa -> vruntime < 200 ms
```

CFS secimi:

```text
En kucuk vruntime secilir.
```

### Linux Oncelik Araliklari

```text
Real-time gorevler = 0-99
Normal gorevler    = 100-139
nice -20           = 100
nice +19           = 139
```

Dusuk sayisal deger = yuksek oncelik.

---

## 11. Windows Scheduling

Temel ozellikler:
- Priority-based preemptive scheduling kullanir.
- En yuksek oncelikli thread calisir.
- Windows'ta scheduler'in adi dispatcher'dir.
- Real-time thread'ler non-real-time thread'leri preempt edebilir.

Thread su durumlardan birine kadar calisir:
- Bloke olur.
- Time slice biter.
- Daha yuksek oncelikli thread tarafindan preempt edilir.

### Windows Priority Scheme

```text
Toplam priority level = 32
Variable class        = 1-15
Real-time class       = 16-31
Priority 0            = memory-management thread
```

Priority classes:
- REALTIME
- HIGH
- ABOVE_NORMAL
- NORMAL
- BELOW_NORMAL
- IDLE

REALTIME disindakiler variable class'tir.

Ek bilgi:

```text
Quantum biterse oncelik duser ama base priority altina dusmez.
Wait olursa priority boost olabilir.
Foreground window 3x priority boost alir.
```

---

## 12. Solaris Scheduling

Solaris priority-based scheduling kullanir.

6 scheduling class:

```text
TS  = Time Sharing, default
IA  = Interactive
RT  = Real Time
SYS = System
FSS = Fair Share
FP  = Fixed Priority
```

Kesin noktalar:
- Bir thread ayni anda tek sinifta olabilir.
- Her sinifin kendi scheduling algoritmasi vardir.
- Time sharing sinifi multi-level feedback queue kullanir.
- Scheduler class-specific priority'leri global priority'ye cevirir.
- Ayni oncelikteki thread'ler Round Robin ile secilir.

---

## 13. Scheduling Algoritmasi Nasil Secilir?

Ilk problem kriterleri belirlemektir.

En onemli kriterler:
- CPU utilization
- Response time
- Throughput
- Waiting time
- Turnaround time

### Degerlendirme Yontemleri

```text
1. Deterministic Modeling
2. Queueing Models
3. Simulations
4. Implementation
```

### Deterministic Modeling

- Analitik degerlendirme turudur.
- Belirli ve sabit bir is yuku alir.
- Her algoritmanin performansini o is yuku icin hesaplar.
- Basit ve hizlidir.
- Sadece verilen durum icin gecerlidir.

Slayttaki ornek:

```text
P1 = 10
P2 = 29
P3 = 3
P4 = 7
P5 = 12
Hepsi t = 0'da geliyor.

FCFS average waiting time = 28 ms
SJF average waiting time  = 13 ms
RR q=10 average waiting   = 23 ms
```

Bu ornekte en iyi algoritma:

```text
SJF = 13 ms
```

### Queueing Models

Little's Formula kesin bilinmeli:

```text
n = lambda x W
```

Anlamlari:

```text
n      = ortalama kuyruk uzunlugu
lambda = ortalama varis hizi
W      = ortalama bekleme suresi
```

Ornek:

```text
n = 14
lambda = 7 process/saniye

W = n / lambda = 14 / 7 = 2 saniye
```

Little's Formula herhangi bir scheduling algoritmasi ve varis dagiliminda gecerlidir.

### Simulations

- Daha dogru degerlendirme icin kullanilir.
- Sistemin bilesenlerini veri yapilari temsil eder.
- Bir saat degiskeni vardir.
- Rastgele sayi uretici kullanilabilir.
- Dagilimlar uniform, exponential, Poisson veya deneysel olabilir.
- Trace tape ile gercek sistemden iz kaydi alinabilir.

### Implementation

Bir scheduling algoritmasini degerlendirmenin tamamen dogru tek yolu:

```text
Algoritmayi kodlamak, OS'e koymak ve gercek sistemde calistirmak.
```

Dezavantaj:

```text
En pahali yontemdir.
```

---

## 14. En Kritik Karsilastirmalar

### PCS vs SCS

| PCS | SCS |
---|---|
| Ayni process icindeki thread'ler yarasir. | Sistemdeki tum thread'ler yarasir. |
| User-level thread scheduling. | Kernel-level thread scheduling. |
| Many-to-one / many-to-many ile ilgili. | One-to-one ile ilgili. |

### RMS vs EDF

| RMS | EDF |
---|---|
| Statik oncelik | Dinamik oncelik |
| Periyoda bakar | Deadline'a bakar |
| Kisa periyot yuksek oncelik | Yakin deadline yuksek oncelik |
| %100 altinda bile deadline kacirabilir | Daha esnek ve gucludur |

### Soft vs Hard Real-Time

| Soft Real-Time | Hard Real-Time |
---|---|
| Oncelik garantisi vardir. | Deadline garantisi vardir. |
| Deadline kesin degildir. | Deadline kacarsa hizmet anlamsizdir. |

### Soft vs Hard Affinity

| Soft Affinity | Hard Affinity |
---|---|
| Ayni CPU garanti edilmez. | Ayni CPU garanti edilir. |

### Push vs Pull Migration

| Push Migration | Pull Migration |
---|---|
| Yuklu CPU process'i iter. | Bos CPU process'i ceker. |

### FIFO vs RR

| SCHED_FIFO | SCHED_RR |
---|---|
| Esit oncelikte time-slicing yok. | Esit oncelikte time-slicing var. |

---

## 15. Sayisal Degerler - Ezber Listesi

```text
Dual-core + dual-threaded = 4 logical processor

RMS kullanim:
P1: 20/50  = 0.40
P2: 35/100 = 0.35
Toplam     = 0.75

RMS missing deadline:
P1: 25/50 = 0.50
P2: 35/80 = 0.4375
Toplam    = 0.9375, yaklasik 0.94

Linux real-time priority = 0-99
Linux normal priority    = 100-139
Linux nice value         = -20 ... +19
nice -20                 = 100
nice +19                 = 139

Windows variable class   = 1-15
Windows real-time class  = 16-31
Windows priority 0       = memory-management thread
Foreground window boost  = 3x

Little:
n = 14, lambda = 7 -> W = 2 saniye

Deterministic modeling:
FCFS = 28 ms
SJF  = 13 ms
RR   = 23 ms
```

---

## 16. Bosluk Doldurma Bankosu

1. Ayni process'e ait thread'ler arasindaki CPU rekabetine __________ denir.
   - PCS

2. Sistemdeki tum thread'ler arasindaki CPU rekabetine __________ denir.
   - SCS

3. `PTHREAD_SCOPE_PROCESS` __________ kullanir.
   - PCS

4. `PTHREAD_SCOPE_SYSTEM` __________ kullanir.
   - SCS

5. Tek master CPU'nun scheduling karari verdigi yaklasim __________ olarak adlandirilir.
   - Asymmetric multiprocessing

6. Master CPU'nun olmadigi, her islemcinin scheduling yapabildigi yaklasim __________ olarak adlandirilir.
   - SMP

7. Ayni islemcide calisma garanti edilmiyorsa bu __________ affinity'dir.
   - Soft

8. Ayni islemcide calisma garanti ediliyorsa bu __________ affinity'dir.
   - Hard

9. Asiri yuklu CPU'nun process'i baska CPU'ya aktarmasi __________ migration'dir.
   - Push

10. Bos CPU'nun baska CPU'dan process almasi __________ migration'dir.
    - Pull

11. CPU'nun bellekten veri beklemesine __________ denir.
    - Memory stall

12. Dual-core ve dual-threaded sistem OS acisindan __________ mantiksal islemci olarak gorunur.
    - 4

13. Deadline garantisi olmayan ama oncelik garantisi veren sistem __________ real-time'dir.
    - Soft

14. Deadline'in mutlaka karsilanmasi gereken sistem __________ real-time'dir.
    - Hard

15. Interrupt gelmesi ile islenmeye baslamasi arasindaki sure __________ latency'dir.
    - Interrupt

16. Bir process'in durdurulup digerinin baslatilmasi icin gecen sure __________ latency'dir.
    - Dispatch

17. Periyodik process icin iliski __________ seklindedir.
    - 0 <= t <= d <= p

18. Periyodik gorevin rate degeri __________ seklindedir.
    - 1 / p

19. RMS'de oncelik periyotla __________ orantilidir.
    - Ters

20. RMS'de oncelik __________ olarak belirlenir.
    - Statik

21. EDF'de oncelik __________ olarak belirlenir.
    - Dinamik

22. EDF'de deadline'i __________ olan process daha yuksek onceliklidir.
    - Daha yakin / daha kisa

23. Proportional share scheduling'de N pay alan process CPU'nun __________ kadarini alir.
    - N / T

24. SCHED_FIFO'da esit oncelikli thread'ler icin __________ yoktur.
    - Time-slicing

25. SCHED_RR'da esit oncelikli thread'ler icin __________ vardir.
    - Time-slicing

26. Linux'un varsayilan scheduler'i __________ algoritmasidir.
    - CFS

27. CFS, en __________ vruntime'a sahip gorevi secer.
    - Kucuk

28. Linux real-time priority araligi __________ seklindedir.
    - 0-99

29. Linux normal priority araligi __________ seklindedir.
    - 100-139

30. Windows'ta scheduler'a __________ denir.
    - Dispatcher

31. Windows variable priority class __________ araligindadir.
    - 1-15

32. Windows real-time priority class __________ araligindadir.
    - 16-31

33. Solaris'in default scheduling class'i __________ sinifidir.
    - TS / Time Sharing

34. Little's Formula __________ seklindedir.
    - n = lambda x W

35. Scheduling algoritmasini degerlendirmenin tamamen dogru ama en pahali yolu __________ yontemidir.
    - Implementation

---

## 17. Klasik Soru Hazir Cevaplari

### Soru: PCS ve SCS farkini aciklayiniz.

PCS, ayni process'e ait user-level thread'lerin CPU icin birbirleriyle rekabet ettigi scheduling kapsamidir. Kernel bu user-level thread'leri dogrudan bilmez; thread kutuphanesi bunlari yonetir. SCS ise sistemdeki tum kernel-level thread'lerin CPU icin rekabet ettigi scheduling kapsamidir. Windows, Linux ve Solaris gibi one-to-one model kullanan sistemler SCS kullanir.

### Soru: Asymmetric multiprocessing ve SMP farkini aciklayiniz.

Asymmetric multiprocessing'te scheduling, I/O ve sistem kararlarini tek bir master CPU verir; diger CPU'lar kullanici kodlarini calistirir. Bu yapi basittir ama master CPU bottleneck olabilir. SMP'de master CPU yoktur; her islemci kendi scheduling algoritmasi veya kuyruğu ile calisabilir. Modern OS'lerde SMP yaygindir.

### Soru: Processor affinity neden kullanilir?

Bir process baska CPU'ya tasindiginda eski CPU'daki cache bilgileri gecersiz hale gelir ve yeni CPU'da cache yeniden doldurulur. Bu islem maliyetlidir. Bu nedenle OS, process'i mumkun oldugunca ayni CPU'da calistirmaya calisir. Buna processor affinity denir.

### Soru: RMS ve EDF farkini aciklayiniz.

RMS statik oncelikli bir algoritmadir; periyodu kisa olan process daha yuksek oncelik alir. EDF dinamik oncelikli bir algoritmadir; deadline'i en yakin olan process daha yuksek oncelik alir. RMS periyoda, EDF deadline'a bakar. RMS'de CPU kullanimi %100'den dusuk olsa bile deadline kacabilir.

### Soru: CFS nasil calisir?

CFS, Linux'un varsayilan scheduling algoritmasidir. Sabit quantum kullanmak yerine her goreve CPU zamanindan bir oran verir. Gorevlerin sanal calisma suresini `vruntime` olarak tutar. Scheduler en kucuk `vruntime` degerine sahip gorevi secer. Dusuk nice value daha yuksek oncelik ve daha fazla CPU zamani anlamina gelir.

### Soru: Little's Formula nedir?

Little's Formula kuyruk modellerinde kullanilir:

```text
n = lambda x W
```

Burada `n` ortalama kuyruk uzunlugu, `lambda` ortalama varis hizi, `W` ortalama bekleme suresidir. Herhangi bir scheduling algoritmasi ve varis dagiliminda gecerlidir.

---

## 18. Mini Deneme

### Test

1. Asagidakilerden hangisi user-level thread'lerin ayni process icinde CPU icin rekabet ettigini ifade eder?
   - A) SCS
   - B) PCS
   - C) SMP
   - D) EDF

2. RMS algoritmasinda oncelik hangi kritere gore verilir?
   - A) Arrival time
   - B) Burst time
   - C) Period
   - D) Vruntime

3. EDF algoritmasinda en yuksek onceligi kim alir?
   - A) En kisa periyotlu process
   - B) En yakin deadline'a sahip process
   - C) En dusuk nice value'ya sahip process
   - D) En uzun CPU burst'e sahip process

4. Linux CFS hangi gorevi secer?
   - A) En buyuk vruntime
   - B) En kucuk vruntime
   - C) En buyuk PID
   - D) En eski process

5. Bos kalan islemcinin baska islemciden process almasina ne denir?
   - A) Push migration
   - B) Pull migration
   - C) Hard affinity
   - D) NUMA

6. Windows'ta scheduler'in adi nedir?
   - A) CFS
   - B) Dispatcher
   - C) Kernel queue
   - D) Runlevel

7. `n = 20`, `lambda = 5` ise `W` kac saniyedir?
   - A) 2
   - B) 4
   - C) 5
   - D) 10

8. SCHED_RR ile SCHED_FIFO arasindaki temel fark nedir?
   - A) SCHED_RR time-slicing yapar
   - B) SCHED_FIFO dinamik onceliklidir
   - C) SCHED_RR sadece Linux'ta vardir
   - D) SCHED_FIFO deadline'a bakar

### Cevap Anahtari

```text
1. B
2. C
3. B
4. B
5. B
6. B
7. B
8. A
```

---

## 19. Son 5 Dakika Ezberi

```text
PCS = ayni process icindeki thread'ler
SCS = sistemdeki tum thread'ler

Asymmetric = master CPU var
SMP = master CPU yok

Soft affinity = garanti yok
Hard affinity = garanti var

Push = yuklu CPU iter
Pull = bos CPU ceker

Soft real-time = oncelik garantisi
Hard real-time = deadline garantisi

RMS = statik, periyot kisa ise oncelik yuksek
EDF = dinamik, deadline yakin ise oncelik yuksek

RMS %100 altinda bile deadline kacirabilir

CFS = Linux varsayilan scheduler
CFS = en kucuk vruntime'i secer

Linux:
RT = 0-99
Normal = 100-139
nice = -20 ... +19

Windows:
Variable = 1-15
Real-time = 16-31
Priority 0 = memory-management thread
Dispatcher = scheduler

Solaris:
Default = TS
Time sharing = multi-level feedback queue

Little:
n = lambda x W

Implementation:
En dogru ama en pahali degerlendirme yontemi
```

