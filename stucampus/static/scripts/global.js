/**
 * JavaScript Framework of StuCampus
 * 
 * @author: Developer Team of StuCampus,
 *          Shenzhen University
 * 
 *          TonySeek<tonyseek@gmail.com>
 *          shonenada<shonenada@gmail.com>
 *
 */
(function(window, $) {
    var StuCampus = {};

    // 初始化全站统一元素
    StuCampus.elementInit = function() {
        $('body').prepend($('<div id="message-box"></div>')); // 信息框容器
    };

    // 全站统一信息提示框
    StuCampus._messagebox = function(message, timeout, specialClass){
        var entity = $('<div class="message-content"></div>').hide()
            .append($('<span class="message-text"></span>').append(message))
            .append($('<a href="javascript:void(0);" class="button message-close-btn">关闭</a>'))
            .addClass(specialClass);
        $('#message-box').append(entity);

        entity.fadeIn(500);

        if (timeout > 0) {
            setTimeout(function(){
                entity.fadeOut(500, function(){
                    $(this).remove();
                });
            }, timeout);
        }

        entity.children('a.message-close-btn').click(function(){
            entity.fadeOut(500, function(){
                $(this).remove();
            });
        });
    };
    StuCampus.notice = function(message, timeout) { this._messagebox(message, timeout, 'notice'); };
    StuCampus.alert  = function(message, timeout) { this._messagebox(message, timeout, 'alert');  };
    StuCampus.error  = function(message, timeout) { this._messagebox(message, timeout, 'error'); };

    StuCampus.ajax = function(url, method, data, success){
        $.ajax({
            url: url,
            type: method,
            data: data,
            cache: false,
            statusCode:{
                403: function() {
                    StuCampus.alert('权限不足，删除失败', 2000);
                },
                404: function () {
                    StuCampus.alert('请求的页面不存在或被删除', 2000);
                }
            },
            success: function(response){
                if (typeof success == 'undefined') {
                    if (response.success){
                        StuCampus.notice(response.messages.join(', '), 2000);
                        if (document.referrer != '' && (document.referrer != document.location)) {
                            setTimeout(function(){document.location = document.referrer;}, 3000);
                        } else {
                            setTimeout(function(){document.location.reload();}, 3000);
                        }
                    }else{
                        StuCampus.alert(response.messages.join(', '), 2000);
                    }
                }else{
                    success(response);
                }
                return false;
            },
            error: function() {
                StuCampus.error('发生技术问题，操作失败。请联系技术开发部');
            }
        });
    };

    StuCampus.ajaxForm = function(forms, success){
        forms.ajaxForm({
            success: function(response){
                if (typeof success == 'undefined') {
                    if (response.success){
                        StuCampus.notice(response.messages.join(', '), 2000);
                        if (document.referrer != '' && (document.referrer != document.location)) {
                            setTimeout(function(){document.location = document.referrer;}, 3000);
                        } else {
                            setTimeout(function(){document.location.reload();}, 3000);
                        }
                    }else{
                        StuCampus.alert(response.messages.join(', '), 2000);
                    }
                }else{
                    success(response);
                }
                return false;
            },
            error: function() {
                StuCampus.error('发生技术问题，操作失败。请联系技术开发部');
            }
        });
    };

    // 用户登录
    StuCampus.signIn = function(email, password){
        url = '/account/signin';
        method = 'POST';
        data = {'email': email, 'password': password};
        StuCampus.ajax(url, method, data);
    };

    // 用户注销
    StuCampus.signOut = function(){
        url = '/account/signout'
        method = 'post';
        StuCampus.ajax(url, method);
    };

    window.StuCampus = window.$S = StuCampus;
})(window, jQuery);

// ajax with csrf token
$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

$(function(){
    // 初始化元素
    $S.elementInit();
});

// 阻止中国电信、中国联通的页面劫持
$(function(){
    if (top !== self) {
        if (top.location == self.location) {
            alert("您的页面可能遭到了网关或运营商的劫持");
        } else {
            top.location = self.location;
        }
    }
});
