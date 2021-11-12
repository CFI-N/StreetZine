var pageLoadingInstance = false;
var previous_page = null;
var previous_title = null;

window.onpopstate = () => {
    var previous_title = document.title;
    var previous_page = window.location.pathname;
    changePage(previous_page, previous_title)
}

$(document).on("click", ".pageChanger", function(){
    let newUrl = encodeURI($(this).attr("page"));
    let newTitle = $(this).attr("title") + " - StreetZine";
    changePage(newUrl, newTitle)
    window.history.pushState(newUrl, newTitle, newUrl);
})

function changePage (page, title) {

    $(".content").load(page + " .content")
    document.title = title;

}