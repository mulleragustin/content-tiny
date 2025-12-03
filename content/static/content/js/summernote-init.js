// Inicialización de Summernote para el editor HTML
(function () {
  // Esperar a que jQuery esté disponible
  var $ = window.jQuery || window.django?.jQuery;

  if (!$) {
    console.error("jQuery no está disponible para Summernote");
    return;
  }

  $(document).ready(function () {
    // Verificar que Summernote esté cargado
    if (typeof $.fn.summernote === "undefined") {
      console.error("Summernote no está cargado");
      return;
    }

    // Inicializar Summernote en el campo descripcion
    var $descripcion = $("#id_descripcion");

    if ($descripcion.length) {
      $descripcion.summernote({
        height: 400,
        lang: "es-ES",
        placeholder: "Escribe el contenido aquí...",
        toolbar: [
          ["style", ["style"]],
          ["font", ["bold", "underline", "italic", "strikethrough", "clear"]],
          ["fontname", ["fontname"]],
          ["fontsize", ["fontsize"]],
          ["color", ["color"]],
          ["para", ["ul", "ol", "paragraph"]],
          ["height", ["height"]],
          ["table", ["table"]],
          ["insert", ["link", "picture", "video", "hr"]],
          ["view", ["fullscreen", "codeview", "help"]],
        ],
        styleTags: ["p", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "pre"],
        callbacks: {
          onChange: function (contents, $editable) {
            // Sincronizar el contenido con el textarea original
            $descripcion.val(contents);
          },
        },
      });
    }
  });
})();
