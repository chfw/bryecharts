var myLayout;
$(document).ready(function () {
  var url = document.URL;
  var python_path;
  if(url.indexOf('chfw.github.io') != -1){
    python_path = ['/bryecharts/','/bryecharts/public/python'];
  }else{
    python_path = ['/', 'public/python' ];
  }
  brython({"pythonpath": python_path});
  var editor = ace.edit("editor");
  editor.setTheme("ace/theme/monokai");
  editor.getSession().setMode("ace/mode/python");
  editor.setOptions({
    'enableLiveAutocompletion': true,
     'enableSnippets': true,
     'highlightActiveLine': false,
     'highlightSelectedWord': true
  });
  myLayout = $('body').layout({
    applyDefaultStyles: true,
    north: {
      applyDefaultStyles: false,
      size: 300,
      onresize_end: function(){
      }
    }
  });
});
