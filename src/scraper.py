from playwright.async_api import async_playwright
import json
import asyncio
import time

timestamp = int(time.time())
url = f"https://ndis.gov.au/sites/default/files/react_extract/provider_finder/build/data/list-providers.json?nocache={timestamp}"
base_url = "https://ndis.gov.au/"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False, args=["--disable-blink-features=AutomationControlled"]
        )
        temp_page = await browser.new_page()

        current_user_agent = await temp_page.evaluate("navigator.userAgent")
        screen_width = await temp_page.evaluate("screen.width")
        screen_height = await temp_page.evaluate("screen.height")

        await temp_page.close()

        print(f"Detected Resolution: {screen_width}x{screen_height}")

        context = await browser.new_context(
            user_agent=current_user_agent,
            viewport={"width": screen_width, "height": screen_height},
            device_scale_factor=1,
        )

        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)

        page = await context.new_page()
        print("Visiting main site to clear security clearance...")

        await page.goto(base_url)
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(2000)
        print("Navigating to JSON URL...")

        await page.goto(url)
        await page.wait_for_load_state("networkidle")
        print("Waiting for data to load...")

        try:
            raw_text = await page.locator("body").inner_text()
            provider_data = json.loads(raw_text)
            print("Success! Bypassed Cloudflare and retrieved data.")
            with open("ndis_providers.json", "w", encoding="utf-8") as f:
                json.dump(provider_data, f, indent=4)
                print("Data saved to ndis_providers.json")
        except json.JSONDecodeError:
            print(
                "Failed. The page content was not valid JSON. Cloudflare might still be blocking us."
            )
            print("Page content snapshot:")
            content = await page.content()
            print(content[:500])
        await page.wait_for_timeout(6000)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
