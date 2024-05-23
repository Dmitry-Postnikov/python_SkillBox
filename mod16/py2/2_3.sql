SELECT customer.full_name, manager.full_name, o.order_no
FROM customer as customer
    JOIN "order" o on customer.customer_id = o.customer_id
    JOIN manager manager on manager.manager_id = customer.manager_id
    WHERE customer.city != manager.city