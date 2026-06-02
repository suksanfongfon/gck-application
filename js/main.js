/* ===================================================================
   สคริปต์รวม: เมนูมือถือ, FAQ accordion, ไฮไลต์ลิงก์หน้าปัจจุบัน, ปีอัตโนมัติ
   =================================================================== */

document.addEventListener("DOMContentLoaded", function () {
  // --- เมนูมือถือ ---
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("show");
    });
  }

  // --- ไฮไลต์ลิงก์เมนูตามหน้าที่เปิดอยู่ ---
  var current = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === current || (current === "" && href === "index.html")) {
      a.classList.add("active");
    }
  });

  // --- FAQ accordion ---
  document.querySelectorAll(".faq-q").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq-item");
      var wasOpen = item.classList.contains("open");
      // ปิดทุกข้อก่อน (เปิดทีละข้อ)
      document.querySelectorAll(".faq-item").forEach(function (i) {
        i.classList.remove("open");
      });
      if (!wasOpen) item.classList.add("open");
    });
  });

  // --- ใส่ปีปัจจุบันใน footer อัตโนมัติ ---
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
});
