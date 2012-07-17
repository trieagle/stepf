function delete_note(note_id) {
  var post_delete_note = {'id': note_id};
  $.ajax({
    url: '/note/remove_note/',
    type: 'post',
    dataType: 'json',
    data: JSON.stringify(post_delete_note),
    success: function (removed) {
      if (removed) {
        $('#note-' + note_id.toString()).remove();
      }
    }
  });
  return false;
}

function done_note(note_id) {
  var post_done_note = {'id': note_id};
  $.ajax({
    url: '/note/done_note/',
    type: 'post',
    dataType: 'json',
    data: JSON.stringify(post_done_note),
    success: function (done) {
      if (done) {
        $('#note-' + note_id).remove();
      }
    }
  });
  return false;
}

$(document).ready(function () {
  document.getElementById("note-list").addEventListener("click", function (e) {
    if (!e.target) {
      return;
    }
    switch (e.target.className) {
    case "delete-note":
      delete_note(parseInt(e.target.id.replace('delete-note-', ''), 10));
      break;
    case "done-note":
      done_note(parseInt(e.target.id.replace('done-note-', ''), 10));
      break;
    }
  });
});
