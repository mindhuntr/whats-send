from PyInquirer import style_from_dict, Token, prompt
import re

style = style_from_dict({
    Token.Separator: '#96cdfb',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#96cdfb',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
    })


def display_list(no_chats,chats,id_list,r_chats):

    if not no_chats:
        no_chats = 15

    re_exps, dist, r_names = list(), list(), list() 

    if chats:
        for chat in chats:
            re_exp = r".*" + re.escape(chat) + r".*" 
            re_exps.append(re_exp) 
    else: 
        for chat in r_chats.data: 
            r_names.append(chat['chatId'])
    r_names = list(dict.fromkeys(r_names)) 

   #  for key in id_list.keys(): 
   #      for re_exp in re_exps: 
   #          if re.search(re_exp,key,re.IGNORECASE):
   #              print(key)
   #              exit(0) 

    for key,val in id_list.items():
        if chats: 
           for re_exp in re_exps: 
               if re.search(re_exp,key,re.IGNORECASE):
                   tmp = {}
                   tmp['name'] = key
                   dist.append(tmp)
        else: 
            for chat_id in r_names: 
                if chat_id == val: 
                   tmp = {}
                   tmp['name'] = key
                   dist.append(tmp)
    if dist: 
        questions = [
               {
                   'type': 'checkbox',
                   'message': 'Select chat',
                   'name': 'Chats',
                   'choices': dist,
                   'validate': lambda answer: 'Choose atleast one chat' \
                           if len(answer) == 0 else True
                           }
               ]

        answers = prompt(questions,style=style) 
        peers = []

        if answers:
           for val in answers.values():
               for answer in val:
                   peers.append(id_list[answer]) 

           return peers

        else:
            exit(1) 
    else: 
        print("No chats found") 
        exit(1) 


