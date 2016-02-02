
// 默认加载第某页
// $(document).ready(function()
// {
//     $.get("page1.html",function(data)
//     {
//         $(".main").html(data);
//     });
// });

// 给使用了nav-sidebar样式的div下的li绑定单击响应动作
$(function()
{
    $('.pure-menu-list li').click(function()
    {
        /* step1：样式替换 */

        // 1.1：先把之前选中的li的active样式去掉
        $('.pure-menu-selected').removeClass('pure-menu-selected');
        // 1.2：再给当前点击的li的添加active样式
        $(this).addClass('pure-menu-selected');

        /* step2：请求页面 */

        // 找到被点击的<li>下的<a>
        var $url = $(this).find('a').attr('target');
        $.ajax
        ({
            url     :   $url,
            success :   function(data){$("#main").html(data);},
            error   :   function(data)
                        {
                            $("#main").html
                            (
                                "<h1>bigwang提示您</h1>" +
                                "<br>当前请求：" + $url +
                                "<br>返回结果：" + data.status +
                                " (" + data.statusText + ")"
                            )
                        },
        });
    });
    
});