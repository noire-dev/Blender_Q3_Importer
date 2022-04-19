# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

from ctypes import (LittleEndianStructure,
                    c_char, c_float, c_int, c_ubyte, sizeof)
from mathutils import Vector


class BSP_HEADER(LittleEndianStructure):
    _fields_ = [
        ("magic_nr", c_char*4),
        ("version_nr", c_int),
        ("checksum", c_int),
    ]


class BSP_ENTITY(LittleEndianStructure):
    _fields_ = [
            ("char", c_char)
    ]


class BSP_SHADER(LittleEndianStructure):
    _fields_ = [
        ("name", c_char * 64),
        ("flags", c_int),
        ("contents", c_int),
        ("subdivisions", c_int),
    ]


class BSP_PLANE(LittleEndianStructure):
    _fields_ = [
        ("normal", c_float * 3),
        ("distance", c_float),
    ]


class BSP_NODE(LittleEndianStructure):
    _fields_ = [
        ("plane", c_int),
        ("children", c_int * 2),
        ("mins", c_int * 3),
        ("maxs", c_int * 3),
    ]


class BSP_LEAF(LittleEndianStructure):
    _fields_ = [
        ("cluster", c_int),
        ("area", c_int),
        ("mins", c_int * 3),
        ("maxs", c_int * 3),
        ("n_leaffaces", c_int),
        ("leafface", c_int),
        ("leafbrush", c_int),
        ("n_leafbrushes", c_int),
    ]


class BSP_LEAF_FACE(LittleEndianStructure):
    _fields_ = [
        ("face", c_int),
    ]


class BSP_LEAF_BRUSH(LittleEndianStructure):
    _fields_ = [
        ("brush", c_int),
    ]


class BSP_MODEL(LittleEndianStructure):
    _fields_ = [
        ("mins", c_float * 3),
        ("maxs", c_float * 3),
        ("face", c_int),
        ("n_faces", c_int),
        ("brush", c_int),
        ("n_brushes", c_int),
    ]


class BSP_BRUSH(LittleEndianStructure):
    _fields_ = [
        ("n_brushsides", c_int),
        ("brushside", c_int),
        ("texture", c_int),
    ]


class BSP_BRUSH_SIDE(LittleEndianStructure):
    _fields_ = [
        ("texture", c_int),
        ("plane", c_int),
    ]


class BSP_VERTEX(LittleEndianStructure):
    _fields_ = [
        ("position", c_float * 3),
        ("texcoord", c_float * 2),
        ("normal", c_float * 3),
        ("color1", c_ubyte * 4),
        ("lod_extra", c_float),
        ("lm1coord", c_float * 2),
    ]


class BSP_INDEX(LittleEndianStructure):
    _fields_ = [
        ("offset", c_int),
    ]


class BSP_FOG(LittleEndianStructure):
    _fields_ = [
        ("name", c_char * 64),
        ("brush", c_int),
        ("visibleSide", c_int),
    ]


class BSP_SURFACE(LittleEndianStructure):
    _fields_ = [
        ("texture", c_int),
        ("effect", c_int),
        ("type", c_int),
        ("vertex", c_int),
        ("n_vertexes", c_int),
        ("index", c_int),
        ("n_indexes", c_int),
        ("lm_indexes", c_int),
        ("lm_x", c_int),
        ("lm_y", c_int),
        ("lm_width", c_int),
        ("lm_height", c_int),
        ("lm_origin", c_float * 3),
        ("lm_vecs", c_float * 9),
        ("patch_width", c_int),
        ("patch_height", c_int),
        ("subdivisions", c_float),
        ("baseLightingSurface", c_int),
        ("inverted", c_int),
        ("faceFlags", c_int * 4),
    ]


class BSP_LIGHTMAP(LittleEndianStructure):
    _fields_ = [
        ("map", c_ubyte * (128 * 128 * 3)),
    ]


class BSP_LIGHTGRID(LittleEndianStructure):
    _fields_ = [
        ("ambient1", c_ubyte * 3),
        ("direct1", c_ubyte * 3),
        ("lat_long", c_ubyte * 2)
    ]


class BSP_VIS(LittleEndianStructure):
    _fields_ = [
        ("bit_set", c_ubyte),
    ]


class BSP_INFO:
    bsp_magic = b'EF2!'
    bsp_version = 0x14

    lightgrid_size = [192, 192, 320]
    lightgrid_inverse_size = [1.0 / float(lightgrid_size[0]),
                              1.0 / float(lightgrid_size[1]),
                              1.0 / float(lightgrid_size[2])]

    lightmap_size = [128, 128]
    lightmaps = 1
    lightstyles = 0
    use_lightgridarray = False

    lumps = {"shaders":          BSP_SHADER,
             "planes":           BSP_PLANE,
             "lightmaps":        BSP_LIGHTMAP,
             "baselightmaps":    BSP_LIGHTMAP,
             "contlightmaps":    BSP_LIGHTMAP,
             "surfaces":         BSP_SURFACE,
             "drawverts":        BSP_VERTEX,
             "drawindexes":      BSP_INDEX,
             "leafbrushes":      BSP_LEAF_BRUSH,
             "leaffaces":        BSP_LEAF_FACE,
             "leafs":            BSP_LEAF,
             "nodes":            BSP_NODE,
             "brushsides":       BSP_BRUSH_SIDE,
             "brushes":          BSP_BRUSH,
             "fogs":             BSP_FOG,
             "models":           BSP_MODEL,
             "entities":         BSP_ENTITY,
             "visdata":          BSP_VIS,
             "lightgrid":        BSP_LIGHTGRID,
             "entlights":        BSP_ENTITY,
             "entlightvis":      BSP_ENTITY,
             "lightdefs":        BSP_ENTITY,
             "baselightingverts": BSP_ENTITY,
             "contlightingverts": BSP_ENTITY,
             "baselightingsurfs": BSP_ENTITY,
             "lightingsurfs":    BSP_ENTITY,
             "lightingvertsurfs": BSP_ENTITY,
             "lightinggroups":   BSP_ENTITY,
             "staticLodModels":  BSP_ENTITY,
             "bspinfo":          BSP_ENTITY,
             }

    header_size = sizeof(BSP_HEADER)

    lightmap_lumps = ("lightmaps",
                      "baselightmaps",
                      "contlightmaps")

    @staticmethod
    def lerp_vec(vec1, vec2, vec_out):
        for i in range(len(vec1)):
            vec_out[i] = (vec1[i] + vec2[i]) / 2.0

    @staticmethod
    def lerp_ivec(vec1, vec2, vec_out):
        for i in range(len(vec1)):
            vec_out[i] = int((vec1[i] + vec2[i]) / 2)

    @classmethod
    def lerp_vertices(
            cls,
            vertex1: BSP_VERTEX,
            vertex2: BSP_VERTEX
            ) -> BSP_VERTEX:
        vec = Vector(vertex1.normal) + Vector(vertex2.normal)
        vec.normalize()

        lerped_vert = BSP_VERTEX()
        lerped_vert.normal[0] = vec[0]
        lerped_vert.normal[1] = vec[1]
        lerped_vert.normal[2] = vec[2]
        cls.lerp_vec(vertex1.position, vertex2.position, lerped_vert.position)
        cls.lerp_vec(vertex1.texcoord, vertex2.texcoord, lerped_vert.texcoord)
        cls.lerp_vec(vertex1.lm1coord, vertex2.lm1coord, lerped_vert.lm1coord)
        cls.lerp_ivec(vertex1.color1, vertex2.color1, lerped_vert.color1)
        return lerped_vert
