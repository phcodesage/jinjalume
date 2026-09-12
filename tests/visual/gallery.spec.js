const { test, expect } = require("@playwright/test");

test.describe("component gallery", () => {
  test("gallery layout remains stable", async ({ page }) => {
    await page.goto("/");
    await expect(page).toHaveTitle(/component gallery/);
    await expect(page).toHaveScreenshot("gallery.png", {
      animations: "disabled",
      fullPage: true,
      maxDiffPixelRatio: 0.05,
    });
  });

  test("mobile layout remains stable", async ({ page }) => {
    await page.goto("/");
    await expect(page).toHaveScreenshot("gallery.png", {
      animations: "disabled",
      fullPage: true,
      maxDiffPixelRatio: 0.05,
    });
  });

  test("dark theme remains readable", async ({ page }) => {
    await page.goto("/");
    await page.evaluate(() => {
      document.documentElement.dataset.theme = "dark";
    });
    await expect(page).toHaveScreenshot("gallery-dark.png", {
      animations: "disabled",
      fullPage: true,
      maxDiffPixelRatio: 0.05,
    });
  });
});
