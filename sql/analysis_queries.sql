-- STEP 2: SQL ANALYSIS
-- Assume the processed dataset 'cleaned_marketing_data.csv' is loaded into a table named 'campaign_performance'.

-- 1. Total Campaign Spend & Revenue
SELECT 
    ROUND(SUM(Cost), 2) AS Total_Spend,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND((SUM(Revenue) - SUM(Cost)) / NULLIF(SUM(Cost), 0) * 100, 2) AS Overall_ROI_Percentage
FROM campaign_performance;


-- 2. ROI by Campaign and Channel
SELECT 
    Campaign_Name,
    Channel,
    ROUND(SUM(Cost), 2) AS Total_Cost,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND((SUM(Revenue) - SUM(Cost)) / NULLIF(SUM(Cost), 0) * 100, 2) AS ROI_Percentage
FROM campaign_performance
GROUP BY Campaign_Name, Channel
ORDER BY ROI_Percentage DESC;


-- 3. Top Performing Campaigns (by Revenue and ROI)
SELECT 
    Campaign_ID,
    Campaign_Name,
    Channel,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND((SUM(Revenue) - SUM(Cost)) / NULLIF(SUM(Cost), 0) * 100, 2) AS ROI_Percentage
FROM campaign_performance
GROUP BY Campaign_ID, Campaign_Name, Channel
ORDER BY Total_Revenue DESC
LIMIT 10;


-- 4. CTR & Conversion Rate by Channel
SELECT 
    Channel,
    SUM(Impressions) AS Total_Impressions,
    SUM(Clicks) AS Total_Clicks,
    SUM(Conversions) AS Total_Conversions,
    ROUND(CAST(SUM(Clicks) AS FLOAT) / NULLIF(SUM(Impressions), 0) * 100, 2) AS Avg_CTR_Percentage,
    ROUND(CAST(SUM(Conversions) AS FLOAT) / NULLIF(SUM(Clicks), 0) * 100, 2) AS Avg_Conversion_Rate_Percentage
FROM campaign_performance
GROUP BY Channel
ORDER BY Avg_Conversion_Rate_Percentage DESC;


-- 5. Daily/Monthly Campaign Trends
-- Monthly Trend Example (using generic SUBSTR for YYYY-MM if Date is YYYY-MM-DD string)
SELECT 
    SUBSTR(Date, 1, 7) AS Month,
    COUNT(Campaign_ID) AS Total_Campaigns_Run,
    ROUND(SUM(Cost), 2) AS Monthly_Spend,
    ROUND(SUM(Revenue), 2) AS Monthly_Revenue
FROM campaign_performance
GROUP BY SUBSTR(Date, 1, 7)
ORDER BY Month ASC;


-- 6. Region-wise Campaign Performance
SELECT 
    Region,
    COUNT(DISTINCT Campaign_ID) AS Unique_Campaigns,
    ROUND(SUM(Cost), 2) AS Region_Spend,
    ROUND(SUM(Revenue), 2) AS Region_Revenue,
    ROUND((SUM(Revenue) - SUM(Cost)) / NULLIF(SUM(Cost), 0) * 100, 2) AS Region_ROI_Percentage
FROM campaign_performance
GROUP BY Region
ORDER BY Region_Revenue DESC;
