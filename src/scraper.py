from playwright.async_api import async_playwright
import json
import asyncio
url = "https://ndis.gov.au/sites/default/files/react_extract/provider_finder/build/data/list-providers.json?nocache=1783790388"
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()
        print("Navigating to JSON URL and solving Cloudflare challenge...")
        await page.goto(url)
        await page.wait_for_load_state("networkidle")
        try:
            raw_text = await page.locator("body").inner_text()
            provider_data = json.loads(raw_text)
            print("Success! Bypassed Cloudflare and retrieved data.")
            with open("ndis_providers.json", "w", encoding="utf-8") as f:
                json.dump(provider_data, f, indent=4)
                print("Data saved to ndis_providers.json")
        except json.JSONDecodeError:
            print("Failed. The page content was not valid JSON. Cloudflare might still be blocking us.")
            print("Page content snapshot:")
            content = await page.content()
            print(content[:500])
        await page.wait_for_timeout(6000)
        await browser.close()
if __name__ == "__main__":
    asyncio.run(main())