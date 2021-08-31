function init() {
    $.getJSON("goods.json", goodsOut);

}
function goodsOut(data) {
    console.log(data);
    var out= ' ';
    for (var key in data) {
        out += '<div class="cart">';
        out += `<p class="name">${data[key].name}</p>`;
        out += `<img src="img/${data[key].img}" alt="">`;
        out += `<a  class="cost" href=" ">${data[key].cost}</div>`;
        out += '</div>';
    }
    $('goods-out').html(out);
}
$(document).ready(function (){
    init();
})