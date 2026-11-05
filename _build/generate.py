# -*- coding: utf-8 -*-
"""
Generator halaman statis website sekolah.
Menghasilkan HTML final dari satu layout agar navbar/footer konsisten.
Jalankan: python _build/generate.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHOOL = "SMK Negeri 1 Nusantara"
TAGLINE = "Unggul - Berkarakter - Siap Kerja"
ADDRESS = "Jl. Pendidikan Raya No. 45, Kel. Nusantara, Kec. Cendekia, Kota Nusantara 12345"
PHONE = "(021) 555-0123"
WHATSAPP = "0812-3456-7890"
EMAIL = "info@smkn1nusantara.sch.id"
HEADMASTER = "Drs. Ahmad Fauzi, M.Pd."

ICONS = {
    "facebook": '<path fill="currentColor" d="M13.5 21v-7h2.4l.4-3h-2.8V9.2c0-.9.3-1.5 1.6-1.5H16V5.1c-.3 0-1.3-.1-2.5-.1-2.5 0-4 1.5-4 4.2V11H7v3h2.5v7h4Z"/>',
    "instagram": '<rect x="3.5" y="3.5" width="17" height="17" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor"/>',
    "youtube": '<rect x="2.5" y="5.5" width="19" height="13" rx="4" fill="currentColor"/><path d="m10 9 5.5 3L10 15V9Z" fill="#fff"/>',
    "phone": '<path fill="currentColor" d="M6.6 3h3l1.2 4-2 1.3a13 13 0 0 0 5.9 5.9l1.3-2 4 1.2v3a2 2 0 0 1-2.2 2A16.8 16.8 0 0 1 4.6 5.2 2 2 0 0 1 6.6 3Z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m4 7 8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "pin": '<path fill="currentColor" d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5Z"/>',
    "clock": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "arrow-up": '<path fill="currentColor" d="M12 4 5 11h4v9h6v-9h4L12 4Z"/>',
    "zoom": '<path fill="currentColor" d="M11 5h2v6h6v2h-6v6h-2v-6H5v-2h6V5Z"/>',
    "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5v-16Z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 18.5V21h13" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "flask": '<path d="M9 3h6M10 3v6l-5 8a2 2 0 0 0 1.7 3h10.6a2 2 0 0 0 1.7-3l-5-8V3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
    "user": '<circle cx="12" cy="8" r="3.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M5 20c0-3.3 3.1-6 7-6s7 2.7 7 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 12h18" fill="none" stroke="currentColor" stroke-width="1.8"/>',
}

BRAND_MARK = (
    '<svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true">'
    '<rect width="64" height="64" rx="14" fill="#8C907E"/>'
    '<path d="M32 13 10 24l22 11 18-9v13h4V24L32 13Z" fill="#F1F1F0"/>'
    '<path d="M18 34v9c0 5 6.3 9 14 9s14-4 14-9v-9l-14 7-14-7Z" fill="#F1F1F0"/>'
    "</svg>"
)

# Menu utama. Item tanpa "children" tampil sebagai tautan langsung;
# item dengan "children" tampil sebagai dropdown di desktop dan accordion di mobile.
NAV_ITEMS = [
    {"href": "index.html", "label": "Beranda"},
    {
        "href": "profil.html",
        "label": "Profil Sekolah",
        "id": "profil",
        "children": [
            ("profil.html", "Ringkasan Profil"),
            ("profil.html#sambutan", "Sambutan Kepala Sekolah"),
            ("profil.html#sejarah", "Sejarah &amp; Keunggulan"),
            ("profil.html#visi-misi", "Visi &amp; Misi"),
            ("profil.html#struktur", "Struktur Sekolah"),
            ("profil.html#tabel-profil", "Data &amp; Tabel Profil"),
            ("profil.html#fasilitas", "Fasilitas"),
        ],
    },
    {
        "href": "jurusan.html",
        "label": "Akademik",
        "id": "akademik",
        "children": [
            ("jurusan.html", "Jurusan"),
            ("ekstrakurikuler.html", "Ekstrakurikuler"),
        ],
    },
    {
        "href": "berita.html",
        "label": "Informasi",
        "id": "informasi",
        "children": [
            ("berita.html", "Berita"),
            ("galeri.html", "Galeri"),
            ("kontak.html", "Kontak"),
        ],
    },
]


def same_page(href, active):
    """True bila href dan halaman aktif menunjuk file yang sama (tanpa hash)."""
    return href.split("#")[0] == active.split("#")[0]


def group_is_active(item, active):
    """Dropdown dianggap aktif bila halaman aktif ada di dalam kelompoknya."""
    if same_page(item["href"], active):
        return True
    return any(same_page(child[0], active) for child in item.get("children", []))


def icon(name, size=20):
    return (
        '<svg width="%d" height="%d" viewBox="0 0 24 24" aria-hidden="true">%s</svg>'
        % (size, size, ICONS[name])
    )


def nav_desktop(active):
    items = []
    for item in NAV_ITEMS:
        href = item["href"]
        label = item["label"]
        children = item.get("children")

        if not children:
            classes = "nav-link"
            current = ""
            if href == active:
                classes += " active"
                current = ' aria-current="page"'
            items.append(
                '<li class="nav-item"><a class="%s"%s href="%s">%s</a></li>'
                % (classes, current, href, label)
            )
            continue

        classes = "nav-link dropdown-toggle"
        if group_is_active(item, active):
            classes += " active"

        sub_items = []
        for child_href, child_label in children:
            child_classes = "dropdown-item item-anchor"
            child_current = ""
            if child_href == active:
                child_classes += " active"
                child_current = ' aria-current="page"'
            sub_items.append(
                '<li><a class="%s"%s href="%s">%s</a></li>'
                % (child_classes, child_current, child_href, child_label)
            )

        menu_id = "menu-%s" % item["id"]
        items.append(
            '<li class="nav-item dropdown">'
            '<a class="%s" href="%s" id="%s" role="button" data-bs-toggle="dropdown" aria-expanded="false">%s</a>'
            '<ul class="dropdown-menu" aria-labelledby="%s">%s</ul>'
            "</li>"
            % (classes, href, menu_id, label, menu_id, "".join(sub_items))
        )

    return "".join(items)


def nav_mobile(active):
    items = []
    for item in NAV_ITEMS:
        href = item["href"]
        label = item["label"]
        children = item.get("children")

        if not children:
            classes = "nav-link"
            current = ""
            if href == active:
                classes += " active"
                current = ' aria-current="page"'
            items.append(
                '<li class="nav-item"><a class="%s"%s href="%s">%s</a></li>'
                % (classes, current, href, label)
            )
            continue

        classes = "nav-link mobile-menu-toggle"
        if group_is_active(item, active):
            classes += " active"

        menu_id = "mobile-menu-%s" % item["id"]
        sub_items = []
        for child_href, child_label in children:
            child_classes = "mobile-submenu-link"
            child_current = ""
            if child_href == active:
                child_classes += " active"
                child_current = ' aria-current="page"'
            sub_items.append(
                '<li><a class="%s"%s href="%s">%s</a></li>'
                % (child_classes, child_current, child_href, child_label)
            )

        items.append(
            '<li class="nav-item">'
            '<button class="%s" type="button" data-bs-toggle="collapse" data-bs-target="#%s" '
            'aria-expanded="false" aria-controls="%s">%s<span class="menu-caret" aria-hidden="true"></span></button>'
            '<div class="collapse mobile-submenu" id="%s"><ul class="list-unstyled mb-0">%s</ul></div>'
            "</li>"
            % (classes, menu_id, menu_id, label, menu_id, "".join(sub_items))
        )

    return "".join(items)


def navbar(active):
    return """
<header class="sticky-top">
  <nav class="navbar navbar-expand-xl bg-light text-uppercase fs-6 p-3 border-bottom align-items-center">
    <div class="container">
      <a class="navbar-brand d-flex align-items-center gap-2 text-decoration-none" href="index.html">
        %s
        <span class="brand-text">%s<span>%s</span></span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar"
        aria-controls="offcanvasNavbar" aria-label="Buka menu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Menu</h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Tutup"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav ms-auto align-items-xl-center gap-1 gap-xl-3 d-none d-xl-flex">
            %s
            <li class="nav-item ms-xl-3"><a class="btn btn-dark btn-sm px-4 text-uppercase" href="kontak.html">PPDB</a></li>
          </ul>
          <div class="d-xl-none w-100">
            <ul class="navbar-nav gap-1">
              %s
              <li class="nav-item mt-2"><a class="btn btn-dark btn-sm px-4 text-uppercase w-100" href="kontak.html">PPDB</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </nav>
</header>
""" % (BRAND_MARK, SCHOOL, TAGLINE, nav_desktop(active), nav_mobile(active))


def footer():
    return """
