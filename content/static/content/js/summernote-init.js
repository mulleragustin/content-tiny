// Inicialización de Summernote para el editor HTML
(function ($) {
  $(document).ready(function () {
    // Inicializar Summernote en el campo descripcion
    $("#id_descripcion").summernote({
      height: 400,
      toolbar: [
        ["style", ["style"]],
        ["font", ["bold", "underline", "italic", "clear"]],
        ["fontname", ["fontname"]],
        ["fontsize", ["fontsize"]],
        ["color", ["color"]],
        ["para", ["ul", "ol", "paragraph"]],
        ["table", ["table"]],
        ["insert", ["link", "picture", "video"]],
        ["view", ["fullscreen", "codeview", "help"]],
      ],
      callbacks: {
        onChange: function (contents, $editable) {
          // Sincronizar el contenido con el textarea original
          $("#id_descripcion").val(contents);
        },
      },
    });
  });
})(django.jQuery || jQuery);
