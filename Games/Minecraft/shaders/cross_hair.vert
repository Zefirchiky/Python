#version 330 core

layout (location = 0) in vec3 in_pos;
layout (location = 1) in vec3 in_col;

out vec3 color;

void main() {
    color = in_col;
    gl_Position = vec4(in_pos, 1.0);
}