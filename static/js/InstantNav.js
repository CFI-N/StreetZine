var pageLoadingInstance = false;
var kekInstance = false;
var url_data = {
    previous_page : null,
    previous_title : null,
    current_page : null,
    current_title:  null,
}

$(document).ready( () => {
    $(".content").removeClass("c-off");
    if (url_data.previous_page == null) {
        $(".returnBtn").remove();
    }
    url_data.current_page = document.documentURI;
    url_data.current_title = document.title;
})

window.onpopstate = () => {
    changePage(url_data.previous_page, url_data.previous_title)
}

$(document).on("click", ".pageChanger", function(){
    let newUrl = encodeURI($(this).attr("page"));
    let newTitle = $(this).attr("title") + " - StreetZine";
    changePage(newUrl, newTitle)
    window.history.pushState(newUrl, url_data.previous_title, url_data.current_page);
})

$(document).on("click", ".returnBtn", function() {
    changePage(url_data.previous_page, url_data.previous_title)
    window.history.pushState(url_data.current_page, url_data.previous_title, url_data.current_page);
})

function changePage (page = null, title = null) {
    url_data.current_page = page;
    url_data.current_title = title;
    setPreviousUrlData();
    clearTimeout(pageLoadingInstance);
    document.title = title;
    $(".content").addClass("c-off-alternate");
    pageLoadingInstance = setTimeout( () => {
        $(".content").empty();
        $(".content").removeClass("c-off-alternate");
        $(".content").load(page + " .content");
        setTimeout( () => {
            $(".content").removeClass("c-off");
        },50)
    }, 300)
    kekInstance = setTimeout(() => {
        if ($(".content").hasClass("c-off")) {
            $(".content").removeClass("c-off");
        }
    },500)
}

function setPreviousUrlData() {
    url_data.previous_title = document.title;
    url_data.previous_page = document.documentURI;
    console.log(url_data);
}