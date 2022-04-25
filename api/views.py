import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ClientUserScore


@csrf_exempt
def upload_score(request):
    request_data = json.loads(request.body.decode())
    client_no = request_data.get('client_no', '')
    score = request_data.get('score', '')
    if not client_no or not score:
        return JsonResponse({'code': 1, 'data': {}, 'msg': '请求参数异常'})
    ClientUserScore.objects.create(client_no=client_no, score=score)
    return JsonResponse({'code': 0, 'data': {}, 'msg': '操作成功'})


@csrf_exempt
def ranking_list(request):
    request_data = json.loads(request.body.decode())
    client_no = request_data.get('client_no', '')
    start = request_data.get('start', 1)
    end = request_data.get('end', 10)
    if start <= 0:
        start = 1
    if not isinstance(client_no, int) or end < start:
        return JsonResponse({'code': 1, 'data': {}, 'msg': '请求参数异常'})
    score_list = ClientUserScore.objects.distinct().order_by('-score')
    score_list_2 = score_list[start - 1:end]
    range_list = range(start, end + 1)
    score_ranking_list = []
    for i, item in enumerate(score_list_2):
        score_ranking_list.append({'ranking': range_list[i], 'client_name': f'客户端{item.client_no}', 'score': item.score})
    self_score_info = {'ranking': 0, 'client_name': f'客户端{client_no}', 'score': 0}
    for i, item in enumerate(score_list):
        if item.client_no == client_no:
            self_score_info['ranking'] = i + 1
            self_score_info['score'] = item.score
            break
    score_ranking_list.append(self_score_info)
    data = {
        'ranking_list': score_ranking_list
    }
    return JsonResponse({'code': 0, 'data': data, 'msg': '操作成功'})
