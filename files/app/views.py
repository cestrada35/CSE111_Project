from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Game, Developer, Publisher, Salestime, Nation, Region
from .serializers import GameSerializer, DeveloperSerializer, PublisherSerializer, \
                            SalestimeSerializer, NationSerializer, RegionSerializer


@api_view(['GET'])
def game_list(request):
    """
    Method for games list
    """
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def publisher_list(request):
    """
    Method for publishers list
    """
    if request.method == 'GET':
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def developer_list(request):
    """
    Method for developers list
    """
    if request.method == 'GET':
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def salestime_list(request):
    """
    Method for Salestime list
    """
    if request.method == 'GET':
        salestime = Salestime.objects.all()
        serializer = SalestimeSerializer(salestime, many=True)

        return Response(serializer.data)

@api_view(['GET'])
def nation_list(request):
    """
    Method for nation list
    """
    if request.method == 'GET':
        nation = Nation.objects.all()
        serializer = NationSerializer(nation, many=True)

        return Response(serializer.data)

@api_view(['GET'])
def region_list(request):
    """
    Method for Region list
    """
    if request.method == 'GET':
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def game_details(request, pk):
    """
    Method for game details
    """
    data = {}
    if request.method == 'GET':
        game = Game.objects.get(pk=pk)
        developer = game.g_developer.d_developer
        publisher = game.g_publisher.p_publisher
        developer_nation = game.g_developer.d_nationkey.n_name
        publisher_nation = game.g_publisher.p_nationkey.n_name
        developer_region = game.g_developer.d_nationkey.n_regionkey.r_name
        publisher_region = game.g_publisher.p_nationkey.n_regionkey.r_name
        serializer = GameSerializer(game)
        data['g_rank'] = serializer.data['g_rank']
        data['g_title'] = serializer.data['g_title']
        data['g_sales'] = serializer.data['g_sales']
        data['g_genre'] = serializer.data['g_genre']
        data['g_releasedate'] = serializer.data['g_releasedate']
        data['g_platform'] = serializer.data['g_platform']
        data['g_developer'] = developer
        data['g_publisher'] = publisher
        data['d_n_name'] = developer_nation
        data['p_n_name'] = publisher_nation
        data['d_r_name'] = developer_region
        data['p_r_name'] = publisher_region


        return Response(data)


@api_view(['GET'])
def developer_details(request, pk):
    """
    Method for game details
    """
    data = {}
    if request.method == 'GET':
        developer = Developer.objects.get(pk=pk)
        nation = developer.d_nationkey.n_name
        region = developer.d_nationkey.n_regionkey.r_name
        serializer = DeveloperSerializer(developer)
        data['d_developer'] = serializer.data['d_developer']
        data['d_doc'] = serializer.data['d_doc']
        data['d_employees'] = serializer.data['d_employees']
        data['d_networth'] = serializer.data['d_networth']
        data['d_nationkey'] = nation
        data['n_regionkey'] = region

        return Response(data)


@api_view(['GET'])
def publisher_details(request, pk):
    """
    Method for game details
    """
    data = {}
    if request.method == 'GET':
        publisher = Publisher.objects.get(pk=pk)
        nation = publisher.p_nationkey.n_name
        region = publisher.p_nationkey.n_regionkey.r_name
        serializer = PublisherSerializer(publisher)
        data['p_publisher'] = serializer.data['p_publisher']
        data['p_doc'] = serializer.data['p_doc']
        data['p_employees'] = serializer.data['p_employees']
        data['p_networth'] = serializer.data['p_networth']
        data['p_nationkey'] = nation
        data['n_regionkey'] = region

        return Response(data)


@api_view(['GET'])
def salestime_details(request, pk):
    """
    Method for game details
    """
    data = {}
    if request.method == 'GET':
        salestime = Salestime.objects.get(pk=pk)
        st_game = salestime.st_game
        game = Game.objects.get(g_title=st_game)
        game_title = game.g_title
        game_id = game.id
        developer = game.g_developer.d_developer
        publisher = game.g_publisher.p_publisher
        developer_nation = game.g_developer.d_nationkey.n_name
        publisher_nation = game.g_publisher.p_nationkey.n_name
        developer_region = game.g_developer.d_nationkey.n_regionkey.r_name
        publisher_region = game.g_publisher.p_nationkey.n_regionkey.r_name
        serializer = SalestimeSerializer(salestime)
        data['st_firstyear'] = serializer.data['st_firstyear']
        data['st_alltime'] = serializer.data['st_alltime']
        data['st_game'] = game_title
        data['g_id'] = game_id
        data['g_developer'] = developer
        data['g_publisher'] = publisher
        data['d_n_name'] = developer_nation
        data['p_n_name'] = publisher_nation
        data['d_r_name'] = developer_region
        data['p_r_name'] = publisher_region

        return Response(data)

@api_view(['GET'])
def nation_details(request, pk):
    """
    Method for nation details
    """
    data = {}
    if request.method == 'GET':
        nation = Nation.objects.get(pk=pk)
        region = nation.n_nationkey.n_regionkey.r_name
        serializer = NationSerializer(nation)
        data['n_name'] = serializer.data['n_name']
        data['n_nationkey'] = nation
        data['n_regionkey'] = region

        return Response(data)

@api_view(['GET'])
def region_details(request, pk):
    """
    Method for region details
    """
    data = {}
    if request.method == 'GET':
        developer = Developer.objects.get(pk=pk)
        nation = developer.d_nationkey.n_name
        region = developer.d_nationkey.n_regionkey.r_name
        serializer = DeveloperSerializer(developer)
        data['d_developer'] = serializer.data['d_developer']
        data['d_doc'] = serializer.data['d_doc']
        data['d_employees'] = serializer.data['d_employees']
        data['d_networth'] = serializer.data['d_networth']
        data['d_nationkey'] = nation
        data['n_regionkey'] = region

        return Response(data)


@api_view(['POST'])
def searching(request):
    """
    Method for search
    """
    data = []
    search = request.data.get('search')
    if request.method == 'POST':
        dev = Developer.objects.filter(d_developer__icontains=search)
        dev = DeveloperSerializer(dev, many=True)
        pub = Publisher.objects.filter(p_publisher__icontains=search)
        pub = PublisherSerializer(pub,many=True)
        gm = Game.objects.filter(g_title__icontains=search)
        gm = GameSerializer(gm, many=True)
        d = [dev.data,pub.data,gm.data]
    return Response(d)
