#version 330 core

in vec2 fragmentTexCoord;
out vec4 fragColor;

uniform sampler2D imageTexture;
const float exposure = 1;
const float bloomThreshold = 0.05;
const float bloomIntensity = 1.2;
const float bloomRadius = 1.5;
const int blurRadius = 64;
const vec2 texture_size = vec2(1920, 1080);
const float vignetteIntensity = 0.35;

void main()
{
    vec2 uv = fragmentTexCoord;
    vec3 bloomColor = vec3(0.0);
    vec2 texelSize = vec2(1.0 / texture_size);
    vec2 offset1 = vec2(texelSize.x * bloomRadius, texelSize.y * bloomRadius);
    vec2 offset2 = vec2(texelSize.x * bloomRadius * 2.0, texelSize.y * bloomRadius * 2.0);

    bloomColor += texture(imageTexture, uv - offset2).rgb;
    bloomColor += texture(imageTexture, uv - offset1).rgb * 4.0;
    bloomColor += texture(imageTexture, uv).rgb * 6.0;
    bloomColor += texture(imageTexture, uv + offset1).rgb * 4.0;
    bloomColor += texture(imageTexture, uv + offset2).rgb;
    bloomColor /= 16.0;

    bloomColor = pow(bloomColor, vec3(1.0 / bloomThreshold));
    bloomColor *= bloomIntensity;

    vec3 baseColor = texture(imageTexture, uv).rgb;
    vec2 screenPos = 2.0 * uv - 1.0;
    float vignette = 1.0 - length(screenPos) * vignetteIntensity;
    vignette = smoothstep(0.0, 1.0, vignette);

    fragColor = vec4((baseColor + bloomColor) * exposure * vignette, 1.0);
    //fragColor = vec4(baseColor * exposure * vignette, 1.0);
}