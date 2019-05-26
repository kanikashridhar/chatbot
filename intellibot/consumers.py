from channels.generic.websocket import WebsocketConsumer
from intellibot.uservalidator import validateUserResponse
from intellibot.utils import createMessage, createBotMessage, getNextQuestion, getResponseFor
from intellibot.userhelper import getUserResponseValue, getFinalMessage, getUserBy
from intellibot.models import UserInfo
import json

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
            greetingMessage = createBotMessage('Welcome to Medius Health Intelligent Bot System', 'send', '-1', 'Greeting')
            self.send(text_data=json.dumps(greetingMessage))
            # get first question 
            firstQues =  getResponseFor(receivedText, command, "Init", 0)
            #firstQues = getNextQuestion(0)
            self.send(text_data=json.dumps(firstQues))

        elif('finish' == command.lower()):
            # get user details from session, create an object of UserInfo model and save that in database 
            # display the message with user details
            user = UserInfo()
            user.name = self.scope['session']['Name']
            user.DOB = self.scope['session']['DOB']
            user.gender = self.scope['session']['Gender']
            user.smoker = self.scope['session']['Smoker'] #TODO change this to Smoker and propogate question changes to db
            print('save user ', user.name)
            print('save user ', user.DOB)
            print('save user ', user.gender)
            print('save user ', user.smoker)
            
            try:
                user.save()
            except ValueError as ve:
                print(ve)
                pass
                # fail
            print('save success')

            # show the final message and put details from user model
            print('saved user is ',user)
            print(user.name)
            print(user.DOB)
            print(user.gender)
            print(user.smoker)
            #user = getUserBy(user.name, user.DOB)
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
        if receivedText != '':

            new_id = -1
            if ('start' == command.lower() and receivedId == 0):
                new_id = receivedId + 1
                
            elif (validateUserResponse(receivedText, receivedContext)):  #User response is validated 
                new_id = receivedId + 1 
                # save val in user session for context
                val = getUserResponseValue(receivedText, receivedContext)
                self.scope['session'][receivedContext] = val
                print('storing {} in user session as {}', receivedContext, val)

            else: #user validation failed, repeat the question
                new_id = receivedId 
            
            next_question = getNextQuestion(new_id)
            result = createBotMessage(next_question.question_text, "reply", next_question.id, next_question.context)
            
            self.send(text_data=json.dumps(result))
            