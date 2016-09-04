var STATIC    = __dirname + '/../static',
    TEMPLATES = __dirname + '/../templates';

var gulp         = require('gulp'),
    stylus       = require('gulp-stylus'),
    pug          = require('gulp-pug'),
    autoprefixer = require('gulp-autoprefixer'),
    bower        = require('gulp-bower'),
    imagemin     = require('gulp-imagemin'),
    concat       = require('gulp-concat'),
    uglify       = require('gulp-uglify'),
    indent       = require('gulp-indent'),
    del          = require('del'), 
    inject       = require('gulp-inject');


gulp.task('build', function() {
    gulp.src(__dirname + '/pages/**/[!_]*.pug')  
        .pipe(pug()).on('error', console.log)
        .pipe(gulp.dest(TEMPLATES));

    gulp.src(__dirname + '/pages/**/*.styl')
        .pipe(indent({tabs: false, amount: 4}))
        .pipe(stylus({compress: true})).on('error', console.log)
        .pipe(autoprefixer())
        .pipe(gulp.dest(STATIC));

    gulp.src(__dirname + '/img/**/*.{png,jpg,jpeg,gif}')
        .pipe(imagemin())
        .pipe(gulp.dest(STATIC + '/img'));

    gulp.src(__dirname + '/js/**/*.js')
        .pipe(gulp.dest(STATIC + '/js'));

    // gulp.src(__dirname + '/js/**/*.js')
    //     .pipe(uglify())
    //     .pipe(concat('scripts.js'))
    //     .pipe(gulp.dest(STATIC + '/js'));

    bower().on('error', console.log)
           .pipe(gulp.dest(STATIC + '/components/'));
});

gulp.task('clean', function() {
    del.sync([STATIC, TEMPLATES], {force: true});
});

gulp.task('rebuild', ['clean', 'build']);

