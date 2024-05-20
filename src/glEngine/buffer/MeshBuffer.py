import glfw
import OpenGL.GL as GL
import glm as GLM

from glEngine.helper.glHelper import *
from glEngine.buffer.ShaderBuffer import VertexShaderBuffer

class MeshBuffer:
  mesh: Mesh
  vao: int
  vbo: int
  ebo: int
  vertex_shader: VertexShaderBuffer
  model: GLM.mat4

  def __init__(self) -> None:
    self.mesh = None
    self.model = GLM.identity(GLM.mat4)
  
  def set_mesh(self, mesh):
    self.mesh = mesh
  
  def set_shader(self, shader: VertexShaderBuffer):
    self.vertex_shader = shader
  
  def initialize(self):
    if self.mesh == None:
      return
    self.vao, self.vbo, self.ebo = create_vertex_buffer(self.mesh)

  def render(self):
    if self.mesh == None:
      return
    self.vertex_shader.bound()
    self.vertex_shader.set_mat4_glm("model", self.model)
    GL.glBindVertexArray(self.vao)
    # # Texture 처리... 들어가야됨
    try:
      GL.glDrawElements(GL.GL_TRIANGLES, len(self.mesh.indices), GL.GL_UNSIGNED_INT, None)
    except Exception as e:
      print(e)
    GL.glBindVertexArray(0)
    