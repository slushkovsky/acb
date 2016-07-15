rm -rf build
mkdir build 
mkdir build/styles 
cp -r img/ build/
cp -r bower_components/ build/
./node_modules/.bin/stylus styles/        -o build/styles/ 
./node_modules/.bin/pug    pug/widget.pug -o build/  