{{ config(materialized='view') }}

SELECT
    s.CONTAINER_ID,
    s.TIMESTAMP,
    s.TEMPERATURE,
    s.HUMIDITY,
    s.VIBRATION,
    s.STATUS,
    s.DATA_VALID,

    c.COMMODITY,
    c.ORIGIN_MARKET,
    c.SECONDARY_MARKET,
    c.ORIGIN_PRICE_PER_KG,
    c.SECONDARY_MARKET_PRICE_PER_KG

FROM {{ ref('stg_sensor_data') }} s

CROSS JOIN {{ ref('stg_commodity_prices') }} c