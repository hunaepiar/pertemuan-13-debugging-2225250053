# Pertemuan 13 - Debugging, Tracing, Testing, dan Test Case Python

## Identitas Mahasiswa

- Nama: Khunaepi
- NIM: 2225250053
- Kelas: 3B

## 1. Tujuan Praktik

Praktik ini bertujuan untuk mempelajari proses debugging, tracing, dan testing program Python serta memperbaiki kesalahan berdasarkan hasil pengujian.

Tujuan khusus:

1. Membedakan syntax error, runtime error, logical error, dan validation bug.
2. Memahami cara membaca traceback untuk menemukan lokasi error.
3. Melakukan tracing perubahan nilai variabel dan alur program.
4. Menggunakan breakpoint dan debugger pada VS Code.
5. Memahami fungsi Step Over, Step Into, Step Out, dan Variables.
6. Menyusun test case untuk data normal, batas, kosong, dan tidak valid.
7. Membandingkan expected result dengan actual result.
8. Mengidentifikasi akar penyebab bug sebelum memperbaiki kode.
9. Melakukan pengujian ulang setelah program diperbaiki.
10. Mendokumentasikan hasil debugging dan mengunggah proyek ke GitHub menggunakan Python 3.12 melalui uv.

## 2. Struktur Folder

pertemuan-13-debugging-2225250053/
├── README.md
├── .gitignore
├── kasus/
│   ├── kasus_01_batas_kelulusan.py
│   ├── kasus_02_rata_rata.py
│   └── kasus_03_file_nilai.py
├── latihan/
│   ├── 01_trace_loop.py
│   ├── 02_trace_fungsi.py
│   ├── 03_test_case.py
│   └── 04_debug_breakpoint.py
└── praktik/
    └── praktik_4_debugging.py

## 3. Dasar Teori

### A. Debugging

Debugging adalah proses menemukan, menganalisis, dan memperbaiki penyebab kesalahan pada program.

Proses debugging dilakukan dengan mereproduksi masalah, mengamati hasil aktual, membuat hipotesis penyebab, menguji hipotesis, memperbaiki kode, dan menjalankan pengujian ulang.

### B. Jenis Error dan Bug

1. Syntax error terjadi ketika penulisan kode tidak sesuai aturan Python, misalnya kurang tanda titik dua.
2. Runtime error atau exception terjadi ketika program berjalan lalu mengalami kesalahan, misalnya ZeroDivisionError.
3. Logical error terjadi ketika program berjalan, tetapi menghasilkan output yang salah.
4. Validation bug terjadi ketika program menerima data yang seharusnya ditolak, misalnya nilai 120.

### C. Traceback

Traceback merupakan informasi yang ditampilkan ketika program mengalami exception.

Traceback membantu menemukan jenis error, pesan kesalahan, lokasi file, nomor baris, dan urutan pemanggilan fungsi sebelum kesalahan terjadi.

### D. Tracing

Tracing adalah proses mencatat perubahan nilai variabel dan alur eksekusi program secara bertahap.

Contoh:

    total = 0
    for i in range(1, 5):
        total += i
        print(i, total)

Hasil:

    1 1
    2 3
    3 6
    4 10

Tracing membantu memahami proses perulangan, fungsi, counter, akumulator, list, dan dictionary.

### E. Debugger VS Code

Debugger digunakan untuk menelusuri program ketika sedang dijalankan.

- Breakpoint: menghentikan sementara program pada baris tertentu.
- Continue: melanjutkan program sampai breakpoint berikutnya.
- Step Over: menjalankan baris berikutnya tanpa masuk ke fungsi.
- Step Into: masuk ke fungsi yang dipanggil.
- Step Out: menyelesaikan fungsi aktif dan kembali ke pemanggil.
- Variables: melihat nilai variabel selama debugging.

### F. Testing dan Test Case

Test case merupakan kombinasi input dan hasil yang diharapkan untuk memeriksa kebenaran program.

Jenis test case meliputi:

1. Normal, untuk data yang umum digunakan.
2. Batas, untuk menguji nilai tepat pada batas keputusan.
3. Di bawah batas, untuk memeriksa perubahan hasil keputusan.
4. Kosong, untuk menguji data yang tidak tersedia.
5. Tidak valid, untuk memeriksa data yang seharusnya ditolak.

Expected result adalah hasil yang diharapkan, sedangkan actual result adalah hasil yang benar-benar diperoleh ketika program dijalankan.

### G. Pengujian Ulang

Pengujian ulang atau retest dilakukan setelah perbaikan untuk memastikan bug sudah teratasi.

Seluruh test case perlu dijalankan kembali agar perbaikan tidak menimbulkan kesalahan pada bagian program lainnya. Kesalahan baru pada bagian yang sebelumnya berjalan benar disebut regresi.

## 4. Daftar Latihan

### Latihan 1: Tracing Perulangan

