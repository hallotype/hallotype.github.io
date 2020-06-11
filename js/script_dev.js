Panwght.addEventListener("mousemove", (event) => {
  let parent = document.querySelector(".Pan");
  parent.style.cssText = "font-variation-settings: 'wght' " + Panwght.value;
});

var pan_dragging = false;

const Panwght = document.querySelector("#Panwght");
const PanANGL = document.querySelector("#PanANGL");
const PanSTEP = document.querySelector("#PanSTEP");

PanANGL.addEventListener("mousedown", (event) => {
  pan_dragging = true;
});
PanANGL.addEventListener("mouseup", (event) => {
  pan_dragging = false;
});
PanANGL.addEventListener("mousemove", (event) => {
  if (pan_dragging) {
    let parent = document.querySelector(".Pan");
    parent.style.cssText = "font-variation-settings: 'ANGL' " + PanANGL.value;
  }
});

PanSTEP.addEventListener("mousemove", (event) => {
  let parent = document.querySelector(".Pan");
  parent.style.cssText = "font-variation-settings: 'STEP' " + PanSTEP.value;
});

const bexwght = document.querySelector("#bexwght");
bexwght.addEventListener("mousemove", (event) => {
  let parent = document.querySelector(".bex");
  parent.style.cssText = "font-variation-settings: 'wght' " + bexwght.value;
});
