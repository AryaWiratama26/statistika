# Penjelasan Lengkap & Studi Kasus — Statistika Deskriptif

Dokumen ini menjelaskan seluruh bab pada `Statistika-Deskriptif` dengan bahasa sederhana, langkah terstruktur, dan studi kasus angka yang bisa langsung diikuti.

---

## 1) Pengantar Statistika Dasar

- **Apa yang dipelajari**: Cara menggunakan data untuk menjawab pertanyaan. Bedakan `populasi` (semua) dan `sampel` (sebagian), `parameter` (populasi) dan `statistik` (sampel).
- **Konsep utama**:
  - Tujuan statistika deskriptif: meringkas dan memvisualkan data agar mudah dipahami.
  - Sampel harus representatif; `random sampling` membantu mengurangi bias.
- **Langkah praktis**:
  1. Tulis pertanyaan: “Apa yang ingin saya ketahui dari data?”
  2. Daftar variabel yang dibutuhkan dan jenis skalanya (lihat Bab 2).
  3. Tentukan sumber data dan cara mengambilnya (lihat Bab 3 dan 4).
- **Studi kasus**: IPK Mahasiswa
  - Pertanyaan: “Bagaimana gambaran IPK angkatan 2023?”
  - Ambil sampel acak 200 mahasiswa; hitung nilai pusat (mean/median) dan sebaran (SD/IQR); buat histogram dan boxplot. Ceritakan apa yang tipikal, ada tidaknya outlier, dan apakah distribusi menceng.

---

## 2) Klasifikasi Data dalam Statistika

- **Apa yang dipelajari**: Tipe/Skala data menentukan alat analisis dan grafik yang boleh dipakai.
- **Konsep utama**:
  - Kualitatif: `nominal` (label, tanpa urutan), `ordinal` (punya urutan, jarak tidak pasti).
  - Kuantitatif: `interval` (beda bermakna, nol bukan mutlak, mis. °C), `rasio` (nol mutlak, bisa perbandingan, mis. berat/harga/usia).
- **Langkah praktis**:
  1. Tandai setiap variabel dengan skalanya.
  2. Pilih ukuran yang cocok: mean/SD untuk interval/rasio; median/modus/proporsi untuk nominal/ordinal.
  3. Pilih grafik: bar/pie untuk kategori; histogram/boxplot untuk numerik.
- **Studi kasus**: Data Restoran
  - Variabel: `menu` (nominal), `rating rasa` 1–5 (ordinal), `harga` (rasio).
  - Analisis: bar chart menu terlaris; median rating per menu; histogram harga dan boxplot untuk outlier.

---

## 3) Desain Eksperimen

- **Apa yang dipelajari**: Cara menata studi agar hasil bisa dipercaya.
- **Konsep utama**:
  - Observasi: mengamati tanpa perlakuan.
  - Eksperimen: memberi perlakuan/treatment, lalu ukur dampaknya.
  - Tiga pilar: `kendali` (kelompok kontrol), `pengacakan` (penugasan acak), `replikasi` (cukup banyak subjek/pengulangan).
- **Langkah praktis**:
  1. Tetapkan variabel bebas (perlakuan) dan terikat (hasil).
  2. Buat kelompok kontrol vs perlakuan; acak penugasan; definisikan durasi/pengukuran.
  3. Catat prosedur konsisten untuk meminimalkan bias.
- **Studi kasus**: Vitamin D3
  - 140 pasien diacak: 70 D3, 70 placebo. Ukur antibodi setelah 12 bulan.
  - Hasil dijelaskan deskriptif: mean, median, SD tiap grup; boxplot bandingkan distribusi. Ceritakan perbedaan pola, efek outlier, dan seberapa konsisten tiap grup.

---

## 4) Pengumpulan Data dalam Statistika

