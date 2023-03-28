from sqlalchemy import distinct, or_
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func

from app import db
from models import Customer, Item, Order, Employee, Supplier, ItemSupplier


class QueriesRepository:
    # SELECT (specific columns)
    def query1(self):
        raw_query = """
                    SELECT first_name, last_name, cnic_no AS identity_no
                    FROM customer
                    """
        result = db.session.query(Customer.first_name, Customer.last_name, Customer.cnic_no.label('identity_no'))
        customers = self.get_all(result)
        return customers

    # WHERE clause
    def query2(self, cnic_no):
        raw_query = """
                    SELECT *
                    FROM customer
                    WHERE cnic_no = value_here
                    """
        query = db.session.query(Customer)
        query = query.filter(Customer.cnic_no == cnic_no)
        result = query.first()
        customer = self.get_object_one(result)
        return customer

    # DISTINCT
    def query3(self):
        raw_query = """
                    SELECT DISTINCT(category)
                    FROM item
                    """
        result = db.session.query(distinct(Item.category))
        item_categories = self.get_all(result)
        return item_categories

    # AND Condition
    def query4(self, first_name, last_name):
        raw_query = """
                    SELECT *
                    FROM customer
                    WHERE first_name = value_here
                    AND last_name = value_here
                    """
        query = db.session.query(Customer)
        result = query.filter(Customer.first_name == first_name, Customer.last_name == last_name)
        customers = self.get_objects_all(result)
        return customers

    # OR Condition
    def query5(self, category1, category2):
        raw_query = """
                    SELECT name
                    FROM item
                    WHERE category = value_here
                    OR category = value_here
                    """
        query = db.session.query(Item.name)
        result = query.filter(or_(Item.category == category1, Item.category == category2))
        items_names = self.get_all(result)
        final_items_names = []
        for item_name in items_names:
            final_items_names.append(item_name.get('name'))
        return final_items_names

    # NOT Condition
    def query6(self, category):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE NOT category = value_here
                    """
        query = db.session.query(Item.name)
        result = query.filter(Item.category != category)
        items_names = self.get_all(result)
        final_items_names = []
        for item_name in items_names:
            final_items_names.append(item_name.get('name'))
        return final_items_names

    # LIKE
    def query7(self):
        raw_query = """
                    SELECT *
                    FROM customer
                    WHERE first_name LIKE 'a%n'
                    AND last_name LIKE '%sherazi%'
                    """
        query = db.session.query(Customer)
        result = query.filter(Customer.first_name.like('a%n'), Customer.last_name.like('%sherazi%'))
        customers = self.get_objects_all(result)
        return customers

    # GROUP BY & aggregate functions
    def query8(self):
        raw_query = """
                    SELECT COUNT(name), MIN(price), MAX(PRICE), AVG(PRICE), SUM(PRICE)
                    FROM item
                    GROUP BY category
                    """
        query = db.session.query(
            Item.category,
            func.count(Item.name).label('items_count'),
            func.min(Item.price).label('items_minimum_price'),
            func.max(Item.price).label('items_maximum_price'),
            func.avg(Item.price).label('items_average_price'),
            func.sum(Item.price).label('items_total_price')
        )
        result = query.group_by(Item.category)
        items_details = self.get_all(result)
        for item_detail in items_details:
            item_detail['items_minimum_price'] = float(item_detail['items_minimum_price'])
            item_detail['items_maximum_price'] = float(item_detail['items_maximum_price'])
            item_detail['items_average_price'] = float(item_detail['items_average_price'])
            item_detail['items_total_price'] = float(item_detail['items_total_price'])
        return items_details

    # ORDER BY
    def query9(self):
        raw_query = """
                    SELECT *
                    FROM customer
                    ORDER BY id DESC
                    """
        query = db.session.query(Customer)
        result = query.order_by(Customer.id.desc())
        customers = self.get_objects_all(result)
        return customers

    # LIMIT
    def query10(self, records_limit):
        raw_query = """
                    SELECT *
                    FROM item
                    LIMIT value_here
                    """
        query = db.session.query(Item)
        result = query.limit(records_limit)
        items = self.get_objects_all(result.all())
        return items

    # BETWEEN
    def query11(self, price1, price2):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price BETWEEN value_here AND value_here
                    """
        query = db.session.query(Item)
        result = query.filter(Item.price.between(price1, price2))
        items = self.get_objects_all(result)
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
        inner_query = db.session.query(Item.id)
        inner_query = inner_query.filter(Item.category == category).subquery()
        query = db.session.query(Item)
        result = query.filter(Item.id.in_(inner_query))
        items = self.get_objects_all(result)
        return items

    # INNER JOIN
    def query13(self):
        raw_query = """
                    SELECT c.first_name, c.last_name, c.cnic_no, i.name, i.category
                    FROM order o
                    INNER JOIN customer c ON o.customer_id = c.id
                    INNER JOIN item i on o.item_id = i.id
                    """
        o = aliased(Order)
        c = aliased(Customer)
        i = aliased(Item)
        query = db.session.query(c.first_name, c.cnic_no, i.name, i.category)
        query = query.select_from(o)
        query = query.join(c)
        result = query.join(i)
        orders = self.get_all(result)
        return orders

    # LEFT JOIN
    def query14(self):
        raw_query = """
                    SELECT i.name, i.category, o.customer_id, o.id AS order_id 
                    FROM item i
                    LEFT JOIN order o ON i.id = o.item_id
                    """
        o = aliased(Order)
        i = aliased(Item)
        query = db.session.query(i.name, i.category, o.customer_id, o.id.label('order_id'))
        result = query.join(o, isouter=True)
        orders_items = self.get_all(result)
        return orders_items

    # RIGHT JOIN
    def query15(self):
        raw_query = """
                    SELECT i.name, i.category, o.customer_id, o.id AS order_id 
                    FROM order o
                    RIGHT JOIN item i ON i.id = o.item_id
                    """
        # right join is not supported by sqlalchemy. To achieve right join results, swap the tables and use left join
        o = aliased(Order)
        i = aliased(Item)
        query = db.session.query(o.customer_id, o.id.label('order_id'), i.name, i.category)
        query = query.select_from(i)
        result = query.join(o, isouter=True)
        orders = self.get_all(result)
        return orders

    # SELF JOIN
    def query16(self):
        raw_query = """
                    SELECT e.name, m.name as manager_name, m.contact_no as manager_contact_no
                    FROM employee e
                    INNER JOIN employee m ON e.id = m.manager_id
                    """
        e = aliased(Employee)
        m = aliased(Employee)
        query = db.session.query(
            e.name, e.contact_no, e.department, m.name.label('manager_name'), m.contact_no.label('manager_contact_no')
        )
        query = query.select_from(e)
        result = query.join(m, e.manager_id == m.id)
        employees = self.get_all(result)
        return employees

    # FULL JOIN
    def query17(self): pass
        # full outer join is implemented using join(full=true) in sqlalchemy but mysql does not support full outer join
        # full outer join can be implemented in mysql by union of left join & right join

    # EXISTS
    def query18(self, item_id):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE EXISTS (  SELECT *
                                    FROM item_supplier
                                    WHERE item_id = value_here
                                )
                    AND id = value_here
                    """
        _query = db.session.query(ItemSupplier)
        _query = _query.filter(ItemSupplier.item_id == item_id)
        query = db.session.query(Item)
        result = query.filter(_query.exists(), Item.id == item_id)
        item = self.get_object_one(result.first())
        return item

    # HAVING
    def query19(self, items_count):
        raw_query = """
                    SELECT category, COUNT(item) AS items_count
                    FROM item
                    GROUP BY category
                    HAVING COUNT(item) > value_here
                    """
        query = db.session.query(Item.category, func.count(Item.name).label('items_count'))
        query = query.group_by(Item.category)
        result = query.having(func.count(Item.name) > items_count)
        items_count = self.get_all(result)
        return items_count

    # >
    def query20(self, price):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price > value_here
                    """
        query = db.session.query(Item)
        result = query.filter(Item.price > price)
        items = self.get_objects_all(result)
        return items

    # >=
    def query21(self, price):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price >= value_here
                    """
        query = db.session.query(Item)
        result = query.filter(Item.price >= price)
        items = self.get_objects_all(result)
        return items

    # <
    def query22(self, price):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price < value_here
                    """
        query = db.session.query(Item)
        result = query.filter(Item.price < price)
        items = self.get_objects_all(result)
        return items

    # <=
    def query23(self, price):
        raw_query = """
                    SELECT *
                    FROM item
                    WHERE price <= value_here
                    """
        query = db.session.query(Item)
        result = query.filter(Item.price <= price)
        items = self.get_objects_all(result)
        return items

    # null functions
    def query24(self):
        raw_query = """
                    SELECT name, category, COALESCE(price, 0) as item_price
                    FROM item
                    """
        result = db.session.query(Item.name, Item.category, func.ifnull(Item.price, 0).label('item_price'))
        items = self.get_all(result)
        return items

    # UNION & CONCAT
    def query25(self):
        raw_query = """
                    SELECT CONCAT(first_name, last_name) as customer_names FROM customer
                    UNION
                    SELECT CONCAT(first_name, last_name) as supplier_names FROM supplier
                    """
        query1 = db.session.query(func.concat(Customer.first_name, ' ', Customer.last_name).label('name'))
        query2 = db.session.query(func.concat(Supplier.first_name, ' ', Supplier.last_name).label('name'))
        result = query1.union(query2)
        users = self.get_all(result)
        final_users = []
        for user in users:
            name = user.get('name')
            final_users.append(name)
        return final_users

    # Practice query
    def query26(self, customer_id, category):
        raw_query = """
                    SELECT CONCAT(c.first_name, c.last_name) AS customer_name, c.cnic_no AS customer_identity,
                    i.name AS order_item_name, i.category AS order_item_category, i.price AS order_item_price, 
                    CONCAT(s.first_name, s.last_name) AS supplier_name, s.phone_no AS supplier_contact_no
                    FROM customer c
                    INNER JOIN order o ON c.id = o.customer_id
                    INNER JOIN item i ON o.item_id = i.id
                    INNER JOIN item_supplier is ON i.id = is.item_id
                    INNER JOIN supplier s ON is.supplier_id = s.id
                    WHERE c.id = value_here
                    AND o.item_id IN ( SELECT id 
                                       FROM item
                                       WHERE category = value_here
                                      )  
                    """
        c = aliased(Customer)
        o = aliased(Order)
        i = aliased(Item)
        i_s = aliased(ItemSupplier)
        s = aliased(Supplier)
        _query = db.session.query(Item.id)
        _query = _query.filter(Item.category == category)
        query = db.session.query(
            func.concat(c.first_name, ' ', c.last_name).label('customer_name'), c.cnic_no.label('customer_identity'),
            i.name.label('order_item_name'), i.category.label('order_item_category'), i.price.label('order_item_price'),
            func.concat(s.first_name, ' ', s.last_name).label('supplier_name'), s.phone_no.label('supplier_contact_no')
        )
        query = query.select_from(c)
        query = query.join(o)
        query = query.join(i)
        query = query.join(i_s)
        query = query.join(s)
        result = query.filter(c.id == customer_id, o.item_id.in_(_query))
        customer_orders_information = self.get_all(result)
        return customer_orders_information

    # utility functions
    def get_objects_all(self, result):
        records = []
        for row in result:
            record = self.get_object_one(row)
            records.append(record)
        return records

    def get_all(self, result):
        records = []
        for row in result:
            if row._fields:
                record = dict(zip(row._fields, row))
            else:
                record = row[0]
            records.append(record)
        return records

    def get_object_one(self, result):
        if not result:
            return {}
        record = result.__dict__
        del record['_sa_instance_state']
        return record

    def get_one(self, result):
        if not result:
            return {}
        record = dict(zip(result._fields, result))
        return record