<footer id="footer" class="mt-5">
  <div class="container">
    <div class="row d-flex flex-wrap justify-content-between py-5">
      <div class="col-md-3 col-sm-6">
        <div class="footer-menu footer-menu-001">
          <div class="footer-intro mb-4">
            <a href="index.html" class="d-inline-flex align-items-center gap-2 text-decoration-none">
              %s
              <span class="brand-text">%s<span>%s</span></span>
            </a>
          </div>
          <p>Sekolah menengah kejuruan yang menyiapkan lulusan kompeten, berkarakter, dan siap bekerja maupun melanjutkan pendidikan.</p>
          <div class="social-links">
            <ul class="list-unstyled d-flex flex-wrap gap-3">
              <li><a href="https://www.instagram.com/" target="_blank" rel="noopener" class="text-secondary" aria-label="Instagram">%s</a></li>
              <li><a href="https://www.facebook.com/" target="_blank" rel="noopener" class="text-secondary" aria-label="Facebook">%s</a></li>
              <li><a href="https://www.youtube.com/" target="_blank" rel="noopener" class="text-secondary" aria-label="YouTube">%s</a></li>
            </ul>
          </div>
        </div>
      </div>

      <div class="col-md-3 col-sm-6">
        <div class="footer-menu footer-menu-002">
          <h5 class="widget-title text-uppercase mb-4">Menu Cepat</h5>
          <ul class="menu-list list-unstyled text-uppercase border-animation-left fs-6">
            <li class="menu-item"><a href="index.html" class="item-anchor">Beranda</a></li>
            <li class="menu-item"><a href="profil.html" class="item-anchor">Profil Sekolah</a></li>
            <li class="menu-item"><a href="jurusan.html" class="item-anchor">Kompetensi Keahlian</a></li>
            <li class="menu-item"><a href="ekstrakurikuler.html" class="item-anchor">Ekstrakurikuler</a></li>
            <li class="menu-item"><a href="berita.html" class="item-anchor">Berita</a></li>
          </ul>
        </div>
      </div>

      <div class="col-md-3 col-sm-6">
        <div class="footer-menu footer-menu-003">
          <h5 class="widget-title text-uppercase mb-4">Informasi</h5>
          <ul class="menu-list list-unstyled text-uppercase border-animation-left fs-6">
            <li class="menu-item"><a href="kontak.html" class="item-anchor">Penerimaan Siswa Baru</a></li>
            <li class="menu-item"><a href="galeri.html" class="item-anchor">Galeri Kegiatan</a></li>
            <li class="menu-item"><a href="profil.html#tabel-profil" class="item-anchor">Data Sekolah</a></li>
            <li class="menu-item"><a href="profil.html#fasilitas" class="item-anchor">Fasilitas</a></li>
            <li class="menu-item"><a href="kontak.html" class="item-anchor">Hubungi Kami</a></li>
          </ul>
        </div>
      </div>

      <div class="col-md-3 col-sm-6">
        <div class="footer-menu footer-menu-004 border-animation-left">
          <h5 class="widget-title text-uppercase mb-4">Kontak</h5>
          <p class="mb-2">%s</p>
          <p class="mb-2"><a href="tel:+62215550123" class="item-anchor">%s</a></p>
          <p class="mb-2"><a href="mailto:%s" class="item-anchor">%s</a></p>
          <p class="mb-0">Senin - Jumat, 07.00 - 16.00 WIB</p>
        </div>
      </div>
    </div>
  </div>

  <div class="border-top py-4">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6">
          <p class="mb-0">&copy; 2026 %s. Seluruh hak cipta dilindungi.</p>
        </div>
        <div class="col-md-6 text-md-end">
          <p class="mb-0">Design by <a href="https://templatesjungle.com" target="_blank" rel="noopener">TemplatesJungle</a></p>
        </div>
      </div>
    </div>
  </div>
</footer>
""" % (BRAND_MARK, SCHOOL, TAGLINE, icon("instagram"), icon("facebook"), icon("youtube"), ADDRESS, PHONE, EMAIL, EMAIL, SCHOOL)


def head(title, description, og_image="images/hero-1.jpg"):
    return """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%s | %s</title>
  <meta name="description" content="%s">
  <meta name="keywords" content="%s, sekolah kejuruan, TKJ, RPL, DKV, akuntansi, PPDB, ekstrakurikuler">
  <meta name="author" content="%s">
  <meta property="og:title" content="%s | %s">
  <meta property="og:description" content="%s">
  <meta property="og:type" content="website">
  <meta property="og:image" content="%s">
  <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/fonts.css">
  <link rel="stylesheet" href="css/vendor.css">
  <link rel="stylesheet" href="css/swiper-bundle.min.css">
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="css/school.css">
</head>
<body>
""" % (title, SCHOOL, description, SCHOOL, SCHOOL, title, SCHOOL, description, og_image)


def scripts():
    return """
  <a href="#" class="btn btn-dark back-to-top" aria-label="Kembali ke atas">%s</a>
  <script src="js/jquery.min.js"></script>
  <script src="js/bootstrap.bundle.min.js"></script>
  <script src="js/swiper-bundle.min.js"></script>
  <script src="js/plugins.js"></script>
  <script src="js/school.js"></script>
</body>
</html>
""" % icon("arrow-up")


def page(title, description, active, body, og_image="images/hero-1.jpg"):
    return head(title, description, og_image) + navbar(active) + "\n<main>\n" + body + "\n</main>\n" + footer() + scripts()


def page_header(title, subtitle, crumb):
    return """
<section class="bg-light py-5">
  <div class="container">
    <div class="row justify-content-center text-center py-4">
      <div class="col-lg-8">
        <p class="text-uppercase fs-6 text-secondary mb-2">
          <a href="index.html" class="text-secondary text-decoration-none">Beranda</a> / %s
        </p>
        <h1 class="section-title mb-3">%s</h1>
        <p class="mb-0">%s</p>
      </div>
    </div>
  </div>
</section>
""" % (crumb, title, subtitle)


def section_heading(kicker, title, link_href=None, link_label=None):
    link = ""
    if link_href:
        link = '<a href="%s" class="btn-link">%s</a>' % (link_href, link_label)
    return """
      <div class="d-flex flex-wrap justify-content-between align-items-end gap-3 mt-4 mb-4">
        <div>
          <p class="text-uppercase fs-6 text-secondary mb-2">%s</p>
          <h2 class="section-title mb-0">%s</h2>
        </div>
        %s
      </div>
""" % (kicker, title, link)


def cta(title, text, href, label):
    return """
<section class="cta-band">
  <div class="container">
    <div class="row align-items-center justify-content-between g-4">
      <div class="col-lg-8">
        <h2 class="section-title">%s</h2>
        <p class="mb-0">%s</p>
      </div>
      <div class="col-lg-auto">
        <a href="%s" class="btn btn-dark btn-lg text-uppercase px-4">%s</a>
      </div>
    </div>
  </div>
</section>
""" % (title, text, href, label)


def stat(number, label, suffix="+", delay=0):
    # Angka final ditulis langsung di HTML agar tetap terbaca tanpa JavaScript.
    # js/school.js menganimasikan dari 0 saat elemen masuk layar.
    return """
        <div class="col-6 col-lg-3 text-center stat-item" data-aos="fade-up" data-aos-delay="%d">
          <div class="stat-number"><span data-count="%d">%d</span>%s</div>
          <div class="stat-label">%s</div>
        </div>
""" % (delay, number, number, suffix, label)


def feature(icon_name, title, text, delay=0):
    return """
        <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="%d">
          <div class="text-center py-4">
            <span class="d-inline-flex text-dark mb-3">%s</span>
            <h3 class="fs-5 text-uppercase mb-2">%s</h3>
            <p class="fs-6 mb-0">%s</p>
          </div>
        </div>
""" % (delay, icon(icon_name, 34), title, text)


def jurusan_card(img, title, desc, href, delay=0):
    return """
        <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="%d">
          <div class="cat-item image-zoom-effect">
            <div class="image-holder">
              <a href="%s"><img src="images/%s" alt="%s" class="jurusan-img img-fluid" loading="lazy"></a>
            </div>
            <div class="category-content">
              <h3 class="element-title text-uppercase fs-5 mt-3"><a href="%s">%s</a></h3>
              <p class="fs-6">%s</p>
              <a href="%s" class="btn-link">Lihat Jurusan &rarr;</a>
            </div>
          </div>
        </div>
""" % (delay, href, img, title, href, title, desc, href)


def post_card(img, category, date, title, excerpt, href, delay=0, searchable=True):
    search_attr = " data-news-item" if searchable else ""
    return """
        <div class="col-md-4"%s data-aos="fade-up" data-aos-delay="%d">
          <article class="post-item">
            <div class="post-image">
              <a href="%s"><img src="images/%s" alt="%s" class="post-grid-image img-fluid" loading="lazy"></a>
            </div>
            <div class="post-content d-flex flex-wrap gap-2 my-3">
              <div class="post-meta text-uppercase fs-6 text-secondary">
                <span class="post-category">%s /</span>
                <span class="meta-day">%s</span>
              </div>
              <h3 class="post-title text-uppercase fs-5"><a href="%s">%s</a></h3>
              <p>%s</p>
              <a href="%s" class="btn-link">Baca Selengkapnya &rarr;</a>
            </div>
          </article>
        </div>
