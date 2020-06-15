#version 300 es
layout(location = 0) in vec3 vertex_position;
layout(location = 1) in vec3 vertex_normal;
layout(location = 2) in vec2 vertex_uv;
layout(location = 3) in vec3 editor_colour;

uniform mat4 ModelViewProjectionMatrix;

out vec3 position;
out vec3 normal;
out vec2 uv;
out vec3 colour;

out float Kd;

void main()
{
    position = vertex_position;
    normal = vertex_normal;
    uv = vec2(vertex_uv.x, -vertex_uv.y);
	colour = editor_colour;

	Kd = abs(normal.x / 3.0 + 1.0/3.0 * normal.y / 3.0 + 2.0/3.0 * normal.z / 3.0);

	gl_Position = ModelViewProjectionMatrix * vec4(vertex_position, 1);
}
