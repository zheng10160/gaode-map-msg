/**
 * 显示砖块(中心点)
 * @class
 * @param{AMap.Map} map
 * @constructor
 */
MS.CenterJ = function (data) {

    data.forEach(function(vals){
        vals['coordinates'].forEach(function(val){

            /*
            new AMap.Marker({
                map: MS.map,
                icon: "//a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-3.png",
                position: [val[0], val[1]],
                offset: new AMap.Pixel(-10, -10)
            });
            */

             // 创建纯文本标记
            var  text = new AMap.Text({
                text:'s1',
                anchor:'center', // 设置文本标记锚点
                draggable:true,
                cursor:'pointer',
                angle:10,
                style:{
                    'padding': '0.1rem 0.1rem',
                    'margin-bottom': '0.1rem',
                    'border-radius': '0.1rem',
                    'background-color': 'white',
                    'width': '2rem',
                    'border-width': 0,
                    'box-shadow': '0 2px 6px 0 rgba(114, 124, 245, .5)',
                    'text-align': 'center',
                    'font-size': '7px',
                    'color': 'blue'
                },
                position: [val[0], val[1]]
            });

            text.setMap(MS.map);
        })
    });

   
    
};

/**
 * 设置显示的样式
 * @private
 */
MS.CenterJ.prototype.m_initStyle = function() {

}


MS.CenterJ.prototype.render = function() {
      //  this.m_initStyle();
        this.layer.render();
};

MS.CenterJ.prototype.loadData = function(data) {
   
    data.forEach(function(vals){
        vals['coordinates'].forEach(function(val){
            new AMap.Marker({
                map: this.map,
                icon: "//a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-3.png",
                position: [val[0], val[1]],
                offset: new AMap.Pixel(-13, -30)
            });
        })
    });
    
    /*
    this.layer.setData(data, {
        lnglat: 'coordinates',  // 区块的边界点
    });
    */
};





