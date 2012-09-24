function hideAllPublications() {
$('#publications_list').children('div').hide();
 $('a.year').removeClass("active");
}

function showPublication(){
  $('#publications_header a.year').click(function(){
  hideAllPublications();
  $(this).addClass("active");
  $('#publications_list #publications_' + $(this).attr('data-year')).show();
});
}

function hideAlumni(){
  $('#alumni_list').hide();
}

function showAlumni(){
  $('#alumni_list a').click(function(){
    $('alumni_list').show();
  })
}

$(showPublication);