- **Apa yang dipelajari**: Cara mengambil data dari populasi.
- **Konsep utama**:
  - `Sensus`: semua orang/objek, mahal tapi lengkap.
  - `Sampling`: sebagian, lebih hemat tapi ada `sampling error` (selisih sampel vs populasi) yang tidak bisa dihilangkan, hanya diperkecil.
  - Teknik sampling: simple random, stratified, cluster, systematic, convenience (hindari karena bias tinggi).
- **Langkah praktis**:
  1. Pilih teknik sampling sesuai struktur populasi dan biaya.
  2. Tentukan ukuran sampel yang memadai (cukup besar untuk stabilitas ringkasan deskriptif).
  3. Hindari pola sistematis saat memakai systematic sampling.
- **Studi kasus**: Survei Kecamatan
  - 7 kelurahan, target 350 responden. Gunakan `stratified`: alokasikan quota proporsional per kelurahan, lalu simple random di tiap kelurahan. Laporkan proporsi kepuasan per kelurahan dan keseluruhan, dengan bar chart.

---

## 5) Distribusi Frekuensi dalam Statistika

- **Apa yang dipelajari**: Mengelompokkan data numerik ke kelas untuk melihat pola global.
- **Konsep utama**:
  - Istilah: `lower/upper class limit`, `class width`, `midpoint`, `relative` dan `cumulative frequency`.
  - Ogive untuk melihat akumulasi (misal P90 dapat dibaca dari ogive).
- **Langkah praktis (contoh kerja)**:
  1. Kumpulkan data harga (n=30), tentukan `min`, `max`, dan `range`.
  2. Pilih 6–10 kelas; hitung `class width = ceil(range / jumlah_kelas)`.
  3. Bangun tabel frekuensi, hitung frekuensi relatif dan kumulatif.
  4. Buat histogram dan ogive untuk visual.
- **Studi kasus angka**: Harga Keyboard (dari materi)
  - min=65, max=340, range=275, kelas=7 → lebar≈40.
  - Terlihat konsentrasi 100–180; ada nilai 340 yang membuat ekor kanan lebih panjang.

---

## 6) Visualisasi Data dalam Statistika

- **Apa yang dipelajari**: Memilih grafik yang cocok untuk menyampaikan pesan data.
- **Konsep utama**:
  - Kategori: bar/pie (komposisi), dot plot/stem-and-leaf (kecil-menengah).
  - Numerik: histogram/frequency polygon (sebaran), boxplot (ringkasan dan outlier), scatter (hubungan dua variabel), time series (tren waktu).
  - Praktik baik: judul jelas, label sumbu, satuan, skala konsisten, hindari chart-ink berlebihan.
- **Langkah praktis**:
  1. Tentukan pesan utama, lalu pilih grafik yang paling langsung menyampaikan pesan itu.
  2. Tunjukkan outlier dan tren bila relevan; jangan memotong sumbu secara menyesatkan.
- **Studi kasus**: Penjualan Harian
  - Time series memperlihatkan kenaikan akhir bulan; scatter `biaya iklan vs penjualan` menunjukkan korelasi positif; bar chart membandingkan penjualan per kategori produk.

---

## 7) Pengukuran Tendensi Sentral

- **Apa yang dipelajari**: Nilai “tipikal” data.
- **Konsep utama**:
  - `Mean`: rata-rata; peka terhadap outlier.
  - `Median`: nilai tengah; tahan terhadap outlier, cocok untuk data menceng.
  - `Modus`: nilai tersering; bisa lebih dari satu (multimodal).
  - `Weighted mean`: rata-rata berbobot; `mean grouped data`: estimasi mean dari tabel frekuensi (pakai midpoint).
- **Langkah praktis**:
  1. Cek outlier/kemencengan; pilih median bila data menceng.
  2. Saat ada bobot (mis. SKS), pakai weighted mean: sum(nilai × bobot)/sum(bobot).
  3. Untuk data kelompok, pakai sum(midpoint × frekuensi)/n.
