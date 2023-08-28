$(document).ready(function() {
  var modalOpened = localStorage.getItem('modalOpened');

  if (!modalOpened) {
    $('.modal').modal();
    $('#modal-about').modal('open');
    localStorage.setItem('modalOpened', true);
  }

  $('.modal-trigger').click(function() {
    $('.modal').modal();
    $('#modal-about').modal('open');
  });
});


$(document).ready(function() {

  //Menu in navbar
  $(".button-collapse").sideNav({
    menuWidth: 200,
    edge: 'right',  
  });

});
