var gulp = require('gulp');
var sass = require('gulp-sass');
var browserify = require('gulp-browserify');

var jcmsPath = 'jcms/';
var jcmsSource = 'src/';
var jcmsStatic = jcmsPath + 'static/';

//Watch task
// gulp.task('default',function() {
//     gulp.watch('sass/**/*.scss',['styles']);
// });

gulp.task('default', function() {

    // Load all dependency's
    gulp.src(jcmsSource + 'scss/jcms.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('static/'));

    gulp.src(jcmsSource + 'js/jcms.js')
        .pipe(browserify({
            insertGlobals : true
        }))
        .pipe(gulp.dest(jcmsStatic));
});
