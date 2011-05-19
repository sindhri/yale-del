function hideAllPublications() {
 $('#publications_2011').hide(); 
 $('#publications_2010').hide();
 $('#publications_2009').hide();
 $('#publications_early').hide();
 
 $('#publications_2011_header').attr("style","color: #666666;font-weight:normal;");
 $('#publications_2010_header').attr("style","color: #666666;font-weight:normal;");
 $('#publications_2009_header').attr("style","color: #666666;font-weight:normal;");
 $('#publications_early_header').attr("style","color: #666666;font-weight:normal;");
}

function showPublication(name) {
  hideAllPublications();
  $(name).show();
  $(name + '_header').attr("style","color: #000000;font-weight:bold;");
}

