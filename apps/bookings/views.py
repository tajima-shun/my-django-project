from django.http import JsonResponse, HttpResponse

def home_view(request):
    """1. ホームページ / 検索画面 (都市と部屋タイプの選択肢を返す想定)"""
    # 演習の注記に基づき、シンプルな操作を表現するために仮のデータを返します
    data = {
        "message": "Welcome to Great Hotels! Please select a city and room type.",
        "available_cities": ["Tokyo", "Aizu", "Kyoto", "Osaka"],
        "room_types": ["Standard", "Double", "Deluxe"]
    }
    return JsonResponse(data)

def hotel_list_view(request):
    """2. ホテル一覧画面 (検索条件にマッチするホテルの一覧)"""
    # ユーザーが指定した値の代わりに、今はハードコーディングされたサンプルデータを返します
    city = request.GET.get('city', 'Aizu')
    room_type = request.GET.get('room_type', 'Standard')
    
    hotels = [
        {"id": 1, "name": f"Great Hotel {city} Station", "city": city, "room_type": room_type},
        {"id": 2, "name": f"{city} Park Hotel", "city": city, "room_type": room_type},
    ]
    return JsonResponse({"searched_city": city, "room_type": room_type, "matching_hotels": hotels})

def booking_confirm_view(request):
    """3. 予約完了画面 (予約詳細の表示)"""
    # 予約が成功したと仮定した、シンプルな確認結果を返します
    confirmation_details = {
        "status": "Success",
        "message": "Reservation completed successfully!",
        "details": {
            "date": "2026-06-30",
            "city": "Aizu",
            "hotel_name": "Great Hotel Aizu Station",
            "room_type": "Standard",
            "guest_name": request.GET.get('name', 'Guest User')
        }
    }
    return JsonResponse(confirmation_details)