""" % (search_attr, delay, href, img, title, category, date, href, title, excerpt, href)


def ekskul_card(img, title, category, desc, pembina, jadwal, delay=0):
    return """
        <div class="col-md-6 col-lg-4" data-category="%s" data-aos="fade-up" data-aos-delay="%d">
          <article class="post-item">
            <div class="post-image">
              <img src="images/%s" alt="%s" class="card-img-school img-fluid" loading="lazy">
            </div>
            <div class="post-content my-3">
              <p class="text-uppercase fs-6 text-secondary mb-1">%s</p>
              <h3 class="fs-4">%s</h3>
              <p>%s</p>
              <ul class="list-unstyled fs-6 text-secondary mb-0">
                <li><span class="text-dark">Pembina:</span> %s</li>
                <li><span class="text-dark">Jadwal:</span> %s</li>
              </ul>
            </div>
          </article>
        </div>
""" % (category, delay, img, title, category, title, desc, pembina, jadwal)


def gallery_item(img, title, category, delay=0):
    return """
        <div class="col-6 col-md-4 col-lg-3" data-category="%s" data-aos="fade-up" data-aos-delay="%d">
          <a href="images/%s" class="gallery-item" data-gallery data-img="images/%s" data-title="%s">
            <img src="images/%s" alt="%s" loading="lazy">
            <span class="gallery-overlay">%s</span>
          </a>
        </div>
""" % (category, delay, img, img, title, img, title, icon("zoom", 28))


def gallery_preview(img, title, delay=0):
    return """
        <div class="col-6 col-md-4 col-lg-2" data-aos="fade-up" data-aos-delay="%d">
          <a href="galeri.html" class="gallery-item">
            <img src="images/%s" alt="%s" loading="lazy">
            <span class="gallery-overlay">%s</span>
          </a>
        </div>
""" % (delay, img, title, icon("zoom", 28))


# ---------------------------------------------------------------------------
# BERANDA
# ---------------------------------------------------------------------------
def home_body():
    hero_slides = [
        ("images/hero-1.jpg", "Selamat Datang", SCHOOL,
         "Mencetak lulusan kompeten, berkarakter, dan siap bersaing di dunia industri."),
        ("images/hero-2.jpg", "Kompetensi Keahlian", "Belajar Sesuai Bidang yang Kamu Pilih",
         "TKJ, RPL, DKV, dan Akuntansi dengan pembelajaran berbasis praktik dan proyek nyata."),
        ("images/hero-3.jpg", "Fasilitas Belajar", "Lingkungan Belajar yang Nyaman",
         "Laboratorium komputer, studio desain, perpustakaan, dan ruang praktik yang lengkap."),
    ]
    slides = []
    for img, kicker, title, text in hero_slides:
        slides.append("""
      <div class="swiper-slide hero-slide" style="background-image: url('%s')">
        <div class="container">
          <div class="hero-caption">
            <p class="hero-kicker">%s</p>
            <p class="hero-title">%s</p>
            <p>%s</p>
            <div class="d-flex flex-wrap gap-3 mt-4">
              <a href="profil.html" class="btn btn-light btn-lg text-uppercase px-4">Profil Sekolah</a>
              <a href="kontak.html" class="btn btn-outline-light btn-lg text-uppercase px-4">Info PPDB</a>
            </div>
          </div>
        </div>
      </div>
""" % (img, kicker, title, text))

    return """
<h1 class="visually-hidden">%s - Beranda</h1>

<section class="hero-swiper swiper" aria-label="Sorotan sekolah">
  <div class="swiper-wrapper">%s
  </div>
  <div class="swiper-pagination"></div>
  <div class="icon-arrow icon-arrow-left"><svg width="50" height="50" viewBox="0 0 24 24"><path fill="currentColor" d="M17 11H9.41l3.3-3.29a1 1 0 1 0-1.42-1.42l-5 5a1 1 0 0 0-.21.33a1 1 0 0 0 0 .76a1 1 0 0 0 .21.33l5 5a1 1 0 0 0 1.42 0a1 1 0 0 0 0-1.42L9.41 13H17a1 1 0 0 0 0-2Z"/></svg></div>
  <div class="icon-arrow icon-arrow-right"><svg width="50" height="50" viewBox="0 0 24 24"><path fill="currentColor" d="M17.92 11.62a1 1 0 0 0-.21-.33l-5-5a1 1 0 0 0-1.42 1.42l3.3 3.29H7a1 1 0 0 0 0 2h7.59l-3.3 3.29a1 1 0 0 0 0 1.42a1 1 0 0 0 1.42 0l5-5a1 1 0 0 0 .21-.33a1 1 0 0 0 0-.76Z"/></svg></div>
</section>

<section class="py-5">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-5" data-aos="fade-up">
        <img src="images/kepala-sekolah.jpg" alt="%s, Kepala Sekolah" class="img-fluid w-100" style="max-height: 520px; object-fit: cover;" loading="lazy">
      </div>
      <div class="col-lg-7" data-aos="fade-up" data-aos-delay="200">
        <p class="text-uppercase fs-6 text-secondary mb-2">Sambutan Kepala Sekolah</p>
        <h2 class="section-title mb-3">Belajar Hari Ini, Berprestasi Esok Hari</h2>
        <p>Assalamualaikum warahmatullahi wabarakatuh. Selamat datang di %s. Kami berkomitmen menyiapkan generasi yang kompeten, berkarakter, dan siap menghadapi dunia kerja maupun melanjutkan pendidikan.</p>
        <p>Melalui pembelajaran berbasis praktik, kerja sama dengan industri, dan pembinaan karakter, kami percaya setiap siswa dapat tumbuh sesuai potensinya.</p>
        <a href="profil.html#sambutan" class="btn-link">Baca Selengkapnya &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="py-4 border-top border-bottom">
  <!-- TODO: ganti angka statistik di bawah dengan data resmi sekolah (guru, siswa, rombel, jurusan). -->
  <div class="container">
    <div class="row">%s%s%s%s
    </div>
  </div>
</section>

<section class="py-5">
  <div class="container">
    %s
    <div class="row g-4">%s%s%s%s
    </div>
  </div>
</section>

<section class="py-5 bg-light">
  <div class="container">
    %s
    <div class="row g-4">%s%s%s
      <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="300">
        <div class="cat-item image-zoom-effect">
          <div class="image-holder">
            <a href="ekstrakurikuler.html"><img src="images/ekskul-musik.jpg" alt="Ekstrakurikuler seni musik" class="jurusan-img img-fluid" loading="lazy"></a>
          </div>
          <div class="category-content">
            <h3 class="element-title text-uppercase fs-5 mt-3"><a href="ekstrakurikuler.html">Seni Musik</a></h3>
            <p class="fs-6">Menumbuhkan kreativitas dan keberanian tampil di panggung.</p>
            <a href="ekstrakurikuler.html" class="btn-link">Lihat Ekstrakurikuler &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="py-5">
  <div class="container">
    %s
    <div class="row g-4">%s%s%s
    </div>
  </div>
</section>

<section class="py-5 bg-light">
  <div class="container">
    %s
    <div class="row g-3">%s%s%s%s%s%s
    </div>
  </div>
</section>

<section class="testimonials py-5">
  <div class="section-header text-center mt-4">
    <p class="text-uppercase fs-6 text-secondary mb-2">Kata Mereka</p>
    <h2 class="section-title">Testimoni Alumni &amp; Siswa</h2>
  </div>
  <div class="swiper testimonial-swiper overflow-hidden my-5">
    <div class="swiper-wrapper d-flex">
      <div class="swiper-slide">
        <div class="testimonial-item text-center">
          <blockquote>
            <p>&ldquo;Bekal praktik di sekolah membuat saya percaya diri saat masuk dunia kerja.&rdquo;</p>
            <div class="review-title text-uppercase">Alumni RPL 2023 - Web Developer</div>
          </blockquote>
        </div>
      </div>
      <div class="swiper-slide">
        <div class="testimonial-item text-center">
          <blockquote>
            <p>&ldquo;Guru-gurunya suportif dan fasilitas laboratoriumnya lengkap.&rdquo;</p>
            <div class="review-title text-uppercase">Alumni TKJ 2022 - Teknisi Jaringan</div>
          </blockquote>
        </div>
      </div>
      <div class="swiper-slide">
        <div class="testimonial-item text-center">
          <blockquote>
            <p>&ldquo;Ekstrakurikuler robotik mengasah kemampuan problem solving saya.&rdquo;</p>
            <div class="review-title text-uppercase">Siswa Kelas XII RPL</div>
          </blockquote>
        </div>
      </div>
    </div>
  </div>
  <div class="testimonial-swiper-pagination d-flex justify-content-center mb-4"></div>
</section>

