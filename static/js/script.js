/*
document.addEventListener('DOMContentLoaded', function() {
  var modalTrigger = document.getElementById('modal-trigger');
  var modalInstance = M.Modal.getInstance(document.getElementById('modal1'));
  
  if (!localStorage.getItem('modalShown')) {
    modalInstance.open();
    localStorage.setItem('modalShown', 'true');
  }
});
*/

/*$(document).ready(function() {
  var modalOpened = localStorage.getItem('modalOpened');

  if (!modalOpened) {
    $('.modal').modal();
    $('#modal-about').modal('open');
    localStorage.setItem('modalOpened', true);
  }
});
*/

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

  //jQuery Plugin Initialization for modal window
  //$('.modal').modal();
  //$('#modal-about').modal('open');
  

});
