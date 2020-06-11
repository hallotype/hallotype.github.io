
const Panwght = document.querySelector("#Panwght");
Panwght.addEventListener("mousemove", (event) => {
  let parent = document.querySelector(".Pan");
  parent.style.cssText = "font-variation-settings: 'wght' " + Panwght.value;
});

const PanANGL = document.querySelector("#PanANGL");
PanANGL.addEventListener("mousemove", (event) => {
  let parent = document.querySelector(".Pan");
  parent.style.cssText = "font-variation-settings: 'ANGL' " + PanANGL.value;
});

const PanSTEP = document.querySelector("#PanSTEP");
PanSTEP.addEventListener("mousemove", (event) => {
  let parent = document.querySelector(".Pan");
  parent.style.cssText = "font-variation-settings: 'STEP' " + PanSTEP.value;
});

const bexwght = document.querySelector("#bexwght");
bexwght.addEventListener("mousemove", (event) => {
  let parent = document.querySelector(".bex");
  parent.style.cssText = "font-variation-settings: 'wght' " + bexwght.value;
});
