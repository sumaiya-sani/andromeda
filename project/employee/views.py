import random
from django.http import HttpResponse
from django.shortcuts import render

import requests
import json


import requests
from django.shortcuts import render
def home(request):
    return render(request ,'index.html')




import random
import requests
from django.shortcuts import render

import random
import requests
from django.shortcuts import render


def home_withQ(request):
    random_question = ""

    chatbot_response = None
    user_answer = None
    corrected_answer = None
    b=""
    d=""
    user_a=""
   
    

    
    
    
    if request.method == 'POST':
        if 'question_button' in request.POST:
            questions = [
                "write a report summarizing the results of a data analysis project. The report should include an executive summary, an introduction to the project, a description of the data used, the methods used for analysis, the results obtained, and recommendations for future actions based on the analysis.",
                
            ]

            
            random_question = random.choice(questions)
            


        elif 'answer_button' in request.POST:
            if 'user_answer' in request.POST:
                url = "https://experimental.willow.vectara.io/v1/chat/completions"
                user_answer = request.POST['user_answer']
                user_a = str(user_answer)

                b = "Does " + user_a + " is a " + "correct answer of "+ "write a report summarizing the results of a data analysis project. The report should include an executive summary, an introduction to the project, a description of the data used, the methods used for analysis, the results obtained, and recommendations for future actions based on the analysis." + "the correct answer of :"+  "write a report summarizing the results of a data analysis project. The report should include an executive summary, an introduction to the project, a description of the data used, the methods used for analysis, the results obtained, and recommendations for future actions based on the analysis."+"is"
                # b += random_question
                print(b)
                print(b)
                d = str(b)

                print(d)
                payload = {
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {
                            "role": "user",
                            "content": d
                        }
                    ]
                }
                headers = {
                    'Content-Type': 'application/json',
                    'customer-id': '689258330',
                    'x-api-key': 'zqt_KRU_WlK4Y4oUZjImuLNhRU7Jyas40mplV0oJSw'
                }
                response = requests.post(url, headers=headers, json=payload)
                if response.status_code == 200:
                    response_data = response.json()
                    if 'choices' in response_data:
                        choices = response_data['choices']
                        chatbot_response = [choice['message']['content'] for choice in choices][0]
                        corrected_answer = chatbot_response.split(':')[-1].strip()
                    else:
                        print("Error: Response does not contain 'choices' key.")
                else:
                    print(f"Error: {response.status_code}")
                print(response.text)


    return render(request, 'question.html', {'question': random_question, 'chatbot_response': chatbot_response, 'user_answer': user_answer, 'corrected_answer': corrected_answer,})



