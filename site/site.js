(function () {
  var STORAGE_KEY = "huma-lang";
  var LANGS = ["ko", "en", "ja", "zh"];

  function currentLangFromPath() {
    var parts = location.pathname.split("/").filter(Boolean);
    for (var i = 0; i < parts.length; i++) {
      if (LANGS.indexOf(parts[i]) >= 0) return parts[i];
    }
    return null;
  }

  var switchEl = document.querySelector("[data-lang-switch]");
  if (switchEl) {
    var pathLang = currentLangFromPath();
    if (pathLang) switchEl.value = pathLang;

    switchEl.addEventListener("change", function () {
      var next = switchEl.value;
      if (LANGS.indexOf(next) < 0) return;
      try {
        localStorage.setItem(STORAGE_KEY, next);
      } catch (e) {}

      var page = switchEl.getAttribute("data-page") || "index";
      var file = page === "bom" ? "bom.html" : "index.html";
      location.href = "../" + next + "/" + file;
    });
  }

  var links = Array.prototype.slice.call(document.querySelectorAll(".toc a[href^='#']"));
  if (!links.length) return;

  var sections = links
    .map(function (link) {
      var id = link.getAttribute("href").slice(1);
      var el = document.getElementById(id);
      return el ? { link: link, el: el } : null;
    })
    .filter(Boolean);

  if (!("IntersectionObserver" in window) || !sections.length) return;

  var activeId = null;

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          activeId = entry.target.id;
        }
      });
      sections.forEach(function (item) {
        item.link.classList.toggle("is-active", item.el.id === activeId);
      });
    },
    {
      rootMargin: "-20% 0px -65% 0px",
      threshold: 0.01,
    }
  );

  sections.forEach(function (item) {
    observer.observe(item.el);
  });
})();
