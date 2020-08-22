import json

from pyproj import Proj


def project_to_plane(points):
    """ 把物理点投影到二维平面.
    """
    p = Proj(4508)
    return [p(point[0], point[1]) for point in points]

# 中心点处理
def project_to_plane_xiaozheng(points):
    """ 把物理点投影到二维平面.
    """
    p = Proj(4508)
   
    def proj_and_round(point):
        q = p(point[0], point[1], inverse=True)
        return round(q[0], 6), round(q[1], 6)

    zxd = []    
    for point in points:
       
        vs = point.split(",",1)

        zxd.append(proj_and_round(vs))
        
    return zxd  
    #return [p(point.split(",",1)[0],point.split(",",1)[1])  for point in points]

def project_to_polar(points):
    """ 把平面上的点转换成极坐标.
    """
    p = Proj(4508)

    def proj_and_round(point):
        q = p(point[0], point[1], inverse=True)
        return round(q[0], 6), round(q[1], 6)

    return [proj_and_round(point) for point in points]


def to_js(points, path, var_name):
    """ 保存成js文件(前端展示).
    """
    data_js = {
        'coordinates': [list(p) for p in points]
    }
    with open(path, 'w', encoding='utf-8') as f:
        f.write('%s = [%s];' % (var_name, json.dumps(data_js)))
