# Rat in a Maze - Backtracking Algorithm

Repository ini berisi implementasi algoritma **Backtracking** untuk menyelesaikan permasalahan "Rat in a Maze" menggunakan bahasa pemrograman Python. Tugas ini dibuat untuk memenuhi instruksi mata kuliah Algoritma dan Pemrograman.

## Deskripsi Program
Program ini menggunakan antarmuka Command Line Interface (CLI) untuk memvisualisasikan langkah demi langkah bagaimana tikus mencari jalan keluar dari labirin. Jika tikus menemui jalan buntu, algoritma *backtracking* akan menarik tikus mundur ke titik percabangan sebelumnya untuk mencari rute alternatif.

## Cara Menjalankan Program
Pastikan Python sudah terinstal di komputer. Buka terminal atau command prompt, arahkan ke direktori file, lalu jalankan perintah berikut:
`python rat_in_a_maze.py`

## Pseudocode / Logika Algoritma
1. Cek apakah titik saat ini adalah tujuan akhir. Jika ya, program selesai.
2. Jika bukan, cek apakah titik saat ini aman (tidak menabrak tembok, di dalam batas labirin, dan belum dilewati).
3. Jika aman, tandai titik sebagai jalur.
4. Lakukan pencarian rekursif ke 4 arah: Bawah, Kanan, Atas, Kiri.
5. Jika semua arah menemui jalan buntu (*backtracking*), hapus tanda jalur pada titik tersebut dan kembali ke langkah percabangan sebelumnya.
