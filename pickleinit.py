import pickle

users_chosen=[]
sector_chosen=[]
outer_color_chosen=[]
inner_color_chosen=[]
#Writing the letters list into the file.
fh = open("users.pkl", 'wb')
pickle.dump(users_chosen, fh)
pickle.dump(sector_chosen, fh)
pickle.dump(outer_color_chosen, fh)
pickle.dump(inner_color_chosen, fh)
fh.close()


fh = open("users.pkl", 'rb')
users_chosen = pickle.load(fh)
inner_color_chosen = pickle.load(fh)
print(users_chosen)
print(inner_color_chosen)