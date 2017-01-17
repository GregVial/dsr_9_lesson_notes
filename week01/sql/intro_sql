/* film titles with their actors' names */
select f.title, a.first_name, a.last_name from film f, actor a, film_actor fa 
where fa.actor_id = a.actor_id
and fa.film_id = f.film_id

/* films not in inventory */
select f.title from film f
left join inventory i
on f.film_id = i.film_id
where i.film_id is null

/* films returned on 2005-05-27 */
select distinct(f.title)
from film f
inner join inventory i
on f.film_id = i.film_id
inner join rental r
on i.inventory_id = r.inventory_id
where cast(r.return_date as date) = '2005-05-27'

/* customers ranked by how much they've spent */
select c.first_name, c.last_name, sum(p.amount) as "Sum ($)" from payment p
full outer join customer c
on p.customer_id = c.customer_id
group by c.customer_id

/* customers who have spent more than 200 */
select c.first_name, c.last_name, sum(p.amount) as "Sum ($)" from payment p
full outer join customer c
on p.customer_id = c.customer_id
group by c.customer_id
having sum (p.amount)> 200

/* stores with more than 100 customers */
SELECT store_id, COUNT (customer_id)
FROM customer GROUP BY   store_id 
HAVING COUNT (customer_id) > 100

/* the number of rentals from each category */
select c.name, count(r.rental_id)
from category c
	join film_category fc using (category_id)
	join film f using (film_id)
	join inventory i using (film_id)
	join rental r using (inventory_id)
group by name
order by sum(r.rental_id) desc
