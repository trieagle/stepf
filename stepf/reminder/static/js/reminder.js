$(document).ready(function () {
  $('.delete-reminder').each(function () {
    $(this).click(function () {
      var id_string = $(this).attr('id').replace('delete-reminder-', '');
      var post_data = {'id': parseInt(id_string, 10)};
      $.ajax({
        url: '/reminder/remove_reminder/',
        type: 'post',
        dataType: 'json',
        data: JSON.stringify(post_data),
        success: function (removed) {
          if (removed) {
            $('#reminder-' + id_string).remove();
          }
        }
      });
      return false;
    });
  });

  $('.done-reminder').each(function () {
    $(this).click(function () {
      var id_string = $(this).attr('id').replace('done-reminder-', '');
      var post_data = {'id': parseInt(id_string, 10)};
      $.ajax({
        url: '/reminder/done_reminder/',
        type: 'post',
        dataType: 'json',
        data: JSON.stringify(post_data),
        success: function (done) {
          if (done) {
            $('#reminder-' + id_string).remove();
          }
        }
      });
      return false;
    });
  });
});
