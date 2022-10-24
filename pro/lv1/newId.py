def solution(new_id):
     new_id = new_id.lower()

     for i in new_id:
         if i.isalnum() or i == '-' or i == '_' or i == '.':
             continue
         else:
             new_id = new_id.replace(i, '')

     while '..' in new_id:
         new_id = new_id.replace('..', '.')

     if new_id.startswith('.'):
         new_id = new_id[1:]
     if new_id.endswith('.'):
         new_id = new_id[:len(new_id) - 1]

     if new_id == '':
         new_id = 'a'

     if len(new_id) >= 16:
         new_id = new_id[:15]
     if new_id.endswith('.'):
         new_id = new_id[:14]

     if len(new_id)<=2:
        while len(new_id) < 3:
            new_id += new_id[-1]

     return new_id
