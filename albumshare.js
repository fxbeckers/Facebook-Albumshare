function getSrc(variable) { 
	var query = variable; 
	var vars = query.split('&'); 
	for (var i=0;i<vars.length;i++) { 
		var pair = vars[i].split('='); 
		if (pair[0] == 'src') { 
			return unescape(pair[1]); 
		}
	}
};
if (!document.URL.match(new RegExp('https?://www.facebook.com/album.php?.+'))) {
	alert('Please use this script on a facebook album');
} else {
	var title = escape(document.title);

	var pictureUrls = new Array();
	var elements = document.getElementsByClassName('uiMediaThumb uiScrollableThumb');
	
	for (var i=0;i<elements.length;i++) {
		var element = elements[i];

		var image = new Object();
		var fbImageUrl = element.attributes.ajaxify.value;
		var imageUrl = getSrc(fbImageUrl);

		image.img   = imageUrl;
		image.thumb = imageUrl.replace('n.jpg','a.jpg');

		pictureUrls.push(image);
	}
	
	url = 'https://fbalbumshare.appspot.com/album';
	params = {'photos':JSON.stringify(pictureUrls),'title':title};
	
	var form = document.createElement('form');
	form.setAttribute('id', 'fbAlbumShare');
	form.setAttribute('method', 'POST');
	form.setAttribute('action', url);
	form.setAttribute('target', '_blank');

	for(var key in params) {
		var hiddenField = document.createElement('input');
		hiddenField.setAttribute('type', 'hidden');
		hiddenField.setAttribute('name', key);
		hiddenField.setAttribute('value', params[key]);
		form.appendChild(hiddenField);
	}
	form.submit();
};