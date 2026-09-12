const { test, expect } = require("@playwright/test");

test.use({ baseURL: "http://127.0.0.1:8000" });

test.describe("landing page", () => {
  test("shows the UI block catalog", async ({ page }) => {
    await page.goto("/");

    await expect(page).toHaveTitle(/UI for Python apps/);
    await expect(page.locator("h1")).toContainText("Jinja.");
    await expect(page.locator("#blocks")).toContainText("Composition blocks");
    await expect(page.locator("#login-block")).toContainText("Welcome back");
    await expect(page.locator("#signup-block")).toContainText("Create your account");
    await expect(page.locator("#admin-block")).toContainText("Recent orders");
  });

  test("mobile navigation exposes the block links", async ({ page }) => {
    test.skip(test.info().project.name !== "mobile", "Mobile navigation is covered by the mobile project.");
    await page.goto("/");

    const menuButton = page.locator("[data-menu-toggle]");
    const mobileMenu = page.locator("[data-mobile-menu]");

    await expect(mobileMenu).toBeHidden();
    await menuButton.click();
    await expect(menuButton).toHaveAttribute("aria-expanded", "true");
    await expect(mobileMenu).toBeVisible();
    await expect(mobileMenu).toContainText("UI blocks");
  });
});
