from django.shortcuts import render

# Create your views here.

from .models import Actor , Movie
from djangoapp.serializers import ActorSerializer , MovieSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework.decorators import action


class ActorViewSet(ModelViewSet):
    queryset=Actor.objects.all()
    serializer_class=ActorSerializer
    
    @action(detail=True,methods=['GET'])
    def movies(self,request,*args,**kwargs):
        actor=self.get_object()
        serializer=MovieSerializer(actor.movie_set.all(),many=True)
        return Response(data=serializer.data)
    
    # @action(detail=True,methods=['DELETE']) #delete funksiyasi , umumiy classiz ishlatishga ishlatishga
    # def delete_actor_from_everywhere(self,request,*args,**kwargs):
    #     get_actor_id=int(kwargs['pk'])
    #     actor_in_actors=Actor.objects.get(pk=get_actor_id)
    #     all_movies=Movie.objects.all()
    #     for item in all_movies:
    #         actor_in_movies=item.actor
    #         actor_in_movies.remove(get_actor_id)
    #     actor_in_actors.delete(get_actor_id)
        
        # return Response(f"remove: {get_actor_id}-actor from everywhere")
    
    @action(detail=True,methods=['DELETE'])
    def delete_actors_from_everywhere(self,request,*args,**kwargs): #insomnia : {"id":[1,2,3,..]}
        get_actors_id = request.data.get('id') #[1,2,3,..]
        # all_movies=Movie.objects.all()
        # for movie in all_movies:
        #     actor_in_movies=movie.actor
        #     for actor_id in get_actors_id:
        #         if actor_id in actor_in_movies:
        #             actor_in_movies.remove(actor_id)
        get_actors_by_id=Actor.objects.filter(pk__in=get_actors_id)
        get_actors_by_id.delete()
        
        return Response(f"remove: {get_actors_id}-actors from everywhere")
        # for id in get_actors_id:
        #     actors_in_actors=Actor.objects.get(pk=id)
            
        
        
        
        
        
        # get_movie_id=int(kwargs['pk'])
        # movies=Movie.objects.get(pk=get_movie_id)
        # get_actor_id = request.data.get('id')
        # movies.actor.remove(get_actor_id)

