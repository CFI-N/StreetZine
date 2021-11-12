var previous_page = null
var previous_title = null

window.addEventListener('popstate', function (event) {
    changePage(previous_page, previous_title)
});

$(document).on("click", ".pageChanger", function(){
    let newUrl = encodeURI($(this).attr("page"));
    let newTitle = $(this).attr("title") + " - StreetZine";

    changePage(newUrl, newTitle)
})

function changePage (page, title) {
    console.log("Changing current content for content on: " + page);
    $(".content").load(page + " .content")
    
    previous_page = window.location.href;
    previous_title = $(document).find("title").text();

    window.history.pushState(page, title, page);
    console.log("new title is " + title + " and new page is " + page);
}