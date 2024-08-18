-- 1. Análise Temporal de Vendas Semanais por Loja
SELECT 
    Store, 
    YEAR(Date) AS Year, 
    WEEK(Date) AS Week, 
    SUM(Weekly_Sales) AS Total_Weekly_Sales
FROM 
    WalmartSales
GROUP BY 
    Store, YEAR(Date), WEEK(Date)
ORDER BY 
    Store, YEAR(Date), WEEK(Date);

-- 2. Impacto de Feriados nas Vendas por Mês
SELECT 
    CASE 
        WHEN MONTH(Date) = 1 THEN 'January'
        WHEN MONTH(Date) = 2 THEN 'February'
        WHEN MONTH(Date) = 3 THEN 'March'
        WHEN MONTH(Date) = 4 THEN 'April'
        WHEN MONTH(Date) = 5 THEN 'May'
        WHEN MONTH(Date) = 6 THEN 'June'
        WHEN MONTH(Date) = 7 THEN 'July'
        WHEN MONTH(Date) = 8 THEN 'August'
        WHEN MONTH(Date) = 9 THEN 'September'
        WHEN MONTH(Date) = 10 THEN 'October'
        WHEN MONTH(Date) = 11 THEN 'November'
        WHEN MONTH(Date) = 12 THEN 'December'
    END AS Month,
    Holiday_Flag AS Holiday,
    SUM(Weekly_Sales) AS Total_Sales
FROM 
    WalmartSales
WHERE 
    Store = '$store'
    AND YEAR(Date) = '$year'
GROUP BY 
    MONTH(Date), Holiday_Flag
ORDER BY 
    MONTH(Date), Holiday_Flag;

-- 3. Influência da Temperatura nas Vendas
SELECT 
    CASE
        WHEN Temperature < 50 THEN 'Below 50°F'
        WHEN Temperature BETWEEN 50 AND 70 THEN '50°F - 70°F'
        WHEN Temperature BETWEEN 71 AND 85 THEN '71°F - 85°F'
        ELSE 'Above 85°F'
    END AS Temperature_Range,
    AVG(Weekly_Sales) AS Average_Sales
FROM 
    WalmartSales
GROUP BY 
    Temperature_Range
ORDER BY 
    Temperature_Range;

-- 4. Análise do Preço do Combustível nas Vendas
SELECT 
    CASE
        WHEN Fuel_Price < 2.5 THEN 'Below $2.50'
        WHEN Fuel_Price BETWEEN 2.5 AND 3.0 THEN '$2.50 - $3.00'
        WHEN Fuel_Price BETWEEN 3.01 AND 3.5 THEN '$3.01 - $3.50'
        ELSE 'Above $3.50'
    END AS Fuel_Price_Range,
    AVG(Weekly_Sales) AS Average_Sales
FROM 
    WalmartSales
GROUP BY 
    Fuel_Price_Range
ORDER BY 
    Fuel_Price_Range;

-- 5. Segmentação de Lojas por Desempenho
SELECT 
    CASE
        WHEN AVG(Weekly_Sales) > (SELECT AVG(Weekly_Sales) + STDDEV(Weekly_Sales) FROM WalmartSales) THEN 'Alto Desempenho'
        WHEN AVG(Weekly_Sales) < (SELECT AVG(Weekly_Sales) - STDDEV(Weekly_Sales) FROM WalmartSales) THEN 'Baixo Desempenho'
        ELSE 'Desempenho Médio'
    END AS Performance_Segment,
    COUNT(Store) AS Number_of_Stores
FROM 
    WalmartSales
GROUP BY 
    Performance_Segment
ORDER BY 
    Performance_Segment;
