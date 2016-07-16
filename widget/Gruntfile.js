module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        stylus: {
            compile: {
                files: {
                    'build/styles/widget.css': ['styles/*.styl']
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
                    production: false
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
        }

    });

    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-pug');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks("grunt-bower-install-simple");

    grunt.registerTask('default', ['stylus', 'pug', 'bower-install-simple', 'imagemin']);
};