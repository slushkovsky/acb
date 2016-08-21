module.exports = function(gulp, plugins) {
	return function(src, dest) {
		return plugins.bower().on('error', console.log)
			          .pipe(gulp.dest(dest))
	}
}