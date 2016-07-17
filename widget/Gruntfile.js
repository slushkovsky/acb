module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        stylus: {
            compile: {
                files: {
                    'build/styles/widget.min.css': ['styles/*.styl']
                }
            }
        },

        pug: {
            compile: {
                files: {
                    'build/index.html': ['pug/widget.pug']
                }
            }
        },

        concat: {
            dist: {
                src: ['js/**/*'],
                dest: 'build/js/widget.js'
            }
        },

        uglify: {
            js: {
                src: 'build/js/widget.js', 
                dest: 'build/js/widget.min.js'
            }
        },

        "bower-install-simple": {
            options: {
                color: true,
                directory: "build/components/"
            },
            prod: {
                options: {
                    production: true
                }
            },
            dev: {
                options: {
                    productionhb: false
                }
            }
        },  

        imagemin: {
            dynamic: {
                files: [
                    {
                        expand: true,
                        cwd: 'img/',
                        src: ['**/*.{jpg,png}'], 
                        dest: 'build/img/'
                    }
                ]
            }
        },

        watch: {
            pug: {
                files: ['pug/**/*'],
                tasks: ['pug'],
                options: {
                    livereload: true
                }
            }, 
            images: {
                files: ['img/**/*'], 
                tasks: ['imagemin'],
                options: {
                    livereload: true
                }
            },
            bower: {
                files: ['bower.json'], 
                tasks: ['bower-install-simple'],
                options: {
                    livereload: true
                }
            }, 
            stylus: {
                files: ['styles/**/*'], 
                tasks: ['stylus'],
                options: {
                    livereload: true
                }
            }, 
            js: {
                files: ['js/**/*'],
                tasks: ['concat', 'uglify'],
                options: {
                    livereload: true
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-pug');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-concat');    
    grunt.loadNpmTasks('grunt-bower-install-simple');


    grunt.registerTask('default', [
        'stylus', 
        'pug', 
        'bower-install-simple', 
        'imagemin', 
        'concat',
        'uglify'
    ]);
};