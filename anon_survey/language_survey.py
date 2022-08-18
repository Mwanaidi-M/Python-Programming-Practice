from survey import AnonymousSurvey

# define a question & make survey
question = "What are some of your dream destinations?"
my_survey = AnonymousSurvey(question)

# show the question
my_survey.show_question()

# store responses
print("Enter 'q' to quit.\n")
while True:
    response = input("Enter your response:\t")

    if response == 'q':
        break

    my_survey.store_response(response)


print("\nThank you for participating!\n")
# show the results
my_survey.show_results()


