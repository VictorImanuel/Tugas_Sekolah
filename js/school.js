/*
 * Website sekolah - interaksi halaman
 * Menggunakan library yang sudah ada di template Kaira:
 * jQuery, Swiper, AOS, dan Bootstrap 5.
 */
(function () {
  "use strict";

  /**
   * Animasi muncul saat halaman digulir.
   */
  function initAOS() {
    if (typeof AOS === "undefined") {
      return;
    }

    AOS.init({
      duration: 1000,
      once: true
    });
  }

  /**
   * Slider hero di halaman beranda.
   */
  function initHeroSwiper() {
    var hero = document.querySelector(".hero-swiper");

    if (!hero || typeof Swiper === "undefined") {
      return;
    }

    new Swiper(".hero-swiper", {
      loop: true,
      speed: 900,
      effect: "fade",
      fadeEffect: {
        crossFade: true
      },
      autoplay: {
        delay: 6500,
        disableOnInteraction: false
      },
      pagination: {
        el: ".hero-swiper .swiper-pagination",
        clickable: true
      },
      navigation: {
        nextEl: ".hero-swiper .icon-arrow-right",
        prevEl: ".hero-swiper .icon-arrow-left"
      }
    });
  }

  /**
   * Slider testimoni alumni.
   */
  function initTestimonialSwiper() {
    var testimonial = document.querySelector(".testimonial-swiper");

    if (!testimonial || typeof Swiper === "undefined") {
      return;
    }

    new Swiper(".testimonial-swiper", {
      slidesPerView: 1,
      spaceBetween: 30,
      loop: true,
      autoplay: {
        delay: 7000,
        disableOnInteraction: false
      },
      pagination: {
        el: ".testimonial-swiper-pagination",
        clickable: true
      },
      breakpoints: {
        768: {
          slidesPerView: 2
        },
        1200: {
          slidesPerView: 3
        }
      }
    });
  }

  /**
   * Animasi angka statistik (guru, siswa, rombel, jurusan).
   */
  function initCounters() {
    var counters = Array.prototype.slice.call(document.querySelectorAll("[data-count]"));

    if (!counters.length) {
      return;
    }

    var reduceMotion = window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function format(value) {
      return value.toLocaleString("id-ID");
    }

    function targetOf(element) {
      return parseInt(element.getAttribute("data-count"), 10) || 0;
    }

    if (reduceMotion) {
      counters.forEach(function (element) {
        element.textContent = format(targetOf(element));
      });
      return;
    }

    function animate(element) {
      var target = targetOf(element);
      var duration = 1400;
      var start = null;

      function step(timestamp) {
        if (start === null) {
          start = timestamp;
        }

        var progress = Math.min((timestamp - start) / duration, 1);
        element.textContent = format(Math.floor(progress * target));

        if (progress < 1) {
          window.requestAnimationFrame(step);
        }
      }

      window.requestAnimationFrame(step);
    }

    function run(element) {
      if (element.getAttribute("data-counted")) {
        return;
      }

      element.setAttribute("data-counted", "true");
      animate(element);
    }

    function isVisible(element) {
      var rect = element.getBoundingClientRect();
      return rect.top < window.innerHeight * 0.9 && rect.bottom > 0;
    }

    /**
     * Cadangan selain IntersectionObserver: cek posisi saat halaman digulir.
     */
    function check() {
      counters.forEach(function (element) {
        if (isVisible(element)) {
          run(element);
        }
      });
    }

    counters.forEach(function (element) {
      element.textContent = "0";
    });

    if ("IntersectionObserver" in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            run(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });

      counters.forEach(function (counter) {
        observer.observe(counter);
      });
    }

    window.addEventListener("scroll", check, { passive: true });
    window.addEventListener("resize", check);
    window.addEventListener("load", check);
    window.setTimeout(check, 500);
    check();
  }

  /**
   * Filter kartu berdasarkan kategori (ekstrakurikuler & galeri).
   */
  function initFilters() {
    var groups = document.querySelectorAll("[data-filter-group]");

    groups.forEach(function (group) {
      var buttons = group.querySelectorAll("[data-filter]");
      var targetSelector = group.getAttribute("data-filter-target");
      var items = document.querySelectorAll(targetSelector + " [data-category]");

      buttons.forEach(function (button) {
        button.addEventListener("click", function (event) {
          event.preventDefault();

          buttons.forEach(function (item) {
            item.classList.remove("is-checked");
          });
          button.classList.add("is-checked");

          var filter = button.getAttribute("data-filter");

          items.forEach(function (item) {
            var categories = (item.getAttribute("data-category") || "").split(" ");
            var matches = filter === "all" || categories.indexOf(filter) !== -1;

            item.classList.toggle("d-none", !matches);
          });
        });
      });
    });
  }

  /**
   * Lightbox galeri memakai modal Bootstrap.
   */
  function initGalleryLightbox() {
    var modalElement = document.getElementById("galleryModal");

    if (!modalElement || typeof bootstrap === "undefined") {
      return;
    }

    var modal = new bootstrap.Modal(modalElement);
    var image = modalElement.querySelector("[data-gallery-image]");
    var caption = modalElement.querySelector("[data-gallery-title]");

    document.querySelectorAll("[data-gallery]").forEach(function (item) {
      item.addEventListener("click", function (event) {
        event.preventDefault();

        image.src = item.getAttribute("data-img");
        image.alt = item.getAttribute("data-title") || "Foto kegiatan sekolah";
        caption.textContent = item.getAttribute("data-title") || "";

        modal.show();
      });
    });
  }

  /**
   * Pencarian berita di halaman daftar berita.
   */
  function initNewsSearch() {
    var input = document.getElementById("news-search");

    if (!input) {
      return;
    }

    var items = document.querySelectorAll("[data-news-item]");
    var emptyMessage = document.getElementById("news-empty");

    input.addEventListener("input", function () {
      var keyword = input.value.toLowerCase().trim();
      var visible = 0;

      items.forEach(function (item) {
        var matches = keyword === "" || item.textContent.toLowerCase().indexOf(keyword) !== -1;

        item.classList.toggle("d-none", !matches);

        if (matches) {
          visible += 1;
        }
      });

      if (emptyMessage) {
        emptyMessage.classList.toggle("d-none", visible !== 0 || keyword === "");
      }
    });
  }

  /**
   * Validasi form kontak (demo front-end).
   * TODO: sambungkan ke endpoint Google Forms / Formspree saat sudah tersedia.
   */
  function initContactForm() {
    var form = document.getElementById("contact-form");

    if (!form) {
      return;
    }

    var successMessage = document.getElementById("form-success");

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      event.stopPropagation();

      if (!form.checkValidity()) {
        form.classList.add("was-validated");
        return;
      }

      var endpoint = form.getAttribute("data-endpoint");

      function showSuccess() {
        if (successMessage) {
          successMessage.classList.remove("d-none");
        }

        form.reset();
        form.classList.remove("was-validated");
      }

      if (endpoint) {
        /**
         * Google Forms menerima POST biasa. Respons tidak dapat dibaca
         * (mode no-cors), jadi pesan sukses ditampilkan setelah request terkirim.
         */
        fetch(endpoint, {
          method: "POST",
          mode: "no-cors",
          body: new FormData(form)
        }).then(showSuccess, showSuccess);
        return;
      }

      showSuccess();
    });
  }

  /**
   * Membuka tab jurusan sesuai hash URL, misalnya jurusan.html#tkj.
   */
  function initTabsFromHash() {
    var tabs = document.querySelectorAll('.jurusan-tabs [data-bs-toggle="tab"]');

    if (!tabs.length) {
      return;
    }

    if (window.location.hash && typeof bootstrap !== "undefined") {
      var trigger = document.querySelector(
        '.jurusan-tabs [data-bs-target="' + window.location.hash + '"]'
      );

      if (trigger) {
        bootstrap.Tab.getOrCreateInstance(trigger).show();
      }
    }

    tabs.forEach(function (tab) {
      tab.addEventListener("shown.bs.tab", function (event) {
        var target = event.target.getAttribute("data-bs-target");

        if (target && window.history.replaceState) {
          window.history.replaceState(null, "", target);
        }
      });
    });
  }

  /**
   * Menandai submenu yang sesuai dengan hash URL, misalnya
   * profil.html#visi-misi, lalu membuka accordion mobile terkait.
   */
  function initNavState() {
    var links = document.querySelectorAll(
      ".navbar .dropdown-item, .navbar .mobile-submenu-link"
    );

    if (!links.length) {
      return;
    }

    function sync() {
      var hash = window.location.hash;

      links.forEach(function (link) {
        var url = new URL(link.getAttribute("href"), window.location.href);

        if (url.pathname !== window.location.pathname) {
          return;
        }

        var matches = hash ? url.hash === hash : url.hash === "";

        link.classList.toggle("active", matches);

        if (matches) {
          link.setAttribute("aria-current", hash ? "location" : "page");
        } else {
          link.removeAttribute("aria-current");
        }
      });
    }

    document.querySelectorAll(".navbar .mobile-submenu").forEach(function (panel) {
      if (!panel.querySelector(".mobile-submenu-link.active")) {
        return;
      }

      panel.classList.add("show");

      var toggle = document.querySelector('[data-bs-target="#' + panel.id + '"]');

      if (toggle) {
        toggle.setAttribute("aria-expanded", "true");
      }
    });

    window.addEventListener("hashchange", sync);
    sync();
  }

  /**
   * Menutup offcanvas setelah tautan menu diklik di layar kecil.
   */
  function initOffcanvasLinks() {
    var offcanvas = document.getElementById("offcanvasNavbar");

    if (!offcanvas || typeof bootstrap === "undefined") {
      return;
    }

    offcanvas.querySelectorAll("a[href]").forEach(function (link) {
      link.addEventListener("click", function () {
        var instance = bootstrap.Offcanvas.getInstance(offcanvas);

        if (instance) {
          instance.hide();
        }
      });
    });
  }

  /**
   * Tombol kembali ke atas.
   */
  function initBackToTop() {
    var button = document.querySelector(".back-to-top");

    if (!button) {
      return;
    }

    window.addEventListener("scroll", function () {
      button.classList.toggle("show", window.scrollY > 400);
    });

    button.addEventListener("click", function (event) {
      event.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initAOS();
    initHeroSwiper();
    initTestimonialSwiper();
    initCounters();
    initFilters();
    initGalleryLightbox();
    initNewsSearch();
    initContactForm();
    initTabsFromHash();
    initNavState();
    initOffcanvasLinks();
    initBackToTop();
  });
})();
