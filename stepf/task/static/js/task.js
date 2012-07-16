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

function update_message(msg_id, msg_content) {
  var post_msg = {
    id: msg_id,
    content: msg_content
  };
  $.ajax({
    url: '/task/update_message/',
    type: 'post',
    dataType: 'json',
    data: JSON.stringify(post_msg),
    success: function (updated) {
      if (updated) {
        $('#message-' + msg_id.toString()).hide();
      }
    }
  });
}

function task_move(task_id, move_step) {
  var post_task_move = {
    'id': task_id,
    'step': move_step
  };
  $.ajax({
    url: '/task/update_step/',
    type: 'post',
    data: JSON.stringify(post_task_move),
    success: function (stepped) {
      if (stepped !== "") {
        $('#task-' + task_id.toString()).replaceWith(stepped);
        $('.message').hide();
      }
    }
  });
  return false;
}

function task_update_nstep(task_id, nstep_delta) {
  var post_task_nstep = {
    id: task_id,
    step: nstep_delta
  };
  $.ajax({
    url: 'task/update_nstep/',
    type: 'post',
    data: JSON.stringify(post_task_nstep),
    success: function (stepped) {
      if (stepped !== "") {
        $('#task-' + task_id.toString()).replaceWith(stepped);
        $('.message').hide();
      }
    }
  });
  return false;
}

function move_select_forward() {
  $('.task-item').each(function () {
    if ($(this).find('input').is(':checked')) {
      task_move(parseInt($(this).attr('id').replace('task-', ''), 10), 1);
    }
  });
  return false;
}

function move_select_backward() {
  $('.task-item').each(function () {
    if ($(this).find('input').is(':checked')) {
      task_move(parseInt($(this).attr('id').replace('task-', ''), 10), -1);
    }
  });
  return false;
}

$(document).ready(function () {
  document.getElementById("task-list").addEventListener("click", function (e) {
    if (!e.target) {
      return;
    }
    if (e.target.className.indexOf("step-past") !== -1) {
      $('.message').hide();
      if ($(e.target).parent().find('div')) {
        $(e.target).parent().find('div').show();
      }
      return;
    }
    if (e.target.className.indexOf("message-update-confirm") !== -1) {
      update_message(parseInt(e.target.id.replace('msg-ok-', ''), 10),
                     $(e.target).parent().find('textarea').val());
      return;
    }
    switch (e.target.className) {
    case "move-forward":
      task_move(parseInt(e.target.id.replace('move-forward-', ''), 10), 1);
      break;
    case "move-backward":
      task_move(parseInt(e.target.id.replace('move-backward-', ''), 10), -1);
      break;
    case "inc-nstep":
      task_update_nstep(parseInt(e.target.id.replace('inc-nstep-', ''), 10), 1);
      break;
    case "dec-nstep":
      task_update_nstep(parseInt(e.target.id.replace('dec-nstep-', ''), 10), -1);
      break;
    }
  });

  $('#delete-select-task').click(delete_task_handler);
  $('#move-select-forward').click(move_select_forward);
  $('#move-select-backward').click(move_select_backward);
  $('#select-all-tasks').click(function () {
    var status = $(this).is(':checked');
    $('#task-list input').each(function () {
      $(this).attr('checked', status);
    });
  });
  $('.message').hide();
});