<section class="py-5">
  <div class="container">
    <div class="row align-items-center g-4">
      <div class="col-lg-3">
        <p class="text-uppercase fs-6 text-secondary mb-2">Mitra Industri</p>
        <h2 class="section-title mb-0">Belajar Langsung dari Dunia Kerja</h2>
      </div>
      <div class="col-lg-9">
        <div class="d-flex flex-wrap justify-content-between align-items-center gap-4">
          <span class="partner-name">PT Nusantara Teknologi</span>
          <span class="partner-name">CV Digital Kreatif</span>
          <span class="partner-name">Bank Cendekia</span>
          <span class="partner-name">PT Jaringan Mandiri</span>
          <span class="partner-name">Studio Visual Nusa</span>
        </div>
      </div>
    </div>
  </div>
</section>

%s
""" % (
        SCHOOL,
        "".join(slides),
        HEADMASTER,
        SCHOOL,
        stat(68, "Guru &amp; Tenaga Kependidikan"),
        stat(1240, "Siswa Aktif"),
        stat(36, "Rombongan Belajar", suffix=""),
        stat(4, "Kompetensi Keahlian", suffix=""),
        section_heading("Kompetensi Keahlian", "4 Jurusan Unggulan", "jurusan.html", "Semua Jurusan &rarr;"),
        jurusan_card("jurusan-tkj.jpg", "Teknik Komputer &amp; Jaringan", "Belajar jaringan, server, dan keamanan siber.", "jurusan.html#tkj", 0),
        jurusan_card("jurusan-rpl.jpg", "Rekayasa Perangkat Lunak", "Bangun aplikasi web dan mobile dari nol.", "jurusan.html#rpl", 100),
        jurusan_card("jurusan-dkv.jpg", "Desain Komunikasi Visual", "Kuasai desain grafis, ilustrasi, dan multimedia.", "jurusan.html#dkv", 200),
        jurusan_card("jurusan-akl.jpg", "Akuntansi &amp; Keuangan Lembaga", "Kelola laporan keuangan dan administrasi bisnis.", "jurusan.html#akl", 300),
        section_heading("Kegiatan Siswa", "Ekstrakurikuler Pilihan", "ekstrakurikuler.html", "Semua Ekstrakurikuler &rarr;"),
        ekskul_card("ekskul-pramuka.jpg", "Pramuka", "Kepemimpinan", "Membentuk disiplin, kemandirian, dan jiwa kepemimpinan.", "Kak Budi Santoso", "Jumat, 14.00 - 16.00", 0),
        ekskul_card("ekskul-futsal.jpg", "Futsal", "Olahraga", "Meningkatkan kebugaran, kerja sama tim, dan sportivitas.", "Coach Rizky Pratama", "Selasa &amp; Kamis, 15.30 - 17.00", 100),
        ekskul_card("ekskul-robotik.jpg", "Robotik", "Akademik", "Merancang robot sederhana dan mengikuti kompetisi teknologi.", "Ibu Dewi Lestari", "Sabtu, 09.00 - 12.00", 200),
        section_heading("Informasi Terbaru", "Berita &amp; Kegiatan Sekolah", "berita.html", "Semua Berita &rarr;"),
        post_card("berita-ppdb.jpg", "PPDB", "5 Januari 2026", "PPDB 2026/2027 Resmi Dibuka", "Pendaftaran gelombang pertama dibuka untuk calon siswa baru.", "berita-ppdb.html", 0),
        post_card("berita-lomba.jpg", "Prestasi", "22 Februari 2026", "Siswa RPL Raih Juara 1 Lomba Web Design", "Tim sekolah berhasil menyisihkan puluhan peserta dari seluruh Indonesia.", "berita-lomba.html", 100),
        post_card("berita-industri.jpg", "Kegiatan", "18 Maret 2026", "Kunjungan Industri ke PT Nusantara Teknologi", "Siswa kelas XI belajar langsung tentang proses kerja di industri.", "berita-kunjungan-industri.html", 200),
        section_heading("Galeri", "Momen Kegiatan Sekolah", "galeri.html", "Buka Galeri &rarr;"),
        gallery_preview("galeri-1.jpg", "Kegiatan belajar di kelas", 0),
        gallery_preview("galeri-2.jpg", "Seminar motivasi siswa", 50),
        gallery_preview("galeri-3.jpg", "Kerja kelompok di perpustakaan", 100),
        gallery_preview("galeri-5.jpg", "Diskusi kelompok", 150),
        gallery_preview("galeri-10.jpg", "Praktik komputer", 200),
        gallery_preview("galeri-9.jpg", "Wisuda siswa", 250),
        cta("Siap Bergabung Bersama Kami?", "Daftarkan dirimu pada penerimaan siswa baru atau hubungi kami untuk informasi lebih lanjut.", "kontak.html", "Hubungi Kami"),
    )


# ---------------------------------------------------------------------------
# PROFIL
# ---------------------------------------------------------------------------
def profil_body():
    return """
%s
<section id="sambutan" class="py-5">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-5" data-aos="fade-up">
        <img src="images/kepala-sekolah.jpg" alt="%s, Kepala Sekolah" class="img-fluid w-100" style="max-height: 520px; object-fit: cover;" loading="lazy">
      </div>
      <div class="col-lg-7" data-aos="fade-up" data-aos-delay="200">
        <p class="text-uppercase fs-6 text-secondary mb-2">Sambutan Kepala Sekolah</p>
        <h2 class="section-title mb-3">Menyiapkan Generasi Siap Kerja</h2>
        <p>Assalamualaikum warahmatullahi wabarakatuh. Selamat datang di %s. Kami berkomitmen menyiapkan lulusan yang kompeten, berkarakter, dan mampu bersaing di dunia industri maupun melanjutkan pendidikan ke jenjang yang lebih tinggi.</p>
        <p>Pembelajaran di sekolah kami dirancang berbasis praktik dan proyek nyata. Dukungan guru profesional, laboratorium lengkap, serta kemitraan dengan industri menjadi bagian penting dari proses belajar siswa.</p>
        <p class="mb-0">Kami mengajak seluruh siswa, orang tua, dan mitra untuk bersama-sama membangun lingkungan belajar yang positif dan berprestasi.</p>
      </div>
    </div>
  </div>
</section>

<section id="sejarah" class="py-5 bg-light">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-6" data-aos="fade-up">
        <p class="text-uppercase fs-6 text-secondary mb-2">Tentang Kami</p>
        <h2 class="section-title mb-3">Sejarah Singkat</h2>
        <p>%s berdiri pada tahun 1998 sebagai sekolah menengah kejuruan yang berfokus pada kebutuhan tenaga kerja terampil. Sejak awal, sekolah tumbuh bersama perkembangan teknologi dan kebutuhan industri di sekitar wilayah.</p>
        <p>Kini sekolah memiliki empat kompetensi keahlian, fasilitas praktik yang lengkap, serta jaringan mitra industri yang aktif. Berbagai prestasi akademik dan non-akademik terus diukir oleh siswa dan guru.</p>
      </div>
      <div class="col-lg-6" data-aos="fade-up" data-aos-delay="200">
        <p class="text-uppercase fs-6 text-secondary mb-2">Fokus Pendidikan</p>
        <h2 class="section-title mb-3">Keunggulan Sekolah</h2>
        <div class="row g-3">
          %s
          %s
          %s
          %s
        </div>
      </div>
    </div>
  </div>
</section>

