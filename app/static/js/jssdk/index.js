$(function(){
    configJssdk(['scanQRCode', 'onMenuShareTimeline', 'onMenuShareAppMessage']);
    $('#scan').on('click', function(){
        wx.scanQRCode({
            needResult: 1, // 默认为0，扫描结果由微信处理，1则直接返回扫描结果，
            scanType: ["qrCode","barCode"], // 可以指定扫二维码还是一维码，默认二者都有
            success: function (res){
                result = res.resultStr;
                $.alert(result);
            }
        });
    });
    wx.ready(function(){
        wx.onMenuShareAppMessage({
            title: '南浔银行年度大礼——丰收之果，诚意奉上！',
            desc: '现在邀请好友注册，即刻获得果果好礼！',
            link: window.location.href,
            imgUrl: BASE_URL + '/static/img/banner02.jpg',
            type: '',
            dataUrl: '',
            success: function () {
                $.toptips('分享成功', 'success');
            },
            cancel: function () {
                $.toptips('取消分享');
            },
        });
        wx.onMenuShareTimeline({
            title: '南浔银行年度大礼——丰收之果，诚意奉上！', // 分享标题
            link: window.location.href,
            imgUrl: BASE_URL + '/static/img/banner02.jpg', // 分享图标
            success: function () {
                $.toptips('分享成功', 'success');
            },
            cancel: function () {
                $.toptips('取消分享');
            }
        });
    });
});
