{{ config(materialized='view') }}

SELECT
    TRIM(COMMODITY) AS COMMODITY,
    TRIM(ORIGIN_MARKET) AS ORIGIN_MARKET,
    TRIM(SECONDARY_MARKET) AS SECONDARY_MARKET,
    ROUND(ORIGIN_PRICE_PER_KG, 2) AS ORIGIN_PRICE_PER_KG,
    ROUND(SECONDARY_MARKET_PRICE_PER_KG, 2) AS SECONDARY_MARKET_PRICE_PER_KG
FROM {{ ref('commodity_prices') }}
WHERE COMMODITY IS NOT NULL
  AND ORIGIN_MARKET IS NOT NULL
  AND SECONDARY_MARKET IS NOT NULL
models:

  - name: stg_sensor_data
    ...

  - name: stg_commodity_prices
    description: "Cleaned commodity pricing data used for AtmoSync market analysis."

    columns:
      - name: COMMODITY
        description: "Name of the commodity."
        tests:
          - not_null

      - name: ORIGIN_MARKET
        description: "Market where the commodity originates."
        tests:
          - not_null

      - name: SECONDARY_MARKET
        description: "Secondary market where the commodity may be rerouted."
        tests:
          - not_null

      - name: ORIGIN_PRICE_PER_KG
        description: "Commodity price per kilogram at the origin market."

      - name: SECONDARY_MARKET_PRICE_PER_KG
        description: "Commodity price per kilogram at the secondary market."


  - name: stg_sensor_commodity
    description: "Combined sensor and commodity market data for AtmoSync analysis."

    columns:
      - name: CONTAINER_ID
        description: "Unique identifier of the shipping container."
        tests:
          - not_null

      - name: COMMODITY
        description: "Commodity associated with the market scenario."
        tests:
          - not_null

      - name: ORIGIN_MARKET
        description: "Origin market for the commodity."
        tests:
          - not_null

      - name: SECONDARY_MARKET
        description: "Secondary market for the commodity."
        tests:
          - not_null