var myLayout;
$(document).ready(function () {
	brython();
	
    myLayout = $('body').layout({
		applyDefaultStyles: true,
		north: {
			applyDefaultStyles: false,
			size: 300,
			onresize_end: function(){
				console.log('xxxx');
			}
		}
	});
});