<section id="visi-misi" class="py-5">
  <div class="container">
    <div class="row g-5 align-items-start">
      <div class="col-lg-5" data-aos="fade-up">
        <p class="text-uppercase fs-6 text-secondary mb-2">Arah Lembaga</p>
        <h2 class="section-title mb-3">Visi &amp; Misi</h2>
        <div class="bg-light p-4 p-lg-5">
          <h3 class="fs-5 text-uppercase mb-3">Visi</h3>
          <p class="mb-0">Menjadi sekolah kejuruan unggul yang menghasilkan lulusan kompeten, berkarakter, dan berdaya saing global.</p>
        </div>
      </div>
      <div class="col-lg-7" data-aos="fade-up" data-aos-delay="200">
        <h3 class="fs-5 text-uppercase mb-3">Misi</h3>
        <ol class="fs-6">
          <li>Menyelenggarakan pembelajaran berbasis kompetensi dan praktik kerja nyata.</li>
          <li>Mengembangkan karakter siswa yang religius, disiplin, dan bertanggung jawab.</li>
          <li>Meningkatkan kualitas guru dan tenaga kependidikan secara berkelanjutan.</li>
          <li>Membangun kerja sama yang aktif dengan dunia usaha dan dunia industri.</li>
          <li>Mendorong lahirnya inovasi, prestasi, dan budaya kerja profesional.</li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section id="struktur" class="py-5 bg-light">
  <div class="container">
    <div class="text-center mb-4" data-aos="fade-up">
      <p class="text-uppercase fs-6 text-secondary mb-2">Organisasi</p>
      <h2 class="section-title mb-0">Struktur Sekolah</h2>
    </div>
    <div class="row g-4">
      <div class="col-md-6 col-lg-3" data-aos="fade-up">
        <div class="bg-white h-100 p-4 text-center">
          <h3 class="fs-5 mb-1">Kepala Sekolah</h3>
          <p class="fs-6 mb-0">%s</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="100">
        <div class="bg-white h-100 p-4 text-center">
          <h3 class="fs-5 mb-1">Wakasek Kurikulum</h3>
          <p class="fs-6 mb-0">Ibu Ratna Sari, S.Pd., M.Pd.</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="200">
        <div class="bg-white h-100 p-4 text-center">
          <h3 class="fs-5 mb-1">Wakasek Kesiswaan</h3>
          <p class="fs-6 mb-0">Bapak Andi Wijaya, S.Pd.</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="300">
        <div class="bg-white h-100 p-4 text-center">
          <h3 class="fs-5 mb-1">Wakasek Sarana</h3>
          <p class="fs-6 mb-0">Bapak Hendra Gunawan, S.T.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="tabel-profil" class="py-5">
  <div class="container">
    <div class="row g-4 mb-4">
      <div class="col-lg-8" data-aos="fade-up">
        <p class="text-uppercase fs-6 text-secondary mb-2">Data Resmi</p>
        <h2 class="section-title mb-0">Tabel Informasi Profil Sekolah</h2>
      </div>
    </div>
    <!-- TODO: ganti seluruh data pada tabel ini (NPSN, akreditasi, alamat, jumlah guru/siswa, dll) dengan data resmi sekolah. -->
    <div class="table-responsive" data-aos="fade-up" data-aos-delay="100">
      <table class="table table-bordered align-middle profile-table mb-0">
        <tbody>
          <tr><th scope="row">Nama Sekolah</th><td>%s</td></tr>
          <tr><th scope="row">NPSN</th><td>12345678</td></tr>
          <tr><th scope="row">Status</th><td>Negeri</td></tr>
          <tr><th scope="row">Akreditasi</th><td>A (Unggul)</td></tr>
          <tr><th scope="row">Kurikulum</th><td>Kurikulum Merdeka</td></tr>
          <tr><th scope="row">Tahun Berdiri</th><td>1998</td></tr>
          <tr><th scope="row">Kepala Sekolah</th><td>%s</td></tr>
          <tr><th scope="row">Alamat</th><td>%s</td></tr>
          <tr><th scope="row">Telepon</th><td>%s</td></tr>
          <tr><th scope="row">Email</th><td>%s</td></tr>
          <tr><th scope="row">Jumlah Guru</th><td>68 orang</td></tr>
          <tr><th scope="row">Jumlah Siswa</th><td>1.240 siswa</td></tr>
          <tr><th scope="row">Jumlah Rombel</th><td>36 rombongan belajar</td></tr>
          <tr><th scope="row">Kompetensi Keahlian</th><td>TKJ, RPL, DKV, Akuntansi dan Keuangan Lembaga</td></tr>
          <tr><th scope="row">Jam Layanan</th><td>Senin - Jumat, 07.00 - 16.00 WIB</td></tr>
        </tbody>
      </table>
    </div>
    <p class="fs-6 text-secondary mt-3 mb-0">Catatan: data di atas adalah contoh. Ganti dengan data resmi sekolah sebelum dipublikasikan.</p>
  </div>
</section>

<section id="fasilitas" class="py-5 bg-light">
  <div class="container">
    %s
    <div class="row g-4">
      <div class="col-md-6 col-lg-3" data-aos="fade-up">
        <div class="post-item">
          <img src="images/galeri-10.jpg" alt="Laboratorium komputer" class="card-img-school img-fluid" loading="lazy">
          <h3 class="fs-5 mt-3 mb-1">Laboratorium Komputer</h3>
          <p class="fs-6 mb-0">Ruang praktik dengan perangkat modern untuk jurusan TKJ dan RPL.</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="100">
        <div class="post-item">
          <img src="images/galeri-4.jpg" alt="Perpustakaan sekolah" class="card-img-school img-fluid" loading="lazy">
          <h3 class="fs-5 mt-3 mb-1">Perpustakaan</h3>
          <p class="fs-6 mb-0">Koleksi buku pelajaran, referensi, dan ruang baca yang nyaman.</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="200">
        <div class="post-item">
          <img src="images/jurusan-dkv.jpg" alt="Studio desain komunikasi visual" class="card-img-school img-fluid" loading="lazy">
          <h3 class="fs-5 mt-3 mb-1">Studio DKV</h3>
          <p class="fs-6 mb-0">Studio desain untuk praktik grafis, ilustrasi, dan multimedia.</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="300">
        <div class="post-item">
          <img src="images/ekskul-futsal.jpg" alt="Lapangan olahraga sekolah" class="card-img-school img-fluid" loading="lazy">
          <h3 class="fs-5 mt-3 mb-1">Lapangan Olahraga</h3>
          <p class="fs-6 mb-0">Area olahraga untuk kegiatan belajar, ekstrakurikuler, dan upacara.</p>
        </div>
      </div>
    </div>
  </div>
</section>

%s
""" % (
        page_header("Profil Sekolah", "Mengenal lebih dekat identitas, arah, dan fasilitas %s." % SCHOOL, "Profil Sekolah"),
        HEADMASTER,
        SCHOOL,
        SCHOOL,
        feature("book", "Kurikulum Praktik", "Belajar melalui proyek dan praktik langsung.", 0),
        feature("flask", "Laboratorium", "Fasilitas praktik sesuai bidang keahlian.", 100),
        feature("user", "Guru Profesional", "Tenaga pendidik berpengalaman di bidangnya.", 200),
        feature("briefcase", "Mitra Industri", "Kemitraan aktif untuk magang dan karier.", 300),
        HEADMASTER,
        SCHOOL,
        HEADMASTER,
        ADDRESS,
        PHONE,
        EMAIL,
        section_heading("Sarana Prasarana", "Fasilitas Pendukung Belajar", "kontak.html", "Hubungi Kami"),
        cta("Ingin Mengenal Sekolah Lebih Dekat?", "Kunjungi sekolah kami atau hubungi panitia untuk informasi profil dan penerimaan siswa baru.", "kontak.html", "Hubungi Kami"),
    )


# ---------------------------------------------------------------------------
# JURUSAN
# ---------------------------------------------------------------------------
def jurusan_body():
    jurusan = [
        (
            "tkj", "Teknik Komputer &amp; Jaringan",
            "Mempelajari instalasi jaringan, administrasi server, keamanan siber, dan layanan internet.",
            ["Network Engineer", "Teknisi Jaringan", "Administrator Server", "Cyber Security Analyst"],
            ["Laboratorium jaringan", "Perangkat router & switch", "Praktik fiber optik"],
            "jurusan-tkj.jpg",
        ),
        (
            "rpl", "Rekayasa Perangkat Lunak",
            "Mempelajari pemrograman web, mobile, basis data, dan pengembangan aplikasi secara terstruktur.",
            ["Web Developer", "Mobile Developer", "Quality Assurance", "Data Analyst"],
            ["Laboratorium pemrograman", "Server pengembangan", "Praktik proyek aplikasi"],
            "jurusan-rpl.jpg",
        ),
        (
            "dkv", "Desain Komunikasi Visual",
            "Mempelajari desain grafis, ilustrasi, fotografi, videografi, dan desain antarmuka.",
            ["Graphic Designer", "UI/UX Designer", "Animator", "Video Editor"],
            ["Studio desain", "Komputer grafis", "Kamera & perangkat produksi"],
            "jurusan-dkv.jpg",
        ),
        (
            "akl", "Akuntansi &amp; Keuangan Lembaga",
            "Mempelajari pencatatan keuangan, perpajakan, administrasi, dan pengelolaan laporan keuangan.",
            ["Staff Akuntansi", "Teller Bank", "Staff Pajak", "Wirausaha"],
            ["Laboratorium akuntansi", "Software akuntansi", "Praktik administrasi"],
            "jurusan-akl.jpg",
        ),
    ]

    tabs = []
    panes = []
    for index, (slug, name, desc, careers, facilities, img) in enumerate(jurusan):
        active = " active" if index == 0 else ""
        selected = "true" if index == 0 else "false"
        tabs.append(
            '<li class="nav-item" role="presentation">'
            '<button class="nav-link%s" id="%s-tab" data-bs-toggle="tab" data-bs-target="#%s" type="button" role="tab" aria-controls="%s" aria-selected="%s">%s</button>'
            "</li>" % (active, slug, slug, slug, selected, name)
        )

        career_list = "".join("<li>%s</li>" % item for item in careers)
        facility_list = "".join("<li>%s</li>" % item for item in facilities)
        panes.append("""
      <div class="tab-pane fade%s" id="%s" role="tabpanel" aria-labelledby="%s-tab" tabindex="0">
        <div class="row align-items-center g-5">
          <div class="col-lg-5">
            <img src="images/%s" alt="Jurusan %s" class="img-fluid w-100 jurusan-img" loading="lazy">
          </div>
          <div class="col-lg-7">
            <p class="text-uppercase fs-6 text-secondary mb-2">Kompetensi Keahlian</p>
            <h2 class="section-title mb-3">%s</h2>
            <p>%s</p>
            <div class="row g-4 mt-1">
              <div class="col-md-6">
                <h3 class="fs-5 text-uppercase mb-2">Prospek Karier</h3>
                <ul class="fs-6">%s</ul>
              </div>
              <div class="col-md-6">
                <h3 class="fs-5 text-uppercase mb-2">Fasilitas Praktik</h3>
                <ul class="fs-6">%s</ul>
              </div>
            </div>
            <a href="kontak.html" class="btn btn-dark text-uppercase px-4 mt-2">Tanya Jurusan Ini</a>
          </div>
        </div>
      </div>
