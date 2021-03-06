from channels.generic.websocket import WebsocketConsumer
from intellibot.uservalidator import validateUserResponse
from intellibot.utils import createMessage, createBotMessage, getNextQuestion
from intellibot.userhelper import getUserResponseValue, getFinalMessage
from intellibot.models import UserInfo
import json
import random

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # dumps convert into string and loads convert into object
        text_data_json = json.loads(text_data)
        print('message received at server ', text_data_json)

        if 'text' not in text_data_json:
            receivedText = ''
        else:
            receivedText = text_data_json['text']
            ## send back actual message also -- with source as CANDIDATE -- the UI just displays that message on screen 
            originalMessage = createMessage(receivedText, 'send', 'CANDIDATE')
            self.send(text_data=json.dumps(originalMessage))

        # check message command type and take action
        command = text_data_json['command']
        if ('start' == command.lower()):
            # send greeting and one question
            greetingMessage = createBotMessage('Hello, I am going to ask you few questions that will help me know you better?', 'send', '-1', 'Greeting')
            self.send(text_data=json.dumps(greetingMessage))
            # get first question 
            next_question = getNextQuestion(1)
            first_question = createBotMessage(next_question.question_text, 
                                              "reply", 
                                               next_question.id, 
                                               next_question.context)
            self.send(text_data=json.dumps(first_question))

        elif('finish' == command.lower()):
            # get user details from session, create an object of UserInfo model and save that in database 
            # display the message with user details
            user = UserInfo()
            user.name = self.scope['session']['Name']
            user.DOB = self.scope['session']['DOB']
            user.gender = self.scope['session']['Gender']
            user.smoker = self.scope['session']['Smoker'] #TODO change this to Smoker and propogate question changes to db

            try:
                user.save()
            except Exception as e:
                print(e)
                
            print('save success')
            finalMessage = createBotMessage(getFinalMessage(user), 'send', '-100', 'finish')
            self.send(text_data=json.dumps(finalMessage))

        # Validate the response as per the context 
        # using receivedText and receivedId and receivedContext
        if 'id' not in text_data_json:
            receivedId = '-1'
        else:
            receivedId = text_data_json['id']

        if 'context' not in text_data_json:
            receivedContext = 'none'
        else:
            receivedContext = text_data_json['context']

        ## validate, save info in session and return response
        userinput = True
        if receivedText != '':

            new_id = -1
            if (validateUserResponse(receivedText, receivedContext)):   
                new_id = receivedId + 1 
                # save val in user session for context
                val = getUserResponseValue(receivedText, receivedContext)
                self.scope['session'][receivedContext] = val
                print('storing {} in user session as {}', receivedContext, val)

            else: #user validation failed, repeat the question
                new_id = receivedId 
                userinput = False
            
            next_question = getNextQuestion(new_id)
            returnMessage = next_question.question_text

            if(userinput == False):
                NameMessage = ""
                try:
                    uname = self.scope['session']['Name'] 
                    if random.randint(-4,2) >= 0 : 
                       NameMessage = uname +", "
                except Exception:
                    uname = ''
                returnMessage = NameMessage + next_question.hint.split(":")[random.randint(0,1)] 

            result = createBotMessage(returnMessage, 
                                      'reply', 
                                       next_question.id, 
                                       next_question.context)
            
            self.send(text_data=json.dumps(result))
            