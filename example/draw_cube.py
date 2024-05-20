from glEngine import *

param = ScreenParameter()
param.width = 640
param.height = 480
param.name = "Test"
scn_buffer = ScreenBuffer(E.ScreenEngineType.GLFW, param)

mainCamera = CameraBuffer()
mainCamera.set_perspective(45, 1, 0.01, 10)
mainCamera.set_view(GLM.vec3(5,0,0), GLM.vec3(0,0,0), GLM.vec3(0,0,1))

basicShader = VertexShaderBuffer()
basicShader.bound()
basicShader.set_mat4_glm("projection", mainCamera.perspective_mat)
basicShader.set_mat4_glm("view", mainCamera.view_mat)

cubeBuffer = MeshBuffer()
cubeBuffer.set_mesh(MeshHelper.make_cube(1,1,0,0))
cubeBuffer.set_shader(basicShader)
cubeBuffer.initialize()

def init_func():
  GL.glEnable(GL.GL_DEPTH_TEST)

def start_func():
  GL.glClearColor(0,0,0,1)
  GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
  GL.glViewport(0,0,640,480)

def render_func():
  global cubeBuffer
  cubeBuffer.render()

scn_buffer.engine.set_initialize_func(init_func)
scn_buffer.engine.set_render_start_func(start_func)
scn_buffer.engine.set_render_func(render_func)
scn_buffer.start()