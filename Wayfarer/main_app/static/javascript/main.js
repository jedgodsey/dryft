$('.carousel.carousel-slider').carousel({
  fullWidth: true,
  indicators: true
});
// Makes Carousel Rotate
setInterval(()=>{
  $('.carousel').carousel('next');
},6000)

// const selectEl = document.getElementById('id_city');
  
// M.FormSelect.init(id_city);
