from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home_view(request):
    """1. 検索フォーム画面 (GET) - テンプレートの呼び出し"""
    return render(request, 'bookings/home.html')

def hotel_list_view(request):
    """2. ホテル一覧・予約入力画面 (GET) - テンプレートへ変数を渡す"""
    city = request.GET.get('city', '').strip()
    room_type = request.GET.get('room_type', '').strip()
    
    if not city or not room_type:
        return HttpResponseBadRequest("Missing search criteria.")
        
    context = {
        'city': city,
        'room_type': room_type
    }
    return render(request, 'bookings/hotel_list.html', context)

@csrf_exempt
def booking_confirm_view(request):
    """3. 予約確定処理 (POST) - テンプレートへ変数を渡す"""
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method. Please use POST.")
        
    guest_name = request.POST.get('guest_name', '').strip()
    city = request.POST.get('city', '')
    room_type = request.POST.get('room_type', '')
    
    if not guest_name:
        return HttpResponseBadRequest("Guest name is required.")
        
    context = {
        'guest_name': guest_name,
        'city': city,
        'room_type': room_type
    }
    return render(request, 'bookings/booking_confirm.html', context)

def hotel_search_ajax_view(request):
    """4. HTMX用: ページをリロードせずにホテルリストのパーツ(HTML)だけを返す"""
    city = request.GET.get('city', 'Aizu').strip()
    context = {'city': city}
    # ページ全体ではなく、部分的なテンプレート(partial)を返します
    return render(request, 'bookings/hotel_list_partial.html', context)