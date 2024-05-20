#version 450 core

layout(location = 0) in vec3 vertexPosition;
layout(location = 1) in vec4 vertexColor;
layout(location = 2) in vec3 normalVector;
layout(location = 3) in vec2 texCoord;

out vec4 fragVertexColor;
out vec2 fragTextureCoord;

uniform mat4 model;
uniform mat4 view;
uniform mat4 perspective;

void main() {
  fragVertexColor = vertexColor;
  fragTextureCoord = texCoord;
  gl_Position = perspective * view * model * vec4(vertexPosition, 1.0f);
}