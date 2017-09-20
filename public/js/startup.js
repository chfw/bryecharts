var myLayout;
$(document).ready(function () {
	brython({"pythonpath": ['/bryecharts/', '/']});
	
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
