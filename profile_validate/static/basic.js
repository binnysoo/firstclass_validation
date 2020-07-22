$(document).ready(function () {
    var confirmCount = $(".confirmShow:visible").length;
    var deniedCount = $(".denyShow:visible").length;
    $("#deniedCount").html(deniedCount/2);
    $("#confirmCount").html(confirmCount);
});

function checkDenied(unique, var_id) {
    var tmp = "td.check.".concat(unique);
    var thisID = "#".concat(var_id);
    var checkStr = "check ".concat(unique).concat(" denied");
    var deniedStr = "#denied-".concat(unique);
    var confirmStr = "#confirm-".concat(unique);

    $(thisID).toggleClass('denied');

    if ($(tmp).hasClass(checkStr) == true) {
      $(deniedStr).show();
      $(confirmStr).hide();
    } else {
      $(deniedStr).hide();
      $(confirmStr).show();
    }

    var confirmCount = $(".confirmShow:visible").length;
    var deniedCount = $(".denyShow:visible").length;
    $("#deniedCount").html(deniedCount);
    $("#confirmCount").html(confirmCount);
}

