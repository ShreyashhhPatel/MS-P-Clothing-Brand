$(document).ready(function () {
    // Check if an element is in the viewport
    function isInViewport(element) {
      const elementTop = $(element).offset().top;
      const elementBottom = elementTop + $(element).outerHeight();
      const viewportTop = $(window).scrollTop();
      const viewportBottom = viewportTop + $(window).height();
  
      return elementBottom > viewportTop + $(window).height() * 0.5 &&
             elementTop < viewportBottom - $(window).height() * 0.5;
    }
  
    // Animate elements when in the viewport
    function animateElements() {
      $('.page').each(function () {
        if (isInViewport(this)) {
          $(this).find('.text-content').addClass('animated');
          $(this).find('.side-image.left').addClass('animated');
          $(this).find('.side-image.right').addClass('animated');
          $(this).find('.scroll-button').addClass('animated');
        }
      });
    }
  
    // Initial animation check
    animateElements();
  
    // Debounce to improve scroll performance
    function debounce(func, wait, immediate) {
      let timeout;
      return function () {
        const context = this, args = arguments;
        const later = function () {
          timeout = null;
          if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
      };
    }
  
    // Scroll event
    $(window).on('scroll', debounce(function () {
      animateElements();
    }, 100));
  
    // Scroll button functionality
    $('.scroll-button').on('click', function (e) {
      e.preventDefault();
      const target = $(this).attr('href');
      const targetSection = $(target);
      if (targetSection.length) {
        $('html, body').animate({ scrollTop: targetSection.offset().top }, 800);
      }
    });
  });
  