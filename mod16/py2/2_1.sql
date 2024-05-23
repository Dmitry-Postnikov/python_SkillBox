SELECT customer.full_name, manager.full_name, o.date, o.purchase_amount
FROM customer AS customer
    JOIN manager manager on customer.manager_id = manager.manager_id
    JOIN "order" o on customer.customer_id = o.customer_id