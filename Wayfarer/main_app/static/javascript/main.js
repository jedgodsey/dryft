$('.carousel.carousel-slider').carousel({
  fullWidth: true,
  indicators: true
});
// Makes Carousel Rotate
setInterval(()=>{
  $('.carousel').carousel('next');
},6000)

console.log("hello")