function move_handler(move_type) {
  var delta = (move_type === "move-forward-") ? 1 : -1;
  return function inner() {
    var id_string = $(this).attr('id').replace(move_type, '');
    var post_data = {'id': parseInt(id_string, 10),
      'step': delta};
    $.ajax({
      url: '/task/update_step/',
      type: 'post',
      data: JSON.stringify(post_data),
      success: function (stepped) {
        if (stepped !== "") {
          $('#task-' + id_string).replaceWith(stepped);
          //$('#' + move_type + id_string).click(inner);
          $('#move-forward-' + id_string).click(move_forward_handler); //TODO
          $('#move-backward-' + id_string).click(move_backward_handler);
        }
      }
    });
    return false;
  };
}

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

//function move_forward_handler() {
//  var id_string = $(this).attr('id').replace('move-forward-', '');
//  var post_data = {'id': parseInt(id_string, 10),
//                   'step': 1};
//  $.ajax({
//    url: '/task/update_step/',
//    type: 'post',
//    data: JSON.stringify(post_data),
//    success: function (stepped) {
//      if (stepped !== "") {
//        $('#task-' + id_string).replaceWith(stepped);
//        $('#move-forward-' + id_string).click(move_forward_handler);
//      }
//    }
//  });
//  return false;
//}

var move_forward_handler = move_handler('move-forward-');
var move_backward_handler = move_handler('move-backward-');


function move_select_forward() {
  $('.task-item').each(function () {
    if ($(this).find('input').is(':checked')) {
      move_forward_handler.apply($(this).find('.move-forward'));
    }
  });
  return false;
}


function move_select_backward() {
  $('.task-item').each(function () {
    if ($(this).find('input').is(':checked')) {
      move_backward_handler.apply($(this).find('.move-backward'));
    }
  });
  return false;
}


$(document).ready(function () {
  $('#delete-select-task').click(delete_task_handler);
  $('#move-select-forward').click(move_select_forward);
  $('#move-select-backward').click(move_select_backward);
  $('#select-all-tasks').click(function () {
    var status = $(this).is(':checked');
    $('#task-list input').each(function () {
      $(this).attr('checked', status);
    });
  });
  $('.move-forward').click(move_forward_handler);
  $('.move-backward').click(move_backward_handler);
});
