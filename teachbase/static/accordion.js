const accordions = document.querySelectorAll(".accordion");

accordions.forEach((accordion) => {
  const bttn = accordion.querySelector(".accordion__button");
  const panel = accordion.querySelector(".accordion__panel");
  const activeClassBtn = "accordion__button-active";
  const activeClassPanel = "accordion__panel-active";

  bttn.addEventListener("click", (event) => {
    event.preventDefault();

    const active__bttn = document.querySelectorAll(
      ".accordion .accordion__button-active"
    );
    active__bttn.forEach((el) =>
      el !== bttn ? el.classList.remove(activeClassBtn) : null
    );
    bttn.classList.toggle(activeClassBtn);

    const active__panel = document.querySelectorAll(
      ".accordion .accordion__panel-active"
    );
    active__panel.forEach((el) =>
      el !== panel ? el.classList.remove(activeClassPanel) : null
    );
    panel.classList.toggle(activeClassPanel);

    panel.style.setProperty("--height", `${panel.scrollHeight}px`);
  });
});
