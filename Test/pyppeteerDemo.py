#  Created by IvanaH on 30/03/18.
#  coding: UTF-8

import asycio
from pyppeteer import launch
from pstats import browser

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.go("https://cn.bing.com")
    await page.screenshot('D:\JavaL\WorkSpace\PyTest','demo.png')
    await browser.close()
    
asyncio.get_event_loop().run_until_complete(main())
