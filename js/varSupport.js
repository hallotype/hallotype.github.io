const PanSliders = document.querySelector("#sliders-Pan");
PanSliders.oninput = PanChanger;
function PanChanger(e) {
  let fontElements = document.querySelectorAll("div.Pan p");
  fontElements.forEach(function (fontElement) {
    console.log(fontElement);
    fontElement.style.cssText =
      "font-variation-settings:" +
      "'wght' " +
      document.querySelector("#Panwght").value +
      ",'ANGL' " +
      document.getElementById("PanANGL").value +
      ",'STEP' " +
      document.querySelector("#PanSTEP").value;
  });
}
const bexSliders = document.querySelector("#sliders-bex");
bexSliders.oninput = bexChanger;
function bexChanger(e) {
  let fontElements = document.querySelectorAll("div.bex p");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
      "'wght' " +
      document.querySelector("#bexwght").value;
  });
}
