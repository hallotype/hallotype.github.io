// var Pan_dragging = false;
// PanSliders.addEventListener("mousedown", (event) => {
//   Pan_dragging = true;
// });
// PanSliders.addEventListener("mouseup", (event) => {
//   Pan_dragging = false;
// });

const PanSliders = document.querySelector("#sliders-Pan");
PanSliders.oninput = PanChanger;
function PanChanger(e) {
  let fontElements = document.querySelectorAll("div.Pan p");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
      "'wght' " +
      document.querySelector("#Panwght").value +
      ",'ANGL' " +
      document.querySelector("#PanANGL").value +
      ",'STEP' " +
      document.querySelector("#PanSTEP").value;
  });
}
// var bex_dragging = false;
// bexSliders.addEventListener("mousedown", (event) => {
//   bex_dragging = true;
// });
// bexSliders.addEventListener("mouseup", (event) => {
//   bex_dragging = false;
// });

// bexSliders.addEventListener("mousemove", (event) => {
//   console.log("BxSL");
//   if (1) {
//     let fontElements = document.querySelectorAll("div.bex p");
//     fontElements.forEach(function (fontElement) {
//       fontElement.style.cssText =
//         "font-variation-settings:" +
//         "'wght' " +
//         document.querySelector("#bexwght").value;
//     });
//   }
// });

const bexSliders = document.querySelector("#sliders-bex");
bexSliders.oninput = bexChanger;
function bexChanger(e) {
  console.log("BxSL");
  let fontElements = document.querySelectorAll("div.bex p");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
      "'wght' " +
      document.querySelector("#bexwght").value;
  });
}
