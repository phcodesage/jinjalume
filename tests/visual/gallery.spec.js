const { test, expect } = require("@playwright/test");

async function screenshotOptions(page, testInfo) {
  const viewport = page.viewportSize();
  const minimumHeight = testInfo.project.name === "mobile" ? 2196 : 1520;
  const contentHeight = await page.evaluate(
    () => document.documentElement.scrollHeight,
  );
  const height = Math.max(contentHeight, minimumHeight);

  await page.setViewportSize({ ...viewport, height });

  return {
    animations: "disabled",
    fullPage: false,
    maxDiffPixelRatio: 0.05,
  };
}

test.describe("component gallery", () => {
  test("gallery layout remains stable", async ({ page }, testInfo) => {
    await page.goto("/");
    await expect(page).toHaveTitle(/component gallery/);
    await expect(page).toHaveScreenshot(
      "gallery.png",
      await screenshotOptions(page, testInfo),
    );
  });

  test("mobile layout remains stable", async ({ page }, testInfo) => {
    await page.goto("/");
    await expect(page).toHaveScreenshot(
      "gallery.png",
      await screenshotOptions(page, testInfo),
    );
  });

  test("dark theme remains readable", async ({ page }, testInfo) => {
    await page.goto("/");
    await page.evaluate(() => {
      document.documentElement.dataset.theme = "dark";
    });
    await expect(page).toHaveScreenshot(
      "gallery-dark.png",
      await screenshotOptions(page, testInfo),
    );
  });
});
