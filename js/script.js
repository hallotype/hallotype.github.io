var pan_dragging = false;

const Panwght = document.querySelector("#Panwght");
const PanANGL = document.querySelector("#PanANGL");
const PanSTEP = document.querySelector("#PanSTEP");
const PanSliders = document.querySelector("#sliders-Pan");

PanSliders.addEventListener("mousedown", (event) => {
  pan_dragging = true;
});
PanSliders.addEventListener("mouseup", (event) => {
  pan_dragging = false;
});

Panwght.addEventListener("mousemove", (event) => {
  if (pan_dragging) {
    let parent = document.querySelector(".Pan");
    parent.style.cssText =
      "font-variation-settings: 'wght' " +
      Panwght.value +
      ", 'STEP' " +
      PanSTEP.value +
      ", 'ANGL' " +
      PanANGL.value;
  }
});
PanANGL.addEventListener("mousemove", (event) => {
  if (pan_dragging) {
    let parent = document.querySelector(".Pan");
    parent.style.cssText =
      "font-variation-settings: 'wght' " +
      Panwght.value +
      ", 'STEP' " +
      PanSTEP.value +
      ", 'ANGL' " +
      PanANGL.value;
  }
});
PanSTEP.addEventListener("mousemove", (event) => {
  if (pan_dragging) {
    let parent = document.querySelector(".Pan");
    parent.style.cssText =
      "font-variation-settings: 'wght' " +
      Panwght.value +
      ", 'STEP' " +
      PanSTEP.value +
      ", 'ANGL' " +
      PanANGL.value;
  }
});

const bexwght = document.querySelector("#bexwght");
bexwght.addEventListener("mousemove", (event) => {
  let parent = document.querySelector(".bex");
  parent.style.cssText = "font-variation-settings: 'wght' " + bexwght.value;
});
