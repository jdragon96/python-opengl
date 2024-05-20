#version 450 core

// !- 입력
in vec4 fragVertexColor;
in vec2 fragTextureCoord;

// !- 출력
out vec4 finalFragColor;

void main(){
  finalFragColor = fragVertexColor;
}