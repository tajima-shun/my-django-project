from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  # 👈 1. これを一番上に追加

def home_view(request):
    # (ここは変更なし)
    html = """
    <h1>Welcome to Great Hotels!</h1>
    <form action="/search/" method="GET">
        <label>Select City:</label>
        <select name="city">
            <option value="Aizu">Aizu</option>
            <option value="Tokyo">Tokyo</option>
            <option value="Kyoto">Kyoto</option>
        </select>
        <br><br>
        <label>Room Type:</label>
        <select name="room_type">
            <option value="Standard">Standard</option>
            <option value="Deluxe">Deluxe</option>
        </select>
        <br><br>
        <button type="submit">Search Hotels</button>
    </form>
    """
    return HttpResponse(html)

def hotel_list_view(request):
    # (ここは変更なし)
    city = request.GET.get('city', '').strip()
    room_type = request.GET.get('room_type', '').strip()
    
    if not city or not room_type:
        return HttpResponseBadRequest("Missing search criteria.")
        
    html = f"""
    <h2>Available Hotels in {city} ({room_type})</h2>
    <ul>
        <li>Great Hotel {city} Station</li>
        <li>{city} Park Hotel</li>
    </ul>
    <br>
    <h3>Book this room</h3>
    <form action="/booking/confirm/" method="POST">
        <input type="hidden" name="city" value="{city}">
        <input type="hidden" name="room_type" value="{room_type}">
        <label>Your Name:</label>
        <input type="text" name="guest_name" required>
        <button type="submit">Confirm Booking</button>
    </form>
    """
    return HttpResponse(html)

@csrf_exempt  # 👈 2. booking_confirm_view のすぐ上にこれを追加！
def booking_confirm_view(request):
    """3. 予約確定処理 (POST)"""
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method. Please use POST.")
        
    guest_name = request.POST.get('guest_name', '').strip()
    city = request.POST.get('city', '')
    room_type = request.POST.get('room_type', '')
    
    if not guest_name:
        return HttpResponseBadRequest("Guest name is required.")
        
    html = f"""
    <h1>🎉 Reservation Completed!</h1>
    <p>Thank you, {guest_name}!</p>
    <p><strong>Details:</strong></p>
    <ul>
        <li>Destination: {city}</li>
        <li>Room Type: {room_type}</li>
        <li>Duration: 1-Night Stay Only</li>
    </ul>
    <a href="/">Back to Home</a>
    """
    return HttpResponse(html)