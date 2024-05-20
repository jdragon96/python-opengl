import glEngine.enums as E

from glEngine.buffer.CameraBuffer import CameraBuffer
from glEngine.buffer.ShaderBuffer import *
from glEngine.buffer.MeshBuffer import MeshBuffer
from glEngine.buffer.screen.glfwScreen import *

from glEngine.helper.MeshHelper import MeshHelper



class ScreenBuffer:  
  screen_type: E.ScreenEngineType
  engine = None

  def __init__(self, scn_tpe: E.ScreenEngineType, param: ScreenParameter) -> None:
    self.screen_type = scn_tpe

    if self.screen_type == E.ScreenEngineType.GLFW:
      self.engine = glfwScreen(param)


  def start(self):
    if self.engine is None:
      raise Exception("Screen 버퍼가 정상적으로 생성되지 않았습니다.")
    self.engine.start()

if __name__ == "__main__":
  param = ScreenParameter()
  param.width = 640
  param.height = 480
  param.name = "Test"
  scn_buffer = ScreenBuffer(E.ScreenEngineType.GLFW, param)
  
