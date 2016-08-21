module.exports = function(gulp, plugins) {
	return function(src, dest) {
		gulp.src(src)
			.pipe(plugins.pug()).on('error', console.log)
			.pipe(gulp.dest(dest));
	}
}