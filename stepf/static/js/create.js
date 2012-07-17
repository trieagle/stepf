$(document).ready(function () {
  $('#step').show();
  $('#alarm-time').hide();
  $('#frequence').show();
 
  $('#alarm-time-input').datetimepicker();
  $('#create-type').click(function () {
    $('#step').hide();
    $('#alarm-time').hide();
    $('#frequence').hide();
    var target = $(this).val();
    switch (target) {
    case "task":
      $('#step').show();
      $('#frequence').show();
      break;
    case "note":
      break;
    case "reminder":
      $('#alarm-time').show();
      break;
    }
  });
  $('#create-confirm').click(function () {
    function create_task() {
      var post_data = {
        title: $('#title-input').val(),
        nstep: parseInt($('#step-input').val(), 10),
        frequence: parseInt($('#freq-input').val(), 10)
      };
      $.ajax({
        url: '/task/create_task/',
        type: 'post',
        dataType: 'json',
        data: JSON.stringify(post_data),
        success: function (ret_task) {
          $('#task-list').append(ret_task);
        }
      });
    }

    function create_note() {
      var post_data = {
        title: $('#title-input').val()
      };
      $.ajax({
        url: '/note/create_note/',
        type: 'post',
        dataType: 'json',
        data: JSON.stringify(post_data),
        success: function (ret_note) {
          $('#note-list').append(ret_note);
        }
      });
    }

    function create_reminder() {
      var post_data = {
        title: $('#title-input').val(),
        alarm_time: $('#alarm-time-input').val()
      };
      $.ajax({
        url: '/reminder/create_reminder/',
        type: 'post',
        dataType: 'json',
        data: JSON.stringify(post_data),
        success: function (ret_reminder) {
          $('#reminder-list').append(ret_reminder);
        }
      });
    }
    var target = $('#create-type').val();
    switch (target) {
    case 'task':
      create_task();
      break;
    case 'note':
      create_note();
      break;
    case 'reminder':
      create_reminder();
      break;
    }
  });
});
