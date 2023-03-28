from django.codes.common.base_resource import BasePostResource
from apis.order.validation import OrderSerializer
from models import Order


class OrderApi(BasePostResource):
    end_point = 'order'
    request_validator = OrderSerializer()

    def populate_request_arguments(self):
        """
        Populates request arguments
        """
        self.item_id = self.request_args.get('item_id')
        self.quantity = self.request_args.get('quantity')

    def save_order(self):
        """
        Saves order
        """
        self.is_order_saved = Order.save_order_into_db(self.item_id, self.quantity)

    def prepare_response(self):
        """
        Prepares response
        """
        self.response = {
            'data': {
                'is_order_saved': True
            }
        }
        if not self.is_order_saved:
            self.response['data']['is_order_saved'] = False

    def process_request(self):
        """
        Process request
        """
        self.populate_request_arguments()
        self.save_order()
        self.prepare_response()
