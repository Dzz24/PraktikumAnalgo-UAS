# PraktikumAnalgo-UAS

### Nama Anggota Kelompok:
1.Elsa Rizki Utami - 140810240040

2.Abraham Gomes Samosir - 140810240044

3.Dzikri Fakhry - 140810240056

4.Fardan Fadhilah Andicha Putra - 140810240084

# Last-Mile Delivery Optimization: Heuristic vs Exact Algorithm

Repositori ini berisi implementasi pipeline simulasi komputasi untuk membandingkan efisiensi finansial antara pendekatan **Algoritma Heuristik (Greedy)** dan **Algoritma Eksak (DFS Backtracking dengan Pruning)** dalam kasus optimasi rute *Last-Mile Delivery*.

Proyek ini bertujuan untuk menjawab tantangan dalam penentuan infrastruktur teknologi operasional ekspedisi, dengan menyeimbangkan antara biaya *cloud computing* dan biaya operasional bahan bakar (BBM)

---

## 1. Cara Menjalankan Program

Program dijalankan melalui *Command Line Interface (CLI)*.

### Prasyarat

* Python 3.x sudah diinstalasi.

###  Langkah Eksekusi

1. Clone repositori ini:

   ```bash
   git clone <url-repository>
   ```

2. Masuk ke direktori proyek:

   ```bash
   cd <nama-folder>
   ```

3. Jalankan program:

   ```bash
   python src/exact/main.py
   ```

###  Output

Program akan:

* Membaca dataset dari folder `data/`
* Menampilkan tabel komparasi **Total Cost of Ownership (TCO)**
* Menampilkan rincian rute dari masing-masing algoritma

Tangkapan layar hasil eksekusi tersedia di folder `docs/`

---

## 2. Pemilihan Algoritma & Trade-Off
### Algoritma A: Heuristik (Greedy - Nearest Neighbour)

**Karakteristik:**

* Memilih node terdekat yang belum dikunjungi pada setiap langkah

**Keunggulan:**
* Sangat cepat
* Biaya komputasi rendah
* Cocok untuk skala besar dan real-time

**Kekurangan:**
* Tidak menjamin solusi optimal
* Rentan terjebak di *local optimum*
* Potensi konsumsi BBM lebih tinggi

### Algoritma B: Eksak (DFS Backtracking + Pruning)

**Karakteristik:**
* Mengeksplorasi semua kemungkinan rute (permutasi)
* Menggunakan **cost pruning** untuk memangkas cabang tidak optimal

**Keunggulan:**
* Menjamin solusi **global optimum**
* Konsumsi BBM paling efisien

**Kekurangan:**
* Waktu komputasi sangat tinggi
* Biaya cloud meningkat drastis (eksponensial)

---

## 3. Analisis Kompleksitas

### Greedy (Heuristik)
* **Waktu:** `O(V²)`
* **Ruang:** `O(V)`

Penjelasan:
* Loop luar: menentukan urutan rute
* Loop dalam: mencari node terdekat

### DFS Backtracking + Pruning (Eksak)
* **Waktu:** `O(V!)` *(worst-case)*
* **Ruang:** `O(V)`

Penjelasan:
* Menjelajahi semua permutasi kemungkinan rute
* Pruning membantu secara praktis, tapi tidak mengubah batas atas kompleksitas

## 4. Analisis Bisnis (Business Insight)

Simulasi dilakukan pada dua skenario:

| Skenario | Harga BBM   |
| -------- | ----------- |
| Subsidi  | Rp 5.000/L  |
| Krisis   | Rp 20.000/L |

### Kesimpulan
* Algoritma Eksak **lebih hemat BBM**
* Namun memiliki **biaya server jauh lebih tinggi**
* Keputusan optimal tergantung pada harga BBM


### Break-Even Point

Algoritma Eksak menjadi lebih menguntungkan ketika:

```
Selisih Biaya Server ≥ Penghematan Biaya BBM
```

