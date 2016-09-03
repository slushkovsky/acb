$(function() {
      $('select[name="routes[]"]').select2({
            tags: [
                  'Марьино', 
                  'Большая ордынка', 
                  'Любнино', 
                  'Пялово',
                  'Косино',
                  'Варшавский'
            ],
            multiple: true, 
            placeholder: 'Маршрут' 
      });
      $('#new-car').click(function() {
            $('#modal-add-car').modal('show');
      });
});

