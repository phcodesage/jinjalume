const { test, expect } = require("@playwright/test");

async function blockScreenshotOptions(page, testInfo, desktopHeight, mobileHeight) {
  const viewport = page.viewportSize();
  const minimumHeight = testInfo.project.name === "mobile" ? mobileHeight : desktopHeight;
  const contentHeight = await page.evaluate(
    () => document.documentElement.scrollHeight,
  );

  await page.setViewportSize({
    ...viewport,
    height: Math.max(contentHeight, minimumHeight),
  });

  return {
    animations: "disabled",
    fullPage: false,
    maxDiffPixelRatio: 0.05,
  };
}

test.describe("UI blocks", () => {
  test("login block remains stable", async ({ page }, testInfo) => {
    await page.goto("/login");
    await expect(page).toHaveScreenshot(
      "login.png",
      await blockScreenshotOptions(page, testInfo, 800, 844),
    );
  });

  test("signup block remains stable", async ({ page }, testInfo) => {
    await page.goto("/signup");
    await expect(page).toHaveScreenshot(
      "signup.png",
      await blockScreenshotOptions(page, testInfo, 800, 844),
    );
  });

  test("admin dashboard remains stable", async ({ page }, testInfo) => {
    await page.goto("/admin");
    await expect(page).toHaveScreenshot(
      "admin.png",
      await blockScreenshotOptions(page, testInfo, 1000, 2050),
    );
  });
});
