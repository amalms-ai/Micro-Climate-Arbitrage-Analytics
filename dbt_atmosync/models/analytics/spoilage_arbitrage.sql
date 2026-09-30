{{ config(materialized='view') }}

SELECT
    CONTAINER_ID,
    TIMESTAMP,
    COMMODITY,
    ORIGIN_MARKET,
    SECONDARY_MARKET,

    TEMPERATURE,
    HUMIDITY,
    VIBRATION,

    STATUS,
    DATA_VALID,

    SPOILAGE_RISK_LEVEL,
    SPOILAGE_RISK_SCORE,

    ORIGIN_PRICE_PER_KG,
    SECONDARY_MARKET_PRICE_PER_KG,

    SPOILAGE_ARBITRAGE_PER_KG,
    ROUND(
    SPOILAGE_ARBITRAGE_PER_KG * 100,
    2
    ) AS POTENTIAL_ARBITRAGE_VALUE,  

    CASE
        WHEN SPOILAGE_RISK_LEVEL = 'High'
             AND SPOILAGE_ARBITRAGE_PER_KG > 0
            THEN 'Consider Rerouting'

        WHEN SPOILAGE_RISK_LEVEL = 'Medium'
             AND SPOILAGE_ARBITRAGE_PER_KG > 0
            THEN 'Monitor and Consider Rerouting'

        WHEN SPOILAGE_RISK_LEVEL = 'Low'
             AND SPOILAGE_ARBITRAGE_PER_KG > 0
            THEN 'Arbitrage Opportunity'

        ELSE 'No Rerouting Opportunity'
        END AS REROUTING_RECOMMENDATION,

    CASE
        WHEN SPOILAGE_RISK_LEVEL = 'High'
             AND SPOILAGE_ARBITRAGE_PER_KG > 0
            THEN 'High Priority'

        WHEN SPOILAGE_RISK_LEVEL = 'Medium'
             AND SPOILAGE_ARBITRAGE_PER_KG > 0
            THEN 'Medium Priority'

        WHEN SPOILAGE_RISK_LEVEL = 'Low'
             AND SPOILAGE_ARBITRAGE_PER_KG > 0
            THEN 'Opportunity'

        ELSE 'Low Priority'
    END AS BUSINESS_PRIORITY

FROM {{ ref('spoilage_risk') }}