- **Studi kasus angka**: Nilai Mata Kuliah
  - Tugas 20% (80), UTS 30% (70), UAS 50% (90) → weighted mean = 0,2×80 + 0,3×70 + 0,5×90 = 82.
  - Jika ada tugas 0 (outlier rendah), median dari beberapa komponen bisa lebih menggambarkan performa tipikal.

---

## 8) Pengukuran Keberagaman/Sebaran

- **Apa yang dipelajari**: Seberapa “lebar” data menyebar dari pusat.
- **Konsep utama**:
  - `Range`: max − min (sangat peka outlier).
  - `Varians` dan `Standar Deviasi (SD)`: simpangan rata-rata dari mean (SD satuannya sama dengan data).
  - `IQR (Q3 − Q1)`: rentang tengah 50% data; dipakai untuk deteksi outlier.
  - `Empirical rule`: ~68% data dalam ±1 SD (jika mendekati normal); `Chebyshev`: batas umum untuk distribusi apa pun.
  - `CV`: perbandingan keragaman lintas skala yang berbeda (SD/mean).
- **Langkah praktis**:
  1. Laporkan pusat + sebaran (mis. mean ± SD atau median + IQR) bersama-sama.
  2. Bandingkan konsistensi antar grup dengan SD atau CV.
- **Studi kasus angka**: Dua Kurir
  - Kurir A: mean 3 hari, SD 0,6; Kurir B: mean 3 hari, SD 1,4 → A lebih konsisten.
  - Pilihan operasional condong ke A untuk SLA yang stabil meski rata-rata sama.

---

## 9) Pengukuran Posisi Data

- **Apa yang dipelajari**: Posisi relatif suatu nilai dalam kumpulan data.
- **Konsep utama**:
  - `Kuartil (Q1, Q2/median, Q3)`, `persentil (P1–P99)`, `z-score` (berapa SD dari mean, bisa negatif/positif/0).
  - `IQR` untuk outlier: batas bawah = Q1 − 1,5×IQR; batas atas = Q3 + 1,5×IQR. Boxplot memvisualisasikan ini.
- **Langkah praktis**:
  1. Gunakan P90 sebagai target layanan (mis. “90% pesanan ≤ 4 hari”).
  2. Gunakan z-score untuk membandingkan nilai dari skala berbeda atau menandai kejadian ekstrem (mis. z > 2,5).
- **Studi kasus angka**: Waktu Pengiriman
  - Q1 = 2,1; median = 2,6; Q3 = 3,3 → IQR = 1,2; batas atas = 3,3 + 1,8 = 5,1 hari.
  - Pesanan 6 hari > 5,1 → outlier; z ≈ (6 − 2,9)/1,1 ≈ 2,82 → kandidat eskalasi.

---

## Studi Kasus Terpadu: Kinerja Toko Online (Langkah demi langkah)

1. Klasifikasi variabel: `waktu_pengiriman` (rasio), `kurir` (nominal), `kota` (nominal), `status_SLA` (biner).
2. Tabel frekuensi dan histogram `waktu_pengiriman`; ogive untuk melihat P90.
3. Hitung mean, median, modus; laporkan mean ± SD dan median + IQR.
4. Boxplot per `kurir` dan `kota` untuk bandingkan konsistensi dan outlier.
5. Hitung P90 dan z-score; tetapkan aturan alarm z > 2,5.
6. Ceritakan temuan dalam bahasa sederhana: “Mayoritas paket tiba 2–3 hari; kurir A lebih konsisten; outlier terjadi di kurir B di kota X.”

---

## Tips Umum Pemakaian

- Selalu cocokkan alat analisis dengan tipe/skalanya.
- Tampilkan angka kunci berdampingan (pusat + sebaran + posisi) agar cerita data lengkap.
- Gunakan visual yang menjawab pertanyaan, bukan sekadar ramai gambar.
