# ==============================================================================
#   TECHNICAL NOTES & DOCUMENTATION: NEBULAHEART 3D (SPACE GESTURE CONTROLLER)
# ==============================================================================
#
#   DESKRIPSI PROYEK:
# Sebuah aplikasi interaktif visualisasi 3D real-time yang mengontrol gerakan 
# dan formasi 1.500 partikel kosmis menggunakan kecerdasan buatan (AI) pelacak 
# tangan berbasis visi komputer.
#
#   TEKNOLOGI UTAMA :
# 1. Python 3.11    - Bahasa pemrograman utama (Sangat stabil untuk proyek ini).
# 2. Pygame         - Mengatur jendela aplikasi, frame-rate (60 FPS), dan input keyboard.
# 3. PyOpenGL       - Akses kartu grafis (GPU) untuk render 3D partikel secara real-time.
# 4. MediaPipe      - AI buatan Google untuk mendeteksi 21 titik koordinat kerangka tangan.
# 5. OpenCV (cv2)   - Mengakses webcam, memproses frame video, dan menampilkan monitor kamera.
# 6. NumPy 1.26.4   - Komputasi matriks kilat untuk kalkulasi posisi rumus matematika 3D.
#
#   PANDUAN KONTROL GESTUR TANGAN :
# ------------------------------------------------------------------------------
# | JARI TANGAN          | MODE | NAMA MODE             | EFEK VISUAL PARTIKEL |
# ------------------------------------------------------------------------------
# | Terbuka Lebar        |  1   | ROTASI COSMOS         | Partikel biru acak   |
# |                      |      |                       | berputar lambat.     |
# |                      |      |                       |                      |
# | 1 Jari Telunjuk Tegak|  2   | SATURNUS 3D           | Mengumpul jadi bola  |
# | (Jari lain menekuk)  |      |                       | oranye & cincin emas.|
# |                      |      |                       |                      |
# | 2 Jari (Peace Sign)  |  3   | TEKS I LOVE YOU       | Berbaris membentuk   |
# |                      |      |                       | tulisan biru neon.   |
# |                      |      |                       |                      |
# | Kepal/Genggam Tangan |  4   | BENTUK HATI (LOVE)    | Mengalir membentuk   |
# |                      |      |                       | ikon hati pink tajam.|
# ------------------------------------------------------------------------------
