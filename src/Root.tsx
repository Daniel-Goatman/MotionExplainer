import React from 'react';
import {AbsoluteFill, Composition} from 'remotion';
import {theme} from './design/tokens';
const Blank=()=> <AbsoluteFill style={{backgroundColor:theme.color.raised}}/>;
export const RemotionRoot=()=> <Composition id="Blank" component={Blank} durationInFrames={30} fps={30} width={1920} height={1080}/>;
