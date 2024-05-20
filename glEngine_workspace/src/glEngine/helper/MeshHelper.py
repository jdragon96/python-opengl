from glEngine.model.Mesh import Mesh, Vertex

class MeshHelper:
  @staticmethod
  def make_cube(size: float, r: float = 1, g: float = 1, b: float = 1, a=1):
    mesh = Mesh()
    mesh.vertices.append(Vertex(-size,size,-size,r,g,b,a,0,1,0,0,1))
    mesh.vertices.append(Vertex(-size,size,size,r,g,b,a,0,1,0,0,0))
    mesh.vertices.append(Vertex(size,size,size,r,g,b,a,0,1,0,1,0))
    mesh.vertices.append(Vertex(size,size,-size,r,g,b,a,0,1,0,1,1))

    mesh.vertices.append(Vertex(-size,-size,-size,r,g,b,a,0,1,0,0,1))
    mesh.vertices.append(Vertex(-size,-size,size,r,g,b,a,0,1,0,0,0))
    mesh.vertices.append(Vertex(size,-size,size,r,g,b,a,0,1,0,1,0))
    mesh.vertices.append(Vertex(size,-size,-size,r,g,b,a,0,1,0,1,1))

    # TOP
    mesh.indices.append(0)
    mesh.indices.append(2)
    mesh.indices.append(1)
    mesh.indices.append(0)
    mesh.indices.append(3)
    mesh.indices.append(2)

    # FRONT
    mesh.indices.append(4)
    mesh.indices.append(3)
    mesh.indices.append(0)
    mesh.indices.append(4)
    mesh.indices.append(7)
    mesh.indices.append(3)

    # RIGHT
    mesh.indices.append(7)
    mesh.indices.append(2)
    mesh.indices.append(3)
    mesh.indices.append(7)
    mesh.indices.append(6)
    mesh.indices.append(2)

    # LEFT
    mesh.indices.append(5)
    mesh.indices.append(0)
    mesh.indices.append(1)
    mesh.indices.append(5)
    mesh.indices.append(4)
    mesh.indices.append(0)

    # BACK
    mesh.indices.append(6)
    mesh.indices.append(1)
    mesh.indices.append(2)
    mesh.indices.append(6)
    mesh.indices.append(5)
    mesh.indices.append(1)

    # BOTTOM
    mesh.indices.append(6)
    mesh.indices.append(4)
    mesh.indices.append(7)
    mesh.indices.append(6)
    mesh.indices.append(5)
    mesh.indices.append(6)

    return mesh

if __name__ == "__main__":
  import sys
  import numpy as np