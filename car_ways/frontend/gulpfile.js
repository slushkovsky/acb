var STATIC    = __dirname + '/../static/',
    TEMPLATES = __dirname + '/../templates/';

var gulp         = require('gulp'),
    stylus       = require('gulp-stylus'),
    pug          = require('gulp-pug'),
    autoprefixer = require('gulp-autoprefixer'),
    bower        = require('gulp-bower'), 
    imagemin     = require('gulp-imagemin'),
    plugins      = require('gulp-load-plugins')();
    del          = require('del');


gulp.task('build-partner', require('./partner/gulp-tasks')(gulp, plugins, {
	pug:    TEMPLATES + 'partner/',
	stylus: STATIC    + 'partner/', 
	img:    STATIC    + 'partner/img',
	js:     STATIC    + 'partner/js'
}))

gulp.task('bower', function() {
	return bower().on('error', console.log)
           .pipe(gulp.dest(STATIC + 'components/'));
});

gulp.task('build', ['build-partner', 'bower']);

gulp.task('clean', function() {
	del.sync([STATIC, TEMPLATES], {force: true});
});

gulp.task('rebuild', ['clean', 'build']);
