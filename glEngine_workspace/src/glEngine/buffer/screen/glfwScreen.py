from typing import Callable
import glfw
import OpenGL.GL as GL
from glEngine.model.Engine import *

def dummy():
  pass

def debug_callback(source, msg_type, msg_id, severity, length, raw, user):
  msg = raw[0:length]
  print('Debug:', source, msg_type, msg_id, severity, msg)

def onDebugMessage(*args, **kwargs):
  print('args = {0}, kwargs = {1}'.format(args, kwargs))

class glfwScreen:
  window: glfw._GLFWwindow
  initialize_func: Callable[[], None]
  render_start_func: Callable[[], None]
  render_func: Callable[[], None]
  render_end_func: Callable[[], None]

  def __init__(self, param: ScreenParameter) -> None:
    if not glfw.init():
      raise Exception("glfw 라이브러리 초기화 실패")
    
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # glfw.window_hint(glfw.OPENGL_DEBUG_CONTEXT, True)
    
    self.window = glfw.create_window(param.width, param.height, param.name, None, None)

    if not self.window:
      raise Exception("glfw 윈도우 생성 실패")
    
    glfw.make_context_current(self.window)
    # glfw.set_window_user_pointer(self.window)

    # GL.glEnable(GL.GL_DEBUG_OUTPUT)
    GL.glDebugMessageCallback(GL.GLDEBUGPROC(debug_callback), None)    

    self.initialize_func = dummy
    self.render_start_func = dummy
    self.render_func = dummy
    self.render_end_func = dummy

  def set_initialize_func(self, func):
    self.initialize_func = func

  def set_render_start_func(self, func):
    self.render_start_func = func

  def set_render_func(self, func):
    self.render_func = func

  def set_render_end_func(self, func):
    self.render_end_func = func

  def start(self):
    self.initialize_func()
    while True:
      if glfw.window_should_close(self.window):
        error = GL.glGetError()
        if error != GL.GL_NO_ERROR:
          print(f"OpenGL 오류 발생: {error}")
        break
      # print(glfw.window_should_close(self.window))
      self.render_start_func()
      self.render_func()
      # self.render_end_func()
      glfw.swap_buffers(self.window)
      glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
  param = ScreenParameter()
  param.width = 640
  param.height = 480
  param.name = "Test Screen"

  screen = glfwScreen(param)

  while True:
    if not glfw.window_should_close(screen.window):
      error = GL.glGetError()
      if error != GL.GL_NO_ERROR:
          print(f"OpenGL 오류 발생: {error}")

    GL.glClearColor(0,0,0,1)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    # Render here, e.g. using pyOpenGL

    # Swap front and back buffers
    glfw.swap_buffers(screen.window)
    glfw.poll_events()

  glfw.terminate()