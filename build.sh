mkdir local
cd local
python -m brython --install
cd ..
bp local/brython_stdlib.js bp-requirements.txt editor.py pyecharts
rm -rf local
cp brython_modules.js public/js
mv brython_modules.js npm/bryecharts.js
mv brython_modules.log.txt changelog/
echo "Done"
