import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render, get_object_or_404
from .models import Company, Sales

def general_sales_graph(request):
    companies = Company.objects.all()
    sales_data = Sales.objects.all()

    plt.figure(figsize=(8, 6))
    for company in companies:
        company_sales = sales_data.filter(company=company)
        dates = [sale.date for sale in company_sales]
        amounts = [sale.amount for sale in company_sales]
        plt.plot(dates, amounts, label=company.name)

    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Sales Amount')
    plt.title('General Sales Graph')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, 'general_sales_graph.html', {'data': uri, 'companies': companies})

def specific_sales_graph(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    sales_data = Sales.objects.filter(company=company)

    plt.figure(figsize=(8, 6))
    dates = [sale.date for sale in sales_data]
    amounts = [sale.amount for sale in sales_data]
    plt.plot(dates, amounts, label=company.name)

    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Sales Amount')
    plt.title(f'Sales Graph for {company.name}')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, 'specific_sales_graph.html', {'data': uri, 'company': company})
