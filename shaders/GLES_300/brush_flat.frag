#version 300 es
layout(location = 0) out mediump vec4 outColour;

in mediump vec3 position;
in mediump vec3 normal;
in mediump vec2 uv;
in mediump vec3 colour;

// uniform sampler2D texture; /* Move toward a Texture Atlas / Array */

void main()
{
	mediump vec4 ambient = vec4(0.75, 0.75, 0.75, 1);
	mediump vec4 diffuse = vec4(1, 1, 1, 1) * dot(normal, vec3(1, 1, 1));
	// mediump vec4 albedo = texture2D(texture, uv);

	outColour = vec4(colour, 1) * (ambient + diffuse);
	// outColour = vec4(uv.x, uv.y, 1, 1);
	// outColour = albedo * (ambient + diffuse);
}