(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }else {
        alert("Loading!")
        // 随机数避免从浏览器cache中load
        document.body.appendChild(document.createElement('script')).src='http://mysite:8000/static/js/bookmarklet.js?r='+Math.floor(Math.random()*9999999999999);
    }
})();
