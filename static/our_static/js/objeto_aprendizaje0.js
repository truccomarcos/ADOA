var initialLoad = true;
var defaultTemplateTag = "default-template";

$(function() {
  $('.add-contenido').hide();
  $('.send-form').hide();
  $('.no-patron').show();

  // $('.send-form').click(function(element){
  //   alert("submit");
  //   debugger;
  // });

  $.ajax({
    type: 'GET',
    url: "actividad",
    success: function(result) {
      var template = result.replace(/[\r\n]/g,"").replace(/form-0/g,"form-"+defaultTemplateTag).replace(/<form  method="post" >/,'').replace(/<\/form>/,'');
      $('.actividad-template').append(result).hide();
    }
  });

  $(window).on('beforeunload',function(){
     $('#id_patron').val("");
  });

  $('#id_patron').click(function() {
    var idPatron = $(this).val();
    if(idPatron == ""){
      $('.add-contenido').hide();
      $('.send-form').hide();
      $('.no-patron').show();
    } else {
      $.ajax({
        type: 'GET',
        url: "patron",
        data: { "pk_patron":idPatron },
        success: function(result) {
          $('.contenido-form').remove();
          var newCont = $(result.replace(/[\r\n]/g,"").replace(/<form  method="post" >/,'').replace(/<\/form>/,''));
          var newHTML='';
          for(var i=0; i < newCont.length; i++){
            newHTML += newCont[i].outerHTML.replace(new RegExp('form-'+i,'g'),'contenido_set-'+parseInt(i));
          }
          $('.contenido-formset').append(newHTML);
          $('#id_contenido_set-TOTAL_FORMS').val(newCont.length);
          $('.add-contenido').show();
          $('.send-form').show();
          $('.no-patron').hide();
        }
      });
    }
  });

  $('.add-contenido').click(function() {
      alert("Add contenido");
      $.ajax({
        type: 'GET',
        url: "contenido",
        success: function(result) {
          var contenidoAmountInput = $('#id_contenido_set-TOTAL_FORMS');
          var contenidoAmount = contenidoAmountInput.val();
          var newCont = result.replace(/[\r\n]/g,"").replace(/<form  method="post" >/,'').replace(/<\/form>/,'');
          newCont = newCont.replace(/form-0/g,"form-"+contenidoAmount);
          $('.contenido-formset').append(newCont);
          $('#id_form-' + contenidoAmount + '-orden').val(parseInt(contenidoAmount)+1);
          $('#id_form-' + contenidoAmount + '-titulo').val("");
          $('#id_form-' + contenidoAmount + '-descripcion').val("");
          contenidoAmountInput.val(parseInt(contenidoAmount) + 1);
        }
      });



  });

  $('.add-actividad').click(function() {
      alert("Add actividad");
      debugger;
      var actividadAmountInput = $('#id_actividad_set-TOTAL_FORMS');
      var actividadAmount = actividadAmountInput.val();
      var templateHtml = $('.actividad-template').html();
      var regexp = new RegExp("form-"+defaultTemplateTag,'g');
      var newActividad = templateHtml.replace(regexp,actividadAmount).replace(/[\r\n]/g,"");
      $('.actividad-formset').append(newActividad).show();
      actividadAmountInput.val(parseInt(actividadAmount) + 1);
      // var template = $('.contenido-formset').find('.contenido-form')[0];
      // var templateHtml = template.outerHTML;
      // templateHtml = templateHtml.replace(/form-0/g,"form-"+actividadAmount);
      // debugger;
      // $('.contenido-formset').append(templateHtml);
      // $('#id_form-' + actividadAmount + '-titulo').val("");
      // actividadAmountInput.val(actividadAmount + 1);
  });
});

function deleteThis(element) {
  $(element).parent().remove();
}

// function deleteActividad(element) {
//   $(element).parent().remove();
// }
