var STATIC    = __dirname + '/../static',
    TEMPLATES = __dirname + '/../templates';

var PUG_FILES    = __dirname + '/pages/**/[!_]*.pug',
    STYLUS_FILES = __dirname + '/pages/**/*.styl',
    IMG_FILES    = __dirname + '/pages/**/*.{png,jpg,jpeg,gif}',
    JS_FILES     = __dirname + '/pages/**/*.js';

var del          = require('del'),
    gulp         = require('gulp'),
    stylus       = require('gulp-stylus'),
    pug          = require('gulp-pug'),
    autoprefixer = require('gulp-autoprefixer'),
    bower        = require('gulp-bower'),
    imagemin     = require('gulp-imagemin'),
    concat       = require('gulp-concat'),
    uglify       = require('gulp-uglify'),
    replace      = require('gulp-replace');


gulp.task('build', function() {
    gulp.src(PUG_FILES)
        .pipe(replace(/\t/g, '    '))
        .pipe(pug()).on('error', console.log)
        .pipe(gulp.dest(TEMPLATES));

    gulp.src(STYLUS_FILES)
        .pipe(replace(/\t/g, '    '))
        .pipe(stylus({compress: true})).on('error', console.log)
        .pipe(autoprefixer())
        .pipe(gulp.dest(STATIC));

    gulp.src(IMG_FILES)
        .pipe(imagemin())
        .pipe(gulp.dest(STATIC + '/img'));

    gulp.src(JS_FILES)
        .pipe(gulp.dest(STATIC + '/js'));

    // gulp.src(JS_FILES)
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

gulp.task('watch', function() {
    gulp.watch([PUG_FILES, STYLUS_FILES, IMG_FILES, JS_FILES], ['rebuild']);
});



