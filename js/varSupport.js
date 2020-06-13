
var Pan_dragging = false;
const PanSliders = document.querySelector("#sliders-Pan");
PanSliders.addEventListener("mousedown", (event) => {
  Pan_dragging = true;
});
PanSliders.addEventListener("mouseup", (event) => {
  Pan_dragging = false;
});

PanSliders.addEventListener("mousemove", (event) => {
  if (Pan_dragging) {
    let fontElements = document.querySelectorAll("div.Pan p");
    fontElements.forEach(function (fontElement) {
      fontElement.style.cssText =
        "font-variation-settings:" +
"'wght' " + document.querySelector("#Panwght").value+",'ANGL' " + document.querySelector("#PanANGL").value+",'STEP' " + document.querySelector("#PanSTEP").value});}});
var bex_dragging = false;
const bexSliders = document.querySelector("#sliders-bex");
bexSliders.addEventListener("mousedown", (event) => {
  bex_dragging = true;
});
bexSliders.addEventListener("mouseup", (event) => {
  bex_dragging = false;
});

bexSliders.addEventListener("mousemove", (event) => {
  if (bex_dragging) {
    let fontElements = document.querySelectorAll("div.bex p");
    fontElements.forEach(function (fontElement) {
      fontElement.style.cssText =
        "font-variation-settings:" +
"'wght' " + document.querySelector("#bexwght").value});}});