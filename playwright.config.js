const fs = require("fs");

const { defineConfig, devices } = require("@playwright/test");

const python =
  process.env.PYTHON_BIN ||
  (process.platform === "win32"
    ? fs.existsSync(".venv\\Scripts\\python.exe")
      ? ".venv\\Scripts\\python.exe"
      : "python"
    : fs.existsSync(".venv/bin/python")
      ? ".venv/bin/python"
      : "python");

module.exports = defineConfig({
  testDir: "./tests/visual",
  timeout: 30_000,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 2 : 0,
  reporter: "list",
  snapshotPathTemplate: "{snapshotDir}/{testFilePath}-snapshots/{arg}-{projectName}{ext}",
  use: {
    baseURL: process.env.BASE_URL || "http://127.0.0.1:5000",
    colorScheme: "light",
    locale: "en-US",
    reducedMotion: "reduce",
    screenshot: "only-on-failure",
    trace: "retain-on-failure",
    launchOptions: process.env.PLAYWRIGHT_EXECUTABLE_PATH
      ? { executablePath: process.env.PLAYWRIGHT_EXECUTABLE_PATH }
      : undefined,
  },
  projects: [
    {
      name: "desktop",
      use: { ...devices["Desktop Chrome"], viewport: { width: 1280, height: 800 } },
    },
    {
      name: "mobile",
      use: { ...devices["Desktop Chrome"], viewport: { width: 390, height: 844 } },
    },
  ],
  webServer: [
    {
      command: `npm run build:css && ${python} -m flask --app demo.app run --no-debugger --no-reload --port 5000`,
      url: "http://127.0.0.1:5000",
      reuseExistingServer: !process.env.CI,
      timeout: 120_000,
    },
    {
      command: `${python} -m http.server 8000 --directory site`,
      url: "http://127.0.0.1:8000",
      reuseExistingServer: !process.env.CI,
      timeout: 120_000,
    },
  ],
});
