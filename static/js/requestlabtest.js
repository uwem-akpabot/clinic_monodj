$(document).ready(function(){
    $('.chkcvalues').click(function(){
      var txt = "";
      $('.chkcvalues:checked').each(function(){
        txt += $(this).val()+", ";
      });
      txt = txt.substring(0, txt.length - 1);
      $('#txtvalues').val(txt);
      if (txt == ""){
        alert("You must select at least one Lab Test from the checkboxes below")
      }
    });
});