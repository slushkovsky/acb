module.exports = function(gulp, plugins) {
    return function(src, dest) {
        gulp.src(src)
            .pipe(plugins.imagemin())
            .pipe(gulp.dest(dest));
    }
}