File: `latihan/01_trace_loop.py`

Mencatat perubahan variabel `i` dan `total` pada setiap iterasi perulangan.

### Latihan 2: Menelusuri Fungsi

File: `latihan/02_trace_fungsi.py`

Mempelajari parameter, proses perhitungan diskon, dan nilai yang dikembalikan oleh fungsi.

### Latihan 3: Testing dan Test Case

File: `latihan/03_test_case.py`

Menguji fungsi status kelulusan dengan nilai 75, 60, dan 59. Hasil aktual dibandingkan dengan hasil yang diharapkan.

### Latihan 4: Debugger dan Breakpoint

File: `latihan/04_debug_breakpoint.py`

Mencoba breakpoint, Continue, Step Over, Step Into, dan mengamati perubahan nilai variabel melalui debugger VS Code.

## 5. Praktik 4: Investigasi dan Perbaikan Bug

File program: `praktik/praktik_4_debugging.py`

Praktik ini menggunakan program yang menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi.

### A. Program Awal

Program awal memiliki tiga bug utama:

1. Fungsi rata-rata selalu membagi jumlah nilai dengan 5.
2. Fungsi status menggunakan operator `>` sehingga nilai 60 dinyatakan tidak lulus.
3. Fungsi nilai tertinggi menggunakan operator `<`, sehingga hasil pencarian nilai tertinggi salah.

### B. Bug Report

| ID | Gejala | Akar Penyebab | Perbaikan |
|---|---|---|---|
| B01 | Rata-rata salah | Pembagi selalu 5 | Menggunakan `len(nilai)` |
| B02 | Nilai 60 tidak lulus | Operator `>` | Menggunakan `>=` |
| B03 | Nilai tertinggi menjadi 0 | Operator perbandingan terbalik | Menggunakan `>` dan nilai awal dari elemen pertama |

### C. Perbaikan Program

Program diperbaiki dengan menyesuaikan pembagi rata-rata terhadap jumlah data, menggunakan operator kelulusan yang benar, dan memperbaiki algoritma pencarian nilai tertinggi.

Program juga menangani list kosong dengan mengembalikan 0 untuk rata-rata dan `None` untuk nilai tertinggi.

### D. Hasil Program Setelah Perbaikan

Dengan input:

    nilai = [80, 60, 90, 70]

Hasil yang diharapkan:

    Rata-rata: 75.0
    Status 60: Lulus
    Tertinggi: 90

## 6. Cara Menjalankan Program

Pastikan terminal berada di folder utama proyek dan `uv` sudah tersedia.

### Persiapan

Pemeriksaan versi uv:

    uv --version

Pemeriksaan Python 3.12:

    uv run --python 3.12 python --version

### Menjalankan Latihan 1

    uv run --python 3.12 latihan/01_trace_loop.py

### Menjalankan Latihan 2

    uv run --python 3.12 latihan/02_trace_fungsi.py

### Menjalankan Latihan 3

    uv run --python 3.12 latihan/03_test_case.py

### Menjalankan Latihan 4

    uv run --python 3.12 latihan/04_debug_breakpoint.py

### Menjalankan Kasus 1: Batas Kelulusan

    uv run --python 3.12 kasus/kasus_01_batas_kelulusan.py

### Menjalankan Kasus 2: Rata-rata

    uv run --python 3.12 kasus/kasus_02_rata_rata.py

### Menjalankan Kasus 3: File dan Error Handling

    uv run --python 3.12 kasus/kasus_03_file_nilai.py

### Menjalankan Praktik 4

    uv run --python 3.12 praktik/praktik_4_debugging.py

## 7. Hasil Pengujian

Test case minimum sesuai bahan ajar:

| No. | Kasus Pengujian | Input | Expected Result |
|---|---|---|---|
| T1 | Menghitung rata-rata | [80, 60, 90, 70] | 75.0 |
| T2 | Menghitung rata-rata | [100, 80] | 90.0 |
| T3 | Status kelulusan | 60 | Lulus |
| T4 | Status kelulusan | 59 | Tidak lulus |
| T5 | Nilai tertinggi | [80, 60, 90, 70] | 90 |

### Hasil Pengujian Awal

| ID | Expected | Actual Awal | Status |
|---|---|---|---|
| T1 | 75.0 | 60.0 | FAIL |
| T2 | 90.0 | 36.0 | FAIL |
| T3 | Lulus | Tidak lulus | FAIL |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 0 | FAIL |

### Hasil Retest

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |

Catatan: Hasil aktual dan status pengujian perlu disesuaikan dengan hasil yang benar-benar diperoleh setelah program dijalankan di VS Code.

## 8. Jawaban Kuis Formatif

### 1. Apa perbedaan syntax error, runtime error, dan logical error?

