module.exports = function(gulp, plugins, dest) {
    function task(task) {
        return require('../gulp-tasks/' + task)(gulp, plugins);
    }

    var src = {
        pug: [
            __dirname + '/pug/add_instructor.pug',
            __dirname + '/pug/timeline.pug'
        ], 
        stylus: [
            __dirname + '/stylus/add_instructor.styl',
            __dirname + '/stylus/timeline.styl'
        ], 
        img: __dirname + '/img/**/*.{png,gif,jpg,jpeg,svg}', 
        js: __dirname + '/js/*.js' 
    };

    return function() {
        task('pug')   (src.pug,    dest.pug);
        task('stylus')(src.stylus, dest.stylus);
        task('img')   (src.img,    dest.img);

        gulp.src(src.js)
            .pipe(gulp.dest(dest.js))
    }
}