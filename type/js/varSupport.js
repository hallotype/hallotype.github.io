
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
const bitmapSliders = document.querySelector("#sliders-bitmap");
bitmapSliders.oninput = bitmapChanger;
function bitmapChanger(e) {
  let fontElements = document.querySelectorAll("div.bitmap");
  fontElements.forEach(function (fontElement) {
    fontElement.style.cssText =
      "font-variation-settings:" +
"'PIXL' " + document.querySelector("#bitmapPIXL").value
+",'PROP' " + document.querySelector("#bitmapPROP").value
+",'slnt' " + document.querySelector("#bitmapslnt").value
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