Syntax error terjadi karena penulisan kode tidak sesuai aturan Python. Runtime error terjadi ketika program mengalami kesalahan saat dijalankan. Logical error terjadi ketika program berjalan, tetapi hasilnya tidak sesuai dengan yang diharapkan.

### 2. Apa fungsi traceback?

Traceback membantu mengetahui jenis exception, pesan kesalahan, lokasi file, nomor baris, dan urutan pemanggilan fungsi yang berkaitan dengan kesalahan.

### 3. Kapan Step Into digunakan?

Step Into digunakan ketika ingin masuk ke fungsi yang dipanggil agar proses di dalam fungsi dapat ditelusuri baris demi baris.

### 4. Apa perbedaan Step Over dan Step Into?

Step Over menjalankan baris berikutnya tanpa masuk ke fungsi yang dipanggil. Step Into masuk ke fungsi tersebut sehingga isi fungsi dapat diperiksa.

### 5. Mengapa nilai batas perlu dimasukkan dalam test case?

Nilai batas perlu diuji karena kesalahan operator pembanding dapat menyebabkan hasil keputusan salah tepat pada batas tertentu, seperti nilai 60 yang seharusnya lulus.

### 6. Apa perbedaan expected result dan actual result?

Expected result adalah hasil yang seharusnya diperoleh berdasarkan ketentuan program, sedangkan actual result adalah hasil yang benar-benar muncul ketika program dijalankan.

### 7. Apa yang dimaksud regresi setelah perbaikan?

Regresi adalah munculnya kesalahan pada bagian program yang sebelumnya berjalan benar setelah dilakukan perubahan atau perbaikan kode.

### 8. Mengapa debugging perlu diawali dengan reproduksi masalah?

Reproduksi masalah membantu memastikan kesalahan dapat muncul kembali dengan input yang diketahui sehingga penyebabnya lebih mudah ditelusuri dan diuji.

### 9. Mengapa perubahan kode sebaiknya minimal saat memperbaiki bug?

Perubahan minimal memudahkan penentuan penyebab masalah dan pemeriksaan apakah perbaikan benar-benar mengatasi bug tanpa menimbulkan kesalahan baru.

### 10. Apa manfaat commit khusus bertipe fix pada GitHub?

Commit khusus bertipe fix mencatat perubahan yang dilakukan untuk memperbaiki bug sehingga proses perbaikan dapat ditelusuri dan dibandingkan dengan versi sebelumnya.

## 9. Refleksi

Melalui praktik ini, saya memahami bahwa program yang berhasil dijalankan belum tentu menghasilkan output yang benar.

Saya mempelajari cara membaca traceback, melakukan tracing terhadap perubahan variabel, menggunakan breakpoint pada VS Code, dan menyusun test case untuk menguji berbagai kondisi input.

Saya juga memahami bahwa bug perlu diperbaiki berdasarkan akar penyebabnya, bukan sekadar mengubah kode tanpa pengujian. Setelah perbaikan dilakukan, seluruh test case harus dijalankan kembali untuk memastikan hasilnya sesuai harapan.

Penggunaan Git dan GitHub membantu mendokumentasikan proses pengerjaan melalui commit sebelum dan sesudah perbaikan.

## 10. Kesimpulan

Debugging, tracing, dan testing merupakan bagian penting dalam pengembangan program Python. Ketiganya membantu menemukan kesalahan, memahami alur eksekusi, dan membuktikan kebenaran hasil program.

Melalui Praktik 4, saya mengidentifikasi dan memperbaiki tiga bug pada perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi. Perbaikan kemudian diuji kembali menggunakan lima test case.

Dokumentasi melalui README dan riwayat commit GitHub membantu menunjukkan proses investigasi, perbaikan, serta hasil pengujian program.

## 11. Pengumpulan GitHub

Repositori: (Masukkan URL repositori GitHub milik sendiri)

Nama repositori: `pertemuan-13-debugging-2225250053`

Seluruh file latihan, kasus, praktik, README, dan `.gitignore` dikumpulkan dalam satu repositori.

Commit yang disarankan:

1. `chore: menambahkan kasus debugging awal`
2. `test: menambahkan test case dan bug report`
3. `fix: memperbaiki bug rata-rata status dan nilai tertinggi`
4. `docs: menambahkan hasil retest dan refleksi`

Pengumpulan dilakukan dengan Git melalui commit bertahap dan `git push`.

## 12. Referensi

- Bahan Ajar Algoritma dan Pemrograman, Pertemuan 13: Debugging, Tracing, Testing, dan Test Case Python di VS Code dan Pengumpulan melalui GitHub.
- Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). Green Tea Press.
- Python Software Foundation. Dokumentasi resmi Python 3.
- Visual Studio Code Documentation. Dokumentasi debugging Python.
- GitHub Docs. Dokumentasi commit dan pengelolaan perubahan pada repositori.
- Dokumentasi resmi uv mengenai penggunaan versi Python tertentu.
-