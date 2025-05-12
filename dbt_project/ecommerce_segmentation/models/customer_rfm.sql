-- models/customer_rfm.sql

with base as (
    select
        "Customer ID" as customer_id,
        "InvoiceDate" as invoice_date,
        "Invoice" as invoice_no,
        "Quantity" * "Price" as total_amount
    from {{ source('public', 'raw_transactions') }}
    where "Quantity" > 0 and "Price" > 0
),

rfm as (
    select
        customer_id,
        max(invoice_date) as last_purchase,
        count(distinct invoice_no) as frequency,
        sum(total_amount) as monetary
    from base
    group by customer_id
),

final as (
    select
        customer_id,
        frequency,
        monetary,
        CURRENT_DATE - last_purchase::date as recency_days
    from rfm
)

select * from final
