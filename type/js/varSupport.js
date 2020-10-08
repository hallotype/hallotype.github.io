
const panv2020Sliders = document.querySelector("#sliders-panv2020");
panv2020Sliders.oninput = panv2020Changer;
function panv2020Changer(e) {
  let fontElements = document.querySelectorAll("div.panv2020");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
"'wght' " + document.querySelector("#panv2020wght").value
+",'ANGL' " + document.querySelector("#panv2020ANGL").value
+",'STEP' " + document.querySelector("#panv2020STEP").value
+",'SHAP' " + document.querySelector("#panv2020SHAP").value
  });}
const PanSliders = document.querySelector("#sliders-Pan");
PanSliders.oninput = PanChanger;
function PanChanger(e) {
  let fontElements = document.querySelectorAll("div.Pan");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
"'wght' " + document.querySelector("#Panwght").value
+",'ANGL' " + document.querySelector("#PanANGL").value
+",'STEP' " + document.querySelector("#PanSTEP").value
  });}
const bexSliders = document.querySelector("#sliders-bex");
bexSliders.oninput = bexChanger;
function bexChanger(e) {
  let fontElements = document.querySelectorAll("div.bex");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
"'wght' " + document.querySelector("#bexwght").value
  });}
const PikselsSliders = document.querySelector("#sliders-Piksels");
PikselsSliders.oninput = PikselsChanger;
function PikselsChanger(e) {
  let fontElements = document.querySelectorAll("div.Piksels");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
"'PIXL' " + document.querySelector("#PikselsPIXL").value
+",'CHAR' " + document.querySelector("#PikselsCHAR").value
+",'PROP' " + document.querySelector("#PikselsPROP").value
+",'slnt' " + document.querySelector("#Pikselsslnt").value
+",'ROTA' " + document.querySelector("#PikselsROTA").value
  });}
const Pan_ClockSliders = document.querySelector("#sliders-Pan_Clock");
Pan_ClockSliders.oninput = Pan_ClockChanger;
function Pan_ClockChanger(e) {
  let fontElements = document.querySelectorAll("div.Pan_Clock");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
"'wght' " + document.querySelector("#Pan_Clockwght").value
+",'ANGL' " + document.querySelector("#Pan_ClockANGL").value
+",'STEP' " + document.querySelector("#Pan_ClockSTEP").value
  });}
const waaveSliders = document.querySelector("#sliders-waave");
waaveSliders.oninput = waaveChanger;
function waaveChanger(e) {
  let fontElements = document.querySelectorAll("div.waave");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
"'LMBD' " + document.querySelector("#waaveLMBD").value
+",'AMPL' " + document.querySelector("#waaveAMPL").value
+",'SHFT' " + document.querySelector("#waaveSHFT").value
  });}
const BexTiltSliders = document.querySelector("#sliders-BexTilt");
BexTiltSliders.oninput = BexTiltChanger;
function BexTiltChanger(e) {
  let fontElements = document.querySelectorAll("div.BexTilt");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
"'ital' " + document.querySelector("#BexTiltital").value
  });}
const PanAnglerSliders = document.querySelector("#sliders-PanAngler");
PanAnglerSliders.oninput = PanAnglerChanger;
function PanAnglerChanger(e) {
  let fontElements = document.querySelectorAll("div.PanAngler");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
"'ANGL' " + document.querySelector("#PanAnglerANGL").value
  });}