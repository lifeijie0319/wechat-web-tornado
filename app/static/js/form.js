$(function(){

    //初始化日期最小值
    min_date = new Date().toISOString().split('T');
    $('input[name="date"]').attr('min', min_date);

    //地址选择器
    $('input[name="address"]').cityPicker({});

    //时间选择器
    $('input[name="date_select"]').datetimePicker({});

    //协议
    $.get(BASE_URL + '/static/doc/1.txt', function(resp){
        $('#protocol1').html('<pre>' + resp + '</pre>');
    });
    $('.ys_agree_clause').on('click', function(){
        $('.ys_fixed_footer').addClass('clause_btn_visible');
    });
    $('.ys_fixed_footer').on('click', function(){
        $(this).removeClass('clause_btn_visible');
    });

    //手机验证码
    $('#send_vcode').on('click', function(){
        cellphone_dom = $('input[name="cellphone"]').parents('.ys_cell');
        $(this).sendVcode(cellphone_dom);
    });

    //图片验证码
    $('.ys_vcode_img').on('click', function(){
        $.get(BASE_URL + '/common/refresh_pic_vcode', function(resp){
            $('.ys_vcode_img').attr('src', resp.url + '?v=' + Math.random());
        }).error(function(){
            $.toptips('刷新图片失败');
        });
    }).trigger('click');

    //表单验证
    $('form').form();
    $('#submit').on('click', function(){
        validate_res = false;
        $('form').validate(function(error){
            if(!error) validate_res = true;
        });
        if (!validate_res) return false;

        data = $('form').serializeForm();
        $.post(BASE_URL + '/form', data, function(resp){
            if(resp.success){
                window.location.href = 'done.html';
            }else{
                $.toptips(resp.msg);
            }
        }).error(function(){
            $.toptips('服务器错误');
        });
    });
});
