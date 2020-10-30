#!/usr/bin/env python3

import os
import sys
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dotenv import load_dotenv


class update():
   
   
   def __init__(self, docId): 
      self.docId = docId

   SCOPES = ['https://www.googleapis.com/auth/documents']
   creds = None

   if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
         creds = pickle.load(token)
         
   if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
         creds.refresh(Request())
      else:
         flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
         creds = flow.run_local_server(port=0)
         with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
      
   service = build('docs', 'v1', credentials=creds)

   def insertText(self, words, index):

      requests = [
      {
         'insertText': {
            'location': {
               'index': 1,
               },
            'text': words
            }
      },
      ]
      result = self.service.documents().batchUpdate(documentId=self.docId, body={'requests': requests}).execute()
   
   def delEvry(self):

      requestpart = self.service.documents().get(documentId=self.docId).execute().get('body').get('content')
      for item in requestpart:
         requestfinalIndex = item.get('endIndex')
      requests = [
        {
            'deleteContentRange': {
                'range': {
                    'startIndex': 1,
                    'endIndex': requestfinalIndex - 1,
                }

            }

        },
         ]
      result = self.service.documents().batchUpdate(documentId=self.docId, body={'requests': requests}).execute()

   def insertImage(self, index, URL):
      requests = [
      {
         'insertInlineImage': {
            'location': {
               'index': index
               },
            'uri':
            URL,
            'objectSize': {
               'height': {
                  'magnitude': 50,
                  'unit': 'PT'
                  },
               'width': {
                  'magnitude': 50,
                  'unit': 'PT'
                     }
                  }
         }  
      },
      ]
      result = self.service.documents().batchUpdate(documentId=self.docId, body={'requests': requests}).execute