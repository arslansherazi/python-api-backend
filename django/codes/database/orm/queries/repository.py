from django.db.models import F, Q, Count, Min, Max, Avg, Sum, Subquery
from django.db.models.functions import Coalesce, Concat

from queries.models import Customer, Item, Order, Supplier, Employee


class QueriesRepository:
    # SELECT (specific columns)
    def query1(self):
        raw_query = """
                    SELECT first_name, last_name, cnic_no AS identity_no
                    FROM customer
                    """
        query = Customer.objects.all()
        query = query.annotate(identity_no=F('cnic_no'))
        customers = query.values('first_name', 'last_name', 'identity_no')
        return customers

    # WHERE clause
    def query2(self, cnic_no):
        raw_query = """
                    SELECT *
                    FROM customer
                    WHERE cnic_no = value_here
                    """
        query = Customer.objects
        query = query.filter(cnic_no=cnic_no)
        customer = query.values()
        if customer:
            return customer[0]
        return {}

    # DISTINCT
    def query3(self):
        raw_query = """
                    SELECT DISTINCT(category)
                    FROM item
                    """
        query = Item.objects
        categories = query.values('category').distinct()
        return categories

    # AND Condition
    def query4(self, first_name, last_name):
        raw_query = """
                    SELECT *
                    FROM customer
                    WHERE first_name = value_here
                    AND last_name = value_here
                    """
        query = Customer.objects
        query = query.filter(first_name=first_name, last_name=last_name)
        customers = query.values()
        return customers

    # OR Condition
    def query5(self, category1, category2):
        raw_query = """
                    SELECT name
                    FROM item
                    WHERE category = value_here
                    OR category = value_here
                    """
        query = Item.objects
        query = query.filter(Q(category=category1) | Q(category=category2))
        items = query.values('name')
        return items

    # NOT Condition
    def query6(self, category):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE NOT category = value_here
                    """
        query = Item.objects
        query = query.filter(~Q(category=category))
        items = query.values()
        return items

    # LIKE
    def query7(self):
        raw_query = """
                    SELECT *
                    FROM customer
                    WHERE first_name LIKE 'a%n'
                    AND last_name LIKE '%sherazi%'
                    """
        query = Customer.objects
        query = query.filter(
            (
                    Q(first_name__startswith='a') &
                    Q(first_name__endswith='n')
            ),
            Q(last_name__contains='sherazi')
        )
        customers = query.values()
        return customers

    # GROUP BY & aggregate functions
    def query8(self):
        raw_query = """
                    SELECT COUNT(name), MIN(price), MAX(PRICE), AVG(PRICE), SUM(PRICE)
                    FROM item
                    GROUP BY category
                    """
        query = Item.objects
        query = query.all()
        query = query.values('category')
        result = query.annotate(
            items_count=Count('name'),
            minimum_price=Min('price'),
            maximum_price=Max('price'),
            average_price=Avg('price'),
            items_total_price=Sum('price')
        )
        return result

    # ORDER BY
    def query9(self):
        raw_query = """
                    SELECT *
                    FROM customer
                    ORDER BY id DESC
                    """
        query = Customer.objects
        query = query.all()
        query = query.order_by('-id')  # dash is used for DESC
        customers = query.values()
        return customers

    # LIMIT
    def query10(self, records_limit):
        raw_query = """
                    SELECT *
                    FROM item
                    LIMIT value_here
                    """
        query = Item.objects
        items = query.values()[:records_limit]
        return items

    # BETWEEN
    def query11(self, price1, price2):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price BETWEEN value_here AND value_here
                    """
        query = Item.objects
        query = query.filter(price__range=(price1, price2))
        items = query.values()
        return items

    # INNER QUERY & IN
    def query12(self, category):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE id IN (   SELECT id
                                    FROM item 
                                    WHERE category = value_here 
                                )
                    """
        inner_query = Item.objects
        inner_query = inner_query.filter(category=category)
        inner_query = inner_query.values('id')
        query = Item.objects
        query = query.filter(id__in=Subquery(inner_query))
        items = query.values()
        return items

    # INNER JOIN
    def query13(self):
        raw_query = """
                    SELECT c.first_name, c.last_name, c.cnic_no, i.name, i.category
                    FROM order o
                    INNER JOIN customer c ON o.customer_id = c.id
                    INNER JOIN item i on o.item_id = i.id
                    """
        query = Order.objects
        query = query.select_related('customer')
        query = query.select_related('item')
        orders_detail = query.values(
            first_name=F('customer__first_name'),
            last_name=F('customer__last_name'),
            cnic_no=F('customer__cnic_no'),
            item_name=F('item__name'),
            item_category=F('item__category')
        )
        return orders_detail

    # LEFT JOIN
    def query14(self):
        raw_query = """
                    SELECT i.name, i.category, o.customer_id, o.id AS order_id 
                    FROM item i
                    LEFT JOIN order o ON i.id = o.item_id
                    """
        query = Item.objects
        query = query.select_related('order')
        query = query.filter(Q(order__isnull=True) | Q(order__isnull=False))
        items_orders = query.values(
            item_name=F('name'),
            item_category=F('category'),
            customer_id=F('order__customer_id'),
            order_id=F('order__id'),
        )
        return items_orders

    # RIGHT JOIN
    def query15(self):
        raw_query = """
                    SELECT i.name, i.category, o.customer_id, o.id AS order_id 
                    FROM order o
                    RIGHT JOIN item i ON i.id = o.item_id
                    """
        # It is not supported by django orm yet. We can handle this by using raw query

    # SELF JOIN
    def query16(self):
        raw_query = """
                    SELECT e.name, m.name as manager_name, m.contact_no as manager_contact_no
                    FROM employee e
                    INNER JOIN employee m ON e.id = m.manager_id
                    """
        query = Employee.objects
        query = query.select_related('employee')
        query = query.filter(Q(employee__isnull=False))
        employees = query.values(
            employee_name=F('employee__name'),
            employee_contact_no=F('employee__contact_no'),
            manager_name=F('name'),
            manager_contact_no=F('contact_no')
        )
        return employees

    # FULL JOIN
    def query17(self):
        raw_query = """
                    SELECT e.name, m.name as manager_name, m.contact_no as manager_contact_no
                    FROM employee e
                    FULL JOIN employee m ON e.id = m.manager_id
                    """
        # It is not supported by django orm yet. We can handle this by using raw query

    # ANY
    def query18(self, category1, category2):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE category = ANY ( SELECT category
                                           FROM item 
                                           WHERE category = value_here
                                           OR category = value_here
                                          )
                    """
        # It is not supported by django orm yet. We can handle this by using raw query

    # ALL
    def query19(self, category):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price = ALL ( SELECT price
                                        FROM item 
                                        WHERE category = value_here 
                                       )
                    """
        # It is not supported by django orm yet. We can handle this by using raw query

    # EXISTS
    def query20(self, item_id):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE EXISTS (  SELECT *
                                    FROM item_supplier
                                    WHERE item_id = value_here
                                )
                    AND id = value_here
                    """
        inner_query = Item.supplier.through.objects
        inner_query = inner_query.filter(item_id=item_id)
        inner_query = inner_query.values()
        if inner_query.exists():
            query = Item.objects
            query = query.filter(id=item_id)
            item = query.values()
            return item
        return {}

    # HAVING
    def query21(self, items_count):
        raw_query = """
                    SELECT COUNT(item)
                    FROM item
                    GROUP BY category
                    HAVING COUNT(item) > value_here
                    """
        query = Item.objects
        query = query.values('category')
        query = query.annotate(items_count=Count('name'))
        items_count = query.filter(items_count__gt = 1)
        return items_count

    # >
    def query22(self, price):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price > value_here
                    """
        query = Item.objects
        query = query.filter(price__gt = price)
        items = query.values()
        return items

    # >=
    def query23(self, price):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price >= value_here
                    """
        query = Item.objects
        query = query.filter(price__gte=price)
        items = query.values()
        return items

    # <
    def query24(self, price):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price < value_here
                    """
        query = Item.objects
        query = query.filter(price__lt=price)
        items = query.values()
        return items

    # <=
    def query25(self, price):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price <= value_here
                    """
        query = Item.objects
        query = query.filter(price__lte=price)
        items = query.values()
        return items

    # null functions
    def query26(self):
        raw_query = """
                    SELECT name, category, COALESCE(price, 0) as item_price
                    FROM item
                    """
        query = Item.objects
        items = query.values('name', 'category', item_price=Coalesce('price', 0))
        return items

    # UNION & CONCAT
    def query27(self):
        raw_query = """
                    SELECT CONCAT(first_name, last_name) as customer_names FROM customer
                    UNION
                    SELECT CONCAT(first_name, last_name) as supplier_names FROM supplier
                    """
        query1 = Customer.objects
        query1 = query1.values(
            name=Concat('first_name', 'last_name')
        )
        query2 = Supplier.objects
        query2 = query2.values(
            name=Concat('first_name', 'last_name')
        )
        names = query1.union(query2)
        return names

    # Practice query
    def query28(self, customer_id, category):
        raw_query = """
                    SELECT CONCAT(c.first_name, c.last_name) AS customer_name, c.cnic_no AS customer_identity,
                    i.name AS order_item_name, i.category AS order_item_category, i.price AS order_item_price, 
                    CONCAT(s.first_name, s.last_name) AS supplier_name, s.phone_no AS supplier_contact_no
                    FROM customer c
                    INNER JOIN order o ON c.id = o.customer_id
                    INNER JOIN item i ON o.item_id = i.id
                    INNER JOIN item_supplier is ON i.id = is.item_id
                    INNER JOIN supplier s ON is.supplier_id = s.supplier_id
                    WHERE c.id = value_here
                    AND o.item_id IN ( SELECT id 
                                       FROM item
                                       WHERE category = value_here
                                      )  
                    """
        inner_query = Item.objects
        inner_query = inner_query.filter(category=category)
        inner_query = inner_query.values('id')
        query = Order.objects
        query = query.select_related('customer')
        query = query.select_related('item')
        query = query.filter(customer__id=customer_id, item_id__in=Subquery(inner_query))
        customer_info = query.values(
            customer_name=Concat('customer__first_name', 'customer__last_name'),
            customer_identity=F('customer__cnic_no'),
            order_item_name=F('item__name'),
            order_item_category=F('item__category'),
            order_item_price=F('item__price'),
        )
        return customer_info

        # writing complex queries are very difficult in django orm. Use raw queries for complex queries
