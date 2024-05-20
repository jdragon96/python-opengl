from typing import List
import numpy as np

class Vertex:
  x: float = 0
  y: float = 0
  z: float = 0

  r: float = 0
  g: float = 0
  b: float = 0
  a: float = 0

  nx: float = 0
  ny: float = 0
  nz: float = 0

  tx: float = 0
  ty: float = 0

  def __init__(self) -> None:
    pass
  def __init__(self,x,y,z,r,g,b,a,nx,ny,nz,tx,ty) -> None:
    self.x = x
    self.y = y
    self.z = z
    self.r = r
    self.g = g
    self.b = b
    self.a = a
    self.nx = nx
    self.ny = ny
    self.nz = nz
    self.tx = tx
    self.ty = ty

  @staticmethod
  def Length():
    return 12
  
  @staticmethod
  def Byte():
    return Vertex.Length() * 4

class Mesh:
  vertices: List[Vertex]
  indices: List[int]

  def __init__(self) -> None:
    self.vertices = list()
    self.indices = list()

  def make_buffer(self):
    # 1. Vertex buffer 생성
    array_byte = Vertex.Byte() * len(self.vertices)
    array_value_count = Vertex.Length() * len(self.vertices)
    vertex_buffer = np.empty((len(self.vertices), Vertex.Length()), dtype=np.float32)
    # vertex_buffer = np.empty((array_value_count), dtype=np.float32)

    for index, vertex in enumerate(self.vertices):
      vertex_buffer[index][0] = vertex.x
      vertex_buffer[index][1] = vertex.y
      vertex_buffer[index][2] = vertex.z
      vertex_buffer[index][3] = vertex.r
      vertex_buffer[index][4] = vertex.g
      vertex_buffer[index][5] = vertex.b
      vertex_buffer[index][6] = vertex.a
      vertex_buffer[index][7] = vertex.nx
      vertex_buffer[index][8] = vertex.ny
      vertex_buffer[index][9] = vertex.nz
      vertex_buffer[index][10] = vertex.tx
      vertex_buffer[index][11] = vertex.ty

    # 2. index buffer 생성
    index_buffer = np.empty(len(self.indices), dtype=np.uint32)
    for index, value in enumerate(self.indices):
      index_buffer[index] = value

    return vertex_buffer, index_buffer

if __name__ == "__main__":
  mesh = Mesh()
  mesh.vertices.append(Vertex())
  mesh.vertices.append(Vertex())
  mesh.vertices.append(Vertex())
  mesh.vertices.append(Vertex())
  mesh.indices.append(0)
  mesh.indices.append(2)
  mesh.indices.append(1)
  mesh.indices.append(0)
  mesh.indices.append(3)
  mesh.indices.append(2)
  vao_cpu, ebo_cpu = mesh.make_buffer()