class MovieViewSet(ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    
    @action(detail=True, methods=['POST'])
    def create_and_add_actor(self,request,*args,**kwargs):
        get_movie_id=int(kwargs['pk'])
        
        
        serializer=ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        get_actor_id = serializer.data.get('id')
        movies=Movie.objects.get(pk=get_movie_id)
        movies.actor.add(get_actor_id)
        movies.save()
        
        return Response(data=serializer.data)
    
    @action(detail=True, methods=['POST'])
    def add_actor(self,request,*args,**kwargs):
        
        get_movie_id=int(kwargs['pk'])
        get_actor_id = request.data.get('id')
        actors_ids=Actor.objects.values_list('id',flat=True)

        if get_actor_id in actors_ids:
            
            movies=Movie.objects.get(pk=get_movie_id)
            movies.actor.add(get_actor_id)
            movies.save()
            
            return Response(f'{get_actor_id} added to {get_movie_id}')
        
        else:
            return Response(f'{get_actor_id} Id NOT in Actors')
    
    @action(detail=True, methods=['POST']) 
    def add_actors(self,request,*args,**kwargs): # insomnia : {"id":[1,2,3,..]}
        get_movie_id=int(kwargs['pk'])
        get_actors_id = request.data.get('id') #[1,2,3,..]
        actors_ids=Actor.objects.values_list('id',flat=True)#[1,2,3,4,5,6,..all] , without flat=True [{1,},{2,},...]
        bool=False
        for actor_id in get_actors_id:
            
            if actor_id in actors_ids:
                movies=Movie.objects.get(pk=get_movie_id)
                movies.actor.add(actor_id)
                movies.save()
                bool=True
            else:
                bool=False
                print(f'False {actor_id}')
                
        if bool: 
            print('If bool True')      
            return Response(f'{actor_id} added to {get_movie_id}')
        else:
            print('If bool False')
            return Response(f'{actor_id} Id NOT in Actors')
    
    
    @action(detail=True,methods=['GET'])
    def actors(self,request,*args,**kwargs):
        get_movie_id=int(kwargs['pk'])
        moviess=Movie.objects.get(pk=get_movie_id)
        get_movie=moviess.actor
        serializer=ActorSerializer(get_movie,many=True)
        return Response(data=serializer.data)
    
    
    @action(detail=True,methods=['DELETE']) # bitta bitta o'chiradi
    def delete_actor_in_movie(self,request,*args,**kwargs):
        get_movie_id=int(kwargs['pk'])
        movies=Movie.objects.get(pk=get_movie_id)
        get_actor_id = request.data.get('id')
        movies.actor.remove(get_actor_id)
        
        return Response(f"remove: {get_actor_id}-actor in {get_movie_id}-movie")
    
    @action(detail=True,methods=['DELETE']) #hohlagancha o'chiradi
    def delete_actors_in_movie(self,request,*args,**kwargs): #{"id":[1,2,3,...]}
        get_movie_id=int(kwargs['pk'])
        movies=Movie.objects.get(pk=get_movie_id)
        get_actors_id = request.data.get('id') #[1,2,3,...]
        for actor_id in get_actors_id:
            movies.actor.remove(actor_id)
            
        return Response(f"remove actors in {get_movie_id}-movie")
    
    @action(detail=True,methods=['DELETE'])
    def remove_actors_in_all_movies(self,request,*args,**kwargs): #insomnia : {"id":[1,2,3,..]}
        get_actors_id = request.data.get('id') #[1,2,3,...]
        all_movies=Movie.objects.all()
        moviee=Movie.objects.get(pk=4)
        # print(moviee)
        # print(moviee.actor)
        # print("*********************")
        # print(all_movies)
        # print("*********************")
        for movie in all_movies:
            # print("*********************")
            # print(movie)
            # print("*********************")
            actor_in_movies=movie.actor
            # print("*********************")
            # print(actor_in_movies.values_list(flat=True))
            # print("*********************")
            for actor_id in get_actors_id:
                if actor_id in actor_in_movies.values_list(flat=True):
                    actor_in_movies.remove(actor_id)
                    
        return Response(f"remove actors in all movies")
        
        
        # movies.actor.add(get_id)
        # movies=self.get_object()
        # movies.actor=movie_id
        # get_id = request.data.get('id')**
        # movies=Movie.objects.get(pk=movie_id)
        # movies.actor.data=get_id
        # movies.save()
        
        # movies=Movie.objects.get(pk=movie_id)**
        # movies.actor.add(Actor.objects.get(pk=get_id))
        # movies.actor.add(get_id)**
        # movies.save()**
        # movies=self.get_object()
        # new=movies. get('actor')
        # new.append(get_id)
        # movies.get('actor').append(get_id)
        # movies.actor=request.data.get('id')
        # movies.save()
        # serializer = self.get_serializer(movies)
        
        
        # moviedan actorni o'chirish
        # moviedagi actorlarni chiqarish
        
        
        # json web token , avtarizatsiya
        


# for and if in one line !
# l = [-2, -1, 0, 1, 2]
# print([x for x in l if x % 2 == 0])
# # [-2, 0, 2]

# print([x for x in l if x % 2 != 0])
# # [-1, 1]

# l_s = ['apple', 'orange', 'strawberry']
# print([x for x in l_s if x.endswith('e')])
# # ['apple', 'orange']

# print([x for x in l_s if not x.endswith('e')])
# # ['strawberry']


# l = [-2, -1, 0, 1, 2]
# print([x for x in l if x])
# # [-2, -1, 1, 2]

# l_2d = [[0, 1, 2], [], [3, 4, 5]]
# print([x for x in l_2d if x])
# # [[0, 1, 2], [3, 4, 5]]
