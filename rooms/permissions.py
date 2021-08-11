from rest_framework.permissions import BasePermission   # BasePermission: permissions.IsAuthenticated 에 있는 것을 타고 들어가서 확인한 것, IsAuthenticated는 has_permission method를 갖고 있다.


class IsOwner(BasePermission):
    
    def has_object_permission(self, request, view, room):
        return room.user == request.user