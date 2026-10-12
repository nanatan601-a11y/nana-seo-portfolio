const root = document.documentElement;
const buttons = document.querySelectorAll("[data-set-lang]");
const savedLanguage = localStorage.getItem("portfolio-language") || "en";

function setLanguage(language) {
  root.setAttribute("data-lang", language);
  localStorage.setItem("portfolio-language", language);
  buttons.forEach((button) => {
    button.classList.toggle("active", button.dataset.setLang === language);
  });
}

buttons.forEach((button) => {
  button.addEventListener("click", () => setLanguage(button.dataset.setLang));
});

setLanguage(savedLanguage);

document.querySelectorAll("[data-carousel]").forEach((carousel) => {
  const track = carousel.querySelector(".carousel-track");
  const slides = Array.from(carousel.querySelectorAll(".proof-card"));
  const prev = carousel.querySelector("[data-carousel-prev]");
  const next = carousel.querySelector("[data-carousel-next]");
  const status = carousel.querySelector("[data-carousel-status]");
  let current = 0;

  function updateCarousel() {
    if (!track || slides.length === 0) return;
    track.style.transform = `translateX(-${current * 100}%)`;
    if (status) status.textContent = `${current + 1} / ${slides.length}`;
  }

  function goTo(index) {
    current = (index + slides.length) % slides.length;
    updateCarousel();
  }

  if (prev) prev.addEventListener("click", () => goTo(current - 1));
  if (next) next.addEventListener("click", () => goTo(current + 1));

  if (slides.length > 1) {
    window.setInterval(() => goTo(current + 1), 5000);
  }

  updateCarousel();
});
