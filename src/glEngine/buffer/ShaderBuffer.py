import numpy as np
import OpenGL.GL as GL
import glm as GLM
from enum import Enum

class ShaderBufferType(Enum):
  VERTEX=1
  GEOMETRY=2

basic_vertex_shader = """
#version 450 core

layout(location = 0) in vec3 vertexPosition;
layout(location = 1) in vec4 vertexColor;
layout(location = 2) in vec3 normalVector;
layout(location = 3) in vec2 texCoord;

out vec4 fragVertexColor;
out vec2 fragTextureCoord;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main() {
  fragVertexColor = vertexColor;
  fragTextureCoord = texCoord;
  gl_Position = projection * view * model * vec4(vertexPosition, 1.0f);
}
"""

basic_fragment_shader = """
#version 450 core

in vec4 fragVertexColor;
in vec2 fragTextureCoord;

out vec4 finalFragColor;

void main(){
  finalFragColor = fragVertexColor;
}
"""


class VertexShaderBuffer:
  vertex_shader: int
  fragment_shader: int
  id: int

  def __init__(self) -> None:
    self.vertex_shader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
    GL.glShaderSource(self.vertex_shader, basic_vertex_shader)
    GL.glCompileShader(self.vertex_shader)
    
    self.fragment_shader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
    GL.glShaderSource(self.fragment_shader, basic_fragment_shader)
    GL.glCompileShader(self.fragment_shader)

    self.error_check(self.vertex_shader)
    self.error_check(self.fragment_shader)
    
    self.id = GL.glCreateProgram()
    GL.glAttachShader(self.id, self.vertex_shader)
    GL.glAttachShader(self.id, self.fragment_shader)

    # 셰이더 프로그램 링크
    GL.glLinkProgram(self.id)

    GL.glDeleteShader(self.vertex_shader)
    GL.glDeleteShader(self.fragment_shader)
  
  def bound(self):
    GL.glUseProgram(self.id)

  def set_mat4_numpy(self, name: str, mat: np.ndarray):
    GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.id, name), 1, GL.GL_FALSE, mat.data)
  def set_mat4_glm(self, name: str, mat: GLM.mat4):
    GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.id, name), 1, GL.GL_FALSE, GLM.value_ptr(mat))

  def error_check(self, shader: int):
    if GL.glGetShaderiv(shader, GL.GL_COMPILE_STATUS) != GL.GL_TRUE:
      info = GL.glGetShaderInfoLog(shader)
      raise RuntimeError('Shader compilation failed: %s' % (info))

if __name__ == "__main__":
  shader = VertexShaderBuffer()
  shader.bound()