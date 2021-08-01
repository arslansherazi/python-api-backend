from Django.Codes.common.base_resource import BasePostResource
from apis.delete_order.validation import DeleteOrderSerializer
from models import Order


class DeleteOrder(BasePostResource):
    end_point = 'delete_order'
    request_validator = DeleteOrderSerializer()

    def populate_request_arguments(self):
        """
        Populates request arguments
        """
        self.order_id = self.request_args.get('order_id')

    def delete_order(self):
        """
        Deletes order
        """
        self.is_order_deleted = Order.delete_order(self.order_id)

    def prepare_response(self):
        """
        Prepares response
        """
        self.response = {
            'data': {
                'is_order_deleted': True
            }
        }
        if not self.is_order_deleted:
            self.response['data']['is_order_deleted'] = False

    def process_request(self):
        """
        Process request
        """
        self.populate_request_arguments()
        self.delete_order()
        self.prepare_response()
