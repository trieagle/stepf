String.prototype.format = function () {
  var formatted = this;
  var i;
  for (i = 0; i < arguments.length; i = i + 1) {
    formatted = formatted.replace("{" + i + "}", arguments[i].toString());
  }
  return formatted;
};


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
          var task = ret_task[0];
          var html_data = '<li id={0} class="task-item">\
                           <div>\
                             <input type="checkbox"></input>\
                             <a>{1}</a>\
                             <a href="#">==></a>\
                           </div>\
                           <div>\
                              <label>{2}/{3}</label>\
                              <label>diary</label>\
                           </div></li>';
          html_data = html_data.format("task-" + task.pk,
                                       task.fields.title,
                                       task.fields.curr_step,
                                       task.fields.nstep);
          $('#task-list').append(html_data);
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
          var note = ret_note[0];
          var html_data = '<li id={0}>\
                             <p>{1}</p>\
                             <a class="delete-note" id={2} href="#" class title="remove this note">delete</a>\
                             <span class="lsep">|</span>\
                             <a class="done-note" id={3} href="#" class title="done this note">done</a>\
                          </li>';
          html_data = html_data.format("note-" + note.pk,
                                       note.fields.title,
                                       "delete-note-" + note.pk,
                                       "done-note-" + note.pk);
          $('#note-list').append(html_data);
          $('#delete-note-' + note.pk).click(delete_note_handler);
          $('#done-note-' + note.pk).click(done_note_handler);
        }
      });
    }

    function create_reminder() {
      var post_data = {
        title: $('#title-input').val(),
        alarm_time: '2012/6/10 10:10' //FIXME
      };
      $.ajax({
        url: '/reminder/create_reminder/',
        type: 'post',
        dataType: 'json',
        data: JSON.stringify(post_data),
        success: function (ret_reminder) {
          var reminder = ret_reminder[0];
          var html_data = '<li id={0}>\
                           <div>\
                             <p>{1}</p>\
                             <a class="delete-reminder" id={2} href="" class title="remove this reminder">delete</a>\
                             <span class="lsep">|</span>\
                             <a class="done-reminder" id={3} href="" class title="done this reminder">done</a>\
                           </div>\
                           <div>\
                           <label>Time:<label>\
                           <p>{4}</p>\
                           </div>\
                           </li>';
          html_data = html_data.format("reminder-" + reminder.pk,
                                       reminder.fields.title,
                                       "delete-reminder-" + reminder.pk,
                                       "done-reminder-" + reminder.pk,
                                       reminder.fields.alarm_time);
          $('#reminder-list').append(html_data);
          $('#delete-reminder-' + reminder.pk).click(delete_reminder_handler);
          $('#done-reminder-' + reminder.pk).click(done_reminder_handler);
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
