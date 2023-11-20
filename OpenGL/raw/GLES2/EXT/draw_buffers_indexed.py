'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_EXT_draw_buffers_indexed'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_EXT_draw_buffers_indexed',error_checker=_errors._error_checker)
GL_BLEND=_C('GL_BLEND',0x0BE2)
GL_BLEND_DST_ALPHA=_C('GL_BLEND_DST_ALPHA',0x80CA)
GL_BLEND_DST_RGB=_C('GL_BLEND_DST_RGB',0x80C8)
GL_BLEND_EQUATION_ALPHA=_C('GL_BLEND_EQUATION_ALPHA',0x883D)
GL_BLEND_EQUATION_RGB=_C('GL_BLEND_EQUATION_RGB',0x8009)
GL_BLEND_SRC_ALPHA=_C('GL_BLEND_SRC_ALPHA',0x80CB)
GL_BLEND_SRC_RGB=_C('GL_BLEND_SRC_RGB',0x80C9)
GL_COLOR_WRITEMASK=_C('GL_COLOR_WRITEMASK',0x0C23)
GL_CONSTANT_ALPHA=_C('GL_CONSTANT_ALPHA',0x8003)
GL_CONSTANT_COLOR=_C('GL_CONSTANT_COLOR',0x8001)
GL_DST_ALPHA=_C('GL_DST_ALPHA',0x0304)
GL_DST_COLOR=_C('GL_DST_COLOR',0x0306)
GL_FUNC_ADD=_C('GL_FUNC_ADD',0x8006)
GL_FUNC_REVERSE_SUBTRACT=_C('GL_FUNC_REVERSE_SUBTRACT',0x800B)
GL_FUNC_SUBTRACT=_C('GL_FUNC_SUBTRACT',0x800A)
GL_MAX=_C('GL_MAX',0x8008)
GL_MIN=_C('GL_MIN',0x8007)
GL_ONE=_C('GL_ONE',1)
GL_ONE_MINUS_CONSTANT_ALPHA=_C('GL_ONE_MINUS_CONSTANT_ALPHA',0x8004)
GL_ONE_MINUS_CONSTANT_COLOR=_C('GL_ONE_MINUS_CONSTANT_COLOR',0x8002)
GL_ONE_MINUS_DST_ALPHA=_C('GL_ONE_MINUS_DST_ALPHA',0x0305)
GL_ONE_MINUS_DST_COLOR=_C('GL_ONE_MINUS_DST_COLOR',0x0307)
GL_ONE_MINUS_SRC_ALPHA=_C('GL_ONE_MINUS_SRC_ALPHA',0x0303)
GL_ONE_MINUS_SRC_COLOR=_C('GL_ONE_MINUS_SRC_COLOR',0x0301)
GL_SRC_ALPHA=_C('GL_SRC_ALPHA',0x0302)
GL_SRC_ALPHA_SATURATE=_C('GL_SRC_ALPHA_SATURATE',0x0308)
GL_SRC_COLOR=_C('GL_SRC_COLOR',0x0300)
GL_ZERO=_C('GL_ZERO',0)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBlendEquationSeparateiEXT(buf,modeRGB,modeAlpha):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glBlendEquationiEXT(buf,mode):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glBlendFuncSeparateiEXT(buf,srcRGB,dstRGB,srcAlpha,dstAlpha):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBlendFunciEXT(buf,src,dst):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glColorMaskiEXT(index,r,g,b,a):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glDisableiEXT(target,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glEnableiEXT(target,index):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum,_cs.GLuint)
def glIsEnablediEXT(target,index):pass