""" % (active, slug, slug, img, name, name, desc, career_list, facility_list))

    return """
%s
<section class="py-5">
  <div class="container">
    <div class="row justify-content-center text-center mb-4" data-aos="fade-up">
      <div class="col-lg-8">
        <p class="text-uppercase fs-6 text-secondary mb-2">Pilih Jalurmu</p>
        <h2 class="section-title mb-3">Empat Kompetensi Keahlian</h2>
        <p class="mb-0">Setiap jurusan dirancang agar siswa memiliki keterampilan praktis, pemahaman teori, dan pengalaman proyek nyata.</p>
      </div>
    </div>
    <ul class="nav nav-tabs jurusan-tabs justify-content-center mb-5" id="jurusanTab" role="tablist">
      %s
    </ul>
    <div class="tab-content" id="jurusanTabContent">
      %s
    </div>
  </div>
</section>

%s
""" % (
        page_header("Kompetensi Keahlian", "Empat jurusan dengan pembelajaran berbasis praktik dan kebutuhan industri.", "Jurusan"),
        "".join(tabs),
        "".join(panes),
        cta("Belum Yakin Memilih Jurusan?", "Konsultasikan minat dan bakatmu dengan guru bimbingan konseling atau hubungi kami.", "kontak.html", "Konsultasi"),
    )


# ---------------------------------------------------------------------------
# EKSTRAKURIKULER
# ---------------------------------------------------------------------------
def ekstrakurikuler_body():
    return """
%s
<section class="py-5">
  <div class="container">
    <div class="row justify-content-center text-center mb-4" data-aos="fade-up">
      <div class="col-lg-8">
        <p class="text-uppercase fs-6 text-secondary mb-2">Kembangkan Minat</p>
        <h2 class="section-title mb-3">Ekstrakurikuler Sekolah</h2>
        <p class="mb-0">Pilih kegiatan yang sesuai dengan minatmu. Setiap ekstrakurikuler dibimbing oleh pembina dan memiliki jadwal rutin.</p>
      </div>
    </div>

    <div class="d-flex justify-content-center mb-5" data-filter-group data-filter-target="#ekskul-grid">
      <div class="filter-group">
        <a href="#" class="btn-link is-checked" data-filter="all">Semua</a>
        <a href="#" class="btn-link" data-filter="Kepemimpinan">Kepemimpinan</a>
        <a href="#" class="btn-link" data-filter="Olahraga">Olahraga</a>
        <a href="#" class="btn-link" data-filter="Akademik">Akademik</a>
        <a href="#" class="btn-link" data-filter="Sosial">Sosial</a>
        <a href="#" class="btn-link" data-filter="Seni">Seni</a>
      </div>
    </div>

    <!-- TODO: sesuaikan nama ekstrakurikuler, pembina, dan jadwal dengan data sekolah. -->
    <div class="row g-4" id="ekskul-grid">
      %s
      %s
      %s
      %s
      %s
      %s
    </div>
  </div>
</section>

%s
""" % (
        page_header("Ekstrakurikuler", "Wadah untuk mengembangkan bakat, minat, dan karakter siswa di luar jam pelajaran.", "Ekstrakurikuler"),
        ekskul_card("ekskul-pramuka.jpg", "Pramuka", "Kepemimpinan", "Membentuk disiplin, kemandirian, dan jiwa kepemimpinan melalui kegiatan alam dan sosial.", "Kak Budi Santoso", "Jumat, 14.00 - 16.00", 0),
        ekskul_card("ekskul-futsal.jpg", "Futsal", "Olahraga", "Meningkatkan kebugaran, kerja sama tim, dan sportivitas melalui latihan rutin.", "Coach Rizky Pratama", "Selasa &amp; Kamis, 15.30 - 17.00", 100),
        ekskul_card("ekskul-robotik.jpg", "Robotik", "Akademik", "Merancang robot sederhana, belajar pemrograman, dan mengikuti kompetisi teknologi.", "Ibu Dewi Lestari", "Sabtu, 09.00 - 12.00", 200),
        ekskul_card("ekskul-paskibra.jpg", "Paskibra", "Kepemimpinan", "Melatih kedisiplinan, kekompakan, dan rasa tanggung jawab dalam upacara bendera.", "Bapak Andi Wijaya", "Rabu, 14.00 - 16.00", 300),
        ekskul_card("ekskul-pmr.jpg", "Palang Merah Remaja", "Sosial", "Belajar pertolongan pertama, kesehatan, dan kegiatan sosial kemanusiaan.", "Ibu Siti Aminah", "Jumat, 14.00 - 15.30", 400),
        ekskul_card("ekskul-musik.jpg", "Seni Musik", "Seni", "Menumbuhkan kreativitas dan keberanian tampil melalui latihan vokal dan instrumen.", "Bapak Rudi Hartono", "Sabtu, 10.00 - 12.00", 500),
        cta("Punya Minat Lain?", "Sampaikan ide kegiatanmu kepada pembina kesiswaan. Kami terbuka untuk mengembangkan ekstrakurikuler baru.", "kontak.html", "Hubungi Sekolah"),
    )


# ---------------------------------------------------------------------------
# GALERI
# ---------------------------------------------------------------------------
def galeri_body():
    items = [
        ("galeri-1.jpg", "Kegiatan belajar di kelas", "Kegiatan", 0),
        ("galeri-2.jpg", "Seminar motivasi siswa", "Kegiatan", 50),
        ("galeri-3.jpg", "Kerja kelompok di perpustakaan", "Kegiatan", 100),
        ("galeri-4.jpg", "Perpustakaan sekolah", "Fasilitas", 150),
        ("galeri-5.jpg", "Diskusi kelompok", "Kegiatan", 200),
        ("galeri-6.jpg", "Laboratorium sains", "Fasilitas", 250),
        ("galeri-7.jpg", "Ruang baca", "Fasilitas", 300),
        ("galeri-8.jpg", "Kegiatan siswa", "Kegiatan", 350),
        ("galeri-9.jpg", "Wisuda siswa", "Prestasi", 400),
        ("galeri-10.jpg", "Praktik komputer", "Kegiatan", 450),
        ("galeri-11.jpg", "Koleksi buku perpustakaan", "Fasilitas", 500),
        ("galeri-12.jpg", "Kelulusan siswa", "Prestasi", 550),
    ]
    cards = "".join(gallery_item(img, title, category, delay) for img, title, category, delay in items)

    return """
%s
<section class="py-5">
  <div class="container">
    <div class="row justify-content-center text-center mb-4" data-aos="fade-up">
      <div class="col-lg-8">
        <p class="text-uppercase fs-6 text-secondary mb-2">Dokumentasi</p>
        <h2 class="section-title mb-3">Galeri Kegiatan</h2>
        <p class="mb-0">Kumpulan momen belajar, kegiatan siswa, fasilitas, dan prestasi sekolah.</p>
      </div>
    </div>

    <div class="d-flex justify-content-center mb-5" data-filter-group data-filter-target="#galeri-grid">
      <div class="filter-group">
        <a href="#" class="btn-link is-checked" data-filter="all">Semua</a>
        <a href="#" class="btn-link" data-filter="Kegiatan">Kegiatan</a>
        <a href="#" class="btn-link" data-filter="Fasilitas">Fasilitas</a>
        <a href="#" class="btn-link" data-filter="Prestasi">Prestasi</a>
      </div>
    </div>

    <div class="row g-3" id="galeri-grid">
      %s
    </div>
  </div>
</section>

<div class="modal fade" id="galleryModal" tabindex="-1" aria-labelledby="galleryModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title fs-5" id="galleryModalLabel" data-gallery-title></h2>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button>
      </div>
      <div class="modal-body p-0">
        <img src="images/galeri-1.jpg" alt="Foto kegiatan sekolah" class="w-100" data-gallery-image>
      </div>
    </div>
  </div>
</div>

%s
""" % (
        page_header("Galeri", "Melihat lebih dekat kegiatan belajar, fasilitas, dan prestasi siswa.", "Galeri"),
        cards,
        cta("Ingin Mengabadikan Momen Lain?", "Ikuti kegiatan sekolah dan bagikan dokumentasinya kepada tim humas.", "kontak.html", "Hubungi Kami"),
    )


# ---------------------------------------------------------------------------
# BERITA
# ---------------------------------------------------------------------------
def berita_body():
    return """
%s
<section class="py-5">
  <div class="container">
    <div class="row justify-content-center text-center mb-4" data-aos="fade-up">
      <div class="col-lg-8">
        <p class="text-uppercase fs-6 text-secondary mb-2">Informasi Sekolah</p>
        <h2 class="section-title mb-3">Berita &amp; Pengumuman</h2>
        <p class="mb-0">Ikuti kabar terbaru seputar kegiatan, prestasi, dan informasi penting sekolah.</p>
      </div>
    </div>

    <div class="row justify-content-center mb-5" data-aos="fade-up">
      <div class="col-lg-6">
        <label for="news-search" class="visually-hidden">Cari berita</label>
        <input type="search" id="news-search" class="form-control form-control-lg" placeholder="Cari berita atau pengumuman...">
      </div>
    </div>

    <p id="news-empty" class="text-center text-secondary d-none">Berita tidak ditemukan.</p>

    <!-- TODO: ganti kartu berita dan pengumuman dengan berita asli sekolah. -->
    <div class="row g-4">
      %s
      %s
      %s
    </div>

    <div class="row mt-5">
      <div class="col-lg-8" data-aos="fade-up">
        <h2 class="section-title mb-3">Pengumuman Singkat</h2>
        <ul class="list-unstyled fs-6">
          <li class="border-bottom py-3"><span class="text-secondary text-uppercase fs-6">2 April 2026 /</span> Workshop literasi digital untuk guru dan tenaga kependidikan.</li>
          <li class="border-bottom py-3"><span class="text-secondary text-uppercase fs-6">2 Mei 2026 /</span> Peringatan Hari Pendidikan Nasional di lapangan sekolah.</li>
          <li class="border-bottom py-3"><span class="text-secondary text-uppercase fs-6">12 Mei 2026 /</span> Pengumuman jadwal ujian akhir semester genap.</li>
        </ul>
      </div>
      <div class="col-lg-4" data-aos="fade-up" data-aos-delay="200">
        <div class="bg-light p-4">
          <h2 class="fs-5 text-uppercase mb-3">Agenda Terdekat</h2>
          <ul class="list-unstyled fs-6 mb-0">
            <li class="mb-3"><span class="text-dark">18 Mei 2026</span><br>Ujian Akhir Semester</li>
            <li class="mb-3"><span class="text-dark">25 Mei 2026</span><br>Pentas Seni Siswa</li>
            <li><span class="text-dark">1 Juni 2026</span><br>Libur Hari Lahir Pancasila</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

%s
""" % (
        page_header("Berita", "Kabar terbaru seputar kegiatan, prestasi, dan pengumuman sekolah.", "Berita"),
        post_card("berita-ppdb.jpg", "PPDB", "5 Januari 2026", "PPDB 2026/2027 Resmi Dibuka", "Pendaftaran gelombang pertama dibuka untuk calon siswa baru.", "berita-ppdb.html", 0),
        post_card("berita-lomba.jpg", "Prestasi", "22 Februari 2026", "Siswa RPL Raih Juara 1 Lomba Web Design", "Tim sekolah berhasil menyisihkan puluhan peserta dari seluruh Indonesia.", "berita-lomba.html", 100),
        post_card("berita-industri.jpg", "Kegiatan", "18 Maret 2026", "Kunjungan Industri ke PT Nusantara Teknologi", "Siswa kelas XI belajar langsung tentang proses kerja di industri.", "berita-kunjungan-industri.html", 200),
        cta("Jangan Lewatkan Informasi Penting", "Ikuti kanal resmi sekolah agar tidak ketinggalan pengumuman terbaru.", "kontak.html", "Hubungi Kami"),
    )


# ---------------------------------------------------------------------------
# ARTIKEL BERITA
# ---------------------------------------------------------------------------
def article_body(category, date, title, img, paragraphs, points):
    point_list = "".join("<li>%s</li>" % point for point in points)
    body_paragraphs = "".join("<p>%s</p>" % paragraph for paragraph in paragraphs)

    return """
<section class="py-5">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-9">
        <p class="text-uppercase fs-6 text-secondary mb-2">
          <a href="berita.html" class="text-secondary text-decoration-none">Berita</a> / %s / %s
        </p>
        <h1 class="section-title mb-3">%s</h1>
        <p class="fs-6 text-secondary mb-4">Ditulis oleh Tim Humas %s</p>
        <img src="images/%s" alt="%s" class="article-hero img-fluid mb-4" loading="lazy">
        %s
        <h2 class="fs-4 text-uppercase mt-4 mb-3">Poin Penting</h2>
        <ul class="fs-6">%s</ul>
        <div class="d-flex flex-wrap gap-3 mt-4">
          <a href="berita.html" class="btn btn-dark text-uppercase px-4">Kembali ke Berita</a>
          <a href="kontak.html" class="btn btn-outline-dark text-uppercase px-4">Hubungi Kami</a>
        </div>
      </div>
    </div>
  </div>
</section>

%s
""" % (
        category,
        date,
        title,
        SCHOOL,
        img,
        title,
        body_paragraphs,
        point_list,
        cta("Ingin Tahu Informasi Lainnya?", "Lihat berita dan pengumuman lain di halaman berita sekolah.", "berita.html", "Semua Berita &rarr;"),
    )


# ---------------------------------------------------------------------------
# KONTAK
# ---------------------------------------------------------------------------
def kontak_body():
    return """
%s
<section class="py-5">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-5" data-aos="fade-up">
        <p class="text-uppercase fs-6 text-secondary mb-2">Hubungi Kami</p>
        <h2 class="section-title mb-3">Informasi Kontak</h2>
        <p>Kami siap membantu pertanyaan seputar penerimaan siswa baru, kerja sama industri, atau informasi sekolah lainnya.</p>
        <!-- TODO: ganti alamat, telepon, WhatsApp, email, dan jam layanan dengan data resmi sekolah. -->
        <ul class="contact-info-list fs-6">
          <li>%s<div><span class="text-dark d-block">Alamat</span>%s</div></li>
          <li>%s<div><span class="text-dark d-block">Telepon</span><a href="tel:+62215550123">%s</a></div></li>
          <li>%s<div><span class="text-dark d-block">WhatsApp</span><a href="https://wa.me/6281234567890">%s</a></div></li>
          <li>%s<div><span class="text-dark d-block">Email</span><a href="mailto:%s">%s</a></div></li>
          <li>%s<div><span class="text-dark d-block">Jam Layanan</span>Senin - Jumat, 07.00 - 16.00 WIB</div></li>
        </ul>
      </div>

      <div class="col-lg-7" data-aos="fade-up" data-aos-delay="200">
        <p class="text-uppercase fs-6 text-secondary mb-2">Formulir</p>
        <h2 class="section-title mb-3">Kirim Pesan</h2>
        <div class="alert alert-success d-none" id="form-success" role="alert">
          Terima kasih. Pesanmu sudah terkirim (demo). Sambungkan form ke Google Forms atau Formspree untuk penggunaan nyata.
        </div>
        <!--
          TODO: HUBUNGKAN FORM KE GOOGLE FORMS (static hosting).
          1. Buat Google Form dengan field: Nama, Email, Telepon, Subjek, Pesan.
          2. Ganti nama input di bawah menjadi entry.xxxxx sesuai Google Form.
          3. Isi data-endpoint dengan:
             https://docs.google.com/forms/d/e/<ID_FORM>/formResponse
             lalu aktifkan pengiriman fetch di js/school.js (fungsi initContactForm).
          Selama endpoint kosong, form hanya menampilkan pesan sukses demo.
        -->
        <form class="row g-3 needs-validation" id="contact-form" method="post" data-endpoint="" novalidate>
          <div class="col-md-6">
            <label for="nama" class="form-label fs-6">Nama Lengkap</label>
            <input type="text" class="form-control" id="nama" name="nama" required>
            <div class="invalid-feedback">Nama wajib diisi.</div>
          </div>
          <div class="col-md-6">
            <label for="email" class="form-label fs-6">Email</label>
            <input type="email" class="form-control" id="email" name="email" required>
            <div class="invalid-feedback">Email wajib diisi dengan format yang benar.</div>
          </div>
          <div class="col-md-6">
            <label for="telepon" class="form-label fs-6">Nomor Telepon</label>
            <input type="tel" class="form-control" id="telepon" name="telepon" required>
            <div class="invalid-feedback">Nomor telepon wajib diisi.</div>
          </div>
          <div class="col-md-6">
            <label for="subjek" class="form-label fs-6">Subjek</label>
            <select class="form-select" id="subjek" name="subjek" required>
              <option value="" selected disabled>Pilih subjek</option>
              <option value="PPDB">Penerimaan Siswa Baru</option>
              <option value="Kerja Sama">Kerja Sama Industri</option>
              <option value="Informasi Umum">Informasi Umum</option>
            </select>
            <div class="invalid-feedback">Pilih salah satu subjek.</div>
          </div>
          <div class="col-12">
            <label for="pesan" class="form-label fs-6">Pesan</label>
            <textarea class="form-control" id="pesan" name="pesan" rows="5" required></textarea>
            <div class="invalid-feedback">Pesan wajib diisi.</div>
          </div>
          <div class="col-12">
            <button type="submit" class="btn btn-dark btn-lg text-uppercase px-4">Kirim Pesan</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="pb-5">
  <!-- TODO: ganti koordinat/lokasi pada iframe peta dengan lokasi sekolah yang sebenarnya. -->
  <div class="container">
    <div class="ratio ratio-21x9">
      <iframe
        src="https://maps.google.com/maps?q=Jl.+Pendidikan+Raya+No.+45,+Jakarta&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"
        title="Peta lokasi sekolah"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        style="border:0;"></iframe>
    </div>
  </div>
