mkdir local
cd local
python -m brython --install
cd ..
bp local/brython_stdlib.js bp-requirements.txt editor.py pyecharts
rm -rf local
echo "Done"
