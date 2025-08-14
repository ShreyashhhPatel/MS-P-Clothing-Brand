$(document).ready(function () {
  // Home Page Images Fade-In
  $("#home-content .images-container img").each(function (index) {
    $(this)
      .delay(500 * index)
      .animate({ opacity: 1 }, 1500, function() {
        $(this).addClass('fade-in');
      });
  });

  // Text and Description Animations
  $("#home-content .text").delay(1000).animate({ opacity: 1 }, 2000, function() {
    $(this).addClass('fade-in');
  });

  // Polo Page Animations
  $("#polo-content .text")
    .delay(1000)
    .animate({ opacity: 1 }, 2000)
    .addClass('fade-in');

  // Polo Page Slider Functionality
  var slides = $('#polo-slider li');
  var x = 0;

  slides.hide();
  slides.eq(x).addClass('active').show();

  setInterval(function () {
    slides.eq(x).removeClass('active').hide();
    x = (x + 1) % slides.length;
    slides.eq(x).addClass('active').show();
  }, 3000);

  // Suits Page Animation (Optional Fade-In)
  $("#suits-content .suits-image").delay(500).animate({ opacity: 1 }, 1000).addClass('fade-in');

  // Navigation bar click events
  $('.nav .title').on('click', function (e) {
    // Check if the link has an external href (e.g., "user.html")
    var href = $(this).attr('href');
    if (href && href !== '#') {
      return; // Allow default navigation for external links
    }
  
    e.preventDefault(); // Prevent default action for internal navigation
    var pageIndex = parseInt($(this).attr('data-page'));
    var pageHeight = $('.page').outerHeight();
    var scrollPosition = pageIndex * pageHeight;
  
    $('.content').animate({ scrollTop: scrollPosition }, 1000);
  });
  

  // Contact Form Submission (optional)
  $('#contact-form').on('submit', function (e) {
    e.preventDefault();
    // Here you can add code to handle form submission,
    // such as sending the data to a server via AJAX.
    alert('Thank you for your feedback!');
    $(this)[0].reset();
  });
});
