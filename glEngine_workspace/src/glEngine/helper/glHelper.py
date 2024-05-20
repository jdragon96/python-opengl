import numpy as np
import OpenGL.GL as GL
import glfw

import ctypes

from glEngine.model.Mesh import Mesh, Vertex

def create_vertex_buffer(mesh: Mesh, draw_type = GL.GL_STATIC_DRAW):
  vertex_cpu, index_cpu = mesh.make_buffer()

  vao = GL.glGenVertexArrays(1)
  vbo = GL.glGenBuffers(1)
  ebo = GL.glGenBuffers(1)

  ## 1 .vertex array 메모리 할당
  GL.glBindVertexArray(vao)
  GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
  GL.glBufferData(GL.GL_ARRAY_BUFFER, vertex_cpu.nbytes, vertex_cpu, draw_type)

  ## 2. vertex buffer 메모리 할당
  GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, ebo)
  GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, index_cpu.nbytes, index_cpu, draw_type)

  ## 3. 메모리 레이아웃 설정
  GL.glEnableVertexAttribArray(0)
  GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, Vertex.Byte(), ctypes.c_void_p(0))
  GL.glEnableVertexAttribArray(1)
  GL.glVertexAttribPointer(1, 4, GL.GL_FLOAT, GL.GL_FALSE, Vertex.Byte(), ctypes.c_void_p(4 * 3))
  GL.glEnableVertexAttribArray(2)
  GL.glVertexAttribPointer(2, 3, GL.GL_FLOAT, GL.GL_FALSE, Vertex.Byte(), ctypes.c_void_p(4 * 7))
  GL.glEnableVertexAttribArray(3)
  GL.glVertexAttribPointer(3, 2, GL.GL_FLOAT, GL.GL_FALSE, Vertex.Byte(), ctypes.c_void_p(4 * 10))

  ## 할당 해제
  GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
  GL.glBindVertexArray(0)

  return vao, vbo, ebo

if __name__ == "__main__":
  arr = np.empty(20, dtype=np.float32)
  print(arr.nbytes)