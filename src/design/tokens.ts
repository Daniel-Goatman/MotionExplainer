// SpeechControl Visuals is the sole design authority. Raw source stays unmodified.
import source from '../../design-source/speechcontrol/tokens.json';
export type ThemeName = 'clear' | 'warm';
export const designSystem = source;
export const fontFamily = source.type.families.sans;

export function colors(mode: ThemeName = 'clear'): Record<string, string> {
  const raw: Record<string, string> = {};
  for (const token of source.color.tokens) {
    const value = token.value;
    raw[token.name] = typeof value === 'string' ? value : value[mode] ?? value.clear;
  }
  const resolve = (name: string, seen = new Set<string>()): string => {
    if (seen.has(name) || !(name in raw)) throw new Error(`Invalid colour alias: ${name}`);
    seen.add(name);
    const value = raw[name];
    return value.startsWith('{') ? resolve(value.slice(1, -1), seen) : value;
  };
  return Object.fromEntries(Object.keys(raw).map((name) => [name, resolve(name)]));
}
export const theme = {color: colors('clear'), fontFamily} as const;
export const categoryOrder = ['blue', 'teal', 'lavender', 'amber', 'rose', 'slate', 'olive'] as const;
export const spacing = Object.fromEntries(source.spacing.tokens.map(t => [t.name, parseFloat(t.value)]));
export const radius = Object.fromEntries(source.radius.tokens.map(t => [t.name, parseFloat(t.value)]));
export const durationMs = Object.fromEntries(source.duration.tokens.map(t => [t.name, parseFloat(t.value)]));
export const easing = Object.fromEntries(source.easing.tokens.map(t => [t.name, t.value]));
export const typography = source.type.groups.flatMap(group => group.styles);
// Original measurements are sidebar CSS pixels. Scale spatial tokens explicitly for video;
// preserve duration in real time. Final video scale needs rendered validation.
export const videoDefaults = {width: 1920, height: 1080, fps: 30} as const;
export const millisecondsToFrames = (ms: number, fps = videoDefaults.fps) => Math.round(ms * fps / 1000);
