var Pan_dragging = false;
const PanSliders = document.querySelector("#sliders-Pan");
const Panwght = document.querySelector("#Panwght");
const PanANGL = document.querySelector("#PanANGL");
const PanSTEP = document.querySelector("#PanSTEP");

PanSliders.addEventListener("mousedown", (event) => {
  Pan_dragging = true;
});
PanSliders.addEventListener("mouseup", (event) => {
  Pan_dragging = false;
});

Panwght.addEventListener("mousemove", (event) => {
  if (Pan_dragging) {
    let parent = document.querySelector(".Pan");
    parent.style.cssText =
      "font-variation-settings:" +
      "'wght' " +
      Panwght.value +
      ",'ANGL' " +
      PanANGL.value +
      ",'STEP' " +
      PanSTEP.value;
  }
});
PanANGL.addEventListener("mousemove", (event) => {
  if (Pan_dragging) {
    let parent = document.querySelector(".Pan");
    parent.style.cssText =
      "font-variation-settings:" +
      "'wght' " +
      Panwght.value +
      ",'ANGL' " +
      PanANGL.value +
      ",'STEP' " +
      PanSTEP.value;
  }
});
PanSTEP.addEventListener("mousemove", (event) => {
  if (Pan_dragging) {
    let parent = document.querySelector(".Pan");
    parent.style.cssText =
      "font-variation-settings:" +
      "'wght' " +
      Panwght.value +
      ",'ANGL' " +
      PanANGL.value +
      ",'STEP' " +
      PanSTEP.value;
  }
});
var bex_dragging = false;
const bexSliders = document.querySelector("#sliders-bex");
const bexwght = document.querySelector("#bexwght");

bexSliders.addEventListener("mousedown", (event) => {
  bex_dragging = true;
});
bexSliders.addEventListener("mouseup", (event) => {
  bex_dragging = false;
});

bexwght.addEventListener("mousemove", (event) => {
  if (bex_dragging) {
    let parent = document.querySelector(".bex");
    parent.style.cssText =
      "font-variation-settings:" + "'wght' " + bexwght.value;
  }
});