</section>
""" % (
        page_header("Kontak", "Hubungi sekolah untuk informasi penerimaan siswa baru, kerja sama, atau pertanyaan umum.", "Kontak"),
        icon("pin", 22),
        ADDRESS,
        icon("phone", 22),
        PHONE,
        icon("phone", 22),
        WHATSAPP,
        icon("mail", 22),
        EMAIL,
        EMAIL,
        icon("clock", 22),
    )


# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------
def not_found_body():
    return """
<section class="py-5">
  <div class="container">
    <div class="row justify-content-center text-center py-5">
      <div class="col-lg-7">
        <p class="text-uppercase fs-6 text-secondary mb-2">Halaman Tidak Ditemukan</p>
        <h1 class="section-title" style="font-size: clamp(4rem, 12vw, 8rem); line-height: 1;">404</h1>
        <p class="mb-4">Maaf, halaman yang kamu cari tidak tersedia atau sudah dipindahkan.</p>
        <a href="index.html" class="btn btn-dark btn-lg text-uppercase px-4">Kembali ke Beranda</a>
      </div>
    </div>
  </div>
</section>
""" % ()


# ---------------------------------------------------------------------------
# GENERATE
# ---------------------------------------------------------------------------
PAGES = [
    ("index.html", "Beranda", f"Website resmi {SCHOOL}: profil, jurusan, ekstrakurikuler, galeri, berita, dan kontak.", "index.html", home_body(), "images/hero-1.jpg"),
    ("profil.html", "Profil Sekolah", f"Profil, sejarah, visi-misi, struktur, tabel informasi, dan fasilitas {SCHOOL}.", "profil.html", profil_body(), "images/hero-1.jpg"),
    ("jurusan.html", "Kompetensi Keahlian", f"Empat kompetensi keahlian {SCHOOL}: TKJ, RPL, DKV, dan Akuntansi.", "jurusan.html", jurusan_body(), "images/jurusan-rpl.jpg"),
    ("ekstrakurikuler.html", "Ekstrakurikuler", f"Daftar ekstrakurikuler {SCHOOL} beserta pembina dan jadwal kegiatan.", "ekstrakurikuler.html", ekstrakurikuler_body(), "images/ekskul-pramuka.jpg"),
    ("galeri.html", "Galeri", f"Galeri foto kegiatan, fasilitas, dan prestasi {SCHOOL}.", "galeri.html", galeri_body(), "images/galeri-1.jpg"),
    ("berita.html", "Berita", f"Berita dan pengumuman terbaru {SCHOOL}.", "berita.html", berita_body(), "images/berita-ppdb.jpg"),
    ("kontak.html", "Kontak", f"Alamat, telepon, email, peta, dan formulir kontak {SCHOOL}.", "kontak.html", kontak_body(), "images/hero-1.jpg"),
    ("404.html", "Halaman Tidak Ditemukan", "Halaman yang diminta tidak tersedia.", "404.html", not_found_body(), "images/hero-1.jpg"),
]


def main():
    for filename, title, description, active, body, og in PAGES:
        content = page(title, description, active, body, og)
        (ROOT / filename).write_text(content, encoding="utf-8")
        print("dibuat:", filename)

    articles = [
        (
            "berita-ppdb.html",
            "PPDB 2026/2027 Resmi Dibuka",
            f"Informasi penerimaan peserta didik baru {SCHOOL} tahun ajaran 2026/2027.",
            "PPDB",
            "5 Januari 2026",
            "berita-ppdb.jpg",
            [
                f"{SCHOOL} resmi membuka penerimaan peserta didik baru (PPDB) tahun ajaran 2026/2027. Pendaftaran gelombang pertama dibuka mulai 5 Januari hingga 28 Februari 2026.",
                "Calon siswa dapat mendaftar secara daring melalui formulir yang tersedia di halaman kontak atau datang langsung ke sekolah pada hari dan jam layanan. Berkas yang perlu disiapkan meliputi fotokopi ijazah, kartu keluarga, akta kelahiran, dan pas foto terbaru.",
                "Sekolah menyediakan empat kompetensi keahlian yang dapat dipilih, yaitu Teknik Komputer dan Jaringan, Rekayasa Perangkat Lunak, Desain Komunikasi Visual, serta Akuntansi dan Keuangan Lembaga.",
                "Panitia mengimbau calon siswa dan orang tua untuk membaca panduan pendaftaran dengan teliti serta menghubungi sekolah apabila ada hal yang belum jelas.",
            ],
            [
                "Pendaftaran gelombang pertama: 5 Januari - 28 Februari 2026.",
                "Empat pilihan kompetensi keahlian tersedia.",
                "Pendaftaran dapat dilakukan daring atau langsung di sekolah.",
                "Informasi resmi hanya melalui kanal sekolah.",
            ],
        ),
        (
            "berita-lomba.html",
            "Siswa RPL Raih Juara 1 Lomba Web Design Nasional",
            "Prestasi siswa Rekayasa Perangkat Lunak pada kompetisi web design tingkat nasional.",
            "Prestasi",
            "22 Februari 2026",
            "berita-lomba.jpg",
            [
                f"Tim siswa Rekayasa Perangkat Lunak {SCHOOL} berhasil meraih juara pertama pada lomba web design tingkat nasional yang diikuti puluhan sekolah.",
                "Karya yang dilombakan berupa website profil sekolah dengan tampilan responsif, navigasi yang mudah, dan informasi yang terstruktur. Tim melalui beberapa tahap seleksi, mulai dari proposal, prototipe, hingga presentasi akhir.",
                "Pembina tim menyampaikan bahwa kemenangan ini merupakan hasil latihan rutin dan budaya kerja proyek di laboratorium sekolah. Siswa didorong untuk terus mengembangkan kemampuan teknis sekaligus kemampuan komunikasi.",
                "Prestasi ini diharapkan menjadi motivasi bagi siswa lain untuk aktif berkarya dan mengikuti kompetisi sesuai bidang keahliannya.",
            ],
            [
                "Juara 1 lomba web design tingkat nasional.",
                "Karya berupa website profil sekolah yang responsif.",
                "Proses seleksi meliputi proposal, prototipe, dan presentasi.",
                "Prestasi menjadi motivasi bagi siswa lain.",
            ],
        ),
        (
            "berita-kunjungan-industri.html",
            "Kunjungan Industri ke PT Nusantara Teknologi",
            "Siswa kelas XI belajar langsung tentang proses kerja dan budaya industri.",
            "Kegiatan",
            "18 Maret 2026",
            "berita-industri.jpg",
            [
                f"Siswa kelas XI {SCHOOL} melaksanakan kunjungan industri ke PT Nusantara Teknologi. Kegiatan ini bertujuan memperkenalkan dunia kerja secara langsung kepada siswa.",
                "Dalam kunjungan tersebut, siswa melihat proses pengembangan produk, alur kerja tim teknologi, serta standar keselamatan dan kualitas yang diterapkan perusahaan. Siswa juga berkesempatan bertanya kepada praktisi yang bekerja di bidangnya.",
                "Kegiatan kunjungan industri merupakan bagian dari program sekolah untuk memperkuat hubungan antara pembelajaran di kelas dan kebutuhan dunia usaha serta dunia industri.",
                "Sekolah berencana menjadikan kunjungan industri sebagai agenda rutin setiap tahun dengan mitra yang berbeda sesuai kompetensi keahlian.",
            ],
            [
                "Kunjungan diikuti siswa kelas XI.",
                "Siswa belajar proses kerja dan budaya industri.",
                "Kegiatan memperkuat hubungan sekolah dengan industri.",
                "Akan menjadi agenda rutin tahunan.",
            ],
        ),
    ]

    for filename, title, description, category, date, img, paragraphs, points in articles:
        body = article_body(category, date, title, img, paragraphs, points)
        content = page(title, description, "berita.html", body, "images/" + img)
        (ROOT / filename).write_text(content, encoding="utf-8")
        print("dibuat:", filename)


if __name__ == "__main__":
    main()



