var i,jssrc, jss=['http://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js','http://fbalbumshare.appspot.com/share.js'];for(i=0;i!=jss.length;i++){jssrc=document.createElement('script');jssrc.src=jss[i];document.body.appendChild(jssrc);}void(0);

http://www.bram.us/projects/js_bramus/lazierload/


- url: /
  static_files: static/index.html
  upload: static/(.*)


	//Parse thumbnail URL
	//element.firstChild.firstChild.style.cssText.match(new RegExp('background-image:\turl\(\t(.+)\t\);\t'))


	- url: /
	  script: main.py