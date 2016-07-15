./build.sh
./node_modules/.bin/stylus styles/        -o build/styles/  -w &
./node_modules/.bin/pug    pug/widget.pug -o build/         -w &