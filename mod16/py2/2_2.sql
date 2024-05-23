SELECT customer.full_name
FROM customer as customer
    WHERE NOT EXISTS(
        SELECT 1 FROM "order" as o
            WHERE o.customer_id == customer.customer_id
        )