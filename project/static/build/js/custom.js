jQuery(document).ready(function(){
  jQuery('#demo1').skdslider({'delay':5000, 'animationSpeed': 2000,'showNextPrev':true,'showPlayButton':true,'autoSlide':true,'animationType':'fading'});

  jQuery('#responsive').change(function(){
    $('#responsive_wrapper').width(jQuery(this).val());
  });

});
