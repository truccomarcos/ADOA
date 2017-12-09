var initialLoad = true;
var defaultTemplateTag = "default-template";

$(document).ready(function() {
  if (initialLoad) {
    $('#id_patron').val("");
  }
  initialLoad = false;
});

$(function() {
  $('#id_patron').click(function() {
    var idPatron = $(this).val();
    $.ajax({
      type: 'GET',
      url: "patron/" + idPatron,
      success: function(result) {
        $('.contenido-formset').empty();
        $('.contenido-formset').append(result);
        var template = $('.contenido-formset').find('.contenido-form')[0];
        var templateHtml = template.outerHTML;
        templateHtml = templateHtml.replace(/form-0/g,"form-"+defaultTemplateTag)
                            .replace("contenido-form","contenido-form-template");
        $('.contenido-formset').append(templateHtml);
        $('.contenido-formset').find('.contenido-form-template').hide();
        var formAmount = $('.contenido-formset').find('contenido-form').length;
        $('.form-amount').val(formAmount);


        // var formset = $($.parseHTML(result));
        // var formsetHtml;
        // for(i=0; i < formset.length-2; i++){
        //   formsetHtml += $(formset[i]).html();
        // }
        // var templateHtml = $(formset[formset.length-2]).html();
        // templateHtml = templateHtml.replace("id_form-" + 0 + "-titulo", "id_form-" + defaultTemplateTag + "-titulo")
        //                     .replace("form-" + 0 + "-titulo", "form-" + defaultTemplateTag + "-titulo")
        //                     .replace("id_form-" + 0 + "-descripcion", "id_form-" + defaultTemplateTag + "-descripcion")
        //                     .replace("form-" + 0 + "-descripcion", "form-" + defaultTemplateTag + "-descripcion")
        //                     .replace("id_form-" + 0 + "-contenido", "id_form-" + defaultTemplateTag + "-contenido")
        //                     .replace("form-" + 0 + "-contenido", "form-" + defaultTemplateTag  + "-contenido")
        //                     .replace("id_form-" + 0 + "-orden", "id_form-" + defaultTemplateTag + "-orden")
        //                     .replace("form-" + 0 + "-orden", "form-" + defaultTemplateTag + "-orden")
        //                     .replace("id_form-" + 0 + "-id", "id_form-" + defaultTemplateTag + "-id");
        // var formAmount = formset.find('contenido-form').length;
        // $('.contenido-formset').append(formsetHtml);
        // $('.contenido-formset').append(templateHtml);
      }
    })
  });
  // $('.add-contenido').click(function() {
  //     alert("Add contenido");
  //     debugger;
  //     var formAmountInput = $('.form-amount');
  //     var formAmount = formAmountInput.val()
  //     var template = $('.contenido-form-template');
  //     var templateHtml = template.html();
  //     templateHtml = templateHtml.replace("id_form-" + (formAmount - 1) + "-titulo", "id_form-" + formAmount + "-titulo")
  //                     .replace("form-" + (formAmount - 1) + "-titulo", "form-" + formAmount + "-titulo")
  //                     .replace("id_form-" + (formAmount - 1) + "-descripcion", "id_form-" + formAmount + "-descripcion")
  //                     .replace("form-" + (formAmount - 1) + "-descripcion", "form-" + formAmount + "-descripcion")
  //                     .replace("id_form-" + (formAmount - 1) + "-contenido", "id_form-" + formAmount + "-contenido")
  //                     .replace("form-" + (formAmount - 1) + "-contenido", "form-" + formAmount  + "-contenido")
  //                     .replace("id_form-" + (formAmount - 1) + "-orden", "id_form-" + formAmount + "-orden")
  //                     .replace("form-" + (formAmount - 1) + "-orden", "form-" + formAmount + "-orden")
  //                     .replace("id_form-" + (formAmount - 1) + "-id", "id_form-" + formAmount + "-id");
  //     template.remove();
  //     ('.contenido-formset').append(templateHtml.replace('contenido-form-template','contenido-form')
  //                                     .replace('hidden',''));
  //     ('.contenido-formset').append(templateHtml);
  //     formAmountInput.val(formAmount + 1);
  // });
});

function deleteContenido(element) {
  $(element).parent().remove();
}
