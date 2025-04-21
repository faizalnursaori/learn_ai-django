from django.shortcuts import render
from django.views.generic import View
from researcher.methods import generate_queries, research, generate_business_profile


# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")
    
    def post(self, request):
        company_name = request.POST.get("company_name")

        queries = []

        financial_queries = generate_queries("Finance", company_name)
        leadership_queries = generate_queries("Leadership", company_name)
        operations_queries = generate_queries("Operations", company_name)
        company_history_queries = generate_queries("Company History", company_name)

        queries.extend(financial_queries.get("queries"))
        queries.extend(leadership_queries.get("queries"))
        queries.extend(operations_queries.get("queries"))
        queries.extend(company_history_queries.get("queries"))

        context = ""

        for query in queries[:3]:
            response = research(query)
            context += f"Query: {query} \nResponse: {response} \n\n"

        # print(context)
        business_profile = generate_business_profile(context)
        print(business_profile)

        return render(request, "index.html")