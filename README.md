# SMK Negeri 1 Nusantara — Website Sekolah

Website profil sekolah multi-halaman untuk tugas sertifikasi **Pengembang Web Pratama (Junior Web Developer)**.
Tampilan memakai template **Kaira** (TemplatesJungle) tanpa mengubah palet, font, atau gaya komponennya.

## Menjalankan

Langsung buka `index.html` di browser, atau jalankan server lokal:

```powershell
cd "D:\Project_Pkl\9 november\smk-web"
python -m http.server 8000
```

Lalu buka `http://localhost:8000`.

> Semua CSS, JavaScript, dan font sudah disimpan lokal sehingga halaman tetap tampil tanpa internet.
> Satu-satunya bagian yang membutuhkan koneksi adalah peta Google Maps di halaman kontak.

## Halaman

| File | Isi |
| --- | --- |
| `index.html` | Beranda: hero slider, sambutan, statistik, jurusan, ekstrakurikuler, berita, galeri, testimoni, CTA |
| `profil.html` | Sambutan kepala sekolah, sejarah, visi-misi, struktur, **tabel profil sekolah**, fasilitas |
| `jurusan.html` | Tab 4 kompetensi keahlian: TKJ, RPL, DKV, AKL |
| `ekstrakurikuler.html` | 6 ekstrakurikuler + filter kategori |
| `galeri.html` | 12 foto + filter kategori + lightbox |
| `berita.html` | Daftar berita, pencarian, pengumuman, agenda |
| `berita-ppdb.html` | Artikel PPDB |
| `berita-lomba.html` | Artikel prestasi lomba web design |
| `berita-kunjungan-industri.html` | Artikel kunjungan industri |
| `kontak.html` | Informasi kontak, form dengan validasi, peta |
| `404.html` | Halaman tidak ditemukan |

## Fitur interaktif

- Hero slider (Swiper) dengan autoplay, panah, dan pagination.
- Slider testimoni alumni.
- Animasi muncul saat digulir (AOS).
- Counter angka guru, siswa, rombel, dan jurusan.
- Filter kategori pada ekstrakurikuler dan galeri.
- Lightbox galeri memakai modal Bootstrap.
- Pencarian berita secara langsung.
- Validasi form kontak (Bootstrap + JavaScript).
- Navigasi mobile berupa offcanvas.
- Tab jurusan yang bisa dibuka lewat hash, misalnya `jurusan.html#rpl`.
- Tombol kembali ke atas.

## Struktur folder

```
smk-web/
├─ index.html
├─ profil.html
├─ jurusan.html
├─ ekstrakurikuler.html
├─ galeri.html
├─ berita.html
├─ berita-ppdb.html
├─ berita-lomba.html
├─ berita-kunjungan-industri.html
├─ kontak.html
├─ 404.html
├─ style.css            # design system Kaira (tidak diubah)
├─ css/
│  ├─ bootstrap.min.css
│  ├─ fonts.css         # @font-face Jost & Marcellus (lokal)
│  ├─ vendor.css        # style vendor + AOS
│  ├─ swiper-bundle.min.css
│  └─ school.css        # perekat layout, tanpa mengubah warna/font
├─ fonts/               # woff2 Jost & Marcellus
├─ images/              # foto sekolah, jurusan, kegiatan, favicon
├─ js/
│  ├─ jquery.min.js
│  ├─ bootstrap.bundle.min.js
│  ├─ swiper-bundle.min.js
│  ├─ plugins.js        # AOS dan plugin bawaan Kaira
│  └─ school.js         # seluruh interaksi halaman sekolah
└─ _build/
   └─ generate.py       # generator HTML agar navbar/footer konsisten
```

## Mengubah data

Semua data sekolah masih berupa contoh. Cari komentar `TODO` di file HTML
(atau di `_build/generate.py` bila ingin regenerasi massal):

| Data | Lokasi |
| --- | --- |
| Nama sekolah, alamat, telepon, email, kepala sekolah | `_build/generate.py` bagian atas (`SCHOOL`, `ADDRESS`, `PHONE`, `EMAIL`, `HEADMASTER`) |
| Statistik guru/siswa/rombel/jurusan | `index.html` — cari `TODO: ganti angka statistik` |
| Tabel profil sekolah | `profil.html` — cari `TODO: ganti seluruh data pada tabel` |
| Ekstrakurikuler, pembina, jadwal | `ekstrakurikuler.html` — cari `TODO: sesuaikan nama ekstrakurikuler` |
| Berita dan pengumuman | `berita.html` + tiga file artikel |
| Kontak dan peta | `kontak.html` — cari `TODO: ganti alamat` dan `TODO: ganti koordinat` |

Setelah mengubah `_build/generate.py`, jalankan:

```powershell
python _build/generate.py
```

### Menghubungkan form ke Google Forms

Form kontak memakai Google Forms agar cocok untuk hosting statis:

1. Buat Google Form dengan field **Nama, Email, Telepon, Subjek, Pesan**.
2. Dapatkan URL `formResponse` dan `entry.xxxxx` untuk setiap field.
3. Ubah atribut `name` pada input di `kontak.html` menjadi `entry.xxxxx`.
4. Isi `data-endpoint` pada `<form id="contact-form">` dengan URL `formResponse`.
5. `initContactForm()` di `js/school.js` akan mengirim data lewat `fetch` (`mode: "no-cors"`).

Selama `data-endpoint` kosong, form menampilkan pesan sukses demo dan tidak mengirim data.

## Catatan desain

- Palet asli Kaira: sage `#8C907E`, light `#F1F1F0`, gelap `#111111`.
- Heading **Marcellus**, body **Jost** — keduanya dimuat lokal dari `fonts/`.
- `css/school.css` hanya mengatur layout (hero, kartu, tabel, filter, galeri, footer, responsif).
  Warna, tipografi, tombol, dan animasi tetap mengikuti `style.css` bawaan Kaira.
- Judul dibuat cair (`clamp()`) agar kata panjang seperti "Ekstrakurikuler" tidak meluber di layar kecil.

## Kredit & lisensi

- Template: **Kaira** oleh [TemplatesJungle](https://templatesjungle.com). Kredit di footer dipertahankan sesuai lisensi.
- Foto: [Unsplash](https://unsplash.com) (lisensi Unsplash).
- Font: [Google Fonts](https://fonts.google.com) — Jost & Marcellus.
- Library: Bootstrap 5.3.3, Swiper 11, jQuery, AOS.
- Ikon: SVG inline buatan sendiri mengikuti gaya garis Kaira.
