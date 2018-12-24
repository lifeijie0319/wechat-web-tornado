$(function(){
    var map = new AMap.Map('container')
    var origin_center;
    map.plugin('AMap.Geolocation', function () {
        geolocation = new AMap.Geolocation({
            enableHighAccuracy: true,//是否使用高精度定位，默认:true
            timeout: 10000,          //超过10秒后停止定位，默认：无穷大
            maximumAge: 0,           //定位结果缓存0毫秒，默认：0
            convert: true,           //自动偏移坐标，偏移后的坐标为高德坐标，默认：true
            showButton: true,        //显示定位按钮，默认：true
            buttonPosition: 'LB',    //定位按钮停靠位置，默认：'LB'，左下角
            buttonOffset: new AMap.Pixel(10, 50),//定位按钮与设置的停靠位置的偏移量，默认：Pixel(10, 20)
            showMarker: true,        //定位成功后在定位到的位置显示点标记，默认：true
            showCircle: true,        //定位成功后用圆圈表示定位精度范围，默认：true
            panToLocation: true,     //定位成功后将定位到的位置作为地图中心点，默认：true
            zoomToAccuracy:true      //定位成功后调整地图视野范围使定位位置及精度范围视野内可见，默认：false
        });
        map.addControl(geolocation);
        geolocation.getCurrentPosition(function (status, result) {
            if (status == "complete") {
                console.log(result);
                origin_center = result.position;
                map.setCenter(result.position);
            } else {
                $.toptips(result.message);
            }
        });
    });

    var marker_list;
    AMapUI.loadUI(['overlay/SimpleMarker', 'misc/MarkerList'], function(SimpleMarker, MarkerList) {
        marker_list = new MarkerList({
            map: map, //关联的map对象
            listContainer: 'mylist', //列表的dom容器的节点或者id, 用于放置getListElement返回的内容
            getDataId: function(dataItem, index) {
                //返回数据项的Id
                return dataItem.id;
            },
            getPosition: function(dataItem) {
                //返回数据项的经纬度，AMap.LngLat实例或者经纬度数组
                return dataItem.position
            },
            getMarker: function(dataItem, context, recycledMarker) {
                var label = String.fromCharCode('A'.charCodeAt(0) + context.index);
                var color;
                if (dataItem.waitman <= 5) {
                    color = 'green'
                }
                else if (dataItem.waitman >= 10) {
                    color = 'red'
                }
                else {
                    color = 'orange'
                }
                if (recycledMarker) {
                    //存在可回收利用的marker,直接setLabel返回
                    recycledMarker.setLabel(label);
                    return recycledMarker;
                }
                //返回一个新的Marker
                return new SimpleMarker({
                    iconLabel: label,
                    iconStyle: color,
                    color: 'green'
                });
            },
            getInfoWindow: function(dataItem, context, recycledInfoWindow) {
                var title = '<h4>' + dataItem.name + '</h4>'
                var tpl = title + '地址:' + dataItem.address;
                //MarkerList.utils.template支持underscore语法的模板
                var content = MarkerList.utils.template(tpl, {
                    dataItem: dataItem,
                    dataIndex: context.index
                });
                if (recycledInfoWindow) {
                    //存在可回收利用的infoWindow, 直接setContent返回
                    recycledInfoWindow.setContent(content);
                    return recycledInfoWindow;
                }
                //返回一个新的InfoWindow
                return new AMap.AdvancedInfoWindow({
                    offset: new AMap.Pixel(0, -23),
                    content: content,
                    panel: 'panel',
                    placeSearch: false,
                    asOrigin: false
                });
            },
            getListElement: function(dataItem, context, recycledListElement) {
                var tpl = '<option value=<%- dataItem.id %>><%- dataItem.name %></option>';
                var content = MarkerList.utils.template(tpl, {
                    dataItem: dataItem,
                    dataIndex: context.index
                });
                if (recycledListElement) {
                    //存在可回收利用的listElement, 直接更新内容返回
                    recycledListElement.innerHTML = content;
                    return recycledListElement;
                }
                //返回一段html，MarkerList将利用此html构建一个新的dom节点
                return content;
            }
        });
        data = [
            {
                id: 1,
                name: '上海国际金融中心',
                address: '上海浦东新区杨高南路388号',
                position: [121.535815, 31.220058]
            },
            {
                id: 2,
                name: '双鸽大厦',
                address: '浦东新区浦电路438号',
                position: [121.533369, 31.222829]
            },
            {
                id: 3,
                name: '阿里金融',
                address: '上海市浦东新区峨山路91弄120号陆家嘴软件园区8号楼5楼',
                position: [121.531191, 31.21737]
            }
        ]
        marker_list.render(data);
    });
    $('select#mylist').on('change', function(){
        id = $(this).val();
        if(id){
            record = marker_list.selectByDataId(id);
            console.log(record);
        }
    });
});
