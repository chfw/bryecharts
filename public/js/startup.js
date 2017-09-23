var myLayout;
$(document).ready(function () {
  brython({"pythonpath": ['/bryecharts/', '/', 'public/python', '/bryecharts/public/python']});
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
