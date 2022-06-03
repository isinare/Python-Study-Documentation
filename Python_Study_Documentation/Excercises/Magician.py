is_magician = True
is_expert = False

#check if magician AND expert: 'you are a master magician'
if is_magician and is_expert:
   print('you are a master magician')

#check if magician but not expert:'atleast u are getting there'
if is_magician and not is_expert:
     print('at least you\'re getting there')

#or

elif is_magician and not is_expert:
    print('at least you\'re getting there')

#check if you're not a magician:"You need magic powers"
if not is_magician and not is_expert:
    print('You Need Magic Powers')