# Bölüm 8: CPU Scheduling (İşlemci Çizelgeleme) - Sınav Çalışma Notları

Bu doküman, CPU Scheduling (İşlemci Çizelgeleme) konusunun önemli yerlerini, sınavda çıkabilecek teorik soruları ve algoritmaların hesaplama yönergelerini içermektedir.

---

## 📌 Temel Kavramlar

### Multiprogramming ve Multitasking
- **Multiprogramming:** İşletim sisteminde birden fazla programın aynı anda bellekte tutularak, CPU'nun her zaman yürütecek bir process bulması durumudur. Bir process I/O (girdi/çıktı) için beklemeye geçerse, CPU boşta durmaz; sıradaki diğer process'e geçer. **Amaç:** CPU verimliliğini artırmaktır.
- **Multitasking (Zaman Paylaşımlı):** Multiprogramming'in genişletilmiş halidir. CPU, process'ler arasında o kadar hızlı geçiş yapar ki, kullanıcılar tüm process'lerin aynı anda çalıştığı hissine kapılır. **Amaç:** Sistemin kullanıcıya olan yanıt verebilirliğini (response time) artırmaktır.

### CPU Burst ve I/O Burst Döngüsü
Process'ler çalışma ömürleri boyunca genellikle iki temel döngü arasında gidip gelirler:
1. **CPU Burst:** İşlemcinin aktif olarak hesaplama yaptığı zaman dilimi.
2. **I/O Burst:** Process'in girdi-çıktı işlemleri için (örneğin bellekten bir şey okuması) beklediği zaman dilimi.
*Not: CPU burst grafikleri genellikle çok sayıda az süreli (kısa) burst ve az sayıda uzun süreli burst şeklinde eksponansiyel bir karakter gösterir.*

---

## 📌 CPU Scheduler (İşlemci Çizelgeyici) ve Dispatcher

### Short-Term Scheduler (CPU Scheduler)
CPU boşta kaldığı anda, hazır konumda (**Ready Queue**) bekleyen process'lerden birini seçip CPU'ya atayan modüldür. *Sınavda sorulabilir: Hangi sıraya göre seçer? İlla FIFO olmak zorunda değildir; öncelik (priority), ağaç yapısı vb. şeklinde olabilir.*

### Dispatcher Modülü
Short-term scheduler'ın seçtiği process'i **fiziksel olarak CPU'ya geçiren** bileşendir. Şu işlevleri yerine getirir:
1. Context Switching (Bağlam değişimi)
2. Kernel modundan Kullanıcı (User) moduna geçiş.
3. Programı kaldığı yerden devam ettirmek.

🔥 **Banko Soru Adayı: Dispatch Latency Nedir?**
**Cevap:** Dispatcher'ın bir process'i durdurup, yerine diğer process'i başlatmasına kadar geçen **gecikme süresine** dispatch latency denir.

---

## 📌 Preemptive vs. Nonpreemptive Scheduling

İşletim sisteminin Scheduling kararı verdiği 4 ana durum vardır:
1. Process **Running** $\rightarrow$ **Waiting** (I/O isteği vb.)
2. Process **Running** $\rightarrow$ **Ready** (Zaman diliminin bitmesi, kesme-interrupt gelmesi)
3. Process **Waiting** $\rightarrow$ **Ready** (I/O bitti)
4. Process **Sonlandırılırsa (Terminated)**

**Nonpreemptive (Kesintiye Uğratılamaz - Kooperatif):**
Sadece 1 ve 4 numaralı durumlarda gerçekleşirse buna *nonpreemptive* denir. İşlemci bir process'e verildiğinde, o process ya kendi isteğiyle beklemeye geçer ya da tamamen bitene kadar işlemciyi **asla bırakmaz.**

**Preemptive (Kesintiye Uğratılabilir):**
2 ve 3 numaralı durumlarda da karar veriliyorsa *preemptive*'dir. Yüksek öncelikli bir process geldiğinde veya zaman bittiğinde işletim sistemi mevcut process'i zorla CPU'dan atar (askıya alır). Çoğu modern OS (Windows, Linux, macOS) bunu kullanır. *Dikkat: Preemptive sistemlerde process'ler arasında paylaşılan verilerde "Race Condition" oluşabilir.*

---

## 📌 Scheduling (Çizelgeleme) Kriterleri
Sınavda eşleştirme veya "hangisinin artırılması/azaltılması hedeflenir?" tarzı sorulur.

* **Artırılması (Maksimize) İstenenler:**
  - **CPU Utilization (CPU Kullanım Oranı):** İşlemcinin meşgul tutulma oranıdır (%40-%90 arası idealdir).
  - **Throughput (İş Hacmi):** Belirli bir zaman diliminde yürütülmesi **tamamlanan** process sayısıdır.

