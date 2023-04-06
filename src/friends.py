# 1. For a given person, return their name
def get_name(person):
    return person['name']
#2
def get_favourite_tv_show(person):
    return person['favourites']['tv_show']
# 3 
def likes_to_eat(person, food_to_search_for):
    for food in  person['favourites']['snacks']:
        if food == food_to_search_for:
            return True

    return False

# 4
def add_friend(person, new_friend):
    
    person['friends'].append(new_friend)
    return len(person['friends'])

# 5 
def remove_friend(person, remove_friend):
    
    person['friends'].remove(remove_friend)
    return len(person['friends'])

# 6

def total_money(people):

  total_money=0
  for person in people:
   individual_money=person['monies']
   total_money+=individual_money
  return total_money


# 7
def lend_money(person_b, person_a, lend_amount):
    person_b['monies'] -= lend_amount
    person_a['monies'] += lend_amount
    # person_one['monies']=person_one['monies']+lend_amount
   

# 8
def all_favourite_foods(people):
    # people = [perosn1, person2, person3 ... ] 
   
    all_favourite_foods=[]
    for person in people:
        snacks = person["favourites"]["snacks"]
        # snacks = [snack1, snack2 ....]
        for snack in snacks:
            all_favourite_foods.append(snack)
        
    return all_favourite_foods

# 9
def find_no_friends(people):
    find_no_friends=[]
    for person in people:
        if len(person['friends'])==0:
          find_no_friends.append(person)
    return find_no_friends


# 10
def unique_favourite_tv_shows(people):
    unique_favourite_tv_shows=[]
    group_favourite_tv_shows=[]
    for person in people:
        favourite_tv_shows=person['favourites']['tv_show']
        group_favourite_tv_shows.append(favourite_tv_shows)
   
    for shows in group_favourite_tv_shows:
      if shows not in unique_favourite_tv_shows:
         unique_favourite_tv_shows.append(shows)
    return unique_favourite_tv_shows
            

