var initialLoad = true;
var defaultTemplateTag = "default-template";

$(function() {
  $('.add-contenido').hide();
  $('.send-form').hide();
  $('.no-patron').show();

  $(window).on('beforeunload', function() {
    $('#id_patron').val("");
  });

  $('#id_patron').click(function() {
    var idPatron = $(this).val();
    if (idPatron == "") {
      $('.add-contenido').hide();
      $('.send-form').hide();
      $('.no-patron').show();
    } else {
      $.ajax({
        type: 'GET',
        url: "patron",
        data: {
          "pk_patron": idPatron
        },
        success: function(result) {
          $('.contenido-form').remove();
          var newCont = $(result.replace(/[\r\n]/g, ""));
          var newHTML = '';
          for (var i = 0; i < newCont.length; i++) {
            newHTML += newCont[i].outerHTML.replace(new RegExp('form-' + i, 'g'), 'contenido_set-' + parseInt(i)).replace(/<( *)form( *) method="post"( *)>( *)/, '').replace(/<\/form>/, '');
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
        debugger;
        var contenidoAmountInput = $('#id_contenido_set-TOTAL_FORMS');
        var contenidoAmount = contenidoAmountInput.val();
        var newCont = result.replace(new RegExp('form-0', 'g'), 'contenido_set-' + parseInt(contenidoAmount)).replace(/<( *)form( *) method="post"( *)>( *)/, '').replace(/<\/form>/, '');
        $('.contenido-formset').append(newCont);
        $('#id_contenido_set-' + contenidoAmount + '-orden').val(parseInt(contenidoAmount) + 1);
        $('#id_contenido_set-' + contenidoAmount + '-titulo').val("");
        $('#id_contenido_set-' + contenidoAmount + '-descripcion').val("");
        contenidoAmountInput.val(parseInt(contenidoAmount) + 1);
      }
    });
  });

  $('.add-elementovof').click(function() {
    alert("add vof")
    $.ajax({
      type: 'GET',
      url: "elementovof",
      success: function(result) {
        debugger;
        var elementovofAmountInput = $('#id_elementovof_set-TOTAL_FORMS');
        var elementovofAmount = elementovofAmountInput.val();
        var newAct = result.replace(new RegExp('form-0', 'g'), 'elementovof_set-' + parseInt(elementovofAmount)).replace(/<( *)form( *) method="post"( *)>( *)/, '').replace(/<\/form>/, '');
        $('.elementovof-formset').append(newAct);
        elementovofAmountInput.val(parseInt(elementovofAmount) + 1);
      }
    });
  });

  $('.add-elementoordenamiento').click(function() {
    $.ajax({
      type: 'GET',
      url: "elementoordenamiento",
      success: function(result) {
        var elementoordenamientoAmountInput = $('#id_elementoordenamiento_set-TOTAL_FORMS');
        var elementoordenamientoAmount = elementoordenamientoAmountInput.val();
        var newAct = result.replace(new RegExp('form-0', 'g'), 'elementoordenamiento_set-' + parseInt(elementoordenamientoAmount)).replace(/<( *)form( *) method="post"( *)>( *)/, '').replace(/<\/form>/, '');
        $('.elementoordenamiento-formset').append(newAct);
        elementoordenamientoAmountInput.val(parseInt(elementoordenamientoAmount) + 1);
      }
    });
  });

  $('.add-elementoasociacion').click(function() {
    $.ajax({
      type: 'GET',
      url: "elementoasociacion",
      success: function(result) {
        var elementoasociacionAmountInput = $('#id_elementoasociacion_set-TOTAL_FORMS');
        var elementoasociacionAmount = elementoasociacionAmountInput.val();
        var newAct = result.replace(new RegExp('form-0', 'g'), 'elementoasociacion_set-' + parseInt(elementoasociacionAmount)).replace(/<( *)form( *) method="post"( *)>( *)/, '').replace(/<\/form>/, '');
        $('.elementoasociacion-formset').append(newAct);
        elementoasociacionAmountInput.val(parseInt(elementoasociacionAmount) + 1);
      }
    });
  });

  $('.add-elementoopcionmultiple').click(function() {
    $.ajax({
      type: 'GET',
      url: "elementoopcionmultiple",
      success: function(result) {
        var elementoopcionmultipleAmountInput = $('#id_elementoopcionmultiple_set-TOTAL_FORMS');
        var elementoopcionmultipleAmount = elementoopcionmultipleAmountInput.val();
        var newAct = result.replace(new RegExp('form-0', 'g'), 'elementoopcionmultiple_set-' + parseInt(elementoopcionmultipleAmount)).replace(/<( *)form( *) method="post"( *)>( *)/, '').replace(/<\/form>/, '');
        $('.elementoopcionmultiple-formset').append(newAct);
        elementoopcionmultipleAmountInput.val(parseInt(elementoopcionmultipleAmount) + 1);
      }
    });
  });

  $('.add-elementoidentificacion').click(function() {
    $.ajax({
      type: 'GET',
      url: "elementoidentificacion",
      success: function(result) {
        var elementoidentificacionAmountInput = $('#id_elementoidentificacion_set-TOTAL_FORMS');
        var elementoidentificacionAmount = elementoidentificacionAmountInput.val();
        var newAct = result.replace(new RegExp('form-0', 'g'), 'elementoidentificacion_set-' + parseInt(elementoidentificacionAmount)).replace(/<( *)form( *) method="post"( *)>( *)/, '').replace(/<\/form>/, '');
        $('.elementoidentificacion-formset').append(newAct);
        elementoidentificacionAmountInput.val(parseInt(elementoidentificacionAmount) + 1);
      }
    });
  });
});

function deleteThis(element) {
  $(element).parent().remove();
}
// $('.send-form').click(function(element){
//   alert("submit");
//   debugger;
// });

// $.ajax({
//   type: 'GET',
//   url: "actividad",
//   success: function(result) {
//     var template = result.replace(/[\r\n]/g,"").replace(/form-0/g,"form-"+defaultTemplateTag).replace(/<form  method="post" >/,'').replace(/<\/form>/,'');
//     $('.actividad-template').append(result).hide();
//   }
// });

// var actividadAmountInput = $('#id_actividad_set-TOTAL_FORMS');
// var actividadAmount = actividadAmountInput.val();
// var templateHtml = $('.actividad-template').html();
// var regexp = new RegExp("form-"+defaultTemplateTag,'g');
// var newActividad = templateHtml.replace(regexp,actividadAmount).replace(/[\r\n]/g,"");
// $('.actividad-formset').append(newActividad).show();
// actividadAmountInput.val(parseInt(actividadAmount) + 1);
// var template = $('.contenido-formset').find('.contenido-form')[0];
// var templateHtml = template.outerHTML;
// templateHtml = templateHtml.replace(/form-0/g,"form-"+actividadAmount);
// debugger;
// $('.contenido-formset').append(templateHtml);
// $('#id_form-' + actividadAmount + '-titulo').val("");
// actividadAmountInput.val(actividadAmount + 1);



// function deleteActividad(element) {
//   $(element).parent().remove();
// }