* **Azaltılması (Minimize) İstenenler:**
  - **Turnaround Time (Dönüş Süresi):** Sürecin sisteme girdiği an ile tamamen bitip sonlandığı an arasındaki **toplam** süredir. *(Hazır kuyrukta bekleme + CPU'da çalışma + I/O işlem sürelerinin toplamı).*
  - **Waiting Time (Bekleme Süresi):** Sadece **Ready Queue'da** (hazır kuyruğunda) geçen toplam bekleme süresidir.
  - **Response Time (Yanıt Süresi):** Sisteme istekte bulunulduğu andan itibaren, **ilk tepkinin/yanıtın gelmeye başladığı** ana kadar geçen süredir. Uygulamanın açılma hızı gibi düşünülebilir.

---

## 📌 Algoritmalar

### 1- First-Come, First-Served (FCFS)
* **Mantığı:** Gelen ilk alır. CPU'yu ilk isteyen ilk geçer (FIFO mantığı).
* **Türü:** Kesinlikle **Nonpreemptive**'dir.
* **Dezavantaj:** Bekleme süreleri ortalaması çok yüksek olabilir. Process'lerin geliş sırasına göre çok değişir.

🔥 **Banko Terim Sorusu: Convoy Effect (Konvoy Etkisi) Nedir?**
**Cevap:** FCFS algoritmasında yaşanan bir sıkıntıdır. CPU'yu çok uzun süre kullanacak olan bir process (CPU-bound) başa geçtiğinde, onun arkasında bekleyen çok sayıda kısa süreli (I/O-bound) process'in tıkanıp kalması ve işlemcinin verimsiz kullanılması durumudur. Kamyon arkasındaki otomobil konvoyu gibi düşünün.

### 2- Shortest-Job-First (SJF)
* **Mantığı:** Bir sonraki CPU burst (çalışma) süresi **en kısa** olan process'i önce çalıştırır.
* **Avantajı:** Belirli bir process seti için **minimum ortalama bekleme süresini (waiting time)** sağlayan optimal algoritmadır.
* **Dezavantajı:** Bir process'in bir sonraki kısa çalışma süresini önceden bilmek imkansıza yakındır. (Geçmiş sürelere dayanarak matematiksel eksponansiyel ortalama *Exponential Average* formülü ile tahmin edilmeye çalışılır: $t_n$ ve $\tau_{n+1}$ parametreleri ile).

**İki Tipi Vardır:**
1. **Nonpreemptive SJF:** CPU process'e verildikten sonra, CPU burst bitene kadar process kesilmez.
2. **Preemptive SJF (Shortest-Remaining-Time-First - SRTF):** Process hazır kuyruğuna girdiğinde; yeni gelen process'in CPU ihtiyacı, şu an çalışmakta olan process'in **kalan işlem süresinden (remaining time)** daha kısaysa, mevcut olan zorla durdurulur ve yeni gelen çalıştırılır. Yukarıdaki sınav sorularınızda tam olarak bu çözüldü!

---

## 🎯 Sınav Simülasyonu - Doğru/Yanlış ve Boşluk Doldurma

**1.** CPU üzerindeki bir process'i fiziksel olarak devredip yetkiyi başka bir process'e aktaran, arada "Context Switch" yapan modülün özel ismi .................................................'dır.
*(Cevap: Dispatcher)*

**2.** Çoğu işletim sistemi non-preemptive zamanlama yaklaşımını benimser. (Doğru / Yanlış)
*(Cevap: Yanlış. Neredeyse tüm modern işletim sistemleri Windows, Linux vb. Preemptive kullanır.)*

**3.** ............................................ zamanlama algoritmasının en temel sorunu Convoy effect yaşatmasıdır.
*(Cevap: FCFS - First Come First Served)*

**4.** Sistemi hızlandırmak için Throughput artırılırken Turnaround time azaltılmaya çalışılır. (Doğru / Yanlış)
*(Cevap: Doğru)*

**5.** Hem gelen süreçlerin bitmesini beklemeyen hem de kalan süreye bakarak eski süreci askıya alan algoritmaya Shortest-Job-First (SJF) denmesinin Preemptive versiyonuna ............................................................. denir.
*(Cevap: Shortest-Remaining-Time-First (SRTF))*

**6.** SJF algoritmasının short-term scheduling için uygulanmasındaki en büyük zorluk ne olabilir? Hesaplayarak bulun?
*(Cevap: İşletim sistemi, process'in bir sonraki adımda işlemcide ne kadar süre vakit geçireceğini bilemez. Geleceği tahmin etmek zordur.)*
