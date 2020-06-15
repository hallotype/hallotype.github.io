const viewslineswitch = document.querySelector("#line");
const viewsgridswitch = document.querySelector("#grid");
const lineviews = document.querySelectorAll("p.lineView");
const gridviews = document.querySelectorAll("p.gridView");
const fontItems = document.querySelectorAll("div.fontItem");

viewslineswitch.addEventListener("change", (event) => {
  // console.log("switch line", lineviews);
  lineviews.forEach(function (item) {
    item.classList.add("visible_line");
    // item.classList.remove("invisible");
  });
  gridviews.forEach(function (item) {
    // item.classList.add("invisible");
    item.classList.remove("visible_grid");
  });
  fontItems.forEach(function (item) {
    // item.classList.add("lineView");
    // item.classList.remove("gridView");
  });
});

viewsgridswitch.addEventListener("change", (event) => {
  // console.log("switch grid");
  gridviews.forEach(function (item) {
    // console.log(item);
    item.classList.add("visible_grid");
    // item.classList.remove("invisible");
  });
  lineviews.forEach(function (item) {
    // item.classList.add("invisible");
    item.classList.remove("visible_line");
  });
  fontItems.forEach(function (item) {
    // item.classList.add("gridView");
    // item.classList.remove("lineView");
  });
});
