#!/usr/bin/node
const fs = require('fs/promises');

async function concatFiles (f1, f2, f3) {
  const [content1, content2] = await Promise.all([
    fs.readFile(f1),
    fs.readFile(f2)
  ]);

  await fs.writeFile(f3, content1 + content2);
}

concatFiles(
  process.argv[2],
  process.argv[3],
  process.argv[4]
);
