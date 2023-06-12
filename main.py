import wikipedia
import webbrowser
import datetime

def get_current_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M")

def personal_assistant():
    print("Hello! I am your personal assistant. How can I assist you today?")
    while True:
        user_input = input("> ")

        # Check for exit command
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        # Handle user queries
        try:
            if user_input.lower() == "time":
                current_time = get_current_time()
                print("The current time is:", current_time)
            elif user_input.lower() == "date":
                current_date = datetime.date.today()
                print("Today's date is:", current_date)
            elif user_input.lower().startswith("calculate"):
                calculation = user_input[10:]
                result = eval(calculation)
                print("The result is:", result)
            elif user_input.lower().startswith("search"):
                search_query = user_input[7:]
                web_search_url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(web_search_url)
            else:
                # Use Wikipedia API to search for information
                search_results = wikipedia.search(user_input)
                if search_results:
                    page = wikipedia.page(search_results[0])
                    print(page.summary)
                    print("For more information, visit:", page.url)
                else:
                    print("Sorry, I couldn't find any information on that topic.")

        except wikipedia.exceptions.DisambiguationError as e:
            print("There are multiple options. Please provide more specific input.")
        except Exception as e:
            print("Oops! An error occurred. Please try again.")

# Run the personal assistant
personal_assistant()
