/*
Template Name: Vegishop - Online Grocery Supermarket HTML Template
Author: Gurdeep Osahan
Author URI: https://wrapbootstrap.com/user/gurdeep
Version: 1.0
*/

(function($) {
"use strict"; // Start of use strict

// Tooltip
$('[data-toggle="tooltip"]').tooltip();

// Categories Slider
$('.categories-slider').slick({
  slidesToScroll: 3,
  slidesToShow: 8,
  arrows: true,
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 3
      }
    }
  ]
});

// Categories Slider
$('.promo-slider').slick({
  slidesToShow: 3,
  arrows: true,
  dots: true,
  infinite: true,
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 1
      }
    }
  ]
});

// Osahan Slider
$('.osahan-slider').slick({
  centerMode: false,
  slidesToShow: 1,
  arrows: false,
  dots: true
});

// Recommend Slider
$('.recommend-slider2').slick({
  infinite: true,
  speed: 300,
  slidesToShow: 1,
  adaptiveHeight: true,
  centerMode: true,
  arrows: false,
  dots: true,
  autoplay: true
  
});

// Recommend Slider
$('.recommend-slider').slick({
  infinite: true,
  speed: 300,
  slidesToShow: 1,
  adaptiveHeight: true,
  arrows: false,
  dots: true,
  autoplay: true
});

// Trending Slider
$('.trending-slider').slick({
  centerPadding: '30px',
  slidesToShow: 4,
  arrows: true,
  autoplay: true,
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: true,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: true,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 1
      }
    }
  ]
});

// Sidebar
var $main_nav = $('#main-nav');
  var $toggle = $('.toggle');

  var defaultOptions = {
      disableAt: false,
      customToggle: $toggle,
      levelSpacing: 40,
      navTitle: 'gurdeeposahan',
      levelTitles: true,
      levelTitleAsBack: true,
      pushContent: '#container',
      insertClose: 2
  };

// call our plugin
var Nav = $main_nav.hcOffcanvasNav(defaultOptions);  

// Dark Mode
const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    document.documentElement.setAttribute('class', currentTheme);
  
    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
    }
}
function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('class', 'dark');
        localStorage.setItem('theme', 'dark');
    }
    else {        document.documentElement.setAttribute('class', 'light');
          localStorage.setItem('theme', 'light');
    }    
}
toggleSwitch.addEventListener('change', switchTheme, false);

})(jQuery); // End of use strict

// Quantity JS
jQuery(document).ready(function(){
  // This button will increment the value
  $('.qtyplus').click(function(e){
      // Stop acting like a button
      e.preventDefault();
      // Get the field name
      fieldName = $(this).attr('field');
      // Get its current value
      var currentVal = parseInt($('input[name='+fieldName+']').val());
      // If is not undefined
      if (!isNaN(currentVal)) {
          // Increment
          $('input[name='+fieldName+']').val(currentVal + 1);
      } else {
          // Otherwise put a 0 there
          $('input[name='+fieldName+']').val(1);
      }
  });
  // This button will decrement the value till 0
  $(".qtyminus").click(function(e) {
      // Stop acting like a button
      e.preventDefault();
      // Get the field name
      fieldName = $(this).attr('field');
      // Get its current value
      var currentVal = parseInt($('input[name='+fieldName+']').val());
      // If it isn't undefined or its greater than 0
      if (!isNaN(currentVal) && currentVal > 1) {
          // Decrement one
          $('input[name='+fieldName+']').val(currentVal - 1);
      } else {
          // Otherwise put a 0 there
          $('input[name='+fieldName+']').val(1);
      }
  });
});