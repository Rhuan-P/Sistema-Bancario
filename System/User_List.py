List = []

List_dict = {}
class User_List:
  
    def add_List(user):
        List.append(user.__dict__)
        id = len(List) - 1

        List_dict.update({id:List[id]})



        return id

    def show(id):
        return List[id]
    
    def list_dict(id):
        return List_dict[id]
    


