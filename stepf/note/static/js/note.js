function delete_note_handler() {
  var id_string = $(this).attr('id').replace('delete-note-', '');
  var post_data = {'id': parseInt(id_string, 10)};
  $.ajax({
    url: '/note/remove_note/',
    type: 'post',
    dataType: 'json',
    data: JSON.stringify(post_data),
    success: function (removed) {
      if (removed) {
        $('#note-' + id_string).remove();
      }
    }
  });
  return false;
}

function done_note_handler() {
  var id_string = $(this).attr('id').replace('done-note-', '');
  var post_data = {'id': parseInt(id_string, 10)};
  $.ajax({
    url: '/note/done_note/',
    type: 'post',
    dataType: 'json',
    data: JSON.stringify(post_data),
    success: function (done) {
      if (done) {
        $('#note-' + id_string).remove();
      }
    }
  });
  return false;
}

$(document).ready(function () {
  $('.delete-note').each(function () {
    $(this).click(delete_note_handler);
  });

  $('.done-note').each(function () {
    $(this).click(done_note_handler);
  });
});
