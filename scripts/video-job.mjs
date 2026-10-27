import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const [job,action,...args]=process.argv.slice(2);
function fail(message){console.error(message);process.exit(1);}
if(!job||!/^[a-z0-9][a-z0-9-]*$/.test(job)||!['studio','compositions','still','render'].includes(action))fail('Usage: node scripts/video-job.mjs <job-id> studio|compositions|still|render [composition] [output filename] [options]');
const dir=path.join(root,'jobs',job);
const entry=['index.ts','index.tsx'].map(f=>path.join(dir,f)).find(f=>fs.existsSync(f));
if(!entry)fail('No job entry point. Create the job storyboard and implementation first.');
const publicDir=path.join(dir,'public');
if(!fs.existsSync(publicDir))fail('Missing job public directory.');
if(args.some(a=>a.startsWith('--public-dir')))fail('The runner owns the job asset directory.');
if(action==='render'||action==='still'){
 if(!args[0]||!args[1]||args[1].startsWith('-'))fail('Supply a composition ID and output filename.');
 const out=path.resolve(dir,'out',args[1]);const boundary=path.resolve(dir,'out')+path.sep;
 if(!out.startsWith(boundary))fail('Output must stay inside the selected job out directory.');
 fs.mkdirSync(path.dirname(out),{recursive:true});args[1]=out;
}
const result=spawnSync(path.join(root,'node_modules','.bin','remotion'),[action,entry,...args,'--public-dir='+publicDir],{cwd:root,stdio:'inherit'});
if(result.error)fail(result.error.message);
process.exit(result.status??1);
