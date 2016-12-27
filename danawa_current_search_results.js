// Martin Kersner, m.kersner@gmail.com
// 2016/09/07 
//
// Render website and take screenshot of it.

var interval = 1000;
var page = require('webpage').create();

page.open('http://search.danawa.com/dsearch.php?k1=iphone', function() {
  setTimeout(function() {
    page.render('shapes.png');
    phantom.exit();
  }, interval);
});
