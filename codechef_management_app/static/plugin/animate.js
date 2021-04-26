
// for tgline
var textWrapper = document.querySelector('.ml3');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: false})
  .add({
    targets: '.ml3 .letter',
    opacity: [0, 1],
    easing: "easeInOutQuad",
    duration: 1250,
    delay: (el, i) => 70 * (i+1)
  }).add({
    targets: '.ml3',
    opacity: 0.7,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1000
  });


