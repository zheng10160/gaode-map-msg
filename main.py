from pathlib import Path

from shapely.geometry import Polygon


from data import boundary_district_330106
from poly_fill import PolyFill
from util import project_to_plane, project_to_polar, to_js,project_to_plane_xiaozheng


def map_seg(radius, k, theta=0):
    # 把经纬度投影到二位平面 

    boundary_plane = Polygon(project_to_plane(boundary_district_330106))
   
    # boundary_plane = Polygon(project_to_polar(boundary_district_330106))
    # print(boundary_plane.xy)
    # return
    # 用正多边形填充

    # result = PolyFill(boundary_plane, boundary_plane.centroid).set_params(radius, k, theta).run()
    xinObj = PolyFill(boundary_plane, boundary_plane.centroid).set_params(radius, k, theta)

    result = xinObj.run()

    # result1 = [project_to_polar(poly) for poly in xinObj.getCenterZb()]

    xz_zxd = project_to_plane_xiaozheng(xinObj.getCenterZb())

    # 把结果转换成极坐标
    result = [project_to_polar(poly) for poly in result]
   
    # 保存结果
    d = Path('web')
    to_js(boundary_district_330106, d / 'data_boundaries.js', 'MS.data.blockBoundaries')
    to_js(result, d / 'data_bricks.js', 'MS.data.bricks ')

    # xiaozheng
    to_js(xz_zxd, d / 'data_center.js', 'MS.data.center')


if __name__ == '__main__':
   # map_seg(1000, 6)  # 六边形分割: 半径1000米
     map_seg(500, 4,20)  # 四边形分割: 半径2000米
    # map_seg(4000, 3)  # 三角形分割: 半径4000米
