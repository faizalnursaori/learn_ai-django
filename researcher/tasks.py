from researcher.methods import generate_queries, research, generate_business_profile
from huey.contrib.djhuey import task
from core.methods import send_notification
import markdown2
# import time

@task()
def process_research(company_name):
    queries = []

    # time.sleep(5)
    # send_notification("test", "Test notif")

    # time.sleep(5)
    # send_notification("test", "Test notif")

    # time.sleep(5)
    # send_notification("test", "Test notif")

    send_notification("notification", "Generating financial queries...")
    financial_queries = generate_queries("Finance", company_name)
    
    send_notification("notification", "Generating leadership queries...")
    leadership_queries = generate_queries("Leadership", company_name)
    
    send_notification("notification", "Generating operations queries...")
    operations_queries = generate_queries("Operations", company_name)

    send_notification("notification", "Generating company history queries...")
    company_history_queries = generate_queries("Company History", company_name)

    queries.extend(financial_queries.get("queries"))
    queries.extend(leadership_queries.get("queries"))
    queries.extend(operations_queries.get("queries"))
    queries.extend(company_history_queries.get("queries"))

    context = ""

    for query in queries:
        send_notification("notification", f"Processhing query: {query}")
        response = research(query)
        context += f"Query: {query} \nResponse: {response} \n\n"

        # print(context)
        send_notification("notification", "Generating business profile...")
        
        business_profile = generate_business_profile(context)
        html = markdown2.markdown(business_profile)
        send_notification("business_profile", html)

        # print(business_profile)