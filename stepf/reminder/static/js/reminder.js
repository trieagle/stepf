function delete_reminder(reminder_id) {
  var post_delete_reminder = {'id': reminder_id};
  $.ajax({
    url: '/reminder/remove_reminder/',
    type: 'post',
    dataType: 'json',
    data: JSON.stringify(post_delete_reminder),
    success: function (removed) {
      if (removed) {
        $('#reminder-' + reminder_id.toString()).remove();
      }
    }
  });
  return false;
}

function done_reminder(reminder_id) {
  var post_done_reminder = {'id': reminder_id};
  $.ajax({
    url: '/reminder/done_reminder/',
    type: 'post',
    dataType: 'json',
    data: JSON.stringify(post_done_reminder),
    success: function (done) {
      if (done) {
        $('#reminder-' + reminder_id.toString()).remove();
      }
    }
  });
  return false;
}

$(document).ready(function () {
  document.getElementById("reminder-list").addEventListener("click", function (e) {
    if (!e.target) {
      return;
    }
    switch (e.target.className) {
    case "delete-reminder":
      delete_reminder(parseInt(e.target.id.replace('delete-reminder-', ''), 10));
      break;
    case "done-reminder":
      done_reminder(parseInt(e.target.id.replace('done-reminder-', ''), 10));
      break;
    }
  });
});
