module.exports = function(gulp, plugins) {
	return function(src, dest) {
		gulp.src(src)
			.pipe(plugins.stylus({compress: true})).on('error', console.log)
			.pipe(plugins.autoprefixer())
			.pipe(gulp.dest(dest));
	}
}