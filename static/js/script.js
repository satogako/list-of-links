/**
 * Сhecks if the modal window has been opened before. 
 * If not, it opens the modal window and saves this state 
 * to local storage. When the modal trigger is clicked, 
 * the modal window opens.
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


/**
 * This code initializes a side navigation menu in the navbar.
 */
$(document).ready(function() {

  $(".button-collapse").sideNav({
    menuWidth: 200,
    edge: 'right',  
  });

});
