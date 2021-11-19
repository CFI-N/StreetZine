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

window.onpopstate = function (event) {
    url_data.previous_page = url_data.current_page;
    console.log("previous = " + url_data.previous_page);
    url_data.current_page = document.documentURI;
    console.log("current = " + url_data.current_page);
    url_data.current_title = url_data.previous_title;
    // console.log( url_data.previous_page);
    // changePage(url_data.previous_page, url_data.previous_title, "override")
    changePage(document.documentURI,  url_data.previous_title, "override")
}

$(document).on("click", ".pageChanger", function(){
    let newUrl = encodeURI($(this).attr("page"));
    console.log(newUrl);
    let newTitle = $(this).attr("title") + " - StreetZine";
    changePage(newUrl, newTitle, "yes")
    window.history.pushState(newUrl, url_data.previous_title, url_data.current_page);
})

$(document).on("click", ".returnBtn", function() {
    changePage(url_data.previous_page, url_data.previous_title)
    window.history.pushState(url_data.current_page, url_data.previous_title, url_data.current_page);
})

function changePage (page = null, title = null, override) {
    url_data.current_page = page;
    url_data.current_title = title;

    if (override != null) {
        setPreviousUrlData("override");
    } else {
        setPreviousUrlData();
    }
    clearTimeout(pageLoadingInstance);
    document.title = title;
    $(".content").addClass("c-off-alternate");
    pageLoadingInstance = setTimeout( () => {
        $(".content").empty();
        $(".content").removeClass("c-off-alternate");
        console.log("new page: " + page);
        $(".content").load(page + " .content");
        setTimeout( () => {
            $(".content").removeClass("c-off");
            changeActiveLink(page)
        },50)
    }, 300)
    kekInstance = setTimeout(() => {
        if ($(".content").hasClass("c-off")) {
            $(".content").removeClass("c-off");
            changeActiveLink(page)
        }
    },500)
}

function setPreviousUrlData(override) {
    if (override != null){
        // pass
    } else {
        url_data.previous_title = document.title;
        url_data.previous_page = document.documentURI;
    }
    console.log(url_data);
}

function changeActiveLink(url) {
    if (url.includes("a-la-une")) {
        $("#homeLink").addClass("active");
        $("#articleLink").removeClass("active");
    } else if (url.includes("nos-articles")) {
        $("#homeLink").removeClass("active");
        $("#articleLink").addClass("active");
    } else {
        $("#homeLink").removeClass("active");
        $("#articleLink").removeClass("active");
    }
}