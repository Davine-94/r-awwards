$(document).ready(function(){

      
  const projectId = document.location.pathname.split('/')[2];

  $.ajax({
      type: 'GET',
      url: `/api/v1/projects/${projectId}/ratings/`,
      success: function (data) {
          alert(data);
      },
      error: function (data) {
        //   alert('An error occurred.');
      },
  });
  
  var frm = $('#ratingForm');

  frm.submit(function (e) {

      e.preventDefault();

      $.ajax({
          type: frm.attr('method'),
          url: frm.attr('action'),
          data: frm.serialize(),
          success: function (data) {
              alert('Submission was successful.');
  
          },
          error: function (data) {
            //   alert('An error occurred.');
          },
      });
  });

    // $("#ratingForm").hide();
  
    // $("#voteBtn").click(function () {
    //   $("#voteBtn").hide();
    //   $("#ratingForm").show();
    // });

    // $("#rateBtn").click(function () {
    //     $("#ratingForm").hide();
    //     $("#voteBtn").show();
    //   });

});