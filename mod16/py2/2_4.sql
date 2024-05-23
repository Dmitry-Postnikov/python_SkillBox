SELECT customer.full_name, o.order_no
FROM customer as customer
    JOIN "order" o on customer.customer_id = o.customer_id
    WHERE customer.manager_id IS NULL