# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers, status
# from hiphopapi.models import Revenue, Order
# from django.utils import timezone

# class RevenueView(ViewSet):
#     """revenue view"""

#     def retrieve(self, request, pk):
#         """Handle GET requests for single revenue.
#         Returns: Response -- JSON serialized revenue"""

#         try:
#             revenue = Revenue.objects.get(pk=pk)
#             serializer = RevenueSerializer(revenue)
#             return Response(serializer.data)
#         except Revenue.DoesNotExist:
#             return Response({'message': 'Revenue not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def list(self, request):
#         """Handle GET requests to get all revenue nodes.
#         Returns: Response -- JSON serialized list of revenue nodes with overall total"""

#         try:
#             # Filter closed orders (open=False)
#             closed_orders = Order.objects.filter(open=False)

#             # Create a list to store revenue data
#             revenue_data = []

#             # Calculate overall total revenue
#             overall_total = 0

#             # Loop through closed orders
#             for closed_order in closed_orders:
#                 tip = closed_order.tip
#                 total = closed_order.total
#                 order_name = closed_order.name

#                 # Create revenue entry
#             revenue = Revenue(
#                 order=closed_order,
#                 date=timezone.now(),
#                 payment=request.query_params.get("payment"),
#                 subtotal=request.query_params.get("subtotal"),
#                 tip=tip,
#                 total=total,
#                 )

#                 # Save revenue entry
#             revenue.save()

#                 # Add revenue data to the list
#             revenue_data.append(RevenueSerializer(revenue).data)

#                 # Update overall total
#             overall_total += total

#             # Include overall total in the response
#             response_data = {'revenues': revenue_data, 'overall_total': overall_total}
#             return Response(response_data)
#         except Exception as e:
#             return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def create(self, request):
#             """Create Revenue Entry"""
#             order_id = Order.objects.get(pk=request.data["orderId"])
#             revenue = Revenue.objects.create(
#                 order=order_id,
#                 date=request.data["date"],
#                 payment=request.data["paymentType"],
#                 subtotal=request.data["subtotal"],
#                 total=request.data["total"],
#                 tip=request.data["tip"],
#             )
#             revenue.save()
#             serializer = RevenueSerializer(revenue)
#             return Response(serializer.data)

# class RevenueSerializer(serializers.ModelSerializer):
#     """JSON serializer for revenue nodes"""

#     class Meta:
#         model = Revenue
#         fields = ('id', 'order', 'date', 'payment', 'subtotal', 'tip', 'total')
#         depth = 1

#     def validate_date(self, value):
#         """Validate the date field to ensure it's in the correct format"""
#         try:
#             # Try parsing the date to check if it's in the correct format
#             value = serializers.DateTimeField().to_internal_value(value)
#             return value
#         except serializers.ValidationError:
#             raise serializers.ValidationError("Invalid date format. Please provide the date in the format: YYYY-MM-DDTHH:MM:SSZ")

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hiphopapi.models import Revenue, Order


class RevenueView(ViewSet):
    """revenue view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single revenue.
        Returns: Response -- JSON serialized revenue"""

        try:
            revenue = Revenue.objects.get(pk=pk)
            serializer = RevenueSerializer(revenue)
            return Response(serializer.data)
        except Revenue.DoesNotExist:
            return Response({'message': 'Revenue not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to get all revenue nodes.
        Returns: Response -- JSON serialized list of revenue nodes"""

        try:
            revenues = Revenue.objects.all()
            serializer = RevenueSerializer(revenues, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
            """Create Revenue Entry"""
            order_id = Order.objects.get(pk=request.data["orderId"])
            revenue = Revenue.objects.create(
                order=order_id,
                date=request.data["date"],
                payment=request.data["paymentType"],
                subtotal=request.data["subtotal"],
                total=request.data["total"],
                tip=request.data["tip"],
            )
            revenue.save()
            serializer = RevenueSerializer(revenue)
            return Response(serializer.data)
class RevenueSerializer(serializers.ModelSerializer):
    """JSON serializer for revenue nodes"""
    class Meta:
        model = Revenue
        fields = ('id', 'order', 'date', 'payment', 'subtotal', 'tip', 'total')
        depth = 1
