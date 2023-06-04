$(document).ready(function(){
  var txt = "";
  $('.chkcbtn').click(function(){
    txt += $('.chkcvalues').val()+" ("+$('.chkcvalues2').val()+"), ";
    
    txt = txt.substring(0, txt.length - 1);
    $('#txtvalues').val(txt);
    if (txt == ""){
      alert("You must select at least one Lab Test from the checkboxes below")
    }
    $('.chkcvalues').val(" ");
    $('.chkcvalues2').val("");
  });

  // $('.chkcvalues2').click(function(){
  //   $('.chkcvalues2:checked').each(function(){
  //     txt += " ("+$(this).val()+"), ";
  //   });
  //   txt = txt.substring(0, txt.length - 1);
  //   $('#txtvalues').val(txt);
  // });
});

// $('.chkcvalues').click(function(){
//   var txt = "";
//   $('.chkcvalues:checked').each(function(){
//     txt += $(this).val()+", ";
//   });
//   txt = txt.substring(0, txt.length - 1);
//   $('#txtvalues').val(txt);
//   if (txt == ""){
//     alert("You must select at least one Lab Test from the checkboxes below")
//   }
// });


// WORKING WELL

// $(document).ready(function(){
//   var txt = "";
//   $('.chkcbtn').click(function(){
//     txt += $('.chkcvalues').val()+", ";
    
//     txt = txt.substring(0, txt.length - 1);
//     $('#txtvalues').val(txt);
//     if (txt == ""){
//       alert("You must select at least one Lab Test from the checkboxes below")
//     }
//     $('.chkcvalues').val("");
//   });
// });