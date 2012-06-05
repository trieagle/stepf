function delete_task_handler() {
  $('.task-item').each(function () {
    if ($(this).find('input').is(':checked')) {
      var id_string = $(this).attr('id').replace('task-', '');
      var post_data = {'id': parseInt(id_string, 10)};
      $.ajax({
        url: '/task/remove_task/',
        type: 'post',
        dataType: 'json',
        data: JSON.stringify(post_data),
        success: function (removed) {
          if (removed) {
            $('#task-' + id_string).remove();
          }
        }
      });
    }
  });
  return false;
}

$(document).ready(function () {
  $('#delete-select-task').click(delete_task_handler);
  $('#select-all-tasks').click(function () {
    var status = $(this).is(':checked');
    $('#task-list input').each(function () {
      $(this).attr('checked', status);
    });
  });
});
