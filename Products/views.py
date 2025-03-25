from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Order , mainPicture,YourEmail
from decimal import Decimal
import json
from django.core.mail import send_mail
from django.conf import settings

def home_page(request):
    """ Render the homepage with all products """
    products = Product.objects.all()
    pic = mainPicture.objects.all().first()
    return render(request, 'index.html', {'products': products , 'pic': pic})

@csrf_exempt
def update_cart(request):
    """ Handle AJAX requests to update cart quantity """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            action = data.get('action')

            product = get_object_or_404(Product, id=product_id)
            order, created = Order.objects.get_or_create(product=product)

            if action == "increase":
                order.quantity += 1
            elif action == "decrease" and order.quantity > 1:
                order.quantity -= 1

            order.save()

            return JsonResponse({
                "quantity": order.quantity,
                "total_price": float(order.total_price)
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Invalid request"}, status=400)




@csrf_exempt
def submit_order(request):
    """ Handle order submission via AJAX """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            address = data.get("address")
            phone = data.get("phone")
            shipping_cost = Decimal(data.get("shipping", 0))
            shipping_location = data.get("shipping_location", "Outside Dhaka")
            products_data = data.get("products", [])

            if not name or not address or not phone:
                return JsonResponse({"error": "All fields are required"}, status=400)

            total_order_price = Decimal(0)
            order_details = []
            for item in products_data:
                product = get_object_or_404(Product, id=item["id"])
                quantity = int(item["quantity"])
                order = Order.objects.create(
                    product=product,
                    quantity=quantity,
                    total_price=product.price * quantity,
                    shipping_cost=shipping_cost,
                    shipping_location=shipping_location,
                    
                    customer_name=name,
                    customer_address=address,
                    customer_phone=phone,
                )
                order.total_with_charge = order.total_price + shipping_cost
                order.save()
                total_order_price += order.total_with_charge
                order_details.append(f"{product.name} ({quantity} x {product.price}৳)")

            # Prepare email content
            email_subject = "New Order Received"
            email_body = (
                f"Customer Name: {name}\n"
                f"Address: {address}\n"
                f"Phone: {phone}\n"
                f"Shipping Location: {shipping_location}\n"
                f"Shipping Cost: {shipping_cost}৳\n"
                f"Order Details:\n" + "\n".join(order_details) + "\n"
                f"Total Price: {total_order_price}৳"
            )

            # Send email
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [YourEmail.objects.all().first().email],
                fail_silently=False,
            )

            return JsonResponse({
                "message": "Order placed successfully!",
                "total_price": str(total_order_price)
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)



