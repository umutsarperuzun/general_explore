import requests
import json


#GET

get_url="http://jsonplaceholder.typicode.com/todos/15"
# get_response = requests.get(get_url)
# print(get_response.json())


#POST
# to_do_item = {"userId":2,"title":"Testing","completed":False}

# post_url="http://jsonplaceholder.typicode.com/todos"
# headers={
#     "Content-Type":"application/json"
# }
# post_response=requests.post(post_url,data=json.dumps(to_do_item),headers=headers)

# print(post_response.json())


#PUT(update data plural)
to_do_item_15 ={'userId': 2, 'id': 15, 'title': 'put title', 'completed': False}
# put_response=requests.put(get_url,to_do_item_15)
# print(put_response.json())


#PATCH(update data singular)
to_do_item_patch_15={"title": "title has been changed"}
patch_response=requests.patch(get_url,to_do_item_patch_15)
print(patch_response.json())

#DELETE
delete_response=requests.delete(get_url)
print(delete_response.status_code)