Atau:

```
(Server Eksak - Server Greedy) = (BBM Greedy - BBM Eksak) × Harga BBM
```

---

## 5. Hasil Simulasi & Analisis Finansial

Berdasarkan simulasi komputasi yang membandingkan dua skenario harga bahan bakar, diperoleh hasil sebagai berikut:

### Skenario Subsidi (Rp 5.000/L)

| Komponen             | Heuristik    | Eksak          |
| -------------------- | ------------ | -------------- |
| Biaya BBM            | Rp 8.902     | Rp 7.714       |
| Biaya Server         | Rp 1         | Rp 289.828     |
| **Total Cost (TCO)** | **Rp 8.904** | **Rp 297.542** |

**Kesimpulan:**
* Algoritma Eksak memang lebih efisien dalam penggunaan BBM
* Namun, biaya komputasi sangat tinggi
* Heuristik jauh lebih murah secara total

### Skenario Krisis (Rp 20.000/L)

| Komponen             | Heuristik     | Eksak          |
| -------------------- | ------------- | -------------- |
| Biaya BBM            | Rp 35.610     | Rp 30.857      |
| Biaya Server         | Rp 1          | Rp 289.828     |
| **Total Cost (TCO)** | **Rp 35.611** | **Rp 320.685** |

**Kesimpulan:**
* Selisih efisiensi BBM semakin besar
* Namun tetap belum mampu menutup biaya server algoritma Eksak

### Grafik Perbandingan
<img width="1189" height="955" alt="tco-graph" src="https://github.com/user-attachments/assets/af322e92-483f-4c7d-b3bd-716492e032ab" />

---

## 6. Analisis Keputusan

Penerapan Algoritma Eksak memberikan peningkatan efisiensi rute sebagai berikut:
* Pengurangan jarak: **10,41 km** *(dari 56,01 km → 45,60 km)*
* Penghematan bahan bakar: **0,2376 Liter / pengantaran**

Namun, efisiensi ini memiliki konsekuensi:
* Waktu eksekusi: **5.796,553 ms (~5.8 detik)**
* Biaya komputasi: **Rp 289.828 / eksekusi**

---

## 7. Kesimpulan
Berdasarkan seluruh pengujian kompleksitas komputasi dan analisis ekonomi komparatif, Algoritma Heuristik (Greedy) ditetapkan sebagai pilihan paling rasional dan direkomendasikan untuk diimplementasikan pada infrastruktur Last-Mile Delivery perusahaan.

Meskipun Algoritma Eksak terbukti sukses menemukan rute optimal mutlak yang memangkas jarak tempuh hingga 10,41 km, pendekatan ini gagal memenuhi kriteria kelayakan finansial operasional. Penghematan bahan bakar yang dihasilkan (sekitar 0,2376 Liter) sangat tidak sebanding dengan ledakan tagihan komputasi server Pay-as-you-go yang membengkak drastis hingga Rp 289.828 per satu kali eksekusi.


Dengan kata lain:

> Penghematan BBM !< Biaya tambahan server

---

## 8. Rekomendasi Tindakan

Untuk sistem produksi, perusahaan wajib menggunakan Algoritma Heuristik (Greedy) sebagai mesin penentu rute harian. Total Cost of Ownership (TCO)-nya terbukti efisien (hanya berkisar Rp 8.904 pada skenario normal) dengan waktu eksekusi yang nyaris instan, membuatnya sangat cocok untuk memproses ratusan pesanan pelanggan secara real-time.

Untuk Audit Internal (Back-Office): Algoritma Eksak (DFS Backtracking) tidak perlu dihapus, melainkan dialihfungsikan sebagai benchmark tool. Algoritma ini cukup dijalankan secara berkala pada lingkungan offline (bukan real-time) untuk mengevaluasi seberapa besar deviasi/selisih akurasi rute Heuristik dari rute optimal mutlak pada dataset berukuran kecil.

---
