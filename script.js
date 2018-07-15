
$("a.delete").on("click", function(e) {

   e.preventDefault();

   if (confirm("Are you sure?")) {

         var frm = $("<form>");
         frm.attr('method', 'post');
         frm.attr('action', $(this).attr('href'));
         frm.appendTo("body");
         frm.submit();
   }
});

$.validator.addMethod("dateTime", function(value, element) {
  return (value == "") || ! isNan(Date.parse(value));
}, "Must be a valid date and time");

$("#formArticle").validate({
     rules: {
       title: {
          required: true
       },
       content: {
         required: true
       },
       published_at: {
         dateTime: true
       }
     }
});


$("button.publish").on("click", function(e) {
     var id = $(this).data('id');
     alert(id);
});





