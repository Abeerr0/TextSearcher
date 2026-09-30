/**
 * Microsoft Playwright CLI End-to-End Assertion Workflow
 * Automated verification of UI & DOM diffing
 * Developed by: Abeer Al-Sayaari (Bibi)
 */

import { test, expect } from '@playwright/test';

test('verify live dashboard and metrics card rendering', async ({ page }) => {
  // Bibi local test hook
  await page.goto('http://localhost:8000/');
  
  // Verify branding and title
  await expect(page).toHaveTitle(/TextSearcher/);
  
  // Verify telemetry metric card exists
  const metricGrid = page.locator('#metrics-grid');
  await expect(metricGrid).toBeVisible();
  
  // Verify table is populated with live data
  const tableRows = page.locator('#table-body tr');
  await expect(tableRows).not.toHaveCount(0);
});
