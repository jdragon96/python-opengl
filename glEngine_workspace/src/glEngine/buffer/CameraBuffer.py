import glfw
import OpenGL.GL as GL
import glm as GLM

class CameraBuffer:
  perspective_mat: GLM.mat4x4
  view_mat: GLM.mat4x4

  def __init__(self) -> None:
    pass

  def set_perspective(self, fovy_deg, aspect, near, far):
    self.perspective_mat = GLM.perspective(GLM.radians(fovy_deg), aspect, near, far)
  def set_view(self, eye: GLM.vec3, target: GLM.vec3, up: GLM.vec3):
    self.view_mat = GLM.lookAt(eye, target, up)

  def update_rotate(self):
    pass
  def update_distance(self, delta):
    pass