function hideAllPublications() {
 $('#publications_list div').hide(); 
 $('a.year').removeClass("active");
}

function showPublication(){
  $('#publications_header a.year').click(function(){
  hideAllPublications();
  $(this).addClass("active");
  $('#publications_list #publications_' + $(this).attr('data-year')).show();
});
}

$(showPublication);