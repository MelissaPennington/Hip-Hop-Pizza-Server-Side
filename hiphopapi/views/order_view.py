from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from hiphopapi.models import Order, User, Item, OrderItem

class OrderView(ViewSet):

    def retrieve(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def list(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        user_instance = User.objects.get(uid=request.data["user"])
        order = Order.objects.create(
            user=user_instance,
            customer=request.data["customer"],
            is_open=request.data["is_open"],
            timestamp=request.data["timestamp"],
            payment_type=request.data["payment_type"],
            tip_amount=request.data["tip_amount"],
            total=request.data["total"],
            order_type=request.data["order_type"]
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.name = request.data["name"]
        order.email = request.data["email"]
        order.phone_number = request.data["phone_number"]
        order.timestamp = request.data["timestamp"]
        order.payment_type = request.data["payment_type"]
        order.tip_amount = request.data["tip_amount"]
        order.total = request.data["total"]
        order.order_type = request.data["order_type"]
        order.is_open = request.data["is_open"]
        order.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # ADD/REMOVE ORDERITEM

    @action(methods=['post'], detail=True)
    def add_order_item(self, request, pk):
        item = Item.objects.get(pk=request.data["item"])
        order = Order.objects.get(pk=pk)
        order_item = OrderItem.objects.create(
            item=item,
            order=order,
            quantity=request.data["quantity"]
        )
        return Response({'message': 'Item added to order'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def remove_order_item(self, request, pk):
        order_item_id = request.data.get("order_item")
        OrderItem.objects.filter(pk=order_item_id, order__pk=pk).delete()
        return Response("Order item removed", status=status.HTTP_204_NO_CONTENT)

class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders"""
    class Meta:
        model = Order
        fields = ('id', 'user', 'name', 'phone_number', 'email', 'is_open', 'timestamp', 'payment_type', 'order_type', 'total', 'is_open')
