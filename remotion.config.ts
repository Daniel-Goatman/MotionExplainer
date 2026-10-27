import fs from 'node:fs';
import { Config } from '@remotion/cli/config';

// Use a local Google Chrome when one is installed (macOS path); otherwise Remotion uses its own headless browser.
const chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
if (fs.existsSync(chrome)) {
  Config.setBrowserExecutable(chrome);
  Config.setChromeMode('chrome-for-testing');
}
Config.setVideoImageFormat('jpeg');
Config.setJpegQuality(95);
