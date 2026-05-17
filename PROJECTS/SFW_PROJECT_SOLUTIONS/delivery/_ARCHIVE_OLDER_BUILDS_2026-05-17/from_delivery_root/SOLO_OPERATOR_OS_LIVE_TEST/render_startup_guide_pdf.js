const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const base = __dirname;
  const htmlPath = path.join(base, 'SOLO_OPERATOR_STARTUP_GUIDE.html');
  const pdfPath = path.join(base, 'SOLO_OPERATOR_STARTUP_GUIDE.pdf');

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(`file://${htmlPath.replace(/\\/g, '/')}`, { waitUntil: 'load' });
  await page.pdf({
    path: pdfPath,
    format: 'A4',
    printBackground: true,
    margin: {
      top: '14mm',
      right: '12mm',
      bottom: '14mm',
      left: '12mm'
    }
  });
  await browser.close();
})();
