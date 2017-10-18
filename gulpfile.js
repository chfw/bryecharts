// reference
// https://codehangar.io/concatenate-and-minify-javascript-with-gulp/


var gulp = require('gulp');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');
var cleanCSS = require('gulp-clean-css');
var autoprefixer = require('gulp-autoprefixer');

//script paths
var jsFiles = [
  'public/js/brython.js',
  'public/js/pyecharts.js',
  'public/js/jquery.2.2.4.min.js',
  'public/js/jquery.ui.1.12.1.js',
  'public/js/popper-1.11.0.min.js',
  'public/js/bootstrap.4.0.0.beta.min.js',
  'public/js/jquery.layout.1.4.3.min.js',
  'public/js/startup.js'
];
var  jsDest = 'public/prd';

gulp.task('css', function(){
gulp.src('public/css/*.css')
    .pipe(cleanCSS())
    .pipe(autoprefixer('last 2 version', 'safari 5', 'ie 8', 'ie 9'))
    .pipe(concat('style.min.css'))
	.pipe(gulp.dest(jsDest));
});

gulp.task('default', ['css'], function() {
    return gulp.src(jsFiles)
    .pipe(concat('scripts.js'))
    .pipe(gulp.dest(jsDest))
	.pipe(rename('scripts.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest(jsDest));
});
