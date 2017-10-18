mkdir local
cd local
python -m brython --install
cd ..
bp local/brython_stdlib.js bp-requirements.txt editor.py pyecharts
rm -rf local
cp brython_modules.js public/js/pyecharts.js
mv brython_modules.js npm/pyecharts.js
mv brython_modules.log.txt changelog/
npm install
gulp
cp README.md npm/
echo